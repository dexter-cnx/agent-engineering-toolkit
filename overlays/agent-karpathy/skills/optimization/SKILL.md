# karpathy-optimizer

## Purpose
Select the best mutation candidate using token efficiency policy and score delta, then promote it to disk or return a REJECT decision with reasoning.

## Use when
- You have a set of regression-passing candidate EvalResults and need to decide which (if any) to promote
- The final_score of at least one candidate exceeds the baseline final_score
- You need a machine-readable PromotionDecision dict for downstream reporting
- You are running the last stage of a full optimization cycle before writing the report

## Do NOT use when
- Regression checks have not been run yet — call `karpathy-regression` first — use a more specific skill instead.
- No candidates passed regression — the optimizer requires at least one passing candidate — use a more specific skill instead.
- You want to force-promote a candidate regardless of score — the optimizer enforces the 0.60 floor — use a more specific skill instead.
- You are in a dry-run context where you only want to see the decision without writing to disk — pass `dry_run=True` to the runner

## Inputs required
- The baseline EvalResult (from `karpathy-evaluation` run on the unmodified skill)
- A list of candidate EvalResults (from `karpathy-evaluation` run on each passing candidate)
- A list of MutationCandidate dicts (matching the candidate_evals by candidate_id)
- The skill_path to write the promoted content (if decision is PROMOTE and not dry-run)
- A dry_run flag (default: False for production runs, True for CI eval-only workflows)

## Constraints
- Apply token policy before ranking: reject any candidate where token increase > 35% AND score improvement < 5%
- A candidate must score at least 0.60 (absolute floor) to be eligible for promotion
- A candidate must exceed the baseline score to be eligible for promotion — equal score is a REJECT
- Back up the existing SKILL.md as `SKILL.<timestamp>.bak.md` before writing the winner
- The PromotionDecision must include reasoning that names the winner_id, mutation_type, score_delta, and token_delta_pct

## Step-by-step workflow
1. For each candidate EvalResult, compute token_increase_pct = (candidate_tokens - baseline_tokens) / baseline_tokens.
2. Apply token policy: if token_increase_pct > 0.35 AND score_improvement < 0.05, mark as token_policy_passed = False and exclude from ranking.
3. Sort remaining candidates by final_score descending.
4. Select the top-scoring candidate as the winner.
5. If winner.final_score <= baseline.final_score, return decision = REJECT with reasoning.
6. If winner.final_score < 0.60, return decision = REJECT with reasoning.
7. If not dry_run, write backup of existing skill and write winner content to skill_path.
8. Return PromotionDecision with: winner_id, decision = PROMOTE, reasoning, score_delta, token_delta_pct, promoted_path.

## Output contract
- A PromotionDecision dict with: winner_id (str or null), decision ("PROMOTE" or "REJECT"), reasoning (str), score_delta (float or null), token_delta_pct (float or null), promoted_path (str or null), token_policy_applied (bool), token_policy_rejections (list of str)
- If PROMOTE: the winning SKILL.md is written to skill_path and the previous version is backed up
- The decision is appended to `memory/score_history.json` via the Orchestrator

## Validation checklist
- Confirm token_policy_rejections contains all candidate_ids where token_increase_pct > 0.35 and score_improvement < 0.05
- Confirm winner_id is null when decision is REJECT
- Confirm the backup file exists at `SKILL.<timestamp>.bak.md` when decision is PROMOTE and not dry_run
- Run `python -m runners.promotion_runner --dry-run ...` and confirm no file is written

## Related skills
- `karpathy-regression` — must complete before calling this skill
- `karpathy-evaluation` — provides the EvalResult inputs this skill needs
- `karpathy-guidelines` — for understanding why a candidate scored as it did

## References
- [`../../agents/promotion_agent.py`](../../agents/promotion_agent.py)
- [`../../docs/promotion-system.md`](../../docs/promotion-system.md)
- [`../../docs/token-optimizer.md`](../../docs/token-optimizer.md)

## Real example
Historical static snapshot: three candidates pass regression for the flutter deep link skill. Candidate `baseline-token_budget` is rejected by token policy (+40% tokens, only +2% score). Of the remaining two, `baseline-decomposition_steps` scores 0.7834 (+0.06 above baseline) and `baseline-verification_ordering` scores 0.7612 (+0.04). The optimizer promotes `baseline-decomposition_steps`, writes the backup, and returns reasoning: "Candidate baseline-decomposition_steps improved score by +0.0600 (+8.3%) with token delta +2.1%."

## Real file output sample
```text
overlays/agent-karpathy/skills/evaluation/SKILL.20260417T120000.bak.md
overlays/agent-karpathy/skills/evaluation/SKILL.md
reports/latest_report.md
```
