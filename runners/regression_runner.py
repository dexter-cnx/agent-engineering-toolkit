"""regression_runner — run regression checks on mutation candidates.

CLI usage:
    python -m runners.regression_runner --skill <path/to/SKILL.md> --candidates <candidates.json>

Exit codes:
    0  — all candidates passed regression
    1  — one or more candidates failed (hard fail)
    2  — input file not found
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


def run_regression_checks(
    candidates: list[dict[str, Any]],
    skill_path: str,
) -> dict[str, Any]:
    """Run regression on every candidate.

    Returns:
        {
          "regression_results":  list of RegressionResult,
          "passing_candidates":  list of candidates that passed,
          "failing_candidates":  list of candidate_ids that failed,
          "all_passed":          bool,
        }
    """
    from agents.regression_agent import RegressionAgent

    if not os.path.exists(skill_path):
        raise FileNotFoundError(f"Baseline skill not found: {skill_path}")

    with open(skill_path, "r", encoding="utf-8") as fh:
        baseline_content = fh.read()
    baseline = {"content": baseline_content}

    agent   = RegressionAgent()
    results:  list[dict[str, Any]] = []
    passing:  list[dict[str, Any]] = []
    failing:  list[str]             = []

    for cand in candidates:
        result = agent.check_silent(cand, baseline, skill_path)
        results.append(result)
        if result["passed"]:
            passing.append(cand)
        else:
            failing.append(cand["candidate_id"])

    return {
        "regression_results":  results,
        "passing_candidates":  passing,
        "failing_candidates":  failing,
        "all_passed":          len(failing) == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run regression checks on mutation candidates."
    )
    parser.add_argument("--skill",      required=True, help="Path to the baseline SKILL.md")
    parser.add_argument("--candidates", required=True,
                        help="Path to candidates JSON (from mutation_runner)")
    parser.add_argument("--pretty",     action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.candidates):
        print(json.dumps({"error": f"Candidates file not found: {args.candidates}"}),
              file=sys.stderr)
        sys.exit(2)

    with open(args.candidates, "r", encoding="utf-8") as fh:
        data       = json.load(fh)
        candidates = data if isinstance(data, list) else data.get("candidates", [])

    try:
        result = run_regression_checks(candidates, args.skill)
    except FileNotFoundError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        sys.exit(2)

    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, default=str))

    if not result["all_passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
