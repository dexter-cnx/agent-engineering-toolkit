Follow `AGENTS.md` strictly.
Apply `overlays/unity/AGENTS.overlay.md`.
Use the `unity-project-structure` skill.

Task:
Create or audit the Unity project structure so the repo has a stable root layout, asmdef boundaries, and namespace conventions.

Requirements:
- keep feature code under the chosen project root, such as `Assets/_Project`
- separate `Scenes`, `Scripts`, `Prefabs`, `Art`, `Audio`, `Addressables`, and `Tests`
- define runtime, editor, and test assembly boundaries
- align namespaces to folder and assembly ownership
- note any structure risks that could make the repo hard to scale

Deliver:
1. folder plan
2. asmdef plan
3. namespace plan
4. ownership notes
5. verification checklist
