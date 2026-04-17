# API Contracts

Follow `../_shared/skill-contract.md`.

## Purpose
Define stable request and response shapes for backend resources.

## Use when
- a new endpoint or resource is being planned

## Do not use when
- the task is runtime wiring only
- the task is database tuning only

## Inputs required
- resource name
- operation list
- validation needs

## Outputs expected
- request and response contract
- error contract
- field list

## Workflow
1. Define the resource.
2. Define operations and fields.
3. Define error shapes.
4. Define examples.
5. Verify that the contract matches the task.

## Validation checklist
- [ ] Contract is explicit
- [ ] Errors are defined
- [ ] Field names are stable

## References
- `../../prompts/generate_api_contract.md`
- `../../examples/profile-update-contract.md`

