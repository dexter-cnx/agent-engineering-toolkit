# Workflow: Release Readiness

## Mission
Prove repository release readiness with evidence, not assumptions.

## Inputs
All governance workflow results, unresolved risk list, security policy status.

## Outputs
- go/no-go recommendation
- explicit unresolved risks
- memory state refresh and next-pass actions

## Boundaries
- Cannot mark ready when critical governance checks fail.
- Cannot hide unresolved known debts.

## Escalation conditions
- failing required CI workflows
- unsupported public claims in docs/security metadata
- missing ownership for post-release follow-up
