# agent-engineering-toolkit

A production-ready, domain-agnostic toolkit for structured AI-assisted software engineering.

This repository is designed as a **foundation toolkit** that can be reused across:
- mobile projects
- backend services
- web frontends
- AI/agent systems
- monorepos
- internal engineering platforms

It is intentionally **not tied to mobile**.  
Mobile is treated as an **overlay**, not the default identity of the toolkit.

## Why this repository exists

Most AI coding setups stop at “generate code from a prompt”.

This toolkit goes further by providing:
- a reusable operating model
- a stage-based prompt pipeline
- an agent team model
- reusable narrow skills
- templates for project adoption
- overlays for stack-specific specialization
- documentation discipline for long-term maintainability

This repository is the **foundation layer**.  
Project-specific rules belong in overlays or in consuming repositories.

## Core lifecycle

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

## Default team model

```text
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY
```

## What is included

- `AGENTS.md` for governance and expectations
- `docs/` for detailed usage and architecture guidance
- `prompts/` for stage-oriented workflows
- `agent_team/` for role definitions
- `skills/` for focused reusable capabilities
- `core/` for rules, routing, verification, and review discipline
- `templates/` for project bootstrap and operational consistency
- `overlays/` for stack-specific extensions
- `examples/` for concrete adoption patterns
- `.github/` for public-repo hygiene and CI

## Repository structure

```text
agent-engineering-toolkit/
├─ AGENTS.md
├─ README.md
├─ README_TH.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ CHANGELOG.md
├─ CODE_OF_CONDUCT.md
├─ docs/
├─ prompts/
├─ agent_team/
├─ skills/
├─ core/
├─ templates/
├─ overlays/
├─ examples/
├─ project_memory/
├─ scripts/
└─ .github/
```

## Quick start

### Use as its own repository
Push this repo directly and maintain it as the canonical toolkit.

### Use as a submodule
```bash
git submodule add <toolkit-repo-url> toolkit
```

### Use with AI tooling
Start with:

```text
Follow AGENTS.md strictly.
Use the full pipeline:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

## Documentation

- `README_TH.md` — Thai overview
- `docs/how-to-use.md` — detailed English guide
- `docs/how-to-use_TH.md` — detailed Thai guide
- `docs/architecture.md` — foundation vs overlay architecture
- `docs/agent-team-system.md` — role system guidance
- `docs/prompt-pipeline.md` — prompt flow
- `docs/overlays.md` — specialization strategy
- `docs/real-world-integration.md` — practical usage guidance
- `docs/repo-bootstrap.md` — applying the toolkit to a new repo
- `docs/public-repo-checklist.md` — pre-publish checklist
- `docs/release-process.md` — suggested release process
- `docs/codex-review-prompt.md` — strict Codex review prompt

## Public release notes

Before publishing broadly:
- confirm your preferred license choice
- review `CODEOWNERS`
- review issue/discussion URLs
- skim both README files for organization-specific wording
- run the CI workflow

## License

MIT
