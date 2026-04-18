# Repository Surface Status Map

This map classifies top-level surfaces to reduce ambiguity.

## Canonical OS surfaces (primary)

- `README.md` (front door)
- `docs/` (canonical onboarding, architecture, reference)
- `agents/` (canonical role/workflow runtime)
- `memory/` (canonical decisions/state memory)
- `system/` (canonical operating contracts)
- `prompts/` (canonical prompt runtime)
- `tools/` (canonical local governance tooling)
- `overlays/` (canonical specialization layer)
- `.github/workflows/` (canonical CI enforcement)

## Compatibility-only surfaces

- `docs/legacy/START_HERE.md`
- `docs/legacy/README_START_HERE.md`
- `docs/legacy/HOW_TO_USE.md`
- `docs/legacy/ONBOARDING_MINIMAL.md`
- `docs/legacy/ONBOARDING_FULL.md`
- `docs/legacy/INDEX_CANONICAL.md`

These are retained for inbound links and are not onboarding sources.

## Legacy / frozen surfaces (retained, non-primary)

- `agent_team/` (legacy role quick refs; superseded by `agents/`)
- `project_memory/` (legacy memory namespace; superseded by `memory/`)
- `core/` (legacy quick references; superseded by `system/` + `docs/`)
- `canonical/` (legacy baseline documents)
- `checklists/` (legacy checklist set; canonical memory checklists live in `memory/checklists/`)
- `skills/` (legacy skill library; retained for historical/compatibility usage)
- `companion-pack/` (legacy Flutter-focused companion integration kit)
- `orchestrator/` (legacy Python orchestration prototype)
- `docs/legacy/INDEX_PROMPTS.md`, `docs/legacy/INDEX_COMPANION.md`, `docs/legacy/INDEX_CHECKLISTS.md` (legacy frozen indexes)
- `docs/how-to-use.md` and `docs/architecture.md` (legacy/frozen references retained for inbound links)

## Reference/archive surfaces (useful but not OS runtime)

- `apps/`, `packages/`, `samples/`, `examples/` (reference implementations)
- `evals/`, `tests/` (validation assets)
- `reports/`, `artifacts/` (generated/report outputs)
- `scripts/`, `runners/`, `templates/`, `assets/`, `audits/` (supporting/operational materials)

## Operational rule

If canonical and legacy/reference surfaces disagree, canonical surfaces win.
New work should start from canonical OS surfaces only.

## Gate boundaries

- Toolkit CI (`.github/workflows/ci.yml`, `tools/ci/*`) is the **governance gate** for repository coherence.
- Composition/app verification (for example `npm run fullstack:verify`) is the **runtime integration gate**.
- Release workflows (`docs/release-process.md`) define the **release gate**.
