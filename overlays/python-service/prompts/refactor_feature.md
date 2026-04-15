# Prompt: Refactor Python Feature

## Intent
Refactor a Python service feature so transport, orchestration, persistence, and side effects remain separated.

## Use when
- a feature mixes routers, services, repositories, and adapters
- the service needs a boundary cleanup

## Required inputs
- current feature path
- target behavior
- pain points

## Expected outputs
- refactor plan
- changed files
- risk notes

## Guardrails
- Do not redesign the entire service.
- Keep the refactor focused on one feature or boundary.

## Repo paths to inspect
- `overlays/python-service/README.md`
- `overlays/python-service/AGENTS.overlay.md`
- `overlays/python-service/examples/python_service_feature.md`

## Related skills/workflows
- `router-boundaries`
- `service-orchestration`
- `repository-boundaries`
- `adapter-boundaries`
