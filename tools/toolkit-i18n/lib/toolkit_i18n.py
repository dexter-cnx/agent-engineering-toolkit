#!/usr/bin/env python3
"""toolkit-i18n CLI implementation."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


class ToolkitError(Exception):
    """Raised for user-facing command failures."""


def _issue(
    severity: str,
    code: str,
    message: str,
    *,
    line: int | None = None,
    column: int | None = None,
    key: str | None = None,
    language: str | None = None,
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


def main(argv: list[str] | None = None) -> int:
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

        csv_path = _resolve_path(args.csv_path)

        if args.command == "validate":
            result = _validate(csv_path)
            if args.json:
                _print_json(result)
            else:
                _print_text(_render_summary(result))
            return 0 if result["counts"]["error"] == 0 else 1

        if args.command == "diff":
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

        raise ToolkitError(f"unknown command: {args.command}")
    except ToolkitError as exc:
        print(f"toolkit-i18n: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
