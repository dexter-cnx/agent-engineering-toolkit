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
- consistency with plan/design
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

## Why this works
A role-separated workflow reduces:
- prompt drift
- incoherent outputs
- architecture shortcuts
- under-verified changes

## When to collapse roles
For trivial work, roles can be simulated in one pass.
For meaningful work, keep them mentally distinct even if one model performs all roles.
