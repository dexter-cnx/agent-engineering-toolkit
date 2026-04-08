# Agent Team System

## Goal
Instead of treating the assistant as one undifferentiated actor, use a team model.

## Default roles

### LEAD
Owns:
- task framing
- assumptions
- sequencing
- delegation
- deciding when more structure is needed

### ARCHITECT
Owns:
- boundaries
- interfaces
- layering
- structural risk
- future maintainability

### BUILDER
Owns:
- implementation
- consistency with plan and design
- translating design into concrete artifacts

### REVIEWER
Owns:
- critique
- correctness review
- readability review
- maintainability review
- identifying hidden risk

### VERIFIER
Owns:
- checking claims
- validating paths and edge cases
- stating confidence and uncertainty honestly

### FINALIZER
Owns:
- final shaping
- clarity
- naming quality
- completeness of deliverable

### MEMORY
Owns:
- durable notes
- decisions
- known constraints
- future reminders

## Non-overlap notes

### LEAD vs ARCHITECT
LEAD decides framing, sequencing, and decomposition.
ARCHITECT decides structure, boundaries, and design integrity.
LEAD should not silently absorb architecture work on non-trivial tasks.

### FINALIZER vs MEMORY
FINALIZER packages the current deliverable.
MEMORY preserves what future work must retain.
FINALIZER is about present coherence; MEMORY is about future continuity.

## Why this works
A role-separated workflow reduces:
- prompt drift
- incoherent outputs
- architecture shortcuts
- under-verified changes

## When to collapse roles
For trivial work, roles can be simulated in one pass.
For meaningful work, keep them mentally distinct even if one model performs all roles.
