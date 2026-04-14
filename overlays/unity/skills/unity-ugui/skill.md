# unity-ugui Skill

Use this skill when the project uses uGUI and needs screen composition or UI maintenance rules.

## Rules

- Keep presentation concerns in UI prefabs and scene composition, not in domain logic.
- Prefer clear Canvas and layout ownership over ad-hoc object hierarchies.
- Use dedicated presenters or binders for UI-to-data translation.
- Control EventSystem and navigation behavior explicitly.
- Watch for hidden coupling between screens, scenes, and shared UI state.

## Deliverables

- screen hierarchy plan
- binding strategy
- layout and navigation risks
- validation notes
