# Full-Stack Dev Workflow

This workflow keeps the new starter layer predictable for humans and agents.

## Common commands

```bash
npm install
npm run check
npm run build
npm run contracts:check
npm run fullstack:verify
```

For the Next.js full-stack starter, set `DATABASE_URL=file:./prisma/dev.db` or source
`apps/nextjs-fullstack-app/.env.example` before running `npm run build` or
`npm run fullstack:verify`.

## Package-level commands

```bash
npm run check -w @agent-toolkit/contracts
npm run build -w @agent-toolkit/contracts
npm run check -w @agent-toolkit/fullstack-client
npm run build -w @agent-toolkit/fullstack-client
npm run check -w @agent-toolkit/nextjs-fullstack-app
npm run build -w @agent-toolkit/nextjs-fullstack-app
npm run check -w @agent-toolkit/nextjs-dotnet-frontend
npm run build -w @agent-toolkit/nextjs-dotnet-frontend
dotnet build apps/nextjs-dotnet-app/backend/src/Web/NextjsDotnetApp.Web.csproj
```

## Contract automation

- Run `npm run contracts:check` before changing shared request or response shapes.
- Run `node tools/contract-check/scripts/check.mjs` when you need to verify starter consumption.
- Run `npm run fullstack:verify` before you treat the layer as ready.

## Agent workflow

1. Read `docs/fullstack/getting-started.md`.
2. Pick the starter that matches the business shape.
3. Update the contract first when request or response shapes change.
4. Update the client package or starter app after the contract settles.
5. Run the workspace checks and the fullstack audit.
