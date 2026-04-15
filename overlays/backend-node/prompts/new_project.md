# Prompt: New Node Backend

## Intent
Plan a Node backend with thin routes, service orchestration, repository boundaries, and adapter isolation.

## Use when
- starting a new Node backend or API service
- defining backend boundaries before implementation

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
- Keep routes thin.
- Keep service orchestration separate from transport.
- Keep provider calls behind adapters.

## Repo paths to inspect
- `overlays/backend-node/README.md`
- `overlays/backend-node/AGENTS.overlay.md`
- `overlays/backend-node/examples/`
- `overlays/backend-common/README.md`

## Related skills/workflows
- `node-service-structure`
- `route-boundaries`
- `service-orchestration`
- `repository-boundaries`
