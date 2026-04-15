# Prompt: Review Frontend Security UX

## Intent
Review the frontend for unsafe authentication UX, data exposure, and security-sensitive message handling.

## Use when
- login, recovery, or session flows change
- route protection or auth-aware UI changes

## Required inputs
- auth flow scope
- files or folders to inspect
- expected protected behavior

## Optional inputs
- redirect rules
- session storage approach
- known security concerns

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the auth and session UX in the account area. Check for sensitive data exposure, unsafe redirect behavior, and token or session state leaking into reusable UI.`

## Guardrails
- Keep the review about frontend behavior, not backend token issuance.
- Prefer concrete evidence from repository paths.

## Repo paths to inspect
- `overlays/web-frontend-common/skills/auth-ux/skill.md`
- `overlays/web-frontend-common/skills/frontend-testing-basics/skill.md`
- `overlays/web-frontend-common/examples/`

## Related skills and workflows
- `auth-ux`
- `frontend-testing-basics`
