# Karpathy Guide

## Purpose

Use the Karpathy overlay to improve `SKILL.md` content with eval-driven, regression-safe,
token-aware changes. This guide is for skill quality and promotion work, not for ordinary
feature implementation.

## When to use it

Use Karpathy when you need:
- a measurable baseline for a skill
- controlled mutations that change one dimension at a time
- regression gates before promotion
- token-growth governance
- a repeatable report trail in `reports/` and `memory/`

## When not to use it

Do not use Karpathy for:
- product feature work that does not touch skill quality
- stack-specific app delivery
- exploratory writing where you do not want rubric scoring or promotion gates
- changes that are clearly foundation-level and not skill-related

## Key terms

- `baseline` - the current `SKILL.md` before mutation
- `candidate` - a mutated variant under evaluation
- `dry-run` - run the cycle without writing a promoted skill
- `promotion` - writing the winning candidate back to `SKILL.md`
- `runtime artifacts` - `reports/latest_report.md`, `reports/history/`, `memory/score_history.json`, and `memory/candidate_archive.json`
- `static examples` - snapshots in `examples/` that document behavior without being runtime output

## Recommended workflow

1. Confirm the skill belongs to the Karpathy overlay.
2. Read `overlays/agent-karpathy/README.md` and `overlays/agent-karpathy/AGENTS.overlay.md`.
3. Check the skill path under `overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md`.
4. Run a baseline evaluation:

```bash
./scripts/karpathy-eval.sh overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md
```

5. Read `reports/latest_report.md` and note the lowest-scoring dimensions.
6. Run a dry-run cycle first, preferably with explicit flags:

```bash
./scripts/karpathy-run-cycle.sh \
  overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md \
  --dry-run --n 3 --pretty
```

7. Inspect the decision trace:
- `baseline_score`
- `candidate_score`
- `score_delta`
- `token_delta`
- `regression_pass`
- `token_policy_pass`
- `final_decision`
- `reason`

8. Promote only after regression and token policy both pass.
9. Verify the runtime artifacts and keep `examples/` as static reference material.

## What to watch for

- `final_score` should be at least `0.60` for promotion eligibility.
- A higher score does not override a regression failure.
- A better score does not justify large token growth unless the token policy allows it.
- A `REJECT` decision is normal when the baseline is already locally optimal.

## Practical recommendations

- Change one thing at a time.
- Prefer the smallest skill set that solves the task.
- Keep the `Validation checklist` executable and specific.
- Avoid filler prose that inflates token count without adding verification value.
- Keep examples static; do not treat `examples/` as live output.
- Use `--dry-run` or `--verify-only` when you want to inspect behavior before promotion.
- Use the older positional `true` / `false` form only when you need backward compatibility.

## Common mistakes

- Using Karpathy for ordinary app implementation work.
- Editing multiple skill dimensions in one mutation and then trying to infer which change helped.
- Skipping regression because the score improved.
- Confusing static snapshots in `examples/` with live reports in `reports/`.
- Treating `REJECT` as a failure when it often just means the baseline was already strong.

## CI and automation

- `karpathy-eval.yml` validates changed skills on push and pull request events.
- `karpathy-cycle.yml` runs the optimization loop on a schedule or manual dispatch.
- CI should default to dry-run mode unless the workflow explicitly allows promotion.

## If something looks wrong

- Re-run the baseline eval and compare the report to the current `SKILL.md`.
- Check that the skill path exists and belongs to the intended overlay.
- Verify that the runtime artifact files were written in the expected locations.
- Check `docs/promotion-system.md`, `docs/token-optimizer.md`, and `docs/guardrails.md` if a gate failed.

## Further reading

- `docs/adoption-guide.md`
- `docs/continuous-optimization.md`
- `docs/eval-system.md`
- `docs/promotion-system.md`
- `docs/token-optimizer.md`
- `docs/guardrails.md`
