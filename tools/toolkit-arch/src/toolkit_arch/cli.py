from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Optional

from .utils import print_json, write_json_file


_DART_USAGE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("context.tr", re.compile(r'\bcontext\.tr\s*\(\s*(?P<quote>["\'])(?P<key>[^"\']+)(?P=quote)\s*\)')),
    ("string.tr", re.compile(r'(?P<quote>["\'])(?P<key>[^"\']+)(?P=quote)\s*\.tr\b')),
    ("tr()", re.compile(r'(?<!\.)\btr\s*\(\s*(?P<quote>["\'])(?P<key>[^"\']+)(?P=quote)\s*\)')),
    ("LocaleKeys", re.compile(r"\bLocaleKeys\.(?P<raw>[A-Za-z_][A-Za-z0-9_]*)\b")),
)

_DEFAULT_DART_SKIP_DIRS = {
    ".dart_tool",
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "coverage",
}

_REVIEW_LAYER_NAMES = {"application", "controller", "viewmodel"}
_FORBIDDEN_LAYER_NAMES = {"domain", "data"}
_ALLOWED_LAYER_NAMES = {"presentation"}
_DATA_EXCEPTION_PATTERNS = (
    re.compile(r"toolkit-arch\s*:\s*allow-i18n(?:-data)?", re.IGNORECASE),
    re.compile(r"i18n-allow\s*:\s*data", re.IGNORECASE),
    re.compile(r"repository-approved\s+i18n\s+exception", re.IGNORECASE),
)
_SOURCE_MATCH_LIMIT = 20


def doctor(args: argparse.Namespace) -> int:
    data = {
        "tool": "toolkit-arch",
        "status": "ok",
        "python": sys.version.split()[0],
        "cwd": str(Path.cwd()),
    }
    print_json(data) if args.json else print("toolkit-arch doctor: ok")
    return 0


def scan(args: argparse.Namespace) -> int:
    target = Path(args.target)
    findings = {
        "target": str(target),
        "status": "scanned",
        "summary": {
            "python_files": len(list(target.rglob("*.py"))) if target.exists() else 0,
            "dart_files": len(list(target.rglob("*.dart"))) if target.exists() else 0,
        },
        "note": "Rule engine skeleton only. Add repository-specific architecture rules.",
    }
    print_json(findings) if args.json else print(f"Scanned {target}")
    return 0


def violations(args: argparse.Namespace) -> int:
    data = {
        "target": args.target,
        "violations": [],
        "limit": args.limit,
        "note": "No concrete rules implemented yet.",
    }
    print_json(data) if args.json else print("No violations found in skeleton mode.")
    return 0


def export_report(args: argparse.Namespace) -> int:
    out = Path(args.output)
    report = {
        "target": args.target,
        "violations": [],
        "status": "exported",
        "note": "Skeleton export. Replace with real architecture findings.",
    }
    write_json_file(out, report)
    print_json({"output": str(out), "status": "ok"}) if args.json else print(f"Exported report to {out}")
    return 0


def ci_check(args: argparse.Namespace) -> int:
    print("toolkit-arch ci-check: pass")
    return 0


def _should_skip_dart_path(path: Path) -> bool:
    return any(part in _DEFAULT_DART_SKIP_DIRS for part in path.parts)


def _iter_dart_files(target: Path) -> list[Path]:
    if not target.exists():
        return []
    files: list[Path] = []
    for candidate in target.rglob("*.dart"):
        if _should_skip_dart_path(candidate):
            continue
        files.append(candidate)
    return files


def _normalize_locale_key(raw: str) -> str:
    key = raw.strip()
    if "_" not in key or "." in key:
        return key
    dotted = key.replace("_", ".")
    return dotted if all(part for part in dotted.split(".")) else key


def _dedupe_by_key(items: Iterable[dict[str, Any]], key_name: str = "key") -> list[dict[str, Any]]:
    seen: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for item in items:
        key = str(item[key_name])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped


