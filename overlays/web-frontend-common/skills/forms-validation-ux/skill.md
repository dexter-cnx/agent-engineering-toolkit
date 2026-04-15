# Forms Validation UX

Follow `../_shared/skill-contract.md`.

## Purpose
Shape user input, validation, and submit feedback for frontend forms.

## Use when
- building a form
- updating validation copy or submit behavior

## Do not use when
- the task is backend validation design
- the task is about auth token logic

## Inputs required
- fields
- validation rules
- submit success/failure behavior

## Outputs expected
- form state model
- field-level feedback
- submit flow

## Workflow
1. List fields and constraints.
2. Define inline and submit validation.
3. Define loading and disabled behavior.
4. Define retry and recovery.
5. Verify accessibility and keyboard flow.

## Validation checklist
- [ ] Required states are visible
- [ ] Error copy is specific
- [ ] Submit handling is obvious

## References
- `../../prompts/new_feature.md`
- `../../examples/profile-state-flow.md`

