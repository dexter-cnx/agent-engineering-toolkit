# Prompt: New Python Service

## Intent
Plan a Python service with thin routers, service orchestration, repository boundaries, and adapter isolation.

## Use when
- starting a new Python service or FastAPI app
- defining service boundaries before implementation

## Required inputs
- service goal
- primary routes or use cases
- data access needs
- external integrations

## Expected outputs
- folder tree
- boundary plan
- implementation order
- verification checklist

## Guardrails
- Keep routers thin.
- Keep service orchestration separate from transport.
- Keep provider calls behind adapters.

## Repo paths to inspect
- `overlays/python-service/README.md`
- `overlays/python-service/AGENTS.overlay.md`
- `overlays/python-service/examples/`
- `overlays/backend-common/README.md`

## Related skills/workflows
- `python-service-structure`
- `router-boundaries`
- `service-orchestration`
- `repository-boundaries`
