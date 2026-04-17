# Promotion System

## Purpose

The promotion system decides whether a mutation candidate is good enough to replace the
current baseline skill.  It applies multiple gates in sequence and writes the winner to
disk only when all gates pass.

---

## Promotion Gates

Gates are applied in order.  A candidate that fails any gate is excluded from further consideration.

```
Candidates
    │
    ▼
Gate 1: Regression passed?
    │ No  → excluded (regression_failures list)
    ▼
Gate 2: Token policy passed?
    │ No  → excluded (token_policy_rejections list)
    ▼
Gate 3: Score > baseline?
    │ No  → REJECT decision
    ▼
Gate 4: Score ≥ 0.60 (absolute floor)?
    │ No  → REJECT decision
    ▼
PROMOTE decision → write to disk (unless dry_run)
```

---

## Gate 1: Regression

A candidate passes Gate 1 only if `RegressionAgent.check_silent()` returns `passed = True`.
See `docs/guardrails.md` for the full list of checks.

Candidates that fail regression are listed in `regression_failures` in the RunReport.

---

## Gate 2: Token Policy

```python
token_increase_pct = (candidate_tokens - baseline_tokens) / baseline_tokens
score_improvement  = candidate_final_score - baseline_final_score

if token_increase_pct > 0.35 and score_improvement < 0.05:
    reject  # token policy violation
```

This policy prevents candidates from being promoted when they cost significantly more tokens
without delivering meaningful quality improvement.

Candidates that fail Gate 2 are listed in `token_policy_rejections` in the RunReport.

---

## Gate 3: Score Improvement

The top-scoring remaining candidate must exceed the baseline `final_score`.
A tie is a REJECT — equal quality does not justify a promotion.

---

## Gate 4: Absolute Floor

The winner must have `final_score ≥ 0.60`.  This floor exists to prevent a skill from being
promoted to a state that still fails CI quality gates.

---

## File Writing

When decision = PROMOTE and dry_run = False:

1. The existing SKILL.md is copied to `SKILL.<UTC_TIMESTAMP>.bak.md` in the same directory.
2. The winner content is written to `SKILL.md`.
3. `promoted_path` in the RunReport is set to the skill path.

When dry_run = True: no files are written.  The RunReport records the would-be winner.

---

## PromotionDecision Fields

| Field | Type | Description |
|-------|------|-------------|
| `winner_id` | str or null | candidate_id of the winner, or null if REJECT |
| `decision` | "PROMOTE" or "REJECT" | Final decision |
| `reasoning` | str | One paragraph explaining the decision |
| `score_delta` | float or null | Winner score minus baseline score |
| `token_delta_pct` | float or null | Token count change as fraction |
| `promoted_path` | str or null | Path where winner was written |
| `token_policy_applied` | bool | Whether any candidate was filtered by token policy |
| `token_policy_rejections` | list[str] | candidate_ids filtered by token policy |
| `baseline_score` | float or null | Baseline final score used in the decision |
| `baseline_token_count` | int or null | Baseline token count used in the decision |
| `winner_score` | float or null | Winning candidate final score, if any |
| `winner_token_count` | int or null | Winning candidate token count, if any |

---

## Running the Promotion Runner

```bash
python -m runners.promotion_runner \
  --baseline-eval   memory/baseline_eval.json \
  --candidate-evals memory/candidate_evals.json \
  --candidates      memory/candidates.json \
  --skill           overlays/agent-karpathy/skills/evaluation/SKILL.md \
  --dry-run
```

Exit codes: `0` = PROMOTE, `1` = REJECT, `2` = input error.
