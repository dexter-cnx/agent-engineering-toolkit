# Internal Operating Model

## Purpose
This toolkit should operate as an internal development system, not just a collection of prompts and docs.

## Operating layers
1. **Foundation**
   - shared rules
   - reusable prompt patterns
   - canonical documentation
   - audit templates
2. **Overlay**
   - team-specific conventions
   - stack-specific guidance
   - environment-specific workflows
3. **Consumer repo**
   - actual implementation
   - product rules
   - domain decisions

## Principle
Foundation informs. Overlay adapts. Consumer repo decides.

## Execution model
### Stage 1: Lead
Clarify scope, assumptions, deliverables, and sequencing.

### Stage 2: Architecture
Map boundaries, responsibilities, folders, interfaces, and migration constraints.

### Stage 3: Implementation
Generate or modify code in small, reviewable units.

### Stage 4: Review
Check drift, coupling, duplication, and rule violations.

## Internal merge gate
A change is not ready until:
- documentation paths are clear
- canonical ownership is preserved
- generated outputs have verification steps
- prompts reference the right docs
- CI passes
