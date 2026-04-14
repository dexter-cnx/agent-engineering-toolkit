Follow `AGENTS.md` strictly.
Apply `overlays/unity/AGENTS.overlay.md`.
Use the `unity-project-structure` skill.

Task:
Review a Unity project structure for boundary clarity, assembly layout, and namespace consistency.

Check:
- whether folders have clear ownership
- whether runtime and editor assemblies are separated
- whether test assemblies exist where needed
- whether namespaces match the folder and asmdef structure
- whether any scene or prefab logic is leaking into the foundation layer

Deliver:
1. findings
2. structure risks
3. concrete recommendations
4. verification notes
