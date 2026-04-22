Follow `AGENTS.md` strictly.
Apply `overlays/mobile-flutter/AGENTS.overlay.md`.
Use the `flutter-production-logging` skill.

Task:
Add or update `flutter-production-logging` in the consuming Flutter repository.

Requirements:
- keep logging boundaries explicit
- keep provider-specific code behind adapters or bootstrap wiring
- produce structured context, redaction, and clear failure handling
- note crash reporting or analytics integration where relevant
- update project memory only with stable conventions

Deliver:
1. file plan
2. boundary plan
3. implementation notes
4. verification notes
5. follow-up risks
