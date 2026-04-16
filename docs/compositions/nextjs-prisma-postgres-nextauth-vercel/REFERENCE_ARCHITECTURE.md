# Reference Architecture

## Recommended stack split
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend concepts: `backend-common`
- App-local implementation: Next.js Server Actions, route handlers, NextAuth.js, Prisma, Postgres, and Vercel config

## Representative repo shape
```text
repo/
├─ apps/
│  └─ web-nextjs/
│     ├─ app/
│     │  ├─ api/
│     │  └─ (routes)/
│     ├─ auth/
│     ├─ components/
│     ├─ db/
│     ├─ features/
│     ├─ prisma/
│     ├─ server/
│     │  ├─ actions/
│     │  ├─ services/
│     │  ├─ adapters/
│     │  └─ repositories/
│     └─ tests/
├─ contracts/
├─ docs/
└─ project_memory/
```

## Contract flow
1. Define the UI need in `web-frontend-common`.
2. Decide the Next.js boundary in `web-frontend-nextjs`.
3. Define the resource, auth, and permission shape in `backend-common`.
4. Implement the Server Action, Prisma adapter, and auth checks inside the Next.js app.

## End-to-end examples
- auth flow: frontend sign-in state -> backend-common session shape -> NextAuth.js config -> protected route behavior
- CRUD flow: frontend form -> backend-common contract -> server action validation -> Prisma write/read
- membership flow: frontend gated UI -> backend-common role rule -> server-side session check -> conditional persistence
- deployment flow: env vars -> Prisma connection -> build checks -> Vercel runtime

## Reuse from web-frontend-nextjs
- App Router placement
- server/client boundaries
- route protection
- data fetching discipline

## What stays app-local
- NextAuth.js provider and callback configuration
- Prisma client setup and repository adapters
- server actions and route handlers
- database migrations and seed tooling
- Vercel runtime and environment-variable handling

## Persistence notes
- keep Prisma calls behind a small adapter or repository boundary
- avoid leaking database models into client components
- treat schema and migration changes as part of the implementation order
- keep env var requirements explicit so deployment does not depend on hidden local state
