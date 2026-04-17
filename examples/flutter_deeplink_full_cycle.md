# Example: Flutter Deep Link Full Optimization Cycle

This is a static worked example snapshot. It is intentionally separate from the runtime
artifacts written to `reports/` and `memory/`.

This document walks through a complete Karpathy Layer V2 optimization run on the
`flutter-go-router-deeplink-wireup` skill.

---

## 1. Baseline Skill

**File**: `evals/testcases/flutter_deeplink/baseline.md`  
**Skill ID**: `flutter-go-router-deeplink-wireup`

The baseline is the unmodified skill covering go_router deep link wireup for Flutter apps.
It has 7 workflow steps, 4 output contract deliverables, and a 4-item validation checklist.

**Baseline Evaluation**:

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| correctness | 0.30 | 0.90 | Steps are correct and already express the target workflow clearly |
| scope_discipline | 0.15 | 1.00 | Use / Do NOT use coverage matches the router-specific use case |
| simplicity | 0.15 | 0.80 | 7 steps for 4 deliverables is appropriate |
| verifiability | 0.15 | 1.00 | Validation commands are concrete and executable |
| architecture_alignment | 0.10 | 0.70 | No violations; router mentioned but no explicit adapter reference |
| token_efficiency | 0.10 | 1.00 | Tight prose with no filler in the current snapshot |
| docs_hygiene | 0.05 | 1.00 | All 13 sections present, no placeholders, references resolve |

**Baseline final_score**: `0.9100`  
**Token count**: `757`  
**Quality/1k tokens**: `1.2021`

---

## 2. Mutation Candidates

Two candidates were generated:

### Candidate 1: `decomposition_steps`
**File**: `evals/testcases/flutter_deeplink/candidate_01_decomposition_steps.md`

This candidate splits the compound workflow step into smaller atomic steps without changing
the underlying behavior or output contract.

**Token count**: `757` (0.0%)

### Candidate 2: `verification_ordering`
**File**: `evals/testcases/flutter_deeplink/candidate_02_verification_ordering.md`

This candidate reorders the validation checklist so that the concrete checks appear first.
The behavior and output contract remain unchanged.

**Token count**: `757` (0.0%)

---

## 3. Regression Check Results

| Candidate | Sections OK | No Arch Violations | Behavior Preserved | Result |
|-----------|-------------|-------------------|-------------------|--------|
| decomposition_steps | PASS | PASS | PASS | **PASS** |
| verification_ordering | PASS | PASS | PASS | **PASS** |

Both candidates pass regression checks.

---

## 4. Candidate Evaluation

| Candidate | final_score | Tokens | Quality/1k | Score Delta |
|-----------|-------------|--------|------------|-------------|
| baseline | 0.9100 | 757 | 1.2021 | - |
| decomposition_steps | 0.9100 | 757 | 1.2021 | 0.0000 |
| verification_ordering | 0.9100 | 757 | 1.2021 | 0.0000 |

---

## 5. Token Policy

Token policy check: reject if token increase > 35% AND score improvement < 5%.

| Candidate | Token Δ% | Score Δ | Policy Verdict |
|-----------|----------|---------|----------------|
| decomposition_steps | 0% | 0.0000 | PASS (no token increase) |
| verification_ordering | 0% | 0.0000 | PASS (no token increase) |

Both candidates satisfy token policy.

## 6. Winner Selection

After token policy filtering, both candidates remain, but neither beats the baseline score.

| Candidate | final_score | vs Baseline |
|-----------|-------------|-------------|
| decomposition_steps | 0.9100 | 0.0000 |
| verification_ordering | 0.9100 | 0.0000 |

**Winner**: none - both candidates tie the baseline score.

## 7. Promotion Decision: REJECT

```
Decision: REJECT
Winner: none
Mutation: none
Score delta: 0.0000 (0.00%)
Token delta: 0.0%
Reasoning: No candidate exceeded the baseline score. Regression checks passed
           and token policy was satisfied, but promotion requires a strict
           improvement.
```

No skill file is written because the run is dry-run or rejected. The report still records
the decision trace, baseline, and candidate archive entries.

---

## 8. Generated Report

This snapshot produces:

- `reports/latest_report.md` - human-readable Markdown report
- `reports/history/` - runtime report location
- `memory/score_history.json` - updated with this run's summary
- `memory/candidate_archive.json` - updated with both candidates

---

## 9. How to Reproduce

```bash
rtk bash scripts/karpathy-eval.sh evals/testcases/flutter_deeplink/baseline.md --pretty
rtk bash scripts/karpathy-run-cycle.sh evals/testcases/flutter_deeplink/baseline.md --dry-run --n 2 --pretty --report-only
```

Expected exit codes:
- `eval_runner` -> exit 0 (score 0.9100 > 0.60 threshold)
- `optimization_cycle --dry-run` -> exit 2 (REJECT decision, no file written)
