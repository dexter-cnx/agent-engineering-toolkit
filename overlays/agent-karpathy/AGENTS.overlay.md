# AGENTS.overlay.md — agent-karpathy

## Overlay purpose

This overlay operationalises **eval-driven development** for AI skills and prompts.
It gives agents the tools, skills, and execution rules needed to measure, mutate, evaluate,
and safely promote improvements to any skill in this repository.

The overlay does NOT replace any foundation skills.  It adds a new domain-specific layer:
self-improvement infrastructure for AI-generated content.

---

## Foundation assumptions (preserved from root)

- Skills are stack-agnostic by default.
- The canonical lifecycle is defined in `docs/prompt-pipeline.md`.
- The agent team model is defined in `docs/agent-team-system.md`.
- Layer boundaries must be respected: overlays specialize, they do not override foundation.

---

## Active skill routing

Route to the correct skill based on the task:

| Task | Skill |
|------|-------|
| Score a skill against the rubric | `skills/evaluation/` |
| Generate single-dimension mutation candidates | `skills/mutation/` |
| Enforce regression guardrails before promotion | `skills/regression/` |
| Select best candidate, apply token policy, promote | `skills/optimization/` |
| Apply Karpathy evaluation criteria manually | `skills/karpathy-guidelines/` |
| Run the full 11-step optimization cycle | Use `runners/optimization_cycle.py` directly |

---

## Orchestration rules

- Use individual skills for isolated tasks (score one skill, generate mutations, check regression).
- Use `runners/optimization_cycle.py` when running the full improvement loop end-to-end.
- Always run regression **before** promotion — never skip this step.
- Always run eval on the baseline **before** generating mutations — you need a baseline score.
- Never promote a candidate that has not passed all binary checks.
- Agents must communicate exclusively via structured JSON matching `evals/schemas/skill_eval.schema.json`.

---

## Delivery rules

- Every promoted skill must have a backup of the previous version (`.bak.md` suffix).
- Every optimization run must produce a report in `reports/latest_report.md`.
- Every run result must be appended to `memory/score_history.json`.
- Dry-run mode (`--dry-run`) must be used in CI unless the workflow explicitly enables promotion.
- Score threshold for promotion eligibility: **0.60 minimum final_score**.

---

## Agent contribution rules

To add a new skill to this overlay:

1. Create the directory: `overlays/agent-karpathy/skills/<category>/<skill-name>/`.
2. Write `SKILL.md` with all 13 required sections.
3. Run `tools/skillgen/bin/skillgen validate overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md`.
4. Run `tools/skillgen/bin/skillgen overlap --overlay overlays/agent-karpathy` to check for duplicates.
5. Update `overlays/agent-karpathy/SKILLS_INDEX.md` via `skillgen sync-index --overlay overlays/agent-karpathy --write`.

To add a new mutation type:

1. Add the type string to `MUTATION_TYPES` in `agents/mutation_agent.py`.
2. Implement `_mutate_<type>(content) -> tuple[str, str]` following the one-dimension constraint.
3. Add a test case in `evals/testcases/` demonstrating the mutation.

---

## Output discipline

- All agent outputs must be valid JSON matching the relevant schema in `evals/schemas/`.
- Reports must be written to `reports/latest_report.md` and `reports/history/<run_id>.md`.
- Memory must be updated on every run (both score_history and candidate_archive).
- Never leave a skill in a partially-promoted state — the backup-then-write pattern is mandatory.

---

## Reference layers

| Purpose | Location |
|---------|----------|
| Rubric (scoring weights + criteria) | `evals/rubrics/coding_task_rubric.v1.json` |
| JSON schemas | `evals/schemas/` |
| Test cases | `evals/testcases/` |
| Score history | `memory/score_history.json` |
| Candidate archive | `memory/candidate_archive.json` |
| Latest report | `reports/latest_report.md` |
| Full example | `examples/flutter_deeplink_full_cycle.md` |
| Adoption guide | `docs/adoption-guide.md` |
| Architecture doc | `docs/karpathy-architecture.md` |
