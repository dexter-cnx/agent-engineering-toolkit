# agent-karpathy overlay

**Production-governed AI skill optimization system. Eval-driven development with hard gates.**

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
./scripts/karpathy-eval.sh <skill>

# Full cycle, no write
./scripts/karpathy-run-cycle.sh <skill> true 3

# Full cycle with promotion enabled
./scripts/karpathy-run-cycle.sh <skill> false 3
```

## Audit & Production Guarantees

Runtime artifacts are `reports/latest_report.md`, `reports/history/<run_id>.md`,
`memory/score_history.json`, and `memory/candidate_archive.json`; `examples/` is static only.
Every promotion decision must include `baseline_score`, `candidate_score`, `score_delta`,
`token_delta`, `regression_pass`, `token_policy_pass`, `final_decision`, and `reason`.
Promotion is blocked by regression failure, token policy violation, score threshold failure,
or missing required artifacts / decision fields. CI must fail closed on any blocked promotion.

- Deterministic: report generation, token counting, binary and regression checks, artifact paths.
- Heuristic: rubric scoring and candidate mutation selection.
- Interpretation: `PROMOTE` means the candidate won under the current rubric and gates;
  `REJECT` means it did not.

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
## Overlay OS contract

### Purpose
Provide specialization for **agent-karpathy** while keeping the repository root stack-neutral.

### When to use
Use this overlay for eval-driven skill optimization, mutation, and promotion governance.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
