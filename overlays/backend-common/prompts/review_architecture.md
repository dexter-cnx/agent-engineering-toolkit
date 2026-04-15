# Prompt: Review Backend Architecture

## Intent
Review the backend for boundary clarity, contract stability, and layer separation.

## Use when
- a backend feature changed structure
- you need a boundary audit before merge

## Required inputs
- folders or files to inspect
- change intent
- runtime if relevant

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the backend architecture for the profile and account modules. Look for unclear boundaries, unstable contracts, and layer leaks.`

## Guardrails
- Prefer concrete file evidence.
- Do not mix runtime-specific implementation concerns into the review.

## Repo paths to inspect
- `overlays/backend-common/skills/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`
- `overlays/backend-common/examples/`

## Related skills and workflows
- `api-contracts`
- `crud-resource-design`
- `backend-testing-strategy`
