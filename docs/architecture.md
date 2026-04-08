# Architecture

## Design goal
The toolkit must remain reusable across stacks and project types.

That means the root of this repository should encode:
- process
- governance
- roles
- verification discipline
- memory discipline

It should not encode:
- Flutter as default
- Node as default
- Python as default
- any single framework as the identity of the toolkit

## Foundation vs overlay

### Foundation
Contains:
- AGENTS.md
- generic prompts
- generic skills
- generic templates
- operating docs
- examples

### Overlay
Contains:
- stack-specific assumptions
- stack-specific verification
- stack-specific architecture patterns
- stack-specific CI ideas
- stack-specific agent prompts

## Why this separation matters
Without separation, a toolkit quickly becomes misleading:
it claims to be reusable, but silently assumes one stack.

By keeping specialization in overlays:
- the root stays honest
- the repo stays easier to maintain
- teams can adopt only what they need
- future overlays are easier to add

## Internal conceptual layers

### Governance layer
Rules, lifecycle, expectations.

### Orchestration layer
Prompt pipeline and role flow.

### Capability layer
Skills that perform focused analysis or execution.

### Specialization layer
Overlays for concrete technology contexts.

### Memory layer
Durable context to keep future work coherent.

## Suggested evolution
1. Use foundation only.
2. Add one overlay.
3. Add project-specific rules on top.
4. Connect to CI/CD and agent runtime.
5. Evolve to platform-style orchestration if needed.
