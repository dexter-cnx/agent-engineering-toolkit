# Prompt: Refactor Node Feature

## Intent
Refactor a Node backend feature so transport, orchestration, persistence, and side effects remain separated.

## Use when
- a feature mixes routes, services, repositories, and adapters
- the backend needs a boundary cleanup

## Required inputs
- current feature path
- target behavior
- pain points

## Expected outputs
- refactor plan
- changed files
- risk notes

## Guardrails
- Do not redesign the entire backend.
- Keep the refactor focused on one feature or boundary.

## Repo paths to inspect
- `overlays/backend-node/README.md`
- `overlays/backend-node/AGENTS.overlay.md`
- `overlays/backend-node/examples/worked_example.md`

## Related skills/workflows
- `route-boundaries`
- `service-orchestration`
- `repository-boundaries`
- `adapter-boundaries`
