# Prompt: New Python Feature

## Intent
Implement one Python service feature with explicit router, service, repository, and adapter boundaries.

## Use when
- adding a new endpoint or worker flow
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
- Do not bury provider calls inside routers.

## Repo paths to inspect
- `overlays/python-service/README.md`
- `overlays/python-service/AGENTS.overlay.md`
- `overlays/python-service/examples/python_service_feature.md`
- `overlays/python-service/SKILLS_INDEX.md`

## Related skills/workflows
- `router-boundaries`
- `service-orchestration`
- `repository-boundaries`
- `adapter-boundaries`
