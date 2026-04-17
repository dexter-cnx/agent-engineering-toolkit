"""promotion_runner — select the best candidate and promote or reject.

CLI usage:
    python -m runners.promotion_runner \
        --baseline-eval   <eval.json> \
        --candidate-evals <evals.json> \
        --candidates      <candidates.json> \
        --skill           <path/to/SKILL.md> \
        [--dry-run]

Exit codes:
    0  — PROMOTE decision
    1  — REJECT decision
    2  — input error
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


def run_promotion(
    baseline_eval: dict[str, Any],
    candidate_evals: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    skill_path: str,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run the promotion decision.  Returns PromotionDecision dict."""
    from agents.promotion_agent import PromotionAgent
    agent = PromotionAgent()
    return agent.decide(
        baseline_eval   = baseline_eval,
        candidate_evals = candidate_evals,
        candidates      = candidates,
        skill_path      = skill_path,
        dry_run         = dry_run,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Select the best mutation candidate and promote.")
    parser.add_argument("--baseline-eval",   required=True, dest="baseline_eval",
                        help="Path to baseline EvalResult JSON")
    parser.add_argument("--candidate-evals", required=True, dest="candidate_evals",
                        help="Path to candidate EvalResults JSON (list)")
    parser.add_argument("--candidates",      required=True,
                        help="Path to MutationCandidates JSON (list)")
    parser.add_argument("--skill",           required=True,
                        help="Path to the target SKILL.md")
    parser.add_argument("--dry-run",         action="store_true",
                        help="Do not write to disk")
    parser.add_argument("--pretty",          action="store_true")
    args = parser.parse_args()

    for path in [args.baseline_eval, args.candidate_evals, args.candidates]:
        if not os.path.exists(path):
            print(json.dumps({"error": f"File not found: {path}"}), file=sys.stderr)
            sys.exit(2)

    with open(args.baseline_eval,   "r", encoding="utf-8") as fh:
        baseline_eval = json.load(fh)
    with open(args.candidate_evals, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
        candidate_evals = raw if isinstance(raw, list) else raw.get("evals", [])
    with open(args.candidates, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
        candidates = raw if isinstance(raw, list) else raw.get("candidates", [])

    decision = run_promotion(
        baseline_eval   = baseline_eval,
        candidate_evals = candidate_evals,
        candidates      = candidates,
        skill_path      = args.skill,
        dry_run         = args.dry_run,
    )

    indent = 2 if args.pretty else None
    print(json.dumps(decision, indent=indent, default=str))

    sys.exit(0 if decision["decision"] == "PROMOTE" else 1)


if __name__ == "__main__":
    main()
