# Unity Overlay

This overlay provides Unity-specific engineering capabilities as reusable skills.
It extends the foundation toolkit without redefining the repository identity.

## Available Skills
See `skills/index.md` for the overlay catalog.

## Operational Docs
- `AGENTS.overlay.md`
- `SKILL_WORKFLOW.md`
- `OVERLAY_VALIDATION_CHECKLIST.md`

## Karpathy integration

- Governed exemplar: `skills/unity-project-structure/skill.md`
- Contract: `skills/unity-project-structure/skill.contract.yaml`
- Eval case: `skills/unity-project-structure/eval/cases/governance-smoke/README.md`

## Examples
See `examples/README.md` for worked examples.

## Usage
Use these skills when working in Unity projects that need structure, runtime, editor, or delivery conventions.
## Overlay OS contract

### Purpose
Provide specialization for **unity** while keeping the repository root stack-neutral.

### When to use
Use this overlay for Unity project architecture and delivery workflows.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
