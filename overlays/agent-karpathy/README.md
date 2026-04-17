# agent-karpathy overlay

**Self-improving AI skill quality system.  Eval-driven development at scale.**

---

## What this overlay does

The `agent-karpathy` overlay transforms the agent-engineering-toolkit into a
**eval-driven skill optimization system**. It provides the infrastructure to:

- Measure the quality of any skill against a weighted rubric
- Generate controlled single-dimension mutations
- Enforce regression guardrails before any change is promoted
- Apply token efficiency policy to prevent token bloat
- Produce structured JSON + Markdown reports for every optimization run
- Run the full improvement loop manually or on a CI schedule

---

## Start here

| Document | Purpose |
|----------|---------|
| `AGENTS.overlay.md` | Operating rules, skill routing, delivery rules |
| `skills/` | Five skills covering the core workflow |
| `docs/adoption-guide.md` | How to add a new skill and run your first cycle |
| `docs/karpathy-architecture.md` | System architecture and data flow |
| `examples/flutter_deeplink_full_cycle.md` | Complete static worked example |
| `docs/continuous-optimization.md` | CI and manual run modes |
| `docs/promotion-system.md` | Promotion gate and decision rules |

---

## Default stack

- **Language**: Python 3.11+
- **Schemas**: JSON Schema draft-07
- **Docs**: Markdown (GitHub-flavored)
- **CI**: GitHub Actions
- **Storage**: JSON flat files (memory/) + Markdown reports (reports/)

No external dependencies beyond the Python standard library are required to run the core system.

Runtime outputs are the committed `reports/latest_report.md`, `reports/history/<run_id>.md`,
`memory/score_history.json`, and `memory/candidate_archive.json`. Static demos live in
`examples/` and must not be confused with live run artifacts.

## How to run

```bash
# Eval only
bash scripts/karpathy-eval.sh <path/to/SKILL.md> --pretty

# Full cycle, no write
bash scripts/karpathy-run-cycle.sh <path/to/SKILL.md> --dry-run --pretty --report-only

# Full cycle with promotion enabled
bash scripts/karpathy-run-cycle.sh <path/to/SKILL.md> --pretty
```

## Audit note

This overlay is safe for CI because promotion is blocked unless all binary regression checks
pass, token policy passes, and the candidate strictly beats the baseline score. The evaluation
model is still partly heuristic: rubric scoring and mutation selection are rule-based, while
`expected_result.json` adds expectation-backed validation when it is present. Maintain
promotion decisions as governance records, not as proof that a candidate is universally better.

---

## Active skill categories

| Category | Skills | Use for |
|----------|--------|---------|
| `evaluation/` | karpathy-evaluation | Scoring a skill against the weighted rubric |
| `mutation/` | karpathy-mutation | Generating single-dimension candidates |
| `regression/` | karpathy-regression | Guardrail enforcement before promotion |
| `optimization/` | karpathy-optimizer | Token policy + winner selection |
| `karpathy-guidelines/` | karpathy-guidelines | Applying evaluation criteria manually |

---

## Operating rule

1. Always run `eval_runner` on the baseline before starting a mutation cycle.
2. Always run `regression_runner` before calling `promotion_runner`.
3. Use `scripts/karpathy-run-cycle.sh` for end-to-end runs — it wraps the full cycle and writes the canonical runtime artifacts.
4. Use `--dry-run` in CI unless the workflow is explicitly a promotion workflow.

---

## Related docs

- `docs/eval-system.md` — Scoring model details
- `docs/mutation-system.md` — Mutation types and one-dimension constraint
- `docs/promotion-system.md` — Promotion gate logic
- `docs/token-optimizer.md` — Token policy formula
- `docs/guardrails.md` — Regression checks and hard-fail conditions
- `docs/continuous-optimization.md` — Scheduling and automation
