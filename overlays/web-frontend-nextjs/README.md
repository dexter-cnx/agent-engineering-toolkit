# Web Frontend Next.js Overlay

Use this overlay when the frontend is built with Next.js and you need App Router conventions, server/client boundaries, route handlers, middleware, data fetching, and auth integration.

## Use with
- `overlays/web-frontend-common/` for reusable frontend patterns
- `docs/compositions/README.md` for full-stack composition choices
- `docs/compositions/nextjs-dotnet/` for Next.js + ASP.NET Core reference usage
- `docs/compositions/nextjs-python-service/` for Next.js + Python service reference usage
- `docs/compositions/nextjs-nodebackend/` for Next.js + Node backend reference usage

## Start here
- `AGENTS.overlay.md`
- `HOW_TO_USE.md`
- `TUTORIAL.md`
- `SKILLS_INDEX.md`
- `prompts/README.md`
- `examples/README.md`

## Karpathy integration

- Governed exemplar: `skills/server-client-boundaries/skill.md`
- Contract: `skills/server-client-boundaries/skill.contract.yaml`
- Eval case: `skills/server-client-boundaries/eval/cases/governance-smoke/README.md`

## What this overlay covers
- App Router structure
- server versus client component boundaries
- route handlers and middleware
- Next.js data fetching patterns
- auth integration in the frontend

## What this overlay does not do
- framework-agnostic UI fundamentals
- backend API contract design
- backend authentication implementation
## Overlay OS contract

### Purpose
Provide specialization for **web-frontend-nextjs** while keeping the repository root stack-neutral.

### When to use
Use this overlay for Next.js-specific frontend implementation and conventions.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
