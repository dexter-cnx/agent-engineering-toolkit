# API Consumption Patterns

Follow `../_shared/skill-contract.md`.

## Purpose
Define how frontend code reads and writes data through a stable service boundary.

## Use when
- UI needs data from an API
- cache or refresh behavior matters

## Do not use when
- you need backend contract design
- you need routing or auth screen behavior

## Inputs required
- endpoint shape
- fetch/write behavior
- cache and refresh expectations

## Outputs expected
- service or hook boundary
- response mapping
- error handling shape

## Workflow
1. Define read and write operations.
2. Decide where data transforms live.
3. Decide how errors are surfaced.
4. Decide cache and refresh behavior.
5. Verify tests for the service boundary.

## Validation checklist
- [ ] API code is outside leaf UI
- [ ] Transforms are explicit
- [ ] Error behavior is documented

## References
- `../../prompts/new_feature.md`
- `../../examples/profile-state-flow.md`

