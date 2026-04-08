Follow `AGENTS.md` strictly.
Apply `overlays/mobile-flutter/AGENTS.overlay.md`.
Use the `flutter-build-flavors` skill.

Task:
Add or update `flutter-build-flavors` in the consuming Flutter repository.

Requirements:
- keep capability boundaries explicit
- keep provider-specific code behind adapters, services, or repositories
- produce typed models and clear failure handling
- note platform-specific behavior where relevant
- update project memory only with stable conventions

Deliver:
1. file plan
2. capability boundary plan
3. implementation notes
4. verification notes
5. follow-up risks
