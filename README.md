# agent-engineering-toolkit

A production-ready, domain-agnostic toolkit for structured AI-assisted software engineering.

This repository is a foundation toolkit that can be reused across:

- mobile projects
- backend services
- web frontends
- AI and agent systems
- monorepos
- internal engineering platforms

It is intentionally stack-neutral at the foundation layer. Stack-specific conventions belong in overlays, not in the root identity of the toolkit.

## Canonical references

- Lifecycle source of truth: `docs/prompt-pipeline.md`
- Role model source of truth: `docs/agent-team-system.md`
- Prompt hub: `prompts/index.md`
- Prompt hub (English): `prompts/index_EN.md`
- Adoption guide: `docs/how-to-use.md`
- Tutorial: `docs/tutorial.md`
- Karpathy guide: `docs/karpathy-guide.md`
- Overlay strategy: `docs/overlays.md`

## Overlay catalog

Detailed guidance lives in each overlay's own README and `AGENTS.overlay.md`.

- [agent-karpathy](overlays/agent-karpathy/README.md) - Eval-driven skill optimization, controlled mutation, regression-safe promotion, and token governance
- [backend-node](overlays/backend-node/README.md) - Node backend, API service, and job processor guidance
- [mobile-flutter](overlays/mobile-flutter/README.md) - Flutter app guidance and capability skills
- [web-frontend-common](overlays/web-frontend-common/README.md) - Framework-agnostic web frontend guidance
- [web-frontend-nextjs](overlays/web-frontend-nextjs/README.md) - Next.js-specific frontend implementation guidance
- [backend-common](overlays/backend-common/README.md) - Runtime-neutral backend guidance
- [backend-dotnet](overlays/backend-dotnet/README.md) - ASP.NET Core and .NET backend guidance
- [unity](overlays/unity/README.md) - Unity project structure, runtime, and delivery skills
- [python-service](overlays/python-service/README.md) - Python service, worker, and adapter guidance
- [web-frontend](overlays/web-frontend/README.md) - Legacy web UI and product frontend guidance

If you are working on AI skill quality or promotion workflows, start with
`overlays/agent-karpathy/README.md`, then read `docs/karpathy-guide.md`, and use the
canonical scripts shown below.

## Full-stack quick path

Start here when you are working on canonical runnable full-stack paths:

- `docs/fullstack/getting-started.md` for path selection
- `docs/fullstack/dev-workflow.md` for local commands
- `docs/fullstack/repo-layout.md` for workspace mapping
- `apps/nextjs-fullstack-app/` for the single-app starter
- `apps/nextjs-dotnet-app/` for the split starter
- `packages/contracts/` for shared schemas
- `packages/fullstack-client/` for typed client helpers

## Mobile-first quick path

Start here when the mobile app is primary:

- `docs/compositions/flutter-dotnet/README.md`
- `docs/compositions/flutter-nodebackend/README.md`
- `docs/fullstack/mobile-backend-integration.md`
- `docs/fullstack/auth-cross-platform.md`
- `docs/fullstack/selection-matrix.md`
- `apps/flutter-api-client-reference/`
- `packages/mobile-contract-adapters/`

Run the full-stack integrity gate from the root:

```bash
npm install
npm run fullstack:verify
```

## When to Use Karpathy Layer

Use the `agent-karpathy` overlay when you are working on AI skill quality or promotion
workflows.

Karpathy quick path:

- Overlay README: `overlays/agent-karpathy/README.md`
- Eval only: `./scripts/karpathy-eval.sh <skill>`
- Dry-run cycle: `./scripts/karpathy-run-cycle.sh <skill> true 3`
- Promotion-enabled cycle: `./scripts/karpathy-run-cycle.sh <skill> false 3`

```bash
./scripts/karpathy-eval.sh <skill>
./scripts/karpathy-run-cycle.sh <skill> true 3
./scripts/karpathy-run-cycle.sh <skill> false 3
```

Karpathy runtime artifacts are written to `reports/latest_report.md`, `reports/history/`, `memory/score_history.json`, and `memory/candidate_archive.json`.

Static worked examples stay in `examples/` and are not runtime output.

