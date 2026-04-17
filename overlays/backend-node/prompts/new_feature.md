# Prompt: New Node Feature

## Intent
Implement one Node backend feature with explicit route, service, repository, and adapter boundaries.

## Use when
- adding a new endpoint or job flow
- updating an existing feature without changing the runtime

## Required inputs
- feature goal
- route or job entry point
- validation needs
- integration needs

## Expected outputs
- implementation plan
- file list
- boundary notes
- test checklist

## Guardrails
- Keep transport, orchestration, persistence, and side effects separate.
- Do not bury provider calls inside routes.

## Repo paths to inspect
- `overlays/backend-node/README.md`
- `overlays/backend-node/AGENTS.overlay.md`
- `overlays/backend-node/examples/worked_example.md`
- `overlays/backend-node/SKILLS_INDEX.md`

## Related skills/workflows
- `route-boundaries`
- `service-orchestration`
- `repository-boundaries`
- `adapter-boundaries`
