# Reference Architecture

## Recommended stack split
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend: `backend-common` + `backend-dotnet`

## Representative repo shape
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
├─ docs/
└─ project_memory/
```

## Contract flow
1. Define the UI need in `web-frontend-common`.
2. Decide the Next.js boundary in `web-frontend-nextjs`.
3. Define the API contract in `backend-common`.
4. Map the contract to ASP.NET Core details in `backend-dotnet`.

## End-to-end examples
- auth flow: frontend session state -> backend token issuance -> protected route behavior
- CRUD flow: frontend form -> backend contract -> backend validation -> persistence
- upload flow: frontend file selection -> backend file safety -> storage and audit
- permission flow: frontend visibility -> backend authorization -> audit trail

