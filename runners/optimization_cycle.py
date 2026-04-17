"""optimization_cycle — the full 11-step Karpathy self-improvement loop.

This is the primary production entry point.

CLI usage:
    python -m runners.optimization_cycle --skill <path/to/SKILL.md> [options]

Options:
    --n <int>      Number of mutation candidates to generate (default: 5)
    --dry-run      Evaluate and compare but do not write promoted skill to disk
    --pretty       Pretty-print JSON report to stdout
    --report-only  Print the Markdown report to stdout in addition to JSON
    --run-id <str> Caller-supplied run ID (generated if omitted)

Exit codes:
    0  — Cycle completed, decision: PROMOTE
    1  — Regression failure or hard system error
    2  — Cycle completed, decision: REJECT (no improvement found)
    3  — Skill file not found

The 11 steps:
    1.  Load baseline skill/prompt
    2.  Run eval → get baseline score
    3.  Generate N mutation candidates
    4.  Evaluate all candidates
    5.  Compare vs baseline
    6.  Run regression checks
    7.  Apply token efficiency policy
    8.  Select best candidate
    9.  Promote or reject
    10. Store results in memory
    11. Generate report
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import traceback


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the full Karpathy optimization cycle for a SKILL.md."
    )
    parser.add_argument("--skill",       required=True,  help="Path to the baseline SKILL.md")
    parser.add_argument("--n",           type=int, default=5,
                        help="Number of mutation candidates (default: 5, min: 1, max: 6)")
    parser.add_argument("--dry-run",     action="store_true",
                        help="Do not write the promoted skill to disk")
    parser.add_argument("--pretty",      action="store_true",
                        help="Pretty-print JSON to stdout")
    parser.add_argument("--report-only", action="store_true",
                        help="Print Markdown report to stdout after JSON")
    parser.add_argument("--run-id",      default=None,
                        help="Optional caller-supplied run ID")
    args = parser.parse_args()

    skill_path = os.path.abspath(args.skill)

    if args.n < 1:
        print(json.dumps({"error": "--n must be at least 1"}), file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(skill_path):
        print(json.dumps({"error": f"Skill not found: {skill_path}"}), file=sys.stderr)
        sys.exit(3)

    # ------------------------------------------------------------------
    # Run the full cycle via Orchestrator
    # ------------------------------------------------------------------
    try:
        from orchestrator.orchestrator import Orchestrator
        orch   = Orchestrator()
        report = orch.run_full_cycle(
            skill_path   = skill_path,
            n_candidates = min(max(args.n, 1), 6),
            dry_run      = args.dry_run,
            run_id       = args.run_id,
        )
    except Exception as exc:
        print(
            json.dumps({"error": str(exc), "traceback": traceback.format_exc()}),
            file=sys.stderr,
        )
        sys.exit(1)

    # ------------------------------------------------------------------
    # Print JSON report
    # ------------------------------------------------------------------
    indent  = 2 if args.pretty else None
    # Omit candidate content bodies from stdout to keep output manageable
    compact = _compact_report(report)
    print(json.dumps(compact, indent=indent, default=str))

    # ------------------------------------------------------------------
    # Optionally print Markdown report
    # ------------------------------------------------------------------
    if args.report_only:
        repo_root   = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        report_path = os.path.join(repo_root, "reports", "latest_report.md")
        if os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as fh:
                print("\n" + fh.read())

    # ------------------------------------------------------------------
    # Exit code based on decision
    # ------------------------------------------------------------------
    decision = report.get("decision", "REJECT")
    if decision == "PROMOTE":
        sys.exit(0)
    sys.exit(2)   # REJECT — no regression failure, just no improvement


def _compact_report(report: dict) -> dict:
    """Return report with candidate content bodies stripped (to keep stdout manageable)."""
    compact = {k: v for k, v in report.items() if k != "candidates"}
    if "candidates" in report:
        compact["candidates"] = [
            {k: v for k, v in c.items() if k != "content"}
            for c in report["candidates"]
        ]
    return compact


if __name__ == "__main__":
    main()
