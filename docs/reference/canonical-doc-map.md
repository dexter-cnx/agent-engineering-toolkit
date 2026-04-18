# Canonical Document Map

## Public front door
- `README.md`

## One onboarding path
Canonical chain: `README.md -> docs/get-started.md -> docs/adoption-paths.md -> docs/overlays.md`.
- `docs/get-started.md`
- `docs/adoption-paths.md`
- `docs/overlays.md`

## Core architecture
- `docs/architecture/os-overview.md`
- `docs/architecture/task-lifecycle.md`

## Runtime subsystems
- `agents/README.md`
- `prompts/README.md`
- `memory/README.md`
- `system/README.md`

## Operational references
- `docs/reference/prompt-catalog.md`
- `docs/reference/repo-surface-status.md`
- `docs/graph/navigation-map.md`
- `docs/release-process.md` (release gate semantics)

## Gate semantics authority
- Governance gate (Toolkit CI): root `tools/ci/*` checks + `.github/workflows/ci.yml`
- Runtime integration gate: composition/app verification flows (for example `docs/fullstack/dev-workflow.md` and `fullstack:verify`)
- Release gate: `docs/release-process.md`

## Supporting references (non-authoritative for onboarding/architecture)
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

## Compatibility redirectors (legacy links only)
These are non-canonical and not onboarding sources:
- `docs/legacy/START_HERE.md`
- `docs/legacy/README_START_HERE.md`
- `docs/legacy/HOW_TO_USE.md`
- `docs/legacy/ONBOARDING_MINIMAL.md`
- `docs/legacy/ONBOARDING_FULL.md`
- `docs/legacy/INDEX_CANONICAL.md`

## Legacy/frozen top-level namespaces (retained, non-primary)
- `agent_team/`
- `project_memory/`
- `core/`
- `canonical/`
- `checklists/`
- `skills/`
- `companion-pack/`
- `orchestrator/`

## Legacy/frozen doc aliases (retained, non-primary)
- `docs/how-to-use.md`
- `docs/architecture.md`
