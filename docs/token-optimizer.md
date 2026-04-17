# Token Optimizer

## Purpose

The token optimizer ensures that promoted skills do not grow unnecessarily verbose.
It enforces a policy that rejects candidates that cost significantly more tokens
without delivering meaningful quality improvement.

---

## Core Metric

```
quality_per_1k_tokens = final_score / (token_count / 1000)
```

Higher values indicate a more efficient skill.  Two skills with the same quality score
but different token counts produce different quality_per_1k_tokens values — the shorter one wins.

---

## Token Policy

```
Reject a candidate if:
    token_increase_pct > 0.35   (more than 35% more tokens than baseline)
    AND
    score_improvement < 0.05    (less than 5% score improvement over baseline)
```

Where:
```
token_increase_pct = (candidate_token_count - baseline_token_count) / baseline_token_count
score_improvement  = candidate_final_score - baseline_final_score
```

### Rationale

- A candidate that uses 35% more tokens must justify that cost with a significant quality gain.
- The 5% threshold (0.05 on a 0–1 scale) represents a meaningful, measurable improvement.
- Small score gains do not justify large token increases — this would degrade the system's
  efficiency over repeated optimization cycles.

### Preference ordering

When multiple candidates pass the policy, rank by `final_score` descending.
If two candidates have equal scores, prefer the one with fewer tokens (lower token_count wins ties).

---

## Token Count Estimation

Token count is estimated as `ceil(word_count × 1.3)`.

This is a word-based approximation consistent with GPT-family tokenisers for English prose.
It is intentionally simple to ensure reproducibility without external dependencies.

---

## Token Budget per Skill

Skills can declare a `token_budget` in their `skill_contract.yaml`.
When set, `token_budget` is the maximum token count a candidate can have after promotion.
A candidate exceeding `token_budget` is rejected regardless of its score.

---

## Token Policy in the `token_budget` Mutation

The `token_budget` mutation type specifically targets token reduction.
It is designed to test whether removing filler improves quality_per_1k_tokens.

A paradox can occur: if the baseline already has no filler, the `token_budget` mutation
produces an almost-identical candidate.  If whitespace normalisation slightly increases
the byte count while leaving word count unchanged, the token count may appear higher.
The policy catches this: +0% score and +0.x% tokens → PASS (well under the 35% threshold).

---

## Examples

| Baseline score | Candidate score | Baseline tokens | Candidate tokens | Token Δ% | Score Δ | Policy |
|----------------|-----------------|-----------------|------------------|----------|---------|--------|
| 0.72 | 0.78 | 487 | 497 | +2.1% | +0.06 | PASS |
| 0.72 | 0.73 | 487 | 661 | +35.7% | +0.01 | REJECT (Δ tokens > 35%, Δ score < 5%) |
| 0.72 | 0.80 | 487 | 700 | +43.7% | +0.08 | PASS (+8% score justifies +43% tokens) |
| 0.72 | 0.71 | 487 | 487 | 0% | -0.01 | PASS by policy, REJECT by Gate 3 (no improvement) |
