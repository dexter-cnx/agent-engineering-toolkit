# Role Permission Model

Follow `../_shared/skill-contract.md`.

## Purpose
Define roles, permissions, and authorization rules.

## Use when
- a feature needs access control
- different users can do different actions

## Do not use when
- the task is only login UX
- the task is only database wiring

## Inputs required
- roles
- actions
- protected resources

## Outputs expected
- permission matrix
- authorization rules
- edge cases

## Workflow
1. List roles.
2. List actions.
3. Map roles to actions.
4. Define exceptions.
5. Verify with a scenario.

## Validation checklist
- [ ] Roles are named
- [ ] Actions are named
- [ ] Exceptions are documented

## References
- `../../prompts/review_security.md`
- `../../examples/profile-update-contract.md`

