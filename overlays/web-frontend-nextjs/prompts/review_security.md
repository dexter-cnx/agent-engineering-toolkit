# Prompt: Review Next.js Security

## Intent
Review route protection, auth boundaries, and data exposure in the Next.js layer.

## Use when
- route protection changes
- auth-aware UI changes

## Required inputs
- route list
- auth flow scope
- files to inspect

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the Next.js account area for route protection, auth-aware rendering, and accidental data exposure.`

## Guardrails
- Keep the review focused on frontend behavior.
- Do not rewrite backend auth implementation here.

## Repo paths to inspect
- `overlays/web-frontend-nextjs/skills/`
- `overlays/web-frontend-common/skills/auth-ux/skill.md`
- `docs/compositions/nextjs-dotnet/`

## Related skills and workflows
- `middleware-protected-routes`
- `nextjs-auth-integration`
