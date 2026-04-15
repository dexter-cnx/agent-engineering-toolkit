# Auth UX

Follow `../_shared/skill-contract.md`.

## Purpose
Design login, signup, recovery, and session UX that is clear and safe.

## Use when
- the task is about user-facing authentication flow
- you need login state, recovery state, or session expiration UX

## Do not use when
- the task is about backend token implementation
- the task is about framework routing

## Inputs required
- auth flow goal
- available entry points
- known session states

## Outputs expected
- page/state flow
- component split
- validation and error behavior

## Workflow
1. Define the auth scenario.
2. List states and transitions.
3. Decide what is reusable.
4. Add recovery and failure behavior.
5. Verify copy, accessibility, and tests.

## Validation checklist
- [ ] States are explicit
- [ ] Recovery is present
- [ ] No token logic leaks into UI primitives

## References
- `../../prompts/new_feature.md`
- `../../examples/profile-state-flow.md`

