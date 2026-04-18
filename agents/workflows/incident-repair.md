# Workflow: Incident Repair

## Mission
Restore repository governance integrity after breakage, drift, or unsafe changes.

## Inputs
Incident description, failing checks, affected subsystem paths.

## Outputs
- containment fix
- root cause notes
- preventive control updates (lint/workflow/policy)

## Boundaries
- Prioritize containment and correctness over broad refactors.
- Do not close incident without prevention step.

## Escalation conditions
- repeated regression after fix
- security-reporting path affected
- cross-subsystem breakage with unclear ownership
