# Prompt: Review Next.js Architecture

## Intent
Review App Router usage, server/client boundaries, and route handler responsibility.

## Use when
- a Next.js feature changes route structure
- server and client responsibilities are unclear

## Required inputs
- route tree
- files to inspect
- change intent

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the Next.js architecture around the settings routes. Check App Router placement, server/client boundaries, and route handler responsibility.`

## Guardrails
- Prefer concrete file evidence.
- Do not broaden the review into backend architecture.

## Repo paths to inspect
- `overlays/web-frontend-nextjs/skills/`
- `overlays/web-frontend-common/skills/`
- `docs/compositions/nextjs-dotnet/`

## Related skills and workflows
- `app-router-structure`
- `server-client-boundaries`
- `route-handlers`
