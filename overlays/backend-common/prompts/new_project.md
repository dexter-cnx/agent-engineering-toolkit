# Prompt: New Backend Project

## Intent
Plan a backend API project using runtime-neutral concepts that can later be implemented in Node, Python, or .NET.

## Use when
- starting a new backend
- defining backend boundaries before selecting the runtime details

## Required inputs
- domain goal
- resource list
- auth needs
- data integrity needs

## Optional inputs
- file handling
- audit/logging needs
- email or reset flows
- background job needs

## Expected outputs
- domain boundary map
- API resource plan
- validation strategy
- auth and permission shape
- test plan

## Example invocation
`Plan a backend for user profile and organization management. Define resource boundaries, validation, auth/permission shape, audit expectations, and a test plan.`

## Guardrails
- Do not pick Node, Python, or .NET unless the task asks for it.
- Keep contract design separate from runtime wiring.

## Repo paths to inspect
- `overlays/backend-common/README.md`
- `overlays/backend-common/HOW_TO_USE.md`
- `overlays/backend-common/SKILLS_INDEX.md`
- `overlays/backend-common/examples/`
- `overlays/backend-common/skills/`

## Related skills and workflows
- `api-contracts`
- `auth-token-concepts`
- `role-permission-model`
- `backend-testing-strategy`
