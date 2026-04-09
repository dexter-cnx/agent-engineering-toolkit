# Unity Skill Contract

Use these shared rules across Unity skills.

- Follow `AGENTS.md` and `overlays/unity/AGENTS.overlay.md`.
- Keep Unity-specific boundaries inside the overlay.
- Prefer typed data, explicit scene/bootstrap boundaries, and editor-visible validation.
- Keep platform, provider, and SDK access behind adapters or services.
- Update project memory only for stable conventions or persistent constraints.
- Verify scenes, prefabs, assemblies, and build settings when relevant.