def _feature_name(key: str) -> str:
    return key.split(".", 1)[0] if key else "unknown"


def _scan_file_for_i18n_usage(path: Path, target: Path) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return matches

    layer = _layer_for_path(path, target)
    lines = content.splitlines()
    for line_no, line in enumerate(lines, start=1):
        for pattern_name, pattern in _DART_USAGE_PATTERNS:
            for match in pattern.finditer(line):
                raw_key = match.groupdict().get("key") or match.groupdict().get("raw") or ""
                canonical_key = _normalize_locale_key(raw_key) if pattern_name == "LocaleKeys" else raw_key.strip()
                matches.append(
                    {
                        "file": str(path),
                        "layer": layer,
                        "line": line_no,
                        "column": match.start() + 1,
                        "pattern": pattern_name,
                        "raw_key": raw_key.strip(),
                        "key": canonical_key,
                        "source": match.group(0).strip(),
                    }
                )
    return matches


def _layer_for_path(path: Path, target: Path) -> str:
    try:
        relative_parts = [part.lower() for part in path.relative_to(target).parts]
    except ValueError:
        relative_parts = [part.lower() for part in path.parts]

    parts = set(relative_parts)
    if "domain" in parts:
        return "domain"
    if "data" in parts:
        return "data"
    for layer in ("application", "controller", "viewmodel"):
        if layer in parts:
            return layer
    if "presentation" in parts:
        return "presentation"
    return "other"


def _is_data_exception(content: str) -> bool:
    return any(pattern.search(content) for pattern in _DATA_EXCEPTION_PATTERNS)


def _load_translation_keys(csv_path: Path) -> dict[str, Any]:
    if not csv_path.is_file():
        raise ToolkitError(f"translation csv not found: {csv_path}")

    issues: list[dict[str, Any]] = []
    keys: list[str] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            raw_headers = next(reader)
        except StopIteration as exc:
            raise ToolkitError(f"translation csv is empty: {csv_path}") from exc

        headers = [header.strip() for header in raw_headers]
        key_indices = [idx for idx, header in enumerate(headers) if header.lower() == "key"]
        if not key_indices:
            issues.append({"severity": "error", "code": "missing_key_column", "message": "missing required key column"})
            return {
                "csv_path": str(csv_path),
                "keys": [],
                "issues": issues,
            }

        key_index = key_indices[0]
        keys_seen: set[str] = set()
        for line_no, row in enumerate(reader, start=2):
            if not row or all(cell.strip() == "" for cell in row):
                continue
            if len(row) != len(headers):
                issues.append(
                    {
                        "severity": "error",
                        "code": "malformed_row",
                        "message": f"expected {len(headers)} columns but found {len(row)}",
                        "line": line_no,
                    }
                )
                continue

            key = row[key_index].strip()
            if not key:
                issues.append(
                    {
                        "severity": "error",
                        "code": "missing_key_value",
                        "message": "missing key value",
                        "line": line_no,
                        "column": key_index + 1,
                    }
                )
                continue

            if any(part == "" for part in key.split(".")):
                issues.append(
                    {
                        "severity": "error",
                        "code": "malformed_key",
                        "message": f"malformed dotted key: {key}",
                        "line": line_no,
                        "column": key_index + 1,
                        "key": key,
                    }
                )
                continue

            if key in keys_seen:
                issues.append(
                    {
                        "severity": "error",
                        "code": "duplicate_key",
                        "message": f"duplicate key: {key}",
                        "line": line_no,
                        "column": key_index + 1,
                        "key": key,
                    }
                )
                continue

            keys_seen.add(key)
            keys.append(key)

    return {
        "csv_path": str(csv_path),
        "keys": keys,
        "issues": issues,
    }