If you are optimizing a skill for quality or promotion, read
`docs/karpathy-guide.md` before starting the cycle so the baseline, regression, and
token-policy checks stay aligned.

## Full-stack composition

- [docs/compositions/README.md](docs/compositions/README.md) - Index of modular full-stack reference paths
- [docs/compositions/nextjs-dotnet/README.md](docs/compositions/nextjs-dotnet/README.md) - Full-stack Next.js + ASP.NET Core reference path
- [docs/compositions/nextjs-python-service/README.md](docs/compositions/nextjs-python-service/README.md) - Full-stack Next.js + Python service reference path
- [docs/compositions/nextjs-nodebackend/README.md](docs/compositions/nextjs-nodebackend/README.md) - Full-stack Next.js + Node backend reference path

## Full Stack Starters

- [`apps/nextjs-fullstack-app/`](apps/nextjs-fullstack-app/README.md) - canonical single-app starter with app-local backend
- [`apps/nextjs-dotnet-app/`](apps/nextjs-dotnet-app/README.md) - canonical split starter with Next.js frontend and ASP.NET Core backend
- [`apps/flutter-api-client-reference/`](apps/flutter-api-client-reference/README.md) - canonical Flutter API client reference
- [`packages/contracts/`](packages/contracts/README.md) - shared schema-first API contract package
- [`packages/fullstack-client/`](packages/fullstack-client/README.md) - reusable typed client helpers
- [`packages/mobile-contract-adapters/`](packages/mobile-contract-adapters/README.md) - mobile contract mapping guidance
- [`docs/fullstack/architecture.md`](docs/fullstack/architecture.md) - full-stack boundary model and lifecycle
- [`docs/fullstack/contracts.md`](docs/fullstack/contracts.md) - contract package purpose, versioning, and envelopes
- [`docs/fullstack/getting-started.md`](docs/fullstack/getting-started.md) - path selection and kickoff guide
- [`docs/fullstack/dev-workflow.md`](docs/fullstack/dev-workflow.md) - local development workflow
- [`docs/fullstack/repo-layout.md`](docs/fullstack/repo-layout.md) - workspace layout and responsibility map
- [`docs/fullstack/mobile-backend-integration.md`](docs/fullstack/mobile-backend-integration.md) - mobile/backend boundary model
- [`docs/fullstack/auth-cross-platform.md`](docs/fullstack/auth-cross-platform.md) - cross-platform auth lifecycle
- [`docs/fullstack/selection-matrix.md`](docs/fullstack/selection-matrix.md) - business-driven composition selection guide

Verification commands:

```bash
npm install
npm run contracts:check
npm run mobile:verify
npm run build -w @agent-toolkit/fullstack-client
npm run check -w @agent-toolkit/fullstack-client
npm run check -w @agent-toolkit/mobile-contract-adapters
npm run check -w @agent-toolkit/nextjs-fullstack-app
npm run build -w @agent-toolkit/nextjs-fullstack-app
npm run check -w @agent-toolkit/nextjs-dotnet-frontend
npm run build -w @agent-toolkit/nextjs-dotnet-frontend
npm run fullstack:verify
```

For the Next.js starter, set `DATABASE_URL=file:./prisma/dev.db` or copy
`apps/nextjs-fullstack-app/.env.example` before running the build or verify path.

## Start here

- `README_START_HERE.md`
- `Makefile` - common repo tasks via `make help`
- `docs/how-to-use.md`
- `docs/tutorial.md`
- `docs/overlays.md`
- If you are working on AI skill quality work, start with `overlays/agent-karpathy/README.md`

## Documentation

- `docs/how-to-use.md`
- `docs/how-to-use_TH.md`
- `docs/tutorial.md`
- `docs/tutorial_TH.md`
- `docs/karpathy-guide.md`
- `docs/karpathy-guide_TH.md`
- `docs/tutorials/index.md`
- `docs/tutorials/index_EN.md`
- `docs/overlays.md`
- `docs/karpathy-ecosystem-index.md`

## Worked examples

- `examples/worked_examples/foundation_feature_flow.md`

Overlay-specific worked examples live under each overlay's own documentation and examples folder.

## License

MIT

This repository is a foundation toolkit for building reusable overlay packages and agent-ready workflows.
