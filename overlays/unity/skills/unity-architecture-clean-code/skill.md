# unity-architecture-clean-code Skill

Use this skill when Unity code needs clean-architecture structure or feature modularization.

## Rules

- Keep gameplay domain logic separate from Unity-facing adapters.
- Use presenters or composition layers to bridge UI and gameplay state.
- Make services and repositories explicit instead of implicit singletons.
- Protect core logic from scene, prefab, and editor coupling.
- Favor modular features over monolithic systems.

## Deliverables

- boundary map
- module ownership plan
- adapter and presenter notes
- validation risks
