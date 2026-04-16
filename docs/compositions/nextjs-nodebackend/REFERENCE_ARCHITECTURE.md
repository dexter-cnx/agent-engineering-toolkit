# Reference Architecture

## Recommended stack split

- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend: `backend-common` + `backend-node`

## Representative repo shape

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
│     ├─ test/
│     └─ project_memory/
├─ contracts/
├─ docs/
└─ project_memory/
```

## Contract flow

1. Define the UI need in `web-frontend-common`.
2. Decide the Next.js boundary in `web-frontend-nextjs`.
3. Define the API contract in `backend-common`.
4. Map the contract to Node backend details in `backend-node`.

## End-to-end examples

- auth flow: frontend session state -> backend token issuance -> protected route behavior
- CRUD flow: frontend form -> backend contract -> backend validation -> persistence
- upload flow: frontend file selection -> backend file safety -> storage and audit
- webhook/job flow: frontend trigger -> backend handler -> service orchestration -> async processing

## Reuse from backend-node

- thin route handlers
- service-oriented orchestration
- repositories and adapters separated
- handler, service, and repository boundary discipline

## What stays Node-specific

- runtime and package scripts
- request/response frameworks
- middleware mechanics
- Node module and deployment conventions
