Follow `AGENTS.md` strictly.
Apply `overlays/unity/AGENTS.overlay.md`.
Use the `unity-scene-and-bootstrap` skill.

Task:
Design or implement the Unity startup flow for a project that needs a bootstrap scene, app lifetime ownership, and service registration.

Requirements:
- keep bootstrap logic separate from gameplay scenes
- separate scene loading from app lifetime and platform initialization
- register services through an explicit composition root or installer layer
- document the load order and fallback behavior

Deliver:
1. scene plan
2. bootstrap plan
3. service registration notes
4. failure and fallback notes
5. verification checklist
