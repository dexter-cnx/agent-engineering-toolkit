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
- Overlay strategy: `docs/overlays.md`

## Overlay catalog

Detailed guidance lives in each overlay's own README and `AGENTS.overlay.md`.

- [backend-node](overlays/backend-node/README.md) - Node backend, API service, and job processor guidance
- [mobile-flutter](overlays/mobile-flutter/README.md) - Flutter app guidance and capability skills
- [web-frontend-common](overlays/web-frontend-common/README.md) - Framework-agnostic web frontend guidance
- [web-frontend-nextjs](overlays/web-frontend-nextjs/README.md) - Next.js-specific frontend implementation guidance
- [backend-common](overlays/backend-common/README.md) - Runtime-neutral backend guidance
- [backend-dotnet](overlays/backend-dotnet/README.md) - ASP.NET Core and .NET backend guidance
- [unity](overlays/unity/README.md) - Unity project structure, runtime, and delivery skills
- [python-service](overlays/python-service/README.md) - Python service, worker, and adapter guidance
- [agent-karpathy](overlays/agent-karpathy/README.md) - Eval-driven skill optimization, controlled mutation, regression-safe promotion, and token governance
- [web-frontend](overlays/web-frontend/README.md) - Legacy web UI and product frontend guidance

If you are working on AI skill quality or promotion workflows, start with
`overlays/agent-karpathy/README.md` and use the canonical scripts shown below.

## When to Use Karpathy Layer

Use the `agent-karpathy` overlay when you are working on AI skill quality or promotion
workflows. It is the repository's eval-driven optimization layer: it measures a skill against
the rubric, generates controlled mutations, blocks regressions, applies token governance, and
only promotes a candidate when it strictly beats the baseline.

For the Karpathy quick path, start with `overlays/agent-karpathy/README.md` and run:
`./scripts/karpathy-eval.sh <skill>`, `./scripts/karpathy-run-cycle.sh <skill> true 3`, or
`./scripts/karpathy-run-cycle.sh <skill> false 3`.

Run it with the canonical scripts:

```bash
./scripts/karpathy-eval.sh <skill>
./scripts/karpathy-run-cycle.sh <skill> true 3
./scripts/karpathy-run-cycle.sh <skill> false 3
```

Karpathy runtime artifacts are written to `reports/latest_report.md`, `reports/history/`, `memory/score_history.json`, and `memory/candidate_archive.json`.

Static worked examples stay in `examples/` and are not runtime output.

## Full-stack composition

- [docs/compositions/README.md](docs/compositions/README.md) - Index of modular full-stack reference paths
- [docs/compositions/nextjs-dotnet/README.md](docs/compositions/nextjs-dotnet/README.md) - Full-stack Next.js + ASP.NET Core reference path
- [docs/compositions/nextjs-python-service/README.md](docs/compositions/nextjs-python-service/README.md) - Full-stack Next.js + Python service reference path
- [docs/compositions/nextjs-nodebackend/README.md](docs/compositions/nextjs-nodebackend/README.md) - Full-stack Next.js + Node backend reference path

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
- `docs/tutorials/index.md`
- `docs/tutorials/index_EN.md`
- `docs/overlays.md`

## Worked examples

- `examples/worked_examples/foundation_feature_flow.md`

Overlay-specific worked examples live under each overlay's own documentation and examples folder.

## License

MIT


This repository is a foundation toolkit for building reusable overlay packages and agent-ready workflows.
