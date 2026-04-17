# Eval System

## Purpose

The eval system produces a numeric quality score for any SKILL.md using a deterministic
weighted rubric.  Scores are reproducible: the same content always produces the same score.
When a testcase includes `expected_result.json`, the orchestrator also validates the run
against that fixture and records the result in the report.

---

## Scoring Model

```
final_score =
  0.30 × correctness
  0.15 × scope_discipline
  0.15 × simplicity
  0.15 × verifiability
  0.10 × architecture_alignment
  0.10 × token_efficiency
  0.05 × docs_hygiene
```

Weights sum to 1.0.  All dimension scores are in [0.0, 1.0].

---

## Dimensions

### correctness (0.30)
Measures whether the workflow steps are technically accurate, logically ordered, and whether
the output contract covers all the deliverables implied by the purpose.

Scoring levels:
- 1.0: All steps correct, optimal order, output contract complete
- 0.8: One minor ordering issue or one gap in the output contract
- 0.6: One technical inaccuracy or a missing non-trivial sub-step
- 0.4: Multiple incorrect steps or output contract mismatch
- 0.2: Cannot produce correct result in most cases

### scope_discipline (0.15)
Measures whether the skill does exactly what it promises — no more, no less.

Scoring levels:
- 1.0: Tight scope, ≥ 2 "Use when" triggers, ≥ 2 "Do NOT use when" cases, no scope creep
- 0.8: One missing refusal case
- 0.6: Steps go beyond stated purpose or important refusal case absent
- 0.4: Steps regularly exceed the stated purpose

### simplicity (0.15)
Measures whether the skill achieves its goal in the fewest necessary steps.

Scoring levels:
- 1.0: Every step necessary, no redundant checks, no speculative abstractions
- 0.8: One non-essential step present
- 0.6: Two or three unnecessary steps
- 0.4: Noticeably bloated

Proxy: words_per_step ratio + filler phrase penalty.

### verifiability (0.15)
Measures whether every claim can be confirmed by running a concrete check.

Scoring levels:
- 1.0: All validation checklist items are executable (grep, run test, open file)
- 0.8: Mostly executable, one or two subjective judgments
- 0.6: Half the checklist is vague
- 0.4: Checklist is mostly subjective or absent

Proxy: ratio of action-keyword bullets to total bullets in the Validation checklist.

### architecture_alignment (0.10)
Measures whether the skill respects layer boundaries for the target stack.

Scoring levels:
- 1.0: All file placements and operations respect canonical architecture layers
- 0.8: One minor layer boundary question
- 0.6: One clear violation (e.g., presentation calling SDK directly)
- 0.4: Multiple violations or structural anti-pattern recommended

### token_efficiency (0.10)
Measures whether the skill communicates its intent concisely.

Scoring levels:
- 1.0: Dense and precise, no filler, no repetition
- 0.8: One paragraph of padding
- 0.6: ~20% unnecessary tokens
- 0.4: Important content buried in filler

Proxy: paragraph uniqueness ratio minus filler phrase penalty.

### docs_hygiene (0.05)
Measures structural completeness and cleanliness.

Scoring levels:
- 1.0: All 13 sections present, no forbidden strings, references resolve, title matches folder
- 0.8: One minor issue (one dead reference link)
- 0.6: Missing one section or one placeholder remains
- 0.4: Multiple missing sections or multiple placeholders

---

## Binary Checks

Binary checks are pass/fail and supplement the dimension scores.

| Check | Description |
|-------|-------------|
| `has_purpose_section` | `## Purpose` section is non-empty |
| `has_workflow_steps` | `## Step-by-step workflow` has ≥ 2 numbered steps |
| `no_placeholder_text` | No unfinished placeholder markers are present |
| `has_validation_checklist` | `## Validation checklist` has ≥ 1 bullet |
| `has_output_contract` | `## Output contract` has ≥ 1 bullet |
| `has_real_example` | `## Real example` has non-empty prose |

A skill with any failing binary check cannot be promoted regardless of its final_score.

For full-cycle runs, the report splits evaluation into explicit components:
- `rubric_score` = weighted `final_score`
- `binary_checks` = pass/fail summary of the evaluator's structural checks
- `regression_check` = pass/fail summary of the regression gate on candidates
- `expected_result_validation` = pass/fail/not_applicable when `expected_result.json` exists next to the testcase

---

## Token Count Estimation

Token count is estimated as `ceil(word_count × 1.3)`.

This is intentionally simple and consistent — it does not use a tokeniser so it produces
the same result in any environment without external dependencies.

`quality_per_1k_tokens = final_score / (token_count / 1000)`

Higher quality_per_1k_tokens indicates a more efficient skill.

---

## Running the Evaluator

```bash
./scripts/karpathy-eval.sh <skill>
```

The wrapper evaluates the skill, writes `memory/score_history.json` when the workflow asks
for history, and exits `2` when the score is below the promotion threshold.

For full-cycle runs, the report also includes:
- a structured promotion decision trace
- optional expectation-backed validation when `expected_result.json` is present next to the skill

---

## Adding a New Rubric

1. Copy `evals/rubrics/coding_task_rubric.v1.json` to `coding_task_rubric.v2.json`.
2. Adjust `weights` — they must sum to 1.0.
3. Update `dimensions` with new scoring levels.
4. Pass `--rubric evals/rubrics/coding_task_rubric.v2.json` to `eval_runner.py`.
