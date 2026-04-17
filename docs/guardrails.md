# Guardrails

## Purpose

Guardrails prevent mutation candidates from degrading the quality or structural integrity
of a skill.  They are enforced as hard-fail checks — any violation aborts the candidate's
path to promotion.

---

## Regression Checks

All five checks run on every candidate.  A single failure is sufficient to exclude the candidate.

### Check 1: Required sections present

All 12 required H2 sections must be present in the candidate content:

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

**Violation message**: `"Missing required section: ## <section name>"`

---

### Check 2: No architecture violations

The following patterns must not appear in a candidate:

| Pattern | Description |
|---------|-------------|
| `import firebase_auth directly` | Direct Firebase import without adapter |
| `bypass repository` | Repository bypass recommended |
| `directly in (widget\|page\|screen)` | Logic placed in presentation layer |
| `skip the validation` | Validation step skipped |

**Violation message**: `"Architecture violation: <description>"`

---

### Check 3: No forbidden file changes

A mutation must not target any of the following protected paths:

- `AGENTS.md`
- `AGENTS.overlay.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`
- `evals/rubrics/`
- `evals/schemas/`
- `.github/workflows/`

If the `skill_path` argument to the regression runner matches any of these patterns,
the candidate is rejected before any other checks run.

**Violation message**: `"Mutation targets a forbidden file path: <path> matches <pattern>"`

---

### Check 4: Behavior preserved

The candidate's Purpose and Output contract must not be degraded relative to the baseline:

- If the baseline has a non-empty Purpose section, the candidate must also have one.
- If the baseline has a non-empty Output contract section, the candidate must also have one.
- The Output contract bullet count must not decrease (mutations may add deliverables but not remove them).

**Violation messages**:
- `"Purpose section was removed or emptied by mutation."`
- `"Output contract section was removed or emptied by mutation."`
- `"Output contract has fewer deliverables after mutation (N < M)."`

---

### Check 5: Section count not reduced

The candidate must contain at least as many H2 sections as the baseline.
Any section present in the baseline must still be present in the candidate.

**Violation message**: `"Section removed by mutation: ## <section name>"`

---

## Hard Fail Behavior

When any check fails:

- `RegressionAgent.check()` raises `RegressionViolation(candidate_id, violations)`.
- `RegressionAgent.check_silent()` returns `{"passed": False, "violations": [...]}` without raising.
- `runners/regression_runner.py` exits with code 1.
- The Orchestrator excludes the candidate from the promotion stage and records its `candidate_id` in `regression_failures`.

---

## What Guardrails Do NOT Check

Guardrails are structural checks only.  They do not check:

- Whether the steps are technically correct (that is `correctness` in the rubric)
- Whether the scope is well-defined (that is `scope_discipline`)
- Whether the checklist items are executable (that is `verifiability`)

Guardrails exist to prevent catastrophic regressions, not to score quality.
