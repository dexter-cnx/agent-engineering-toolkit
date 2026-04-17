# karpathy-guidelines

## Purpose
Apply the Karpathy Layer V2 evaluation criteria to a skill or prompt to assess its quality across seven weighted dimensions before submitting it for automated optimization.

## Use when
- You are writing or reviewing a new skill and want a pre-flight quality check before running the automated eval pipeline
- You need to explain why a skill scored low on a specific dimension and propose targeted improvements
- You are onboarding a contributor and need to teach the evaluation model by example
- You want to triage a low-scoring skill (below 0.60) before investing in a full mutation cycle

## Do NOT use when
- You only need a numeric score — use `runners/eval_runner.py` directly — use a more specific skill instead.
- You want to generate mutation candidates — use the `karpathy-mutation` skill instead — use a more specific skill instead.
- You are checking for regression safety — use the `karpathy-regression` skill instead — use a more specific skill instead.
- The skill is already above 0.85 and no specific dimension concern has been raised

## Inputs required
- The full SKILL.md content (all 13 sections)
- The dimension weights from `evals/rubrics/coding_task_rubric.v1.json`
- The specific concern or dimension the reviewer wants to focus on (optional)

## Constraints
- Apply the weights exactly: correctness 0.30, scope_discipline 0.15, simplicity 0.15, verifiability 0.15, architecture_alignment 0.10, token_efficiency 0.10, docs_hygiene 0.05
- Do not substitute subjective opinion for the rubric criteria
- Do not score a dimension higher than 0.8 if the Validation checklist has no executable items
- Do not score docs_hygiene above 0.6 if any placeholder text (TODO, TBD, FIXME, {{}}) exists

## Step-by-step workflow
1. Read all 13 sections of the skill and confirm none are empty or contain placeholder text.
2. Score `correctness` (0.30): check that workflow steps are ordered correctly, technically accurate, and the output contract matches the stated purpose.
3. Score `scope_discipline` (0.15): count bullets in "Use when" and "Do NOT use when" — each section must have at least two items that cover distinct cases.
4. Score `simplicity` (0.15): count numbered steps and total word count — flag any step containing " and " as a compound step, and any filler phrases.
5. Score `verifiability` (0.15): read the Validation checklist — each bullet must contain an action verb (run, check, grep, confirm, assert, verify).
6. Score `architecture_alignment` (0.10): check whether any steps recommend placing logic in the wrong layer (e.g., SDK calls in presentation widgets).
7. Score `token_efficiency` (0.10): flag repeated content, filler sentences ("It is important to note that…"), and unnecessary preamble.
8. Score `docs_hygiene` (0.05): confirm all 13 sections are present, no forbidden strings, and References section links to real files.
9. Compute weighted final_score = sum(weight_i × score_i).
10. List the two lowest-scoring dimensions and propose one concrete improvement for each.

## Output contract
- A score table with one row per dimension (name, weight, score, rationale in one sentence)
- A computed final_score (rounded to 4 decimal places)
- A binary checks summary (pass/fail for each of the 6 checks)
- A prioritised improvement list (at most 3 items, highest ROI first)

## Validation checklist
- Confirm all 7 dimension scores are in [0.0, 1.0]
- Confirm final_score = sum(weight × score) for all 7 dimensions
- Confirm at least one improvement recommendation is actionable (not vague)
- Confirm binary checks match the actual skill content (not assumed)

## Related skills
- `karpathy-mutation` — generate candidates based on low-scoring dimensions
- `karpathy-regression` — check candidates for structural integrity
- `karpathy-optimizer` — apply token policy and select the best candidate

## References
- [`../../evals/rubrics/coding_task_rubric.v1.json`](../../evals/rubrics/coding_task_rubric.v1.json)
- [`../../docs/eval-system.md`](../../docs/eval-system.md)
- [`../../examples/flutter_deeplink_full_cycle.md`](../../examples/flutter_deeplink_full_cycle.md)

## Real example
Historical static snapshot: a reviewer applies this skill to `flutter-go-router-deeplink-wireup/SKILL.md`. The Validation checklist has three bullets, two of which say "ensure deep links work" and "make sure tests pass" — both are vague. `verifiability` scores 0.40. The improvement recommendation is: "Replace 'ensure deep links work' with 'Run `flutter test test/routing/deep_link_test.dart` and confirm exit code 0'."

## Real file output sample
```text
docs/eval-sessions/flutter-deeplink-manual-eval.md
reports/latest_report.md
```
