# Web Frontend Next.js Overlay Rules

## Overlay purpose
Provide Next.js-specific implementation guidance that composes with the common frontend overlay.

## Default assumptions
- Treat App Router as the default.
- Keep server and client boundaries explicit.
- Keep route handlers thin.
- Keep auth and middleware decisions visible.
- Keep data fetching decisions close to the owning route or feature.

## Entry points
- App structure -> `skills/app-router-structure/skill.md`
- Boundaries -> `skills/server-client-boundaries/skill.md`
- Route handlers -> `skills/route-handlers/skill.md`
- Middleware and protected routes -> `skills/middleware-protected-routes/skill.md`
- Data fetching -> `skills/nextjs-data-fetching/skill.md`
- Auth integration -> `skills/nextjs-auth-integration/skill.md`

## Boundary rules
- Do not re-explain framework-agnostic UI here.
- Do not add backend contract semantics here.
- Do not let middleware own feature business logic.

