# agent-karpathy overlay

**Self-improving AI skill quality system.  Eval-driven development at scale.**

---

## What this overlay does

The `agent-karpathy` overlay transforms the agent-engineering-toolkit into a
**self-optimising system**.  It provides the infrastructure to:

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
| `examples/flutter_deeplink_full_cycle.md` | Complete worked example |

---

## Default stack

- **Language**: Python 3.11+
- **Schemas**: JSON Schema draft-07
- **Docs**: Markdown (GitHub-flavored)
- **CI**: GitHub Actions
- **Storage**: JSON flat files (memory/) + Markdown reports (reports/)

No external dependencies beyond the Python standard library are required to run the core system.

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
3. Use `optimization_cycle.py` for end-to-end runs — it handles all steps automatically.
4. Use `--dry-run` in CI unless the workflow is explicitly a promotion workflow.

---

## Related docs

- `docs/eval-system.md` — Scoring model details
- `docs/mutation-system.md` — Mutation types and one-dimension constraint
- `docs/promotion-system.md` — Promotion gate logic
- `docs/token-optimizer.md` — Token policy formula
- `docs/guardrails.md` — Regression checks and hard-fail conditions
- `docs/continuous-optimization.md` — Scheduling and automation
