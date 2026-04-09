# unity-event-driven-gameplay Skill

Use this skill when systems need event-driven coordination instead of direct coupling.

## Rules

- Use the lightest event mechanism that keeps dependencies clear.
- Reserve `UnityEvent` for cases that benefit from inspector wiring.
- Use C# events or message buses when the flow stays clearer in code.
- Use ScriptableObject channels only when they improve authoring or decoupling.
- Keep event ownership, lifetime, and unsubscribe behavior explicit.

## Deliverables

- event-pattern decision
- ownership notes
- unsubscribe risks
- verification checklist
