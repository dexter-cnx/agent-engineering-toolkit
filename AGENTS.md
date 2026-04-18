# AGENTS.md

## Repository identity

This repository is a **stack-neutral Agent Engineering OS**.
It is not a mobile-only starter.
Mobile belongs in overlays, not in root assumptions.

## Canonical references

- Front door + onboarding: `README.md` -> `docs/get-started.md` -> `docs/adoption-paths.md`
- Canonical doc/status map: `docs/reference/canonical-doc-map.md` and `docs/reference/repo-surface-status.md`
- OS invariants: `system/kernel/os-invariants.md`
- Architecture authority: `docs/architecture/os-overview.md` and `docs/architecture/task-lifecycle.md`
- Lifecycle: `docs/prompt-pipeline.md`
- Role model: `docs/agent-team-system.md`

## Mandatory execution lifecycle

Use the canonical lifecycle from `docs/prompt-pipeline.md` for meaningful work.

Do not skip phases unless the task is truly trivial and non-structural.

## Mandatory output structure

When producing substantial work, prefer this output order:

- Assumptions
- Plan
- Architecture / structure
- Implementation
- Review notes
- Verification notes
- Final result
- Memory update

## Team model

Use the role model defined in `docs/agent-team-system.md`.

## Hard rules

- Do not implement before understanding the task.
- Do not finalize without verification.
- Do not merge planning, architecture, implementation, and review into one blurred step when the task is complex.
- Do not hide risk.
- Do not hide failed assumptions.
- Do not introduce stack-specific assumptions at the foundation layer.

## Architecture rules

- Keep boundaries clear.
- Prefer layered responsibilities.
- Avoid circular dependencies.
- Keep external providers behind adapters.
- Isolate side effects.
- Keep conventions explainable to future maintainers.

## Documentation rules

If a workflow or architecture changes, update relevant docs:

- README / README_TH when the repository identity changes
- `docs/get-started.md`, `docs/adoption-paths.md`, and `docs/overlays.md` when onboarding/overlay guidance changes
- `docs/architecture/os-overview.md` and `docs/architecture/task-lifecycle.md` when system boundaries or lifecycle changes
- `docs/reference/canonical-doc-map.md` and `docs/reference/repo-surface-status.md` when canonical vs legacy surface status changes
- templates and examples when recommended usage changes

## Verification expectations

At minimum:

- check structural correctness
- check obvious edge cases
- check architecture fit
- check that docs remain consistent
- call out anything not yet verified

## Overlay rules

Foundation stays general.
Specialization goes into overlays or project-specific consuming repositories.

## Memory expectations

Project memory is not optional decoration.
It should capture:

- decisions
- patterns
- constraints
- known issues
- next-step reminders

## Toolkit System (MANDATORY)

For architecture, CI, and design workflows:

- Use toolkit-i18n for localization verify
- Use toolkit-arch for structure validation
- Use toolkit-ci for pipeline debugging
- Use toolkit-design for design token sync

Refer to:
docs/toolkit/00-MOC/toolkit-index.md

Do not bypass toolkit flows unless explicitly required.
