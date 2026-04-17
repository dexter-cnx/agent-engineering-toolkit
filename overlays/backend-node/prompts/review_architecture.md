# Prompt: Review Node Architecture

## Intent
Review routes, services, repositories, adapters, and schema placement for boundary drift.

## Use when
- the Node backend structure changes
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
- Keep the review focused on Node backend boundaries.

## Repo paths to inspect
- `overlays/backend-node/README.md`
- `overlays/backend-node/AGENTS.overlay.md`
- `overlays/backend-node/examples/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`

## Related skills/workflows
- `route-boundaries`
- `service-orchestration`
- `repository-boundaries`
