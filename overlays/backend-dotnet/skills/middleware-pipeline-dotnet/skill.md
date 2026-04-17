# Middleware Pipeline .NET

Follow `../_shared/skill-contract.md`.

## Purpose
Define middleware ordering for auth, exceptions, logging, and request shaping.

## Use when
- pipeline order matters

## Do not use when
- the task is only endpoint logic

## Inputs required
- middleware list
- ordering constraints
- exception policy

## Outputs expected
- pipeline order
- responsibility notes
- failure handling

## Workflow
1. List middleware.
2. Decide order.
3. Keep exception behavior first-class.
4. Keep logging and auth explicit.
5. Verify request paths.

## Validation checklist
- [ ] Order is explicit
- [ ] Exceptions are handled predictably
- [ ] Auth and logging are visible

## References
- `../../prompts/review_architecture.md`

