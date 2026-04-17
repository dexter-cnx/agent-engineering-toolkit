# karpathy-regression

## Purpose
Enforce structural and behavioral guardrails on mutation candidates before any promotion decision is made, hard-failing on any violation.

## Use when
- You have generated mutation candidates and need to verify none of them break existing behavior, remove required sections, or introduce architecture violations
- You are running a CI gate and need a hard stop before a potentially broken skill reaches the promotion stage
- A candidate has an unexpectedly high score and you want to confirm it was not achieved by removing constraints or degrading the output contract
- You are manually reviewing a candidate before committing it to the repository

## Do NOT use when
- You are checking the baseline skill before mutation — regression is for candidates only — use a more specific skill instead.
- You only want a quality score — use `karpathy-evaluation` instead — use a more specific skill instead.
- The skill is not in SKILL.md format (regression checks assume the 13-section schema) — use a more specific skill instead.
- You are reviewing policies, templates, or documentation files (not SKILL.md content)

## Inputs required
- One or more MutationCandidate dicts (output of `karpathy-mutation`)
- The baseline SKILL.md content (to compare section counts and output contract)
- The skill_path (to check forbidden file paths)

## Constraints
- Must hard-fail (exit 1) if ANY of the five checks fail for a candidate
- Must not modify any file during a check — read-only inspection only
- Must return a RegressionResult for every candidate, even if some pass and others fail
- Forbidden mutation paths include: AGENTS.md, AGENTS.overlay.md, docs/prompt-pipeline.md, evals/rubrics/, evals/schemas/, .github/workflows/
- A candidate that removes an existing H2 section always fails — no exceptions

## Step-by-step workflow
1. For each candidate, extract all `## ` section headers and compare to the baseline set — fail if any are missing.
2. Scan candidate content for architecture violation patterns: direct SDK imports in presentation layer, repository bypass, logic placed directly in a widget.
3. Check that the skill_path does not match any entry in the forbidden paths list.
4. Compare the Purpose section between candidate and baseline — fail if candidate's Purpose is empty when baseline's was not.
5. Compare Output contract bullet count between candidate and baseline — fail if candidate has fewer deliverables.
6. If all checks pass, set `passed = True` and return an empty `violations` list.
7. If any check fails, set `passed = False`, populate `violations` with one message per failure, and raise `RegressionViolation`.

## Output contract
- A RegressionResult dict per candidate: candidate_id, passed (bool), violations (list of strings)
- A summary dict with: regression_results (list), passing_candidates (list of candidates that passed), regression_failures (list of failing candidate_ids), all_passed (bool)
- Exit code 1 from `regression_runner.py` if any candidate fails

## Validation checklist
- Run `python -m runners.regression_runner --skill <path> --candidates <file>` and confirm exit code 0 for clean candidates
- Confirm a candidate with a removed section produces `passed: false` and a non-empty `violations` list
- Confirm the `regression_failures` list matches the set of candidate_ids with `passed: false`
- Confirm passing candidates are forwarded to the promotion stage without modification

## Related skills
- `karpathy-mutation` — produces the candidates this skill checks
- `karpathy-optimizer` — receives only regression-passing candidates
- `karpathy-evaluation` — runs after regression to score passing candidates

## References
- [`../../agents/regression_agent.py`](../../agents/regression_agent.py)
- [`../../docs/guardrails.md`](../../docs/guardrails.md)
- [`../../evals/testcases/flutter_deeplink/`](../../evals/testcases/flutter_deeplink/)

## Real example
The `token_budget` mutation for flutter deep link removes the Constraints section in an aggressive attempt to reduce tokens. The regression check on step 1 immediately detects the missing `## Constraints` header and raises `RegressionViolation(candidate_id='baseline-token_budget', violations=['Missing required section: ## Constraints'])`. This candidate is excluded from the promotion stage.

## Real file output sample
```text
memory/candidate_archive.json
reports/latest_report.md
```
