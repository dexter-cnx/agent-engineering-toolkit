# AGENTS.md

## Repository identity
This repository is a **domain-agnostic engineering toolkit**.  
It is not a mobile-only starter.  
Mobile belongs in overlays, not in root assumptions.

## Mandatory execution lifecycle
Every meaningful task should respect this flow:

1. PLAN
2. DESIGN
3. IMPLEMENT
4. REVIEW
5. VERIFY
6. FINALIZE
7. MEMORY UPDATE

Do not skip phases unless the task is truly trivial and non-structural.

## Mandatory output structure
When producing substantial work, prefer this output order:

- Assumptions
- Plan
- Architecture / structure
- Implementation
- Review notes
- Verification notes
- Final result
- Memory update

## Team model
The default team model is:

- LEAD
- ARCHITECT
- BUILDER
- REVIEWER
- VERIFIER
- FINALIZER
- MEMORY

Each role should remain narrow and explicit.

## Hard rules
- Do not implement before understanding the task.
- Do not finalize without verification.
- Do not merge planning, architecture, implementation, and review into one blurred step when the task is complex.
- Do not hide risk.
- Do not hide failed assumptions.
- Do not introduce stack-specific assumptions at the foundation layer.

## Architecture rules
- Keep boundaries clear.
- Prefer layered responsibilities.
- Avoid circular dependencies.
- Keep external providers behind adapters.
- Isolate side effects.
- Keep conventions explainable to future maintainers.

## Documentation rules
If a workflow or architecture changes, update relevant docs:
- README / README_TH when the repository identity changes
- docs/how-to-use(.md / _TH.md) when operator workflow changes
- docs/architecture.md when system boundaries change
- templates and examples when recommended usage changes

## Verification expectations
At minimum:
- check structural correctness
- check obvious edge cases
- check architecture fit
- check that docs remain consistent
- call out anything not yet verified

## Overlay rules
Foundation stays general.
Specialization goes into:
- overlays/mobile-flutter
- overlays/backend-node
- overlays/web-frontend
- overlays/python-service
or project-specific consuming repositories.

## Memory expectations
Project memory is not optional decoration.
It should capture:
- decisions
- patterns
- constraints
- known issues
- next-step reminders
