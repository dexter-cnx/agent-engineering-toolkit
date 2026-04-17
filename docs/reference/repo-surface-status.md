# Repository Surface Status Map

Use this map to distinguish canonical OS surfaces from compatibility and legacy areas.

## Canonical OS surfaces

- `README.md`
- `docs/get-started.md`, `docs/adoption-paths.md`, `docs/overlays.md`
- `docs/architecture/`, `docs/reference/`
- `agents/`, `memory/`, `system/`, `prompts/`
- `tools/ci`, `tools/prompts`, `tools/graph`, `tools/memory`
- `.github/workflows/*governance*.yml`, `.github/workflows/release-readiness.yml`

## Compatibility redirect surfaces

- `START_HERE.md`
- `README_START_HERE.md`
- `HOW_TO_USE.md`
- `ONBOARDING_MINIMAL.md`
- `ONBOARDING_FULL.md`
- `INDEX_CANONICAL.md`

These are retained for inbound links and are non-canonical.

## Legacy but retained surfaces (frozen or transitional)

- `agent_team/` (legacy role quick refs; canonical runtime model is `agents/`)
- `project_memory/` (legacy memory namespace; canonical memory is `memory/`)
- `core/` (legacy quick references; canonical contracts live in `system/`, `docs/`, `agents/`)
- `INDEX_PROMPTS.md`, `INDEX_COMPANION.md`, `INDEX_CHECKLISTS.md` (legacy root indexes)
- `web-frontend` overlay (retained for historical compatibility; prefer common+nextjs overlays when possible)

## Operational guidance

If a canonical and legacy surface disagree, follow canonical surfaces.
New work should not be started from compatibility or legacy surfaces.
