# Prompt: Review Frontend Architecture

## Intent
Review a frontend repository for boundary clarity, reuse safety, and maintainability.

## Use when
- checking a feature branch before merge
- auditing a legacy frontend for drift

## Required inputs
- repository paths to inspect
- stack or framework
- the change intent

## Optional inputs
- design system constraints
- performance concerns
- accessibility concerns

## Expected outputs
- findings
- severity
- exact file paths
- recommended fixes

## Example invocation
`Review the frontend architecture in src/features/profile and src/components. Look for feature logic in reusable components, data access in leaf UI, missing loading or error recovery, and test gaps.`

## Guardrails
- Prefer concrete file evidence over theory.
- Do not rewrite the architecture unless the findings require it.
- Keep the review focused on frontend boundaries.

## Repo paths to inspect
- `overlays/web-frontend-common/skills/`
- `overlays/web-frontend-common/examples/`
- `overlays/web-frontend-common/README.md`

## Related skills and workflows
- `frontend-testing-basics`
- `loading-error-empty-states`
- `forms-validation-ux`
