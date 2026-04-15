# Next.js + .NET Composition

This composition layer shows how to combine:
- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/backend-dotnet/`

Use it as a reference path for production-minded full-stack work.

## Shared concepts
- frontend state and UX shape live in `web-frontend-common`
- Next.js routing and boundary choices live in `web-frontend-nextjs`
- backend contracts and policy shape live in `backend-common`
- ASP.NET Core implementation details live in `backend-dotnet`

## Suggested scaffold
```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  │  ├─ app/
│  │  ├─ components/
│  │  ├─ features/
│  │  └─ services/
│  └─ backend-dotnet/
│     ├─ src/
│     ├─ tests/
│     └─ Api/
├─ contracts/
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## Feature to skill map
| Feature | Frontend skills | Backend skills |
| --- | --- | --- |
| Auth/login | `auth-ux`, `nextjs-auth-integration`, `middleware-protected-routes` | `auth-token-concepts`, `jwt-auth-dotnet`, `refresh-token-dotnet`, `role-permission-model` |
| CRUD screen | `loading-error-empty-states`, `forms-validation-ux`, `api-consumption-patterns` | `api-contracts`, `crud-resource-design`, `validation-error-handling`, `efcore-basics` |
| File upload | `loading-error-empty-states`, `api-consumption-patterns` | `file-handling-safety`, `validation-error-handling`, `efcore-basics` |

## End-to-end review checklist
- [ ] Frontend states are explicit
- [ ] Contract is defined before implementation
- [ ] Auth and permission rules are enforced on the backend
- [ ] AI-generated code follows the folder tree
- [ ] Tests cover the risky path

## Related compositions
- `docs/compositions/nextjs-python-service/` if your backend is Python
- `docs/compositions/nextjs-nodebackend/` if your backend is Node

## Read first
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