def _collect_i18n_usage(target: Path) -> dict[str, Any]:
    dart_files = _iter_dart_files(target)
    matches: list[dict[str, Any]] = []
    for path in dart_files:
        matches.extend(_scan_file_for_i18n_usage(path, target))

    unique_key_items = _dedupe_by_key(
        [{"key": match["key"], "first_seen": {"file": match["file"], "line": match["line"]}} for match in matches]
    )
    used_keys = [item["key"] for item in unique_key_items]
    pattern_counts: dict[str, int] = {}
    layer_counts: dict[str, int] = {
        "presentation": 0,
        "application": 0,
        "controller": 0,
        "viewmodel": 0,
        "domain": 0,
        "data": 0,
        "other": 0,
    }
    for match in matches:
        pattern_counts[match["pattern"]] = pattern_counts.get(match["pattern"], 0) + 1
        layer_counts[match["layer"]] = layer_counts.get(match["layer"], 0) + 1

    return {
        "tool": "toolkit-arch",
        "command": "i18n-usage",
        "target": str(target),
        "status": "ok",
        "dart_files_scanned": len(dart_files),
        "match_count": len(matches),
        "unique_key_count": len(used_keys),
        "pattern_counts": pattern_counts,
        "used_keys": used_keys,
        "used_key_details": unique_key_items,
        "matches": matches,
        "layer_counts": layer_counts,
    }


def _collect_layer_violations(target: Path) -> dict[str, Any]:
    usage = _collect_i18n_usage(target)
    forbidden: list[dict[str, Any]] = []
    review: list[dict[str, Any]] = []
    allowed_exceptions: list[dict[str, Any]] = []

    for match in usage["matches"]:
        layer = match["layer"]
        if layer in _FORBIDDEN_LAYER_NAMES:
            if layer == "data":
                try:
                    content = Path(match["file"]).read_text(encoding="utf-8")
                except OSError:
                    content = ""
                if _is_data_exception(content):
                    allowed_exceptions.append({**match, "exception": "repository-approved"})
                    continue
            forbidden.append({**match, "policy": "forbidden"})
            continue
        if layer in _REVIEW_LAYER_NAMES:
            review.append({**match, "policy": "review"})

    return {
        "tool": "toolkit-arch",
        "command": "i18n-layer-check",
        "target": str(target),
        "status": "ok" if not forbidden else "error",
        "forbidden_count": len(forbidden),
        "review_count": len(review),
        "exception_count": len(allowed_exceptions),
        "forbidden_usages": forbidden,
        "review_usages": review,
        "exception_usages": allowed_exceptions,
    }


def _collect_i18n_coverage(target: Path, translations_csv: Path) -> dict[str, Any]:
    usage = _collect_i18n_usage(target)
    translations = _load_translation_keys(translations_csv)

    defined_keys = _ordered_unique(translations["keys"])
    used_keys = _ordered_unique(usage["used_keys"])
    defined_set = set(defined_keys)
    used_set = set(used_keys)

    missing_keys = [key for key in used_keys if key not in defined_set]
    unused_keys = [key for key in defined_keys if key not in used_set]
    matched_keys = [key for key in used_keys if key in defined_set]

    return {
        "tool": "toolkit-arch",
        "command": "i18n-coverage",
        "target": str(target),
        "translations": str(translations_csv),
        "status": "ok" if not missing_keys and not unused_keys and not translations["issues"] else "error",
        "defined_keys": defined_keys,
        "used_keys": used_keys,
        "missing_keys": missing_keys,
        "unused_keys": unused_keys,
        "feature_coverage": _summarize_feature_coverage(defined_keys, used_keys),
        "source_matches": usage["matches"][:_SOURCE_MATCH_LIMIT],
        "source_match_count": len(usage["matches"]),
        "translation_issues": translations["issues"],
    }


