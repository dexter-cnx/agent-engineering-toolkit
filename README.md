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

---

## Why this repository exists

Most AI coding setups stop at "generate code from a prompt".

This toolkit aims higher:

- enforce structured workflows
- separate planning, architecture, implementation, review, verification, and memory
- make outputs more deterministic
- keep knowledge reusable across repositories
- support multiple AI surfaces such as Codex CLI, Claude Code, OpenClaw, and future agents

This repository is the **foundation layer**.  
Project-specific rules belong in overlays or consuming repositories.

---

## Core operating model

The default lifecycle is:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

The default team model is:

```text
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY
```

---

## What is included

### Governance
- `AGENTS.md`
- reusable operating rules
- architecture and verification expectations

### Prompt pipeline
- planning prompts
- architecture prompts
- implementation prompts
- review prompts
- verification prompts
- finalization prompts
- memory update prompts

### Skill system
- reusable narrow capabilities
- audit-focused and architecture-focused building blocks
- skill router and risk model guidance

### Templates
- project bootstrap templates
- runbook templates
- project memory templates
- review templates
- verification templates

### Overlays
- `mobile-flutter`
- `backend-node`
- `web-frontend`
- `python-service`

### Examples
- example prompts
- example workflows
- example integration guidance

### CI
- lightweight validation workflow for this toolkit repository

---

## Repository structure

```text
agent-engineering-toolkit/
├─ AGENTS.md
├─ README.md
├─ README_TH.md
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
└─ .github/workflows/
```

---

## Quick start

### 1) Use as a standalone toolkit repo
Clone and push as its own repository.

### 2) Use as a submodule in another repo
```bash
git submodule add <toolkit-repo-url> toolkit
```

### 3) Use with an AI coding surface
Start with:

```text
Follow AGENTS.md strictly.
Use the full pipeline:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

---

## Typical use cases

### Use case 1: foundation for a mobile toolkit
Use this repo as the base, then apply:
- `overlays/mobile-flutter`
- Flutter-specific project rules
- Flutter-specific verification
- Flutter-specific prompts

### Use case 2: backend platform
Use:
- `overlays/backend-node` or `overlays/python-service`
- API and service architecture rules
- adapter-based integration guidance

### Use case 3: web product
Use:
- `overlays/web-frontend`
- frontend design system rules
- operator dashboard conventions

### Use case 4: internal engineering platform
Use:
- the full team model
- skill router
- runbook templates
- memory system
- verification gates

---

## Recommended adoption sequence

### Phase 1 — Foundation adoption
Adopt:
- `AGENTS.md`
- prompt pipeline
- project memory
- repo audit and architecture review skills

### Phase 2 — Team workflow
Adopt:
- lead/architect/builder/reviewer/verifier roles
- runbooks
- verification gate
- review templates

### Phase 3 — Overlay specialization
Add:
- mobile/backend/web/python overlay
- repo-specific instructions
- project-specific verification and CI

### Phase 4 — Platform integration
Integrate with:
- Codex CLI
- Claude Code Agent Teams
- OpenClaw gateway
- CI/CD pipelines
- internal dashboards

---

## Documentation

- `README_TH.md` — Thai overview
- `docs/how-to-use.md` — detailed English guide
- `docs/how-to-use_TH.md` — detailed Thai guide
- `docs/architecture.md` — architecture model
- `docs/agent-team-system.md` — detailed team model
- `docs/prompt-pipeline.md` — prompt flow and usage
- `docs/overlays.md` — overlay strategy
- `docs/real-world-integration.md` — practical integration
- `docs/repo-bootstrap.md` — how to apply toolkit to a new repository
- `docs/roadmap.md` — future evolution

---

## Publishing checklist

Before pushing publicly, update:
- repository URL references
- author metadata
- license
- organization-specific wording if needed

---

## License

Add your preferred license before publishing.
