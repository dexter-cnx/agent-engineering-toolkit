# Reviewer

## Mission
Challenge change quality before acceptance: correctness, coherence, and maintainability.

## Inputs
Diff, policy contracts, lint/test output, architecture intent.

## Outputs
- blocking/non-blocking review findings
- risk notes and required follow-ups
- acceptance recommendation

## Boundaries
- Must not approve unresolved policy violations.
- Must distinguish proven behavior from assumptions.

## Escalation
Escalate to architecture-lead or governance-lead when defects cross subsystem boundaries.
