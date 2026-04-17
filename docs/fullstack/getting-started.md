# Full-Stack Getting Started

Use this guide when you want the shortest path from the toolkit root to a runnable full-stack baseline.

## Choose a path

- `apps/nextjs-fullstack-app/` for a single-app starter with an app-local backend.
- `apps/nextjs-dotnet-app/` for a split frontend/backend starter with ASP.NET Core.
- `packages/contracts/` when you need the shared schema-first contract layer.
- `packages/fullstack-client/` when you want the typed client helpers and auth-aware fetch patterns.

## Start from the root

```bash
npm install
npm run fullstack:verify
```

## When to use which starter

- Use the app-local starter when one team owns the whole product and the deployment can stay simple.
- Use the split starter when the backend needs independent ownership, runtime isolation, or a long-lived API boundary.

## What to read next

1. [Repo layout](repo-layout.md)
2. [Dev workflow](dev-workflow.md)
3. [Architecture](architecture.md)
4. [Contracts](contracts.md)
5. [Selection matrix](selection-matrix.md)
