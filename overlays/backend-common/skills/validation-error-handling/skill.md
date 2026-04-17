# Validation Error Handling

Follow `../_shared/skill-contract.md`.

## Purpose
Define how invalid input is rejected and how errors are reported.

## Use when
- request validation matters
- failure responses must be predictable

## Do not use when
- the task is purely transport wiring

## Inputs required
- invalid cases
- field-level constraints
- response style

## Outputs expected
- validation rules
- error response shape
- client-facing message strategy

## Workflow
1. List invalid cases.
2. Choose field versus form-level errors.
3. Define response payload.
4. Define message safety.
5. Verify examples.

## Validation checklist
- [ ] Invalid cases are listed
- [ ] Error response shape is stable
- [ ] Messages do not expose sensitive detail

## References
- `../../prompts/review_security.md`
- `../../examples/profile-update-contract.md`

