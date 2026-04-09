Follow `AGENTS.md` strictly.
Apply `overlays/unity/AGENTS.overlay.md`.
Use the `unity-scene-and-bootstrap` skill.

Task:
Review a Unity startup flow for scene-loading clarity, bootstrap ownership, and app-lifetime separation.

Check:
- whether bootstrap logic is isolated
- whether scene loading order is visible and deterministic
- whether platform init is separated from gameplay code
- whether services are registered once and resolved through explicit seams
- whether any startup logic is scattered through unrelated scenes or prefabs

Deliver:
1. findings
2. startup risks
3. recommendations
4. verification notes
