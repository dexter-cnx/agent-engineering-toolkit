# Prompt: Refactor Frontend Feature

## Intent
Refactor one frontend feature so the state flow, component split, and data access boundaries stay explicit.

## Use when
- a feature is too large
- a feature has unclear loading or error behavior
- component reuse is drifting

## Required inputs
- current feature path
- target behavior
- known pain points

## Optional inputs
- files to preserve
- test constraints
- design constraints

## Expected outputs
- refactor plan
- changed files
- risk notes
- verification steps

## Example invocation
`Refactor the profile settings feature so loading, error, and empty states are explicit and the form keeps service access out of leaf components.`

## Guardrails
- Do not rewrite unrelated features.
- Do not move backend concerns into frontend components.

## Repo paths to inspect
- `overlays/web-frontend-common/skills/`
- `overlays/web-frontend-common/examples/`
- `overlays/web-frontend-common/prompts/`

## Related skills and workflows
- `loading-error-empty-states`
- `forms-validation-ux`
- `api-consumption-patterns`
