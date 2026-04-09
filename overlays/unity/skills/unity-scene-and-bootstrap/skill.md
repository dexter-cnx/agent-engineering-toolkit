# unity-scene-and-bootstrap Skill

Use this skill when scene loading, startup flow, or platform initialization needs structure.

## Rules

- Keep bootstrap logic in a dedicated entry scene or bootstrapper object.
- Separate scene loading from app lifetime and from platform initialization.
- Register services once, then inject or resolve them through explicit seams.
- Avoid scattering startup logic across unrelated scenes or prefabs.
- Make load order and fallback behavior visible to reviewers.

## Deliverables

- startup flow plan
- scene ownership map
- service registration notes
- validation and risk notes
