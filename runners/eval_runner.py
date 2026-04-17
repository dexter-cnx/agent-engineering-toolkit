"""eval_runner — evaluate a single skill and print a JSON EvalResult.

CLI usage:
    python -m runners.eval_runner --skill <path/to/SKILL.md> [--rubric <path>] [--pretty]
    python -m runners.eval_runner --skill <path> --out-json <output.json>

Exit codes:
    0  — evaluation completed (regardless of score)
    1  — file not found or JSON error
    2  — score below promotion threshold (0.60)
"""

from __future__ import annotations

import argparse
import json
import os
import sys


RUBRIC_DEFAULT = os.path.join(
    os.path.dirname(__file__), "..", "evals", "rubrics", "coding_task_rubric.v1.json"
)
PROMOTION_THRESHOLD = 0.60


def run_eval(skill_path: str, rubric_path: str = RUBRIC_DEFAULT) -> dict:
    """Evaluate one skill file.  Returns EvalResult dict."""
    rubric_abs = os.path.abspath(rubric_path)
    skill_abs  = os.path.abspath(skill_path)

    if not os.path.exists(skill_abs):
        raise FileNotFoundError(f"Skill file not found: {skill_abs}")
    if not os.path.exists(rubric_abs):
        raise FileNotFoundError(f"Rubric file not found: {rubric_abs}")

    with open(rubric_abs, "r", encoding="utf-8") as fh:
        rubric = json.load(fh)

    with open(skill_abs, "r", encoding="utf-8") as fh:
        content = fh.read()

    from agents.evaluator_agent import EvaluatorAgent

    # Derive skill_id from path
    parts = os.path.normpath(skill_abs).split(os.sep)
    try:
        idx = next(i for i, p in enumerate(parts) if p == "skills")
        skill_id = parts[idx + 1]
    except (StopIteration, IndexError):
        skill_id = os.path.basename(os.path.dirname(skill_abs))

    agent = EvaluatorAgent(rubric=rubric)
    return agent.evaluate(
        skill_id     = skill_id,
        candidate_id = "baseline",
        content      = content,
        mutation_type= "baseline",
    )


def run_eval_batch(
    skill_paths: list[str],
    rubric_path: str = RUBRIC_DEFAULT,
) -> list[dict]:
    """Evaluate multiple skills.  Returns list of EvalResult dicts."""
    return [run_eval(p, rubric_path) for p in skill_paths]


def _append_to_history(eval_result: dict, history_path: str, skill_path: str | None = None) -> None:
    """Persist a summary entry to memory/score_history.json."""
    os.makedirs(os.path.dirname(history_path), exist_ok=True)
    from datetime import datetime, timezone

    if os.path.exists(history_path):
        with open(history_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    else:
        data = {"entries": [], "last_updated": ""}

    data["entries"].append({
        "run_id":      "eval-only",
        "skill_id":    eval_result.get("skill_id"),
        "skill_path":  skill_path,
        "final_score": eval_result.get("final_score"),
        "token_count": eval_result.get("token_count"),
        "decision":    "eval_only",
        "timestamp":   eval_result.get("timestamp"),
    })
    data["last_updated"] = datetime.now(timezone.utc).isoformat()

    with open(history_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, default=str)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a SKILL.md against the Karpathy rubric.")
    parser.add_argument("--skill",    required=True, help="Path to SKILL.md")
    parser.add_argument("--rubric",   default=RUBRIC_DEFAULT, help="Path to rubric JSON")
    parser.add_argument("--pretty",   action="store_true", help="Pretty-print JSON output")
    parser.add_argument("--out-json", dest="out_json", default=None, help="Write result to file")
    parser.add_argument("--save-history", action="store_true",
                        help="Append result to memory/score_history.json")
    args = parser.parse_args()

    try:
        result = run_eval(args.skill, args.rubric)
    except FileNotFoundError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        sys.exit(1)

    indent = 2 if args.pretty else None
    output = json.dumps(result, indent=indent, default=str)

    print(output)

    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as fh:
            fh.write(output)

    if args.save_history:
        repo_root    = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        history_path = os.path.join(repo_root, "memory", "score_history.json")
        _append_to_history(result, history_path, os.path.relpath(os.path.abspath(args.skill), repo_root))

    # Exit 2 if score is below threshold (for CI gates)
    if result.get("final_score", 0) < PROMOTION_THRESHOLD:
        sys.exit(2)


if __name__ == "__main__":
    main()
