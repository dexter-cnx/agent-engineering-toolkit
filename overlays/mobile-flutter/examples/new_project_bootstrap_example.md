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

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-localization-csv-sync`
- `policies/architecture/README.md`
- `policies/testing/README.md`

## Reference files

- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/prompts/new_project.md`
- `overlays/mobile-flutter/policies/architecture/README.md`
- `overlays/mobile-flutter/policies/testing/README.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/state-management-template.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-clean-architecture-audit
- flutter-feature-folder-scaffold
- flutter-feature-contract-scaffold
- flutter-riverpod-state-skeleton

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
