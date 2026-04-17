# FluentValidation .NET

Follow `../_shared/skill-contract.md`.

## Purpose
Integrate validation rules into .NET request handling.

## Use when
- input validation needs to be centralized

## Do not use when
- the task is only persistence

## Inputs required
- request DTO
- field rules
- error format

## Outputs expected
- validator rules
- validation behavior
- error response mapping

## Workflow
1. Define DTO constraints.
2. Translate them to validator rules.
3. Map errors to responses.
4. Keep messages safe and clear.
5. Verify negative cases.

## Validation checklist
- [ ] Rules match DTO shape
- [ ] Errors are consistent
- [ ] Messages are safe

## References
- `../../prompts/refactor_feature.md`

