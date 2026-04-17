# karpathy-mutation

## Purpose
Generate controlled single-dimension mutation candidates from a baseline SKILL.md, producing one variant per mutation type so that each can be independently evaluated.

## Use when
- You have a baseline EvalResult and want to explore whether targeted changes improve the score
- The baseline scores below 0.85 on at least one dimension and you have identified the lowest-scoring dimensions
- You are running a full optimization cycle and need the mutation stage to produce candidates
- You want to test whether decomposing compound steps or tightening wording improves correctness or simplicity scores

## Do NOT use when
- The baseline final_score is already above 0.90 — the improvement margin is unlikely to justify the cycle cost — use a more specific skill instead.
- You want to change multiple dimensions at once — that violates the one-dimension constraint and makes it impossible to isolate the cause of any score change — use a more specific skill instead.
- You have not yet run `karpathy-evaluation` on the baseline — you need a baseline score before mutating — use a more specific skill instead.
- The skill has failing binary checks — fix structural issues before running mutations — use a more specific skill instead.

## Inputs required
- Full baseline SKILL.md content
- A stable `skill_id` and `parent_id` (use `"baseline"` for unmodified content)
- The desired number of candidates (1–6, default 5)
- The baseline EvalResult (to know which dimensions to prioritise)

## Constraints
- Each candidate must change exactly ONE mutation dimension
- All 13 required SKILL.md sections must be present in every candidate
- The Purpose and Output contract sections must not be emptied or materially degraded
- Mutation must not introduce forbidden strings (TODO, TBD, FIXME, {{}})
- Each candidate_id must be stable: `<parent_id>-<mutation_type>`

## Step-by-step workflow
1. Confirm the baseline content has all 13 required sections and no placeholder text.
2. For each selected mutation type (up to n), apply exactly the one-dimension transformation described in `docs/mutation-system.md`.
3. After each mutation, verify that the section count in the candidate equals the section count in the baseline.
4. Count tokens for each candidate: `ceil(word_count × 1.3)`.
5. Assemble each MutationCandidate dict with: candidate_id, parent_id, mutation_type, mutation_description, content, token_count.
6. Return the list of candidates for downstream regression and evaluation.

## Output contract
- A list of MutationCandidate dicts, each matching `evals/schemas/run_report.schema.json#/definitions/MutationCandidate`
- Each dict includes: candidate_id, parent_id, mutation_type, mutation_description, content, token_count
- At most 6 candidates per run (one per mutation type)
- The list is appended to `memory/candidate_archive.json`

## Validation checklist
- Confirm each candidate has exactly 12 `## ` section headers (matching the baseline count)
- Confirm each candidate_id follows the pattern `<parent_id>-<mutation_type>`
- Confirm no candidate content contains TODO, TBD, FIXME, or `{{`
- Run `python -m runners.mutation_runner --skill <path> --n 3` and confirm valid JSON returned
- Confirm the `mutation_description` accurately describes what changed in one sentence

## Related skills
- `karpathy-evaluation` — must be run on baseline before calling this skill
- `karpathy-regression` — must be run on every candidate output from this skill
- `karpathy-optimizer` — selects the best candidate from this skill's output

## References
- [`../../docs/mutation-system.md`](../../docs/mutation-system.md)
- [`../../agents/mutation_agent.py`](../../agents/mutation_agent.py)
- [`../../evals/testcases/flutter_deeplink/`](../../evals/testcases/flutter_deeplink/)

## Real example
Given the flutter deep link baseline, the `decomposition_steps` mutation finds the compound step "Configure the route and register it in the router" and splits it into "Configure the route in `app_router.dart`" and "Register the route in `route_registry.dart`". The `simplicity` dimension improves from 0.75 to 0.88 because each step is now independently executable.

## Real file output sample
```text
memory/candidate_archive.json
```
