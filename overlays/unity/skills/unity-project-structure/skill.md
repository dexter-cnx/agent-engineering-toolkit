# unity-project-structure Skill

Use this skill when a Unity repo needs a stable project layout or a structure audit.

## Rules

- Keep feature code under the repo's chosen project root, such as `Assets/_Project`.
- Lock folder ownership for `Scenes`, `Scripts`, `Prefabs`, `Art`, `Audio`, `Addressables`, and `Tests`.
- Split assemblies by runtime, editor, and test boundaries when coupling starts to grow.
- Match namespaces to folders and assembly boundaries.
- Treat structure changes as architectural changes, not cosmetic cleanup.

## Deliverables

- folder and asmdef plan
- namespace plan
- naming and ownership notes
- validation risks
