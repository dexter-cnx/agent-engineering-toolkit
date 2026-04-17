# .NET DI Layering

Follow `../_shared/skill-contract.md`.

## Purpose
Define how services, repositories, and infrastructure are registered and separated.

## Use when
- dependency injection or layer registration changes

## Do not use when
- the task is only transport or UI

## Inputs required
- service list
- repository list
- composition root

## Outputs expected
- DI map
- layer registration plan
- boundary notes

## Workflow
1. List services and repositories.
2. Define composition root.
3. Keep registration centralized.
4. Verify dependencies point inward.
5. Check testability.

## Validation checklist
- [ ] Registration is centralized
- [ ] Layers are explicit
- [ ] Dependencies are testable

## References
- `../../prompts/review_architecture.md`

