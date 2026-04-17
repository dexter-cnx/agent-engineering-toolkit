# Next.js Full Stack Composition

This composition layer shows how to build a full-stack Next.js app in a single deployment while keeping the modular overlay boundaries visible.

Use it when:
- the frontend and backend live in the same Next.js app
- route handlers or server actions own the backend entry points
- you still want shared contract and policy design in `backend-common`

## Shared concepts
- frontend state and UX shape live in `web-frontend-common`
- Next.js routing, server/client boundaries, middleware, and data fetching live in `web-frontend-nextjs`
- backend contracts, validation, auth, and permission shape live in `backend-common`
- Next.js route handlers, server actions, and app-local persistence live in the app itself

## Suggested scaffold
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
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## Feature to skill map
| Feature | Frontend skills | Backend skills |
| --- | --- | --- |
| Auth/login | `app-router-structure`, `server-client-boundaries`, `middleware-protected-routes`, `nextjs-auth-integration` | `auth-token-concepts`, `refresh-token-strategy`, `role-permission-model`, `api-contracts`, `route-handlers` |
| CRUD screen | `app-router-structure`, `server-client-boundaries`, `nextjs-data-fetching`, `nextjs-auth-integration` | `api-contracts`, `crud-resource-design`, `validation-error-handling`, `backend-testing-strategy`, `route-handlers` |
| File upload | `server-client-boundaries`, `nextjs-data-fetching` | `file-handling-safety`, `validation-error-handling`, `backend-testing-strategy`, `route-handlers` |

## End-to-end review checklist
- [ ] Frontend states are explicit
- [ ] Contract is defined before implementation
- [ ] Permission rules are enforced in shared policy and server logic
- [ ] Route handlers or server actions stay thin
- [ ] AI-generated code follows the folder tree
- [ ] Tests cover the risky path

## Related compositions
- `docs/compositions/nextjs-dotnet/` if you want a separate ASP.NET Core backend
- `docs/compositions/nextjs-prisma-postgres-nextauth-vercel/` if you want the app-local Prisma/Postgres/NextAuth/Vercel stack
- `docs/compositions/nextjs-python-service/` if you want a separate Python service backend
- `docs/compositions/nextjs-nodebackend/` if you want a separate Node backend

## Read first
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
