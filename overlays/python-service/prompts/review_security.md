# Prompt: Review Python Security

## Intent
Review provider isolation, request handling, and sensitive-data exposure in the Python service.

## Use when
- external integrations change
- request or response handling changes

## Required inputs
- paths to inspect
- security concern
- runtime context if relevant

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Guardrails
- Keep the review about backend behavior and provider isolation.
- Prefer concrete evidence from repository paths.

## Repo paths to inspect
- `overlays/python-service/README.md`
- `overlays/python-service/AGENTS.overlay.md`
- `overlays/python-service/examples/`
- `overlays/backend-common/skills/file-handling-safety/skill.md`

## Related skills/workflows
- `adapter-boundaries`
- `repository-boundaries`
- `service-orchestration`
