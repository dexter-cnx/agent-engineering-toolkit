# Next.js + Prisma + Postgres + NextAuth.js + Vercel Composition

This composition is the reference path for a single Next.js app that uses Server Actions, Prisma, Postgres, NextAuth.js, and Vercel.

Use it when:
- the UI, mutations, auth, and persistence live in one Next.js deployment
- you want server actions for form submissions and data mutations
- Prisma owns the database adapter boundary
- NextAuth.js owns the session and sign-in flow
- Vercel is the default deployment target

## Shared concepts
- frontend state and UX shape live in `web-frontend-common`
- Next.js routing and server/client boundaries live in `web-frontend-nextjs`
- contract, validation, auth shape, and permissions live in `backend-common`
- app-local server actions, auth handlers, and Prisma access live inside the Next.js app

## Suggested scaffold
```text
repo/
├─ apps/
│  └─ web-nextjs/
│     ├─ app/
│     │  ├─ api/
│     │  └─ (routes)/
│     ├─ auth/
│     ├─ db/
│     ├─ prisma/
│     ├─ server/
│     │  ├─ actions/
│     │  ├─ services/
│     │  └─ adapters/
│     ├─ components/
│     ├─ features/
│     └─ tests/
├─ contracts/
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## Feature to skill map
| Feature | Frontend skills | Backend skills |
| --- | --- | --- |
| Auth/login | `nextjs-auth-integration`, `server-client-boundaries`, `middleware-protected-routes` | `auth-token-concepts`, `role-permission-model`, `nextauth-session-shape` |
| CRUD screen | `loading-error-empty-states`, `forms-validation-ux`, `api-consumption-patterns` | `api-contracts`, `validation-error-handling`, `prisma-schema-design`, `database-adapter-patterns` |
| Protected mutation | `server-client-boundaries`, `forms-validation-ux` | `api-contracts`, `role-permission-model`, `server-actions-boundary`, `prisma-repository-patterns` |
| Vercel deploy | `deployment-ready-ui`, `runtime-constraints-awareness` | `env-var-management`, `build-time-safety`, `migration-strategy` |

## End-to-end review checklist
- [ ] Frontend states are explicit
- [ ] Contract is defined before implementation
- [ ] Auth and permission rules are enforced on the server
- [ ] Server actions stay thin and call services or adapters
- [ ] Prisma access is isolated behind a small boundary
- [ ] Vercel-specific config is documented and reproducible
- [ ] Tests cover the risky path

## Related compositions
- `docs/compositions/nextjs-fullstack/` if you want a more generic full-stack Next.js path
- `docs/compositions/nextjs-dotnet/` if you want Next.js paired with ASP.NET Core
- `docs/compositions/nextjs-python-service/` if you want Next.js paired with Python
- `docs/compositions/nextjs-nodebackend/` if you want Next.js paired with Node

## Read first
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
