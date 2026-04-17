# File Handling Safety

Follow `../_shared/skill-contract.md`.

## Purpose
Define safe upload, download, storage, and validation behavior for files.

## Use when
- a feature handles user files

## Do not use when
- the task does not touch files

## Inputs required
- file type
- storage target
- size and validation rules

## Outputs expected
- file safety rules
- validation steps
- storage constraints

## Workflow
1. Define accepted file types.
2. Define validation and size limits.
3. Define storage target and naming.
4. Define download and access rules.
5. Verify the unsafe paths.

## Validation checklist
- [ ] File type is constrained
- [ ] Size limit is stated
- [ ] Access rules are explicit

## References
- `../../prompts/review_security.md`

