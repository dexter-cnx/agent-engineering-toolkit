# Prompt: Generate Next.js Feature

## Intent
Implement one Next.js feature with correct App Router placement and explicit server/client boundaries.

## Use when
- adding a new page, route group, or layout
- creating a feature that depends on route placement

## Required inputs
- route goal
- layout ownership
- data loading needs
- auth or protection needs

## Optional inputs
- route handlers
- middleware requirements
- server actions or client interactivity

## Expected outputs
- route tree
- boundary plan
- files to create or update
- verification checklist

## Example invocation
`Implement a protected account settings route in Next.js. Place the page in the App Router, split server and client responsibilities, and show the files to create.`

## Guardrails
- Keep route handlers thin.
- Keep server/client boundaries explicit.
- Do not place backend contract logic in the Next.js layer.

## Repo paths to inspect
- `overlays/web-frontend-nextjs/skills/`
- `overlays/web-frontend-nextjs/examples/`
- `overlays/web-frontend-common/skills/`

## Related skills and workflows
- `app-router-structure`
- `server-client-boundaries`
- `nextjs-data-fetching`
- `nextjs-auth-integration`
