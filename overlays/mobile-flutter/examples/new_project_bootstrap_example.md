# New Project Bootstrap Example

## Scenario

A team needs to start a new Flutter app with production-oriented defaults:

- Flutter stable and Dart 3
- Material 3
- Clean Architecture
- Riverpod
- `go_router`
- `dio`
- CSV-based localization

## Recommended skills

- `flutter-dev`
- `guide-new-flutter-project-bootstrap`
- `guide-clean-architecture-feature`
- `policy-folder-structure`
- `policy-testing-minimum`

## Reference files

- `overlays/mobile-flutter/skills/guide-new-flutter-project-bootstrap/SKILL.md`
- `overlays/mobile-flutter/prompts/new_project.md`
- `overlays/mobile-flutter/skills/policy-folder-structure/SKILL.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-dev
- guide-new-flutter-project-bootstrap
- policy-folder-structure
- policy-testing-minimum

Task:
Bootstrap a new mobile Flutter app with a clear folder structure, router
scaffold, localization baseline, and first-pass tests.

Deliver:
1. project structure
2. bootstrap notes
3. boundary decisions
4. verification checklist
```

## Expected output

- a clean app shell
- a route registry
- a starter localization setup
- a test baseline
- a short list of decisions that future work must preserve

## Review notes

- bootstrap code should stay thin and easy to extend
- the app shell should not embed feature business logic
- default state management should be explicit, not implicit

## Verification notes

- confirm the overlay starts from `flutter-dev`
- confirm the bootstrap prompt stays inside `overlays/mobile-flutter/prompts/`
- confirm the resulting folder structure matches policy