def _summarize_feature_coverage(defined_keys: list[str], used_keys: list[str]) -> dict[str, Any]:
    features: dict[str, dict[str, int]] = {}
    defined_counts: dict[str, int] = {}
    used_counts: dict[str, int] = {}
    defined_set = set(defined_keys)

    for key in defined_keys:
        feature = _feature_name(key)
        defined_counts[feature] = defined_counts.get(feature, 0) + 1

    for key in used_keys:
        feature = _feature_name(key)
        used_counts[feature] = used_counts.get(feature, 0) + 1

    feature_names = sorted(set(defined_counts) | set(used_counts))
    for feature in feature_names:
        defined_count = defined_counts.get(feature, 0)
        used_count = used_counts.get(feature, 0)
        matched_count = min(defined_count, used_count)
        missing_count = max(used_count - defined_count, 0)
        unused_count = max(defined_count - used_count, 0)
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

    overall_used = len(used_keys)
    overall_matched = len([key for key in used_keys if key in defined_set])
    if overall_used == 0:
        overall_percent = 100.0 if len(defined_keys) == 0 else 0.0
    else:
        overall_percent = round((overall_matched / overall_used) * 100, 1)
    return {
        "overall": {
            "defined_count": len(defined_keys),
            "used_count": overall_used,
            "matched_count": overall_matched,
            "coverage_percent": overall_percent,
        },
        "by_feature": features,
    }


def _ordered_unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def _summary_with_samples(result: dict[str, Any], *, sample_limit: int) -> dict[str, Any]:
    summary = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "matches",
            "source_matches",
            "forbidden_usages",
            "review_usages",
            "exception_usages",
            "translation_issues",
        }
    }
    if "matches" in result:
        summary["source_matches"] = result["matches"][:sample_limit]
    if "source_matches" in result:
        summary["source_matches"] = result["source_matches"][:sample_limit]
    if "forbidden_usages" in result:
        summary["forbidden_usages"] = result["forbidden_usages"][:sample_limit]
    if "review_usages" in result:
        summary["review_usages"] = result["review_usages"][:sample_limit]
    if "exception_usages" in result:
        summary["exception_usages"] = result["exception_usages"][:sample_limit]
    if "translation_issues" in result:
        summary["translation_issues"] = result["translation_issues"][:sample_limit]
    return summary


def _load_used_keys_input(path: Path) -> dict[str, Any]:
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


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="toolkit-arch")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("doctor")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=doctor)

    p = sub.add_parser("scan")
    p.add_argument("--target", required=True)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=scan)

    p = sub.add_parser("violations")
    p.add_argument("--target", required=True)
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=violations)

    p = sub.add_parser("export")
    p.add_argument("--target", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=export_report)

    p = sub.add_parser("ci-check")
    p.add_argument("--target", required=True)
    p.set_defaults(func=ci_check)

    p = sub.add_parser("i18n-usage")
    p.add_argument("--target", required=True)
    p.add_argument("--output", help="write the full usage report to this JSON file")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=i18n_usage)

    p = sub.add_parser("i18n-layer-check")
    p.add_argument("--target", required=True)
    p.add_argument("--output", help="write the full layer-check report to this JSON file")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=i18n_layer_check)

    p = sub.add_parser("i18n-coverage")
    p.add_argument("--target", required=True)
    p.add_argument("--translations", required=True)
    p.add_argument("--output", help="write the full coverage report to this JSON file")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=i18n_coverage)

    return parser


def _resolve_target(args: argparse.Namespace) -> Path:
    return Path(args.target)


