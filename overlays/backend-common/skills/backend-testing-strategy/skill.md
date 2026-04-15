# Backend Testing Strategy

Follow `../_shared/skill-contract.md`.

## Purpose
Define practical test coverage for backend contracts, validation, permissions, and critical flows.

## Use when
- behavior changes
- a new endpoint or flow is being added

## Do not use when
- the task is documentation only

## Inputs required
- scenario
- risk areas
- available test layers

## Outputs expected
- test scope
- coverage map
- verification steps

## Workflow
1. Identify the risky behavior.
2. Split unit, integration, and contract tests.
3. Keep assertions user- and contract-facing.
4. Add regression tests for failure paths.
5. Verify locally.

## Validation checklist
- [ ] Happy path covered
- [ ] Failure path covered
- [ ] Contract boundary is tested

## References
- `../../prompts/review_architecture.md`
- `../../prompts/refactor_feature.md`

