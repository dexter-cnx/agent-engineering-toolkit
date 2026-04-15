# Prompt: Refactor Next.js Feature

## Intent
Refactor a Next.js feature so the route, server code, and client code stay clearly separated.

## Use when
- a feature mixes server and client responsibilities
- route placement needs cleanup

## Required inputs
- current route path
- files to refactor
- target behavior

## Expected outputs
- refactor plan
- changed files
- boundary notes

## Example invocation
`Refactor the account settings feature so the route, server component, and client form are separated cleanly.`

## Guardrails
- Do not move backend contract responsibilities into the Next.js layer.
- Keep route handlers thin.

## Repo paths to inspect
- `overlays/web-frontend-nextjs/skills/`
- `overlays/web-frontend-common/skills/`
