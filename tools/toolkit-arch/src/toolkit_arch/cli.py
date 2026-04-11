from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .utils import print_json, write_json_file


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
    # Skeleton: always passes. Replace with real threshold logic.
    print("toolkit-arch ci-check: pass")
    return 0


def build_parser() -> argparse.ArgumentParser:
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

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
