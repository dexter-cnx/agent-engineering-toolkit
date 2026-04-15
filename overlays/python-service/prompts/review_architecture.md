# Prompt: Review Python Architecture

## Intent
Review route handlers, services, repositories, adapters, and schema placement for boundary drift.

## Use when
- the Python service structure changes
- boundaries need a review before merge

## Required inputs
- folders or files to inspect
- change intent
- runtime context if needed

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Guardrails
- Prefer concrete file evidence.
- Keep the review focused on Python service boundaries.

## Repo paths to inspect
- `overlays/python-service/README.md`
- `overlays/python-service/AGENTS.overlay.md`
- `overlays/python-service/examples/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`

## Related skills/workflows
- `router-boundaries`
- `service-orchestration`
- `repository-boundaries`
