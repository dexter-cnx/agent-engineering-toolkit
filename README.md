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
- [python-service](overlays/python-service/README.md) - Python service, worker, and adapter guidance
- [web-frontend](overlays/web-frontend/README.md) - Web UI and product frontend guidance

## Start here

- `README_START_HERE.md`
- `docs/how-to-use.md`
- `docs/tutorial.md`
- `docs/overlays.md`

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
