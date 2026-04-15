# Prompt: Connect Frontend to Backend

## Intent
Wire the Next.js frontend to backend APIs without leaking transport details into reusable UI.

## Use when
- a feature needs API access
- the frontend must consume a backend contract safely

## Required inputs
- endpoint list
- request and response shapes
- auth/session dependencies

## Optional inputs
- cache or refresh needs
- error handling policy
- retry rules

## Expected outputs
- service or hook boundary
- mapping notes
- loading and error behavior

## Example invocation
`Connect the account settings page to the backend API. Show the request and response shapes, the service boundary, and how auth/session state flows through the UI.`

## Guardrails
- Do not put fetch logic inside leaf UI.
- Keep transport details behind services or hooks.

## Repo paths to inspect
- `overlays/web-frontend-nextjs/skills/`
- `overlays/web-frontend-common/skills/api-consumption-patterns/skill.md`
- `overlays/backend-common/skills/api-contracts/skill.md`

## Related skills and workflows
- `nextjs-data-fetching`
- `nextjs-auth-integration`
- `api-consumption-patterns`
