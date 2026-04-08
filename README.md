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
- a stage-based prompt pipeline
- an agent team model
- reusable narrow skills
- templates for project adoption
- overlays for stack-specific specialization
- documentation discipline for long-term maintainability
- public-repo hygiene for open collaboration

This repository is the foundation layer. Project-specific rules belong in overlays or in consuming repositories.

## Core lifecycle

The canonical lifecycle lives in `docs/prompt-pipeline.md`.

Short form:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

## Default team model

```text
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY
```

## What is included

- `AGENTS.md` for governance and expectations
- `docs/` for usage, architecture, adoption, release, and tutorial guidance
- `prompts/` for stage-oriented workflows
- `agent_team/` for role definitions
- `skills/` for focused reusable capabilities
- `core/` for rules, routing, verification, and review discipline
- `templates/` for project bootstrap and operational consistency
- `overlays/` for stack-specific extensions
- `examples/` for concrete adoption patterns
- `.github/` for CI, issue templates, PR template, CODEOWNERS, and security policy

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
Use the canonical lifecycle from docs/prompt-pipeline.md.
```

## Documentation

- `docs/how-to-use.md` — canonical English guide
- `docs/how-to-use_TH.md` — canonical Thai guide
- `docs/tutorial.md` — English tutorial
- `docs/tutorial_TH.md` — Thai tutorial
- `docs/architecture.md` — foundation vs overlay architecture
- `docs/agent-team-system.md` — role system guidance
- `docs/prompt-pipeline.md` — canonical lifecycle reference
- `docs/overlays.md` — specialization strategy
- `docs/real-world-integration.md` — practical usage guidance
- `docs/repo-bootstrap.md` — applying the toolkit to a new repo
- `docs/public-repo-checklist.md` — pre-publish checklist
- `docs/release-process.md` — suggested release process
- `docs/codex-review-prompt.md` — strict Codex review prompt

## License

MIT
