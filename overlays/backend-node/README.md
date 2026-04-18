# Backend Node Overlay

Use this overlay when the consuming repository is a Node backend, API service, or job processor.

## Use with
- `overlays/backend-common/` for runtime-neutral backend guidance
- `docs/compositions/README.md` for full-stack composition choices
- `docs/compositions/nextjs-nodebackend/` for the Next.js + Node backend reference path
- `overlays/backend-common/docs/backend-node-reuse-analysis.md` for what can be shared conceptually

## Start here
- `AGENTS.overlay.md`
- `HOW_TO_USE.md`
- `TUTORIAL.md`
- `SKILLS_INDEX.md`
- `README.th.md`
- `HOW_TO_USE.th.md`
- `TUTORIAL.th.md`

## Recommended structure
```text
repo/
├─ src/
│  ├─ routes/
│  ├─ services/
│  ├─ repositories/
│  ├─ adapters/
│  ├─ domain/
│  └─ schemas/
├─ test/
└─ project_memory/
```

## Responsibilities
- route handlers own entry concerns only
- business orchestration stays in a dedicated feature/service/domain layer
- external integrations stay behind service or adapter boundaries
- project memory captures recurring stack-specific conventions

Canonical operational rules live in `AGENTS.overlay.md`; this README is the human overview and example index.

## Verification examples
```bash
npm run lint
npm test
```

## Review guidance
Reject changes when:
- routes/controllers becoming too fat
- services leaking transport concerns
- direct provider calls outside adapters

## Overlay rule
This overlay extends the foundation.
It should not redefine the foundation identity.

## Karpathy integration

- Governed exemplar: `skills/node-service-structure/skill.md`
- Contract: `skills/node-service-structure/skill.contract.yaml`
- Eval case: `skills/node-service-structure/eval/cases/governance-smoke/README.md`
## Overlay OS contract

### Purpose
Provide specialization for **backend-node** while keeping the repository root stack-neutral.

### When to use
Use this overlay for Node.js backend APIs, workers, and service patterns.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
