# Python Service Overlay

Use this overlay when the consuming repository is a Python service, FastAPI application,
worker, adapter layer, or automation system.

## Use with
- `overlays/backend-common/` for runtime-neutral backend guidance
- `docs/compositions/README.md` for full-stack composition choices
- `docs/compositions/nextjs-python-service/` for the Next.js + Python service reference path

## Start here
- `AGENTS.overlay.md`
- `HOW_TO_USE.md`
- `TUTORIAL.md`
- `SKILLS_INDEX.md`
- `README.th.md`
- `HOW_TO_USE.th.md`
- `TUTORIAL.th.md`

## Purpose
This overlay adds practical guidance for Python service repositories, FastAPI apps,
workers, and automation services while preserving the foundation identity.

## Recommended structure
```text
repo/
├─ app/
│  ├─ routers/
│  ├─ services/
│  ├─ repositories/
│  ├─ domain/
│  ├─ adapters/
│  └─ schemas/
├─ tests/
├─ scripts/
└─ project_memory/
```

## Responsibilities
- `routers/` handle transport concerns only
- `services/` contain orchestration and business use-case flow
- `repositories/` own persistence access
- `domain/` contains core business models or business rules
- `adapters/` isolate external providers and side effects
- `schemas/` define request/response shapes
- keep entry handlers thin and framework-light

Canonical operational rules live in `AGENTS.overlay.md`; this README is the human overview and example index.

## Verification expectations
At minimum, the consuming repo should define commands for:
- import sanity
- startup sanity
- automated tests if present
- lint or static checks if present

Example:
```bash
python -m pytest
python -c "from app.main import app; print(app.title)"
```

## Review guidance
Review should look for:
- route handlers becoming too fat
- services leaking framework concerns
- repositories containing business logic
- adapters bypassing service boundaries
- direct external-provider usage outside adapters

## Memory guidance
Useful durable notes include:
- provider constraints
- API contract rules
- retry and timeout conventions
- background-job behavior assumptions

## Overlay rule
This overlay extends the foundation.
It should not redefine the foundation’s identity.

## Karpathy integration

- Governed exemplar: `skills/python-service-structure/skill.md`
- Contract: `skills/python-service-structure/skill.contract.yaml`
- Eval case: `skills/python-service-structure/eval/cases/governance-smoke/README.md`
## Overlay OS contract

### Purpose
Provide specialization for **python-service** while keeping the repository root stack-neutral.

### When to use
Use this overlay for Python services and worker-oriented backend components.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
