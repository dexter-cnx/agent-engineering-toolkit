# Example: Flutter Deep Link Full Optimization Cycle

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
| correctness | 0.30 | 0.80 | Steps are correct; step 3 is compound ("add... and register...") |
| scope_discipline | 0.15 | 0.80 | Good Use when / Do NOT use when coverage |
| simplicity | 0.15 | 0.80 | 7 steps for 4 deliverables is appropriate |
| verifiability | 0.15 | 0.60 | adb command is concrete; "confirm routing" is vague |
| architecture_alignment | 0.10 | 0.70 | No violations; router mentioned but no explicit adapter reference |
| token_efficiency | 0.10 | 0.85 | Tight prose; no filler |
| docs_hygiene | 0.05 | 1.00 | All 13 sections present, no placeholders, references resolve |

**Baseline final_score**: `0.7725`  
**Token count**: `487`  
**Quality/1k tokens**: `1.586`

---

## 2. Mutation Candidates

Three candidates were generated (one per mutation type):

### Candidate 1: `decomposition_steps`
**File**: `evals/testcases/flutter_deeplink/candidate_01_decomposition_steps.md`

Step 3 in the baseline reads: *"Add a new GoRoute… and register it with the route registry."*
This compound step is split into:
- Step 3: *"Add a new GoRoute with the correct path and builder."*
- Step 4: *"Register the new route in `lib/app/router/route_registry.dart`."*
- (Steps 4–7 become 5–9)

**Token count**: `497` (+2.1%)

### Candidate 2: `verification_ordering`
**File**: `evals/testcases/flutter_deeplink/candidate_02_verification_ordering.md`

The Validation checklist is reordered: the concrete `flutter test` and `flutter analyze` commands
move to the top, followed by the `adb` command, and the review step moves last.

**Token count**: `487` (unchanged)

### Candidate 3: `token_budget` (not shown as separate file — generated at runtime)

Filler phrases are removed. In this case, there are no filler phrases in the baseline, so the
mutation produces an almost-identical document with slightly collapsed whitespace.

**Token count**: `661` (+35.7%)

---

## 3. Regression Check Results

| Candidate | Sections OK | No Arch Violations | Behavior Preserved | Result |
|-----------|-------------|-------------------|-------------------|--------|
| decomposition_steps | PASS | PASS | PASS | **PASS** |
| verification_ordering | PASS | PASS | PASS | **PASS** |
| token_budget | PASS | PASS | PASS | **PASS** |

All three candidates pass regression checks.

---

## 4. Candidate Evaluation

| Candidate | final_score | Tokens | Quality/1k | Score Delta |
|-----------|-------------|--------|------------|-------------|
| baseline | 0.7725 | 487 | 1.586 | — |
| decomposition_steps | **0.7846** | 497 | 1.579 | **+0.0121** |
| verification_ordering | 0.7612 | 487 | 1.563 | -0.0113 |
| token_budget | 0.7390 | 661 | 1.118 | -0.0335 |

---

## 5. Token Policy

Token policy check: reject if token increase > 35% AND score improvement < 5%.

| Candidate | Token Δ% | Score Δ | Policy Verdict |
|-----------|----------|---------|----------------|
| decomposition_steps | +2.1% | +0.0121 | PASS (token increase is minimal) |
| verification_ordering | 0% | -0.0113 | PASS (no token increase) |
| token_budget | **+35.7%** | **-0.0335** | **REJECT** (exceeds threshold, score decreased) |

`token_budget` is rejected by token policy: +35.7% tokens with -0.0335 score change violates both conditions.

---

## 6. Winner Selection

After token policy filtering, two candidates remain:

| Candidate | final_score | vs Baseline |
|-----------|-------------|-------------|
| decomposition_steps | **0.7846** | +0.0121 |
| verification_ordering | 0.7612 | -0.0113 |

**Winner**: `decomposition_steps` — only candidate that beats the baseline score.

---

## 7. Promotion Decision: PROMOTE

```
Decision: PROMOTE
Winner: baseline-decomposition_steps
Mutation: decomposition_steps
Score delta: +0.0121 (+1.57%)
Token delta: +2.1%
Reasoning: Candidate baseline-decomposition_steps (mutation: decomposition_steps)
           improved score by +0.0121 (+1.6%) with token delta +2.1%.
           All regression checks passed. Token policy satisfied.
```

The promoted skill is written to the target path. The previous version is backed up as
`SKILL.<timestamp>.bak.md`.

---

## 8. Generated Report

The run produces:

- `reports/latest_report.md` — human-readable Markdown report
- `reports/history/run-demo-flutter-deeplink.md` — archived copy
- `memory/score_history.json` — updated with this run's summary
- `memory/candidate_archive.json` — updated with all three candidates

---

## 9. How to Reproduce

```bash
# Evaluate the baseline
python -m runners.eval_runner \
  --skill evals/testcases/flutter_deeplink/baseline.md \
  --pretty

# Run the full cycle (dry-run — no file written)
python -m runners.optimization_cycle \
  --skill evals/testcases/flutter_deeplink/baseline.md \
  --n 3 \
  --dry-run \
  --pretty \
  --report-only
```

Expected exit codes:
- `eval_runner` → exit 0 (score 0.7725 > 0.60 threshold)
- `optimization_cycle --dry-run` → exit 0 (PROMOTE decision, dry-run so no file written)
