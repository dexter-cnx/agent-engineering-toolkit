# Prompt: New Backend Feature

## Intent
Implement one backend feature with explicit contract, validation, and permission shape.

## Use when
- adding a new endpoint or resource
- changing backend behavior without changing the runtime

## Required inputs
- feature goal
- resource name
- validation constraints
- permission rules

## Expected outputs
- implementation plan
- contract shape
- validation and error behavior
- test checklist

## Example invocation
`Implement a user profile update feature. Define the contract, validation, permission rules, audit notes, and test checklist.`

## Guardrails
- Keep transport, validation, and persistence boundaries explicit.
- Do not hide auth or permission rules in UI assumptions.

## Repo paths to inspect
- `overlays/backend-common/skills/`
- `overlays/backend-common/examples/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`

## Related skills and workflows
- `api-contracts`
- `validation-error-handling`
- `role-permission-model`
