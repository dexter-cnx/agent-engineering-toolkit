# CRUD Resource Design

Follow `../_shared/skill-contract.md`.

## Purpose
Design a clean resource shape for create, read, update, and delete operations.

## Use when
- planning a standard backend resource

## Do not use when
- the task is event-driven or stream-driven

## Inputs required
- resource name
- operations
- field rules

## Outputs expected
- resource contract
- operation map
- lifecycle notes

## Workflow
1. Define the resource.
2. Define the operations.
3. Define field ownership.
4. Define delete semantics.
5. Verify that the resource stays stable.

## Validation checklist
- [ ] Operations are explicit
- [ ] Delete semantics are stated
- [ ] Ownership is clear

## References
- `../../prompts/generate_api_contract.md`
- `../../examples/profile-update-contract.md`

