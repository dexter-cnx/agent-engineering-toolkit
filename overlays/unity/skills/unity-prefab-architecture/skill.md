# unity-prefab-architecture Skill

Use this skill when a change touches prefab structure, prefab variants, or scene coupling.

## Rules

- Use prefabs for reusable object composition, not for hidden scene orchestration.
- Prefer prefab variants for controlled specialization instead of copy-paste forks.
- Keep nested prefabs intentional and easy to trace.
- Avoid scene-only overrides that make prefab behavior hard to reason about.
- Review coupling between prefab state and scene-specific dependencies.

## Deliverables

- prefab usage decision
- variant or nesting plan
- coupling risks
- validation checklist
