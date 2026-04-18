# Memory Subsystem (Canonical)

`memory/` is the canonical continuity layer for repository decisions and state.

## Sections

- `decisions/` → durable architecture/governance decisions (ADRs)
- `state/` → current operational status and near-term execution context
- `patterns.md` → practices that repeatedly improve outcome quality
- `anti-patterns.md` → failure modes that caused drift or rework
- `checklists/` → repeatable release/verification checks
- `glossary.md` → shared operational vocabulary

## Update expectations

- Update `decisions/` only when policy/architecture direction changes.
- Update `state/` on every meaningful repo-hardening or release-readiness pass.
- If a repeated failure appears, add it to `anti-patterns.md` with a prevention rule.

## Boundary note

`project_memory/` is legacy/transitional and retained for historical reads only.
All new memory entries belong in `memory/`.
