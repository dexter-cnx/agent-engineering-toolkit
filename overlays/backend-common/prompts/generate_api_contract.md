# Prompt: Generate API Contract

## Intent
Produce a request/response contract for a backend resource with validation and error behavior.

## Use when
- defining a new API resource
- changing request or response shapes

## Required inputs
- resource name
- operations
- field rules
- error behavior

## Expected outputs
- request/response contract
- validation rules
- error response shape

## Example invocation
`Generate an API contract for a profile update resource. Include request fields, response shape, validation, and error behavior.`

## Guardrails
- Keep the contract runtime-neutral.
- Do not add implementation details that belong in Node, Python, or .NET overlays.

## Repo paths to inspect
- `overlays/backend-common/skills/api-contracts/skill.md`
- `overlays/backend-common/examples/profile-update-contract.md`

## Related skills and workflows
- `api-contracts`
- `validation-error-handling`
