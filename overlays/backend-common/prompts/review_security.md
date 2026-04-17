# Prompt: Review Backend Security

## Intent
Review auth, permission, file safety, and sensitive-data handling.

## Use when
- auth or permission rules changed
- file or reset flows changed

## Required inputs
- paths to inspect
- security concern
- runtime if relevant

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the backend for auth, permission, and file safety issues. Focus on the profile update and upload paths.`

## Guardrails
- Keep the review about backend boundaries and policy shape.
- Prefer evidence in repository paths over assumptions.

## Repo paths to inspect
- `overlays/backend-common/skills/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`

## Related skills and workflows
- `auth-token-concepts`
- `role-permission-model`
- `file-handling-safety`
