# Prompt: Review Node Security

## Intent
Review provider isolation, request handling, and sensitive-data exposure in the Node backend.

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
- `overlays/backend-node/README.md`
- `overlays/backend-node/AGENTS.overlay.md`
- `overlays/backend-node/examples/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`

## Related skills/workflows
- `adapter-boundaries`
- `repository-boundaries`
- `service-orchestration`
