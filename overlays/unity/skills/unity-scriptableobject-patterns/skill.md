# unity-scriptableobject-patterns Skill

Use this skill when a Unity repo needs config, shared data, or event-channel patterns based on ScriptableObject.

## Rules

- Use ScriptableObjects for config and static data first.
- Use event channels only when they reduce coupling and stay easy to trace.
- Avoid using ScriptableObjects as mutable global state without a clear lifecycle.
- Keep runtime mutation rules explicit and reviewable.
- Separate authoring-time data from runtime-owned state.

## Deliverables

- data ownership plan
- mutation lifecycle notes
- event-channel risks
- validation notes
