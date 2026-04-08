# agent-engineering-toolkit

A production-ready, domain-agnostic toolkit for structured AI-assisted software engineering.

This repository is a foundation toolkit that can be reused across:
- mobile projects
- backend services
- web frontends
- AI and agent systems
- monorepos
- internal engineering platforms

It is intentionally not tied to mobile. Mobile is treated as an overlay, not the default identity of the toolkit.

## Why this repository exists

Most AI coding setups stop at “generate code from a prompt”.

This toolkit goes further by providing:
- a reusable operating model
- a canonical prompt pipeline
- an agent team model
- reusable narrow skills
- templates for project adoption
- overlays for stack-specific specialization
- documentation discipline for long-term maintainability
- public-repo hygiene for open collaboration

This repository is the foundation layer. Project-specific rules belong in overlays or in consuming repositories.

## Canonical references

- Lifecycle source of truth: `docs/prompt-pipeline.md`
- Role model source of truth: `docs/agent-team-system.md`
- Prompt hub: `prompts/index.md`
- Prompt hub (English): `prompts/index_EN.md`
- Adoption guide: `docs/how-to-use.md`
- Tutorial: `docs/tutorial.md`
- Audit prompt (role-based): `prompts/review/audit_repo.md`
- Audit prompt (invocation template): `docs/strict-audit-prompt.md`

## What is included

- `AGENTS.md` for governance and expectations
- `docs/` for usage, architecture, adoption, release, and tutorial guidance
- `prompts/` for stage-oriented workflows
- `agent_team/` for role definitions
- `skills/` for focused reusable capabilities
- `core/` for rules, routing, verification, and review discipline
- `templates/` for project bootstrap and operational consistency
- `overlays/` for stack-specific extensions
- `examples/` for concrete adoption patterns and worked examples
- `.github/` for CI, issue templates, PR template, CODEOWNERS, and security policy
- `.gitignore` for repository hygiene

## Quick start

### Use as its own repository
Push this repo directly and maintain it as the canonical toolkit.

### Use as a submodule
```bash
git submodule add <toolkit-repo-url> toolkit
```

### Optional bootstrap helper
```bash
bash scripts/bootstrap-project-memory.sh
```

### Use with AI tooling
Start with:

```text
Follow AGENTS.md strictly.
Use the canonical lifecycle from docs/prompt-pipeline.md.
Use the role model from docs/agent-team-system.md.
```

### Start-here guide
- `README_START_HERE.md` for the shortest public onboarding path

## Worked examples

- Foundation-level example: `examples/worked_examples/foundation_feature_flow.md`
- Overlay examples:
  - `overlays/mobile-flutter/examples/worked_example.md`
  - `overlays/backend-node/examples/worked_example.md`
  - `overlays/web-frontend/examples/worked_example.md`
  - `overlays/python-service/examples/python_service_feature.md`

## Documentation

- `docs/how-to-use.md` — canonical English guide
- `docs/how-to-use_TH.md` — canonical Thai guide
- `docs/tutorial.md` — English tutorial
- `docs/tutorial_TH.md` — Thai tutorial
- `docs/tutorials/index.md` — Obsidian-friendly tutorial hub grouped by platform (Thai)
- `docs/tutorials/index_EN.md` — Obsidian-friendly tutorial hub grouped by platform (English)
- `docs/tutorials/agents-and-prompts.md` — AGENTS.md and prompt guide (Thai)
- `docs/tutorials/agents-and-prompts_EN.md` — AGENTS.md and prompt guide (English)
- `docs/architecture.md` — foundation vs overlay architecture
- `docs/agent-team-system.md` — role system guidance
- `docs/prompt-pipeline.md` — canonical lifecycle reference
- `docs/overlays.md` — specialization strategy
- `docs/real-world-integration.md` — practical usage guidance
- `docs/repo-bootstrap.md` — applying the toolkit to a new repo
- `docs/public-repo-checklist.md` — pre-publish checklist
- `scripts/check-public-repo.paths` — machine-readable public-release gate source
- `docs/release-process.md` — suggested release process
- `docs/strict-audit-prompt.md` — strict audit prompt
- `docs/obsidian-friendly.md` — consolidated Obsidian-friendly reference
- `scripts/bootstrap-project-memory.sh` — small helper for submodule plus memory-template bootstrap

## License

MIT