def i18n_usage(args: argparse.Namespace) -> int:
    target = _resolve_target(args)
    report = _collect_i18n_usage(target)
    if getattr(args, "output", None):
        output_path = Path(args.output)
        write_json_file(output_path, report)
        summary = {
            "tool": report["tool"],
            "command": report["command"],
            "target": report["target"],
            "status": report["status"],
            "used_keys": report["used_keys"],
            "used_key_count": report["unique_key_count"],
            "source_matches": report["matches"][:_SOURCE_MATCH_LIMIT],
            "source_match_count": report["match_count"],
            "output": str(output_path),
        }
    else:
        summary = {
            "tool": report["tool"],
            "command": report["command"],
            "target": report["target"],
            "status": report["status"],
            "used_keys": report["used_keys"],
            "used_key_count": report["unique_key_count"],
            "source_matches": report["matches"][:_SOURCE_MATCH_LIMIT],
            "source_match_count": report["match_count"],
        }

    if args.json:
        print_json(summary)
    else:
        lines = [
            f"status={summary['status']}",
            f"target={summary['target']}",
            f"keys={summary['used_key_count']}",
            f"matches={summary['source_match_count']}",
        ]
        if "output" in summary:
            lines.append(f"output={summary['output']}")
        print("\n".join(lines))
    return 0


def i18n_layer_check(args: argparse.Namespace) -> int:
    target = _resolve_target(args)
    report = _collect_layer_violations(target)
    if getattr(args, "output", None):
        output_path = Path(args.output)
        write_json_file(output_path, report)
        summary = {
            "tool": report["tool"],
            "command": report["command"],
            "target": report["target"],
            "status": report["status"],
            "forbidden_usages": report["forbidden_usages"][:_SOURCE_MATCH_LIMIT],
            "review_usages": report["review_usages"][:_SOURCE_MATCH_LIMIT],
            "exception_usages": report["exception_usages"][:_SOURCE_MATCH_LIMIT],
            "output": str(output_path),
        }
    else:
        summary = {
            "tool": report["tool"],
            "command": report["command"],
            "target": report["target"],
            "status": report["status"],
            "forbidden_usages": report["forbidden_usages"][:_SOURCE_MATCH_LIMIT],
            "review_usages": report["review_usages"][:_SOURCE_MATCH_LIMIT],
            "exception_usages": report["exception_usages"][:_SOURCE_MATCH_LIMIT],
        }

    if args.json:
        print_json(summary)
    else:
        print(f"status={summary['status']}")
        print(f"target={summary['target']}")
        print(f"forbidden={len(report['forbidden_usages'])}")
        print(f"review={len(report['review_usages'])}")
        if "output" in summary:
            print(f"output={summary['output']}")
    return 0 if report["forbidden_count"] == 0 else 1


def i18n_coverage(args: argparse.Namespace) -> int:
    target = _resolve_target(args)
    translations = Path(args.translations)
    report = _collect_i18n_coverage(target, translations)
    if getattr(args, "output", None):
        output_path = Path(args.output)
        write_json_file(output_path, report)
        summary = {
            "tool": report["tool"],
            "command": report["command"],
            "target": report["target"],
            "translations": report["translations"],
            "status": report["status"],
            "defined_keys": report["defined_keys"],
            "used_keys": report["used_keys"],
            "missing_keys": report["missing_keys"],
            "unused_keys": report["unused_keys"],
            "feature_coverage": report["feature_coverage"],
            "output": str(output_path),
        }
    else:
        summary = {
            "tool": report["tool"],
            "command": report["command"],
            "target": report["target"],
            "translations": report["translations"],
            "status": report["status"],
            "defined_keys": report["defined_keys"],
            "used_keys": report["used_keys"],
            "missing_keys": report["missing_keys"],
            "unused_keys": report["unused_keys"],
            "feature_coverage": report["feature_coverage"],
        }

    if args.json:
        print_json(summary)
    else:
        print(f"status={summary['status']}")
        print(f"target={summary['target']}")
        print(f"defined={len(summary['defined_keys'])}")
        print(f"used={len(summary['used_keys'])}")
        print(f"missing={len(summary['missing_keys'])}")
        print(f"unused={len(summary['unused_keys'])}")
        print(f"coverage={summary['feature_coverage']['overall']['coverage_percent']}%")
        if "output" in summary:
            print(f"output={summary['output']}")
    return 0 if not report["missing_keys"] and not report["unused_keys"] and not report["translation_issues"] else 1


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
