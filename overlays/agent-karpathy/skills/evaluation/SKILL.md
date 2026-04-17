# karpathy-evaluation

## Purpose
Produce a structured EvalResult JSON for a given SKILL.md by applying the weighted rubric, running binary checks, and estimating token count.

## Use when
- You need a machine-readable quality score for a skill before deciding whether to mutate it
- You are comparing baseline vs candidate scores and need consistent, reproducible numbers
- You are running a CI gate that must fail if the skill scores below 0.60
- You are building a report and need per-dimension breakdown alongside the final score

## Do NOT use when
- You only want a qualitative review without numeric output — use `karpathy-guidelines` instead — use a more specific skill instead.
- You are generating mutations — that is the `karpathy-mutation` skill's responsibility — use a more specific skill instead.
- You need to check regression safety — use `karpathy-regression` instead — use a more specific skill instead.
- The skill does not follow the 13-section SKILL.md format (e.g., foundation skills use README.md)

## Inputs required
- Full content of the SKILL.md to evaluate
- The parsed rubric dict from `evals/rubrics/coding_task_rubric.v1.json`
- A stable `skill_id` (typically derived from the directory name)
- A `candidate_id` (use `"baseline"` for unmodified skills)

## Constraints
- Use the exact weights from the rubric: correctness 0.30, scope_discipline 0.15, simplicity 0.15, verifiability 0.15, architecture_alignment 0.10, token_efficiency 0.10, docs_hygiene 0.05
- Token count must be estimated as `ceil(word_count × 1.3)` for consistency across runs
- `quality_per_1k_tokens` must equal `final_score / (token_count / 1000)`
- Never set `regression_passed = True` in this skill — that field is set by the regression agent
- Binary checks are pass/fail only, not partial credit

## Step-by-step workflow
1. Load the SKILL.md content and the rubric from `evals/rubrics/coding_task_rubric.v1.json`.
2. Count tokens: split content on whitespace, multiply word count by 1.3, ceiling-round.
3. Score each of the 7 dimensions using the rubric criteria and scoring levels.
4. Compute `final_score = sum(weight × score)` across all 7 dimensions.
5. Compute `quality_per_1k_tokens = final_score / (token_count / 1000)`.
6. Run all 6 binary checks (has_purpose_section, has_workflow_steps, no_placeholder_text, has_validation_checklist, has_output_contract, has_real_example).
7. Set `binary_checks_passed = all(binary_checks.values())`.
8. Set `regression_passed = True` as a placeholder — downstream regression agent overwrites this.
9. Assemble and return the EvalResult dict matching `evals/schemas/skill_eval.schema.json`.

## Output contract
- An EvalResult dict with fields: skill_id, candidate_id, mutation_type, scores (7 dimensions), final_score, token_count, quality_per_1k_tokens, binary_checks (6 keys), binary_checks_passed, regression_passed, evaluator_notes, timestamp
- The dict must validate against `evals/schemas/skill_eval.schema.json`
- `evaluator_notes` must name the two lowest-scoring dimensions if any score below 0.5

## Validation checklist
- Confirm `sum(weight × score) == final_score` to within floating-point tolerance (1e-6)
- Confirm all 7 dimension score keys are present in the `scores` dict
- Confirm `quality_per_1k_tokens > 0` when `token_count > 0`
- Run `python -m runners.eval_runner --skill <path>` and confirm valid JSON is returned
- Confirm `timestamp` is a valid ISO 8601 datetime string

## Related skills
- `karpathy-guidelines` — manual qualitative application of the same criteria
- `karpathy-mutation` — uses EvalResult to decide which dimensions to mutate
- `karpathy-optimizer` — uses EvalResult to rank candidates and apply token policy

## References
- [`../../evals/schemas/skill_eval.schema.json`](../../evals/schemas/skill_eval.schema.json)
- [`../../evals/rubrics/coding_task_rubric.v1.json`](../../evals/rubrics/coding_task_rubric.v1.json)
- [`../../agents/evaluator_agent.py`](../../agents/evaluator_agent.py)

## Real example
Historical static snapshot: running the evaluator on `flutter-go-router-deeplink-wireup/SKILL.md` returns final_score 0.7234 with correctness 0.80, scope_discipline 0.70, simplicity 0.90, verifiability 0.60 (two vague checklist items), architecture_alignment 0.70, token_efficiency 0.85, docs_hygiene 1.0. The `evaluator_notes` field reads: "Low-scoring dimensions: verifiability. Failed binary checks: none."

## Real file output sample
```text
memory/score_history.json
reports/latest_report.md
```
