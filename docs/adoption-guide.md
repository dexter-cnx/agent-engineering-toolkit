# Adoption Guide

## Who this is for

This guide is for engineers who want to:
- Add a new skill and run their first optimization cycle
- Integrate the Karpathy system into an existing CI pipeline
- Understand how to interpret optimization reports and score histories

For a deeper operator walkthrough, pair this guide with `docs/karpathy-guide.md`.

---

## Prerequisites

- Python 3.11 or later
- No external Python dependencies required (the system uses only the standard library)
- The repository checked out locally

---

## Step 1: Write your skill

Create a new skill following the 13-section SKILL.md schema:

```
overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md
```

Required sections in order:
1. Purpose
2. Use when
3. Do NOT use when
4. Inputs required
5. Constraints
6. Step-by-step workflow
7. Output contract
8. Validation checklist
9. Related skills
10. References
11. Real example
12. Real file output sample

The validator counts the file title/H1 plus these 12 markdown sections, which is why the
repository still refers to the format as "13 required sections."

See `overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md`
for a reference implementation.

Worked examples live in `examples/` and are intentionally static snapshots separate from
the runtime outputs written to `reports/` and `memory/`.

---

## Step 2: Run your first evaluation

```bash
./scripts/karpathy-eval.sh overlays/agent-karpathy/skills/<category>/<name>/SKILL.md
```

Read the output.  The two most important fields:
- `final_score`: must be ≥ 0.60 to be promotion-eligible
- `evaluator_notes`: names the lowest-scoring dimensions

If `final_score` < 0.60, fix the identified issues before running a mutation cycle.

---

## Step 3: Run a dry-run optimization cycle

```bash
./scripts/karpathy-run-cycle.sh \
  overlays/agent-karpathy/skills/<category>/<name>/SKILL.md \
  true 5
```

This runs all 11 steps without writing any file.  Read the output:
- Which candidates passed regression?
- Which candidates were rejected by token policy?
- What is the PROMOTE/REJECT decision and why?

---

## Step 4: Interpret the report

`reports/latest_report.md` contains:

1. **Baseline score table** — per-dimension breakdown showing where quality is strong and where it is weak
2. **Candidates table** — each mutation with its score, token count, regression result, and token policy result
3. **Decision** — PROMOTE or REJECT with reasoning
4. **Decision trace** — baseline score, winner score, token delta, regression failures, token policy rejections
5. **Expected-result validation** — if the testcase provides `expected_result.json`, the report shows whether the run matched it

A REJECT decision is normal when the baseline is already high-quality.
It means none of the 6 mutation types found an improvement this cycle.

---

## Step 5: Run a production cycle (with promotion)

When you are satisfied with the dry-run results and want the system to actually update the skill:

```bash
./scripts/karpathy-run-cycle.sh \
  overlays/agent-karpathy/skills/<category>/<name>/SKILL.md \
  false 5
```

The system will back up the existing skill and write the winner.

---

## Adding the skill to CI

To automatically gate PRs that touch your skill:

1. The `karpathy-eval.yml` workflow already triggers on changes to `overlays/agent-karpathy/**`.
   No additional configuration is needed — it will run `eval_runner` on changed skills.

2. To add a weekly optimization run for your skill, update `.github/workflows/karpathy-cycle.yml`
   and add your skill path to the `skills_to_optimize` input default.

---

## Adding a new rubric dimension

1. Open `evals/rubrics/coding_task_rubric.v1.json`.
2. Add the new dimension under `dimensions`.
3. Update `weights` — they must sum to 1.0.
4. Add a `_score_<dimension>()` method in `agents/evaluator_agent.py`.
5. Add the dimension key to `_score_all_dimensions()`.
6. Run the evaluator on a test skill and confirm the new dimension appears in the output.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `final_score` = 0.0 | SKILL.md is empty or has no sections | Add all 13 required sections |
| All candidates fail regression | Mutation removed a section | Check mutation logic in `agents/mutation_agent.py` |
| Decision always REJECT | Baseline score is already locally optimal | Manually edit the baseline to introduce variation, then re-run |
| `FileNotFoundError` on rubric | Running from wrong directory | Run from the repo root |
| Token count unexpectedly high | Filler phrases in content | Apply `token_budget` mutation or edit manually |
