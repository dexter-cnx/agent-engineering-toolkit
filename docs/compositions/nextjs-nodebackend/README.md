# Next.js + Node Backend Composition

This composition layer shows how to combine:
- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/backend-node/`

Use it as the reference path for a Next.js frontend paired with a Node backend.

## Shared concepts
- frontend state and UX shape live in `web-frontend-common`
- Next.js routing and boundary choices live in `web-frontend-nextjs`
- backend contracts and policy shape live in `backend-common`
- Node implementation details live in `backend-node`

## Suggested scaffold
```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  │  ├─ app/
│  │  ├─ components/
│  │  ├─ features/
│  │  └─ services/
│  └─ backend-node/
│     ├─ src/
│     │  ├─ routes/
│     │  ├─ services/
│     │  ├─ repositories/
│     │  ├─ adapters/
│     │  ├─ domain/
│     │  └─ schemas/
│     ├─ test/
│     └─ project_memory/
├─ contracts/
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## Feature to skill map
| Feature | Frontend skills | Backend skills |
| --- | --- | --- |
| Auth/login | `auth-ux`, `nextjs-auth-integration`, `middleware-protected-routes` | `auth-token-concepts`, `refresh-token-strategy`, `role-permission-model` |
| CRUD screen | `loading-error-empty-states`, `forms-validation-ux`, `api-consumption-patterns` | `api-contracts`, `crud-resource-design`, `validation-error-handling`, `backend-testing-strategy` |
| Webhook/job flow | `loading-error-empty-states`, `api-consumption-patterns` | `api-contracts`, `backend-testing-strategy` |

## End-to-end review checklist
- [ ] Frontend states are explicit
- [ ] Contract is defined before implementation
- [ ] Permission rules are enforced in backend code
- [ ] AI-generated code follows the folder tree
- [ ] Tests cover the risky path

## Reuse note
For what can be shared conceptually from `backend-node`, read `overlays/backend-common/docs/backend-node-reuse-analysis.md`.

## Related compositions
- `docs/compositions/nextjs-dotnet/` if your backend is ASP.NET Core
- `docs/compositions/nextjs-python-service/` if your backend is Python

## Read first
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
