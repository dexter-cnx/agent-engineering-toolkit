# ADR 0001: Canonical Documentation Architecture

## Status
Accepted

## Decision
Adopt a canonical documentation model centered on:
- `README.md`
- `docs/get-started.md`
- `docs/adoption-paths.md`
- `docs/overlays.md`
- `docs/architecture/os-overview.md`
- `docs/architecture/task-lifecycle.md`
- `docs/reference/canonical-doc-map.md`

Legacy root onboarding/index docs are retained as compatibility redirectors.

## Consequences
- reduced onboarding ambiguity
- easier CI enforcement for doc governance
- explicit migration path for existing inbound links
