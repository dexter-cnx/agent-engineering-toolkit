# Frontend Testing Basics

Follow `../_shared/skill-contract.md`.

## Purpose
Define lightweight but meaningful tests for frontend behavior.

## Use when
- behavior changes
- state handling changes
- UI copy or validation changes

## Do not use when
- the task is just documentation
- the task is backend-only

## Inputs required
- user scenario
- behavior that must not regress
- available test tools

## Outputs expected
- test scope
- sample test cases
- verification steps

## Workflow
1. Identify the behavior to protect.
2. Split unit, integration, and UI-level coverage.
3. Keep assertions user-facing.
4. Add regressions for the risky path.
5. Verify locally.

## Validation checklist
- [ ] Happy path covered
- [ ] Error path covered
- [ ] Tests assert behavior, not implementation trivia

## References
- `../../prompts/review_architecture.md`
- `../../prompts/refactor_feature.md`

