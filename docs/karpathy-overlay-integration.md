# Karpathy Overlay Integration

This guide explains how overlay skills participate in the Karpathy governance plane.
It is intentionally operational and mirrors the runtime checks already enforced by the
Karpathy scripts and validators.

## When to govern a skill

Use Karpathy governance when a skill needs all of the following:

- measurable quality improvement over a baseline
- regression-safe mutation or promotion
- token-growth control
- a stable evaluation fixture

If a skill is purely exploratory, keep it draft-only until it can ship with a contract and
an eval case.

## Required contract fields

Every governed skill should declare a `skill.contract.yaml` with these fields:

| Field | Purpose |
|---|---|
| `skill_id` | Stable identifier for the skill |
| `overlay` | Owning overlay name |
| `status` | `governance-ready` or `draft-only` |
| `karpathy_governed` | `true` when the skill participates in the Karpathy plane |
| `token_budget_class` | Budget class for the skill (`standard`, `compact`, or `strict`) |
| `promotion_threshold` | Minimum score needed for promotion eligibility |
| `regression_required` | Whether regression checks are mandatory |
| `token_policy.max_token_increase_pct` | Maximum allowed token growth |
| `token_policy.min_score_improvement_pct` | Minimum score gain required to justify token growth |
| `eval.case_dir` | Relative path to the eval case directory |
| `eval.expected_result_file` | Expected-result fixture filename |
| `promotion.owner` | Promotion owner or maintainer group |

## Eval fixture expectations

A governed skill should keep its eval case small and static:

- one directory per case under `eval/cases/`
- one human-readable case summary file
- one `expected_result.json` fixture when the outcome is known
- no dependency on runtime-generated reports

`expected_result.json` is a static expectation fixture. It does not replace runtime reports;
it complements them.

## Promotion expectations

The runtime promotion trace must remain fail-closed. The validated decision trace currently
requires the fields enforced by `runners/karpathy_validate.py`, including:

- `baseline_score`
- `candidate_score`
- `score_delta`
- `token_delta`
- `regression_pass`
- `token_policy_pass`
- `final_decision`
- `reason`

The runtime validator also checks the surrounding promotion metadata and the committed
report artifacts. If any required field or file is missing, CI fails.

## Token budget classes

- `standard` - default governed skill with the shared Karpathy policy
- `compact` - favor smaller prompts or tighter wording
- `strict` - keep token growth near-flat unless the score gain is clearly justified

The policy remains the same across classes: reject token growth above 35% when the score
gain is below 5%.

## Regression responsibilities

Regression checks stay with the overlay that owns the skill:

- Flutter overlays validate widget, router, and platform boundaries
- backend overlays validate transport, service, repository, and adapter boundaries
- Next.js overlays validate server/client boundaries and route ownership
- Unity validates folder, assembly, and namespace boundaries

Promotion is blocked when regression fails, when token policy fails, or when the required
runtime artifacts are missing.
