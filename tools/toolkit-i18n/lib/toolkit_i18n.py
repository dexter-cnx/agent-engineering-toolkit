#!/usr/bin/env python3
"""toolkit-i18n CLI implementation."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Optional


class ToolkitError(Exception):
    """Raised for user-facing command failures."""


def _issue(
    severity: str,
    code: str,
    message: str,
    *,
    line: Optional[int] = None,
    column: Optional[int] = None,
    key: Optional[str] = None,
    language: Optional[str] = None,
) -> dict[str, Any]:
    issue: dict[str, Any] = {
        "severity": severity,
        "code": code,
        "message": message,
    }
    if line is not None:
        issue["line"] = line
    if column is not None:
        issue["column"] = column
    if key is not None:
        issue["key"] = key
    if language is not None:
        issue["language"] = language
    return issue


def _print_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def _print_text(lines: Iterable[str]) -> None:
    for line in lines:
        print(line)


def _normalize_header(value: str) -> str:
    return value.strip()


def _sanitize_filename(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    cleaned = cleaned.strip("._-")
    if not cleaned:
        raise ToolkitError(f"invalid language name for output file: {value!r}")
    return cleaned


def _resolve_path(path: str) -> Path:
    return Path(path).expanduser().resolve()


def _issue_counts(issues: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"error": 0, "warning": 0}
    for issue in issues:
        severity = issue["severity"]
        if severity in counts:
            counts[severity] += 1
    return counts


def _fatal_issue_count(issues: list[dict[str, Any]]) -> int:
    return sum(1 for issue in issues if issue["severity"] == "error")


def _ordered_unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def _feature_name(key: str) -> str:
    return key.split(".", 1)[0] if key else "unknown"


def _feature_coverage_summary(defined_keys: list[str], used_keys: list[str]) -> dict[str, Any]:
    defined_by_feature: dict[str, set[str]] = {}
    used_by_feature: dict[str, set[str]] = {}

    for key in defined_keys:
        feature = _feature_name(key)
        defined_by_feature.setdefault(feature, set()).add(key)

    for key in used_keys:
        feature = _feature_name(key)
        used_by_feature.setdefault(feature, set()).add(key)

    features: dict[str, dict[str, Any]] = {}
    for feature in sorted(set(defined_by_feature) | set(used_by_feature)):
        defined_set = defined_by_feature.get(feature, set())
        used_set = used_by_feature.get(feature, set())
        matched_set = defined_set & used_set
        defined_count = len(defined_set)
        used_count = len(used_set)
        matched_count = len(matched_set)
        missing_count = len(used_set - defined_set)
        unused_count = len(defined_set - used_set)
        if used_count == 0:
            percent = 100.0 if defined_count == 0 else 0.0
        else:
            percent = round((matched_count / used_count) * 100, 1)
        features[feature] = {
            "defined_count": defined_count,
            "used_count": used_count,
            "matched_count": matched_count,
            "missing_count": missing_count,
            "unused_count": unused_count,
            "coverage_percent": percent,
        }

    return features


def _load_csv(csv_path: Path) -> dict[str, Any]:
    if not csv_path.is_file():
        raise ToolkitError(f"csv file not found: {csv_path}")

    issues: list[dict[str, Any]] = []
    rows: list[dict[str, Any]] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            raw_headers = next(reader)
        except StopIteration as exc:
            raise ToolkitError(f"csv file is empty: {csv_path}") from exc

        headers = [_normalize_header(header) for header in raw_headers]
        if not any(headers):
            raise ToolkitError(f"csv file is missing a header row: {csv_path}")

        header_counts: dict[str, int] = {}
        for idx, header in enumerate(headers):
            if not header:
                issues.append(
                    _issue(
                        "error",
                        "missing_column_name",
                        "missing required column name",
                        line=1,
                        column=idx + 1,
                    )
                )
                continue
            header_counts[header] = header_counts.get(header, 0) + 1

        for name, count in header_counts.items():
            if count > 1:
                issues.append(
                    _issue(
                        "error",
                        "duplicate_column",
                        f"duplicate column header: {name}",
                        line=1,
                        column=headers.index(name) + 1,
                    )
                )

        key_indices = [idx for idx, header in enumerate(headers) if header.lower() == "key"]
        if not key_indices:
            issues.append(
                _issue(
                    "error",
                    "missing_key_column",
                    "missing required key column",
                    line=1,
                )
            )
            key_index = None
        else:
            key_index = key_indices[0]
            if len(key_indices) > 1:
                issues.append(
                    _issue(
                        "error",
                        "duplicate_key_column",
                        "multiple key columns found",
                        line=1,
                        column=key_index + 1,
                    )
                )

        language_columns: list[tuple[int, str]] = []
        for idx, header in enumerate(headers):
            if key_index is not None and idx == key_index:
                continue
            if not header:
                continue
            language_columns.append((idx, header))

        if not language_columns:
            issues.append(
                _issue(
                    "error",
                    "missing_language_columns",
                    "missing one or more language columns",
                    line=1,
                )
            )

        keys_seen: dict[str, int] = {}
        for line_no, row in enumerate(reader, start=2):
            if not row or all(cell.strip() == "" for cell in row):
                continue

            if len(row) != len(headers):
                issues.append(
                    _issue(
                        "error",
                        "malformed_row",
                        f"expected {len(headers)} columns but found {len(row)}",
                        line=line_no,
                    )
                )
                continue

            if key_index is None:
                continue

            key = row[key_index].strip()
            if not key:
                issues.append(
                    _issue(
                        "error",
                        "missing_key_value",
                        "missing key value",
                        line=line_no,
                        column=key_index + 1,
                    )
                )
                continue

            if any(part == "" for part in key.split(".")):
                issues.append(
                    _issue(
                        "error",
                        "malformed_key",
                        f"malformed dotted key: {key}",
                        line=line_no,
                        column=key_index + 1,
                        key=key,
                    )
                )
                continue

            if key in keys_seen:
                issues.append(
                    _issue(
                        "error",
                        "duplicate_key",
                        f"duplicate key: {key}",
                        line=line_no,
                        column=key_index + 1,
                        key=key,
                    )
                )
                continue

            keys_seen[key] = line_no
            values: dict[str, str] = {}
            for column_index, language in language_columns:
                value = row[column_index].strip()
                values[language] = value
                if value == "":
                    issues.append(
                        _issue(
                            "warning",
                            "missing_value",
                            f"missing value for {language}",
                            line=line_no,
                            column=column_index + 1,
                            key=key,
                            language=language,
                        )
                    )

            rows.append({"line": line_no, "key": key, "values": values})

    return {
        "csv_path": str(csv_path),
        "headers": headers,
        "key_index": key_index,
        "language_columns": language_columns,
        "rows": rows,
        "issues": issues,
    }


def _build_nested_map(rows: list[dict[str, Any]], language: str) -> dict[str, Any]:
    root: dict[str, Any] = {}

    for row in rows:
        key = row["key"]
        value = row["values"].get(language, "")
        node = root
        parts = key.split(".")
        for part in parts[:-1]:
            existing = node.get(part)
            if existing is None:
                node[part] = {}
                node = node[part]
                continue
            if not isinstance(existing, dict):
                raise ToolkitError(f"nested key conflict for {key} in {language}")
            node = existing
        leaf = parts[-1]
        existing = node.get(leaf)
        if isinstance(existing, dict):
            raise ToolkitError(f"nested key conflict for {key} in {language}")
        node[leaf] = value

    return root


def _load_used_keys_file(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ToolkitError(f"used keys file not found: {path}")

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ToolkitError(f"invalid used keys json: {path}") from exc

    raw_items: list[Any]
    if isinstance(payload, list):
        raw_items = payload
    elif isinstance(payload, dict):
        for field in ("used_keys", "unique_keys", "keys", "source_matches", "matches", "used_key_details"):
            value = payload.get(field)
            if isinstance(value, list):
                raw_items = value
                break
        else:
            raise ToolkitError(f"unsupported used keys format: {path}")
    else:
        raise ToolkitError(f"unsupported used keys format: {path}")

    keys: list[str] = []
    for item in raw_items:
        key: Optional[str] = None
        if isinstance(item, str):
            key = item
        elif isinstance(item, dict):
            for field in ("key", "normalized_key", "used_key", "name", "value"):
                value = item.get(field)
                if isinstance(value, str) and value.strip():
                    key = value
                    break
            if key is None:
                raw_key = item.get("raw_key")
                if isinstance(raw_key, str) and raw_key.strip():
                    key = raw_key
        if key is None:
            continue
        normalized = key.strip()
        if "_" in normalized and "." not in normalized:
            dotted = normalized.replace("_", ".")
            if all(part for part in dotted.split(".")):
                normalized = dotted
        keys.append(normalized)

    return {
        "path": str(path),
        "keys": _ordered_unique(keys),
    }


def _validate(csv_path: Path) -> dict[str, Any]:
    analysis = _load_csv(csv_path)
    issues = analysis["issues"]
    counts = _issue_counts(issues)
    return {
        "status": "ok" if counts["error"] == 0 else "error",
        "csv_path": analysis["csv_path"],
        "row_count": len(analysis["rows"]),
        "language_count": len(analysis["language_columns"]),
        "languages": [language for _, language in analysis["language_columns"]],
        "counts": counts,
        "issues": issues,
    }


def _diff(csv_path: Path) -> dict[str, Any]:
    validation = _validate(csv_path)
    files = [
        {
            "language": language,
            "file": f"{_sanitize_filename(language)}.json",
            "rows": validation["row_count"],
        }
        for language in validation["languages"]
    ]
    return {
        **validation,
        "generated_files": files,
    }


def _generate(csv_path: Path, output_dir: Path) -> dict[str, Any]:
    analysis = _load_csv(csv_path)
    issues = analysis["issues"]
    counts = _issue_counts(issues)

    if _fatal_issue_count(issues) > 0:
        return {
            "status": "error",
            "csv_path": analysis["csv_path"],
            "output_dir": str(output_dir),
            "counts": counts,
            "issues": issues,
            "written_files": [],
        }

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise ToolkitError(f"cannot create output directory: {output_dir}") from exc

    planned_files: list[tuple[str, Path]] = []
    seen_targets: set[Path] = set()
    for _, language in analysis["language_columns"]:
        target_path = output_dir / f"{_sanitize_filename(language)}.json"
        if target_path in seen_targets:
            raise ToolkitError(f"output file collision for language: {language}")
        seen_targets.add(target_path)
        planned_files.append((language, target_path))

    written_files: list[dict[str, Any]] = []
    for language, target_path in planned_files:
        nested = _build_nested_map(analysis["rows"], language)
        try:
            target_path.write_text(
                json.dumps(nested, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except OSError as exc:
            raise ToolkitError(f"cannot write file: {target_path}") from exc
        written_files.append(
            {
                "language": language,
                "path": str(target_path),
                "rows": len(analysis["rows"]),
            }
        )

    return {
        "status": "ok",
        "csv_path": analysis["csv_path"],
        "output_dir": str(output_dir.resolve()),
        "counts": counts,
        "issues": issues,
        "written_files": written_files,
    }


def _keys_list(csv_path: Path) -> dict[str, Any]:
    analysis = _load_csv(csv_path)
    issues = analysis["issues"]
    counts = _issue_counts(issues)
    keys = [row["key"] for row in analysis["rows"]]
    unique_keys = _ordered_unique(keys)
    return {
        "status": "ok" if counts["error"] == 0 else "error",
        "csv_path": analysis["csv_path"],
        "row_count": len(analysis["rows"]),
        "language_count": len(analysis["language_columns"]),
        "languages": [language for _, language in analysis["language_columns"]],
        "counts": counts,
        "issues": issues,
        "key_count": len(unique_keys),
        "defined_keys": unique_keys,
        "keys": unique_keys,
    }


def _keys_diff(csv_path: Path, used_keys_path: Path) -> dict[str, Any]:
    analysis = _load_csv(csv_path)
    used_keys = _load_used_keys_file(used_keys_path)
    issues = analysis["issues"]
    counts = _issue_counts(issues)

    defined_keys = _ordered_unique(row["key"] for row in analysis["rows"])
    defined_set = set(defined_keys)
    used_set = set(used_keys["keys"])

    matched_keys = [key for key in used_keys["keys"] if key in defined_set]
    missing_keys = [key for key in used_keys["keys"] if key not in defined_set]
    unused_keys = [key for key in defined_keys if key not in used_set]

    return {
        "status": "error" if counts["error"] > 0 or missing_keys or unused_keys else "ok",
        "csv_path": analysis["csv_path"],
        "used_keys_path": used_keys["path"],
        "row_count": len(analysis["rows"]),
        "language_count": len(analysis["language_columns"]),
        "languages": [language for _, language in analysis["language_columns"]],
        "counts": counts,
        "issues": issues,
        "total_defined": len(defined_keys),
        "total_used": len(used_keys["keys"]),
        "defined_key_count": len(defined_keys),
        "used_key_count": len(used_keys["keys"]),
        "matched_count": len(matched_keys),
        "matched_key_count": len(matched_keys),
        "missing_key_count": len(missing_keys),
        "unused_key_count": len(unused_keys),
        "missing_in_translations": missing_keys,
        "unused_in_code": unused_keys,
        "defined_keys": defined_keys,
        "used_keys": used_keys["keys"],
        "matched_keys": matched_keys,
        "missing_keys": missing_keys,
        "unused_keys": unused_keys,
    }


def _coverage(csv_path: Path, used_keys_path: Path) -> dict[str, Any]:
    diff = _keys_diff(csv_path, used_keys_path)
    used_count = diff["total_used"]
    matched_count = diff["matched_count"]
    feature_coverage = 100.0 if used_count == 0 else round((matched_count / used_count) * 100, 1)
    feature_summary = _feature_coverage_summary(diff["defined_keys"], diff["used_keys"])
    return {
        "status": "error" if diff["counts"]["error"] > 0 or diff["missing_in_translations"] or diff["unused_in_code"] else "ok",
        "csv_path": diff["csv_path"],
        "used_keys_path": diff["used_keys_path"],
        "defined_keys": diff["defined_keys"],
        "used_keys": diff["used_keys"],
        "missing_keys": diff["missing_in_translations"],
        "unused_keys": diff["unused_in_code"],
        "total_defined": diff["total_defined"],
        "total_used": used_count,
        "defined_key_count": diff["total_defined"],
        "used_key_count": used_count,
        "matched_count": matched_count,
        "matched_key_count": matched_count,
        "missing_count": len(diff["missing_in_translations"]),
        "missing_key_count": len(diff["missing_in_translations"]),
        "unused_count": len(diff["unused_in_code"]),
        "unused_key_count": len(diff["unused_in_code"]),
        "feature_coverage": {
            "overall": {
                "defined_count": diff["total_defined"],
                "used_count": used_count,
                "matched_count": matched_count,
                "coverage_percent": feature_coverage,
            },
            "by_feature": feature_summary,
        },
        "missing_in_translations": diff["missing_in_translations"],
        "unused_in_code": diff["unused_in_code"],
        "issues": diff["issues"],
        "counts": diff["counts"],
    }


def _summary_with_samples(result: dict[str, Any], *, sample_limit: int) -> dict[str, Any]:
    summary = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "keys",
            "missing_keys",
            "unused_keys",
            "matched_keys",
            "issues",
        }
    }
    if "keys" in result:
        summary["sample_keys"] = result["keys"][:sample_limit]
    if "missing_keys" in result:
        summary["missing_sample"] = result["missing_keys"][:sample_limit]
    if "unused_keys" in result:
        summary["unused_sample"] = result["unused_keys"][:sample_limit]
    if "matched_keys" in result:
        summary["matched_sample"] = result["matched_keys"][:sample_limit]
    if "issues" in result:
        summary["issues"] = result["issues"][:sample_limit]
    return summary


def _doctor() -> dict[str, Any]:
    return {
        "status": "ok",
        "python": sys.version.split()[0],
        "python_executable": sys.executable,
        "csv_parser": "stdlib",
        "json_writer": "stdlib",
        "cwd": str(Path.cwd()),
        "readiness": "ready",
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="toolkit-i18n")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="check runtime readiness")
    doctor.add_argument("--json", action="store_true", help="print JSON output")

    validate = subparsers.add_parser("validate", help="validate a localization CSV")
    validate.add_argument("csv_path")
    validate.add_argument("--json", action="store_true", help="print JSON output")

    diff = subparsers.add_parser("diff", help="summarize generated output")
    diff.add_argument("csv_path")
    diff.add_argument("--json", action="store_true", help="print JSON output")

    generate = subparsers.add_parser("generate", help="write localization JSON files")
    generate.add_argument("csv_path")
    generate.add_argument("--output", required=True, help="target output directory")
    generate.add_argument("--json", action="store_true", help="print JSON output")

    keys = subparsers.add_parser("keys", help="inspect and compare localization keys")
    keys_subparsers = keys.add_subparsers(dest="keys_command", required=True)

    keys_list = keys_subparsers.add_parser("list", help="list keys from a CSV")
    keys_list.add_argument("csv_path")
    keys_list.add_argument("--output", help="write the full key report to this JSON file")
    keys_list.add_argument("--limit", type=int, default=10, help="sample size for compact output")
    keys_list.add_argument("--json", action="store_true", help="print JSON output")

    keys_diff = keys_subparsers.add_parser("diff", help="compare used keys against a CSV")
    keys_diff.add_argument("csv_path", nargs="?", help="translation CSV path")
    keys_diff.add_argument("--translations", help="translation CSV path")
    keys_diff.add_argument("--used-file", "--used-keys", dest="used_file", required=True, help="JSON file exported by toolkit-arch")
    keys_diff.add_argument("--output", help="write the full diff report to this JSON file")
    keys_diff.add_argument("--limit", type=int, default=10, help="sample size for compact output")
    keys_diff.add_argument("--json", action="store_true", help="print JSON output")

    coverage = subparsers.add_parser("coverage", help="summarize key coverage")
    coverage.add_argument("csv_path", nargs="?", help="translation CSV path")
    coverage.add_argument("--translations", help="translation CSV path")
    coverage.add_argument("--used-file", "--used-keys", dest="used_file", required=True, help="JSON file exported by toolkit-arch")
    coverage.add_argument("--output", help="write the full coverage report to this JSON file")
    coverage.add_argument("--limit", type=int, default=10, help="sample size for compact output")
    coverage.add_argument("--json", action="store_true", help="print JSON output")

    return parser


def _render_summary(result: dict[str, Any]) -> list[str]:
    counts = result["counts"]
    issues = result["issues"]
    lines = [
        "status=ok" if counts["error"] == 0 else "status=error",
        f"csv={result['csv_path']}",
        f"rows={result['row_count']}",
        f"languages={result['language_count']}",
        f"errors={counts['error']}",
        f"warnings={counts['warning']}",
    ]

    for issue in issues[:10]:
        parts = [issue["severity"], issue["code"], issue["message"]]
        if "line" in issue:
            parts.append(f"line={issue['line']}")
        if "language" in issue:
            parts.append(f"language={issue['language']}")
        if "key" in issue:
            parts.append(f"key={issue['key']}")
        lines.append(" ".join(parts))

    remaining = len(issues) - min(len(issues), 10)
    if remaining > 0:
        lines.append(f"truncated={remaining}")

    return lines


def _write_optional_report(result: dict[str, Any], output: Optional[str]) -> dict[str, Any]:
    if not output:
        return result
    output_path = _resolve_path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {**result, "output": str(output_path)}


def _print_compact_result(result: dict[str, Any], lines: list[str]) -> None:
    if result.get("output"):
        lines.append(f"output={result['output']}")
    _print_text(lines)


def _resolve_translations_path(args: argparse.Namespace) -> Path:
    csv_value = getattr(args, "translations", None) or getattr(args, "csv_path", None)
    if not csv_value:
        raise ToolkitError("missing required translation csv path")
    return _resolve_path(csv_value)


def _resolve_used_file_path(args: argparse.Namespace) -> Path:
    used_value = getattr(args, "used_file", None)
    if not used_value:
        raise ToolkitError("missing required used keys file")
    return _resolve_path(used_value)


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "doctor":
            result = _doctor()
            if args.json:
                _print_json(result)
            else:
                _print_text(
                    [
                        f"status={result['status']}",
                        f"python={result['python']}",
                        f"cwd={result['cwd']}",
                        f"readiness={result['readiness']}",
                    ]
                )
            return 0

        if args.command == "validate":
            csv_path = _resolve_path(args.csv_path)
            result = _validate(csv_path)
            if args.json:
                _print_json(result)
            else:
                _print_text(_render_summary(result))
            return 0 if result["counts"]["error"] == 0 else 1

        if args.command == "diff":
            csv_path = _resolve_path(args.csv_path)
            result = _diff(csv_path)
            if args.json:
                _print_json(result)
            else:
                _print_text(
                    [
                        f"status={result['status']}",
                        f"csv={result['csv_path']}",
                        f"languages={result['language_count']}",
                        f"rows={result['row_count']}",
                        f"files={','.join(item['file'] for item in result['generated_files'])}",
                        f"errors={result['counts']['error']}",
                        f"warnings={result['counts']['warning']}",
                    ]
                )
            return 0 if result["counts"]["error"] == 0 else 1

        if args.command == "generate":
            csv_path = _resolve_path(args.csv_path)
            output_dir = _resolve_path(args.output)
            result = _generate(csv_path, output_dir)
            if args.json:
                _print_json(result)
            else:
                _print_text(
                    [
                        f"status={result['status']}",
                        f"csv={result['csv_path']}",
                        f"output={result['output_dir']}",
                        f"written={len(result['written_files'])}",
                        f"files={','.join(Path(item['path']).name for item in result['written_files'])}",
                        f"errors={result['counts']['error']}",
                        f"warnings={result['counts']['warning']}",
                    ]
                )
            return 0 if result["status"] == "ok" else 1

        if args.command == "keys":
            if args.keys_command == "list":
                csv_path = _resolve_path(args.csv_path)
                result = _keys_list(csv_path)
                result = _write_optional_report(result, args.output)
                summary = _summary_with_samples(result, sample_limit=args.limit)
                if args.json:
                    _print_json(summary)
                else:
                    _print_text(
                        [
                            f"status={summary['status']}",
                            f"csv={summary['csv_path']}",
                            f"keys={summary['key_count']}",
                            f"languages={summary['language_count']}",
                            f"sample_keys={','.join(summary['sample_keys']) if summary.get('sample_keys') else ''}",
                            f"errors={summary['counts']['error']}",
                            f"warnings={summary['counts']['warning']}",
                            *([f"output={summary['output']}"] if "output" in summary else []),
                        ]
                )
                return 0 if result["counts"]["error"] == 0 else 1

            if args.keys_command == "diff":
                csv_path = _resolve_translations_path(args)
                used_keys_path = _resolve_used_file_path(args)
                result = _keys_diff(csv_path, used_keys_path)
                result = _write_optional_report(result, args.output)
                summary = {
                    "status": result["status"],
                    "csv_path": result["csv_path"],
                    "used_keys_path": result["used_keys_path"],
                    "total_defined": result["total_defined"],
                    "total_used": result["total_used"],
                    "missing_in_translations": result["missing_in_translations"][: args.limit],
                    "unused_in_code": result["unused_in_code"][: args.limit],
                    "missing_count": result["missing_key_count"],
                    "unused_count": result["unused_key_count"],
                    "matched_count": result["matched_count"],
                    "sample_missing": result["missing_in_translations"][: args.limit],
                    "sample_unused": result["unused_in_code"][: args.limit],
                }
                if "output" in result:
                    summary["output"] = result["output"]
                if args.json:
                    _print_json(summary)
                else:
                    _print_text(
                        [
                            f"status={summary['status']}",
                            f"csv={summary['csv_path']}",
                            f"used={summary['total_used']}",
                            f"defined={summary['total_defined']}",
                            f"missing={summary['missing_count']}",
                            f"unused={summary['unused_count']}",
                            f"missing_sample={','.join(summary['sample_missing']) if summary.get('sample_missing') else ''}",
                            f"unused_sample={','.join(summary['sample_unused']) if summary.get('sample_unused') else ''}",
                            *([f"output={summary['output']}"] if "output" in summary else []),
                        ]
                    )
                return 0 if result["status"] == "ok" else 1

        if args.command == "coverage":
            csv_path = _resolve_translations_path(args)
            used_keys_path = _resolve_used_file_path(args)
            result = _coverage(csv_path, used_keys_path)
            result = _write_optional_report(result, args.output)
            summary = _summary_with_samples(result, sample_limit=args.limit)
            if args.json:
                _print_json(summary)
            else:
                _print_text(
                    [
                        f"status={summary['status']}",
                        f"csv={summary['csv_path']}",
                        f"used={summary['used_key_count']}",
                        f"defined={summary['defined_key_count']}",
                        f"missing={summary['missing_key_count']}",
                        f"unused={summary['unused_key_count']}",
                        f"feature_coverage={summary['feature_coverage']['overall']['coverage_percent']}%",
                        *([f"output={summary['output']}"] if "output" in summary else []),
                    ]
                )
            return 0 if result["status"] == "ok" else 1

        raise ToolkitError(f"unknown command: {args.command}")
    except ToolkitError as exc:
        print(f"toolkit-i18n: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
