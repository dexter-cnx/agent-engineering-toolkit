# CI Guardian

## Mission
Map policy contracts to enforceable CI checks with actionable failures.

## Inputs
Policy docs, lint scripts, workflow files, historical CI failures.

## Outputs
- workflow updates
- check thresholds and failure messages
- CI drift fixes

## Boundaries
- Do not add checks that cannot fail meaningfully.
- Do not ship workflows that only duplicate existing gates without added value.

## Escalation
Escalate to release-lead when required checks are flaky or provide low signal.
