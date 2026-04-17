# Soft Delete Audit

Follow `../_shared/skill-contract.md`.

## Purpose
Define deletion semantics, traceability, and history expectations.

## Use when
- records must remain recoverable or traceable

## Do not use when
- records are truly disposable

## Inputs required
- delete policy
- audit needs
- restore expectations

## Outputs expected
- soft-delete rule
- audit fields
- restore behavior

## Workflow
1. Define deletion meaning.
2. Define audit fields.
3. Define restore path.
4. Define what cannot be restored.
5. Verify with scenarios.

## Validation checklist
- [ ] Delete semantics are clear
- [ ] Audit fields are defined
- [ ] Restore behavior is documented

## References
- `../../prompts/review_architecture.md`

