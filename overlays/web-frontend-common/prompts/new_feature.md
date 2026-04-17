# Prompt: New Frontend Feature

## Intent
Implement one frontend feature using the reusable patterns from the common overlay.

## Use when
- adding a page or feature module
- updating an existing feature without changing framework choices

## Required inputs
- feature goal
- user journey
- data fields
- failure modes

## Optional inputs
- existing component names
- service or hook boundaries
- test framework

## Expected outputs
- implementation plan
- file list
- state shape examples
- validation checklist

## Example invocation
`Implement a user profile editor feature. Split the UI into reusable pieces, define loading/empty/error states, keep API access behind a service boundary, and include tests for the important behavior.`

## Guardrails
- Keep reusable components free of feature logic.
- Keep loading/error/empty states explicit.
- Do not hide data access inside leaf UI.

## Repo paths to inspect
- `overlays/web-frontend-common/skills/`
- `overlays/web-frontend-common/examples/`
- `overlays/web-frontend-common/prompts/`

## Related skills and workflows
- `loading-error-empty-states`
- `forms-validation-ux`
- `api-consumption-patterns`
- `frontend-testing-basics`
