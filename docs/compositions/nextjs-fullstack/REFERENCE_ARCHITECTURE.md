# Reference Architecture

## Recommended stack split
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend concepts: `backend-common`
- Backend implementation: route handlers, server actions, middleware, and data access inside the Next.js app

## Representative repo shape
```text
repo/
├─ apps/
│  └─ web-nextjs/
│     ├─ app/
│     │  ├─ api/
│     │  └─ (routes)/
│     ├─ components/
│     ├─ features/
│     ├─ services/
│     ├─ server/
│     ├─ db/
│     └─ tests/
├─ contracts/
├─ docs/
└─ project_memory/
```

## Contract flow
1. Define the UI need in `web-frontend-common`.
2. Decide the Next.js boundary in `web-frontend-nextjs`.
3. Define the API contract and policy shape in `backend-common`.
4. Implement the route handler, server action, or server utility inside the Next.js app.

## End-to-end examples
- auth flow: frontend session state -> backend-common token and permission shape -> Next.js auth entry point -> protected route behavior
- CRUD flow: frontend form -> backend-common contract -> route handler validation -> persistence adapter
- upload flow: frontend file selection -> backend-common file safety -> Next.js server-side upload handling
- webhook/job flow: frontend trigger -> server entry point -> service orchestration -> async processing

## Reuse from web-frontend-nextjs
- thin route handlers
- clear server and client boundaries
- middleware protection
- Next.js data fetching discipline

## What stays Next.js-specific
- App Router and route segments
- server actions and route handlers
- middleware mechanics
- server/client rendering boundaries
- app-local persistence and adapter wiring
