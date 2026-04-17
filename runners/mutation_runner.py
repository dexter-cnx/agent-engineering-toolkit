"""mutation_runner — generate mutation candidates for a skill file.

CLI usage:
    python -m runners.mutation_runner --skill <path/to/SKILL.md> [--n 5] [--out-json candidates.json]

Exit codes:
    0  — candidates generated successfully
    1  — skill file not found
"""

from __future__ import annotations

import argparse
import json
import os
import sys


def generate_mutations(skill_path: str, n: int = 6) -> list[dict]:
    """Load a skill file and return a list of MutationCandidate dicts."""
    skill_abs = os.path.abspath(skill_path)
    if not os.path.exists(skill_abs):
        raise FileNotFoundError(f"Skill file not found: {skill_abs}")

    with open(skill_abs, "r", encoding="utf-8") as fh:
        content = fh.read()

    parts = os.path.normpath(skill_abs).split(os.sep)
    try:
        idx = next(i for i, p in enumerate(parts) if p == "skills")
        skill_id = parts[idx + 1]
    except (StopIteration, IndexError):
        skill_id = os.path.basename(os.path.dirname(skill_abs))

    from agents.mutation_agent import MutationAgent
    agent = MutationAgent()
    candidates = agent.generate_candidates(
        skill_id  = skill_id,
        parent_id = "baseline",
        content   = content,
        n         = n,
    )

    # Persist to candidate_archive
    _archive_candidates(candidates, skill_id)
    return candidates


def _archive_candidates(candidates: list[dict], skill_id: str) -> None:
    from datetime import datetime, timezone

    repo_root    = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    archive_path = os.path.join(repo_root, "memory", "candidate_archive.json")
    os.makedirs(os.path.dirname(archive_path), exist_ok=True)

    if os.path.exists(archive_path):
        with open(archive_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    else:
        data = {"candidates": [], "last_updated": ""}

    for cand in candidates:
        data["candidates"].append({**cand, "skill_id": skill_id})
    data["last_updated"] = datetime.now(timezone.utc).isoformat()

    with open(archive_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, default=str)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate mutation candidates for a SKILL.md.")
    parser.add_argument("--skill",    required=True, help="Path to SKILL.md")
    parser.add_argument("--n",        type=int, default=6, help="Number of candidates (max 6)")
    parser.add_argument("--pretty",   action="store_true", help="Pretty-print JSON output")
    parser.add_argument("--out-json", dest="out_json", default=None, help="Write result to file")
    args = parser.parse_args()

    try:
        candidates = generate_mutations(args.skill, args.n)
    except FileNotFoundError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        sys.exit(1)

    indent = 2 if args.pretty else None
    output = json.dumps({"candidates": candidates}, indent=indent, default=str)
    print(output)

    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as fh:
            fh.write(output)


if __name__ == "__main__":
    main()
