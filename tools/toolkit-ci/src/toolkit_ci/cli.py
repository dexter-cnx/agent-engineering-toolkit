from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .utils import print_json, write_json_file


def doctor(args: argparse.Namespace) -> int:
    data = {"tool": "toolkit-ci", "status": "ok", "python": sys.version.split()[0]}
    print_json(data) if args.json else print("toolkit-ci doctor: ok")
    return 0


def auth_status(args: argparse.Namespace) -> int:
    data = {"tool": "toolkit-ci", "auth": "not_configured", "note": "Connect your CI provider API here."}
    print_json(data) if args.json else print("CI auth not configured")
    return 0


def runs_list(args: argparse.Namespace) -> int:
    data = {
        "branch": args.branch,
        "runs": [
            {"id": "12345", "status": "failed", "branch": args.branch, "summary": "Skeleton run"},
            {"id": "12344", "status": "success", "branch": args.branch, "summary": "Skeleton run"},
        ][: args.limit]
    }
    print_json(data) if args.json else print(f"Listed runs for {args.branch}")
    return 0


def runs_read(args: argparse.Namespace) -> int:
    data = {
        "id": args.run_id,
        "status": "failed",
        "steps": ["checkout", "setup", "flutter test"],
        "note": "Skeleton metadata. Replace with real provider response.",
    }
    print_json(data) if args.json else print(f"Read run {args.run_id}")
    return 0


def logs_download(args: argparse.Namespace) -> int:
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / f"{args.run_id}.log"
    log_path.write_text("Skeleton CI log\nStep failed: flutter test\n", encoding="utf-8")
    payload = {"run_id": args.run_id, "log_path": str(log_path)}
    print_json(payload) if args.json else print(f"Downloaded log to {log_path}")
    return 0


def debug(args: argparse.Namespace) -> int:
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    summary_path = out_dir / f"{args.run_id}-summary.json"
    summary = {
        "run_id": args.run_id,
        "first_failing_step": "flutter test",
        "suggested_next_action": "inspect test output and reproduce locally",
    }
    write_json_file(summary_path, summary)
    payload = {"run_id": args.run_id, "summary_path": str(summary_path)}
    print_json(payload) if args.json else print(f"Debug summary written to {summary_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="toolkit-ci")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("doctor")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=doctor)

    auth = sub.add_parser("auth")
    auth_sub = auth.add_subparsers(dest="auth_command", required=True)
    p = auth_sub.add_parser("status")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=auth_status)

    runs = sub.add_parser("runs")
    runs_sub = runs.add_subparsers(dest="runs_command", required=True)

    p = runs_sub.add_parser("list")
    p.add_argument("--branch", required=True)
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=runs_list)

    p = runs_sub.add_parser("read")
    p.add_argument("run_id")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=runs_read)

    logs = sub.add_parser("logs")
    logs_sub = logs.add_subparsers(dest="logs_command", required=True)
    p = logs_sub.add_parser("download")
    p.add_argument("run_id")
    p.add_argument("--output", required=True)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=logs_download)

    p = sub.add_parser("debug")
    p.add_argument("run_id")
    p.add_argument("--output", required=True)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=debug)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
