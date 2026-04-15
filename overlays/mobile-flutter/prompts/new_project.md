# Prompt: New Project

## Intent

Bootstrap a new Flutter app from the overlay with clean architecture, routing, state, localization, and baseline tests.

## When to use

- Starting a new consuming Flutter repository
- Initializing a starter app from `starter-app-template/`
- You need a production-oriented baseline before feature work begins

## Required inputs

- App name
- Package name
- State management choice
- Target platforms
- Localization source of truth

## Optional inputs

- Feature list for the first slice
- CI provider details
- Web support yes/no
- Firebase yes/no

## Expected outputs

- App shell and folder structure
- Router shell
- State layer baseline
- Localization baseline
- Test baseline
- First-pass release notes

## Repo paths to inspect

- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/starter-app-template/`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/translations.csv`
- `overlays/mobile-flutter/examples/real-world/new-feature-module.md`

## Related skills and workflows

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-getx-controller-skeleton`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-localization-csv-sync`
- `workflows/new-project/README.md`

## Guardrails

- Keep business logic out of widgets
- Do not mix Riverpod and GetX in the same baseline unless the app already does
- Do not add Firebase, routing, or release logic before the shell exists
- Keep file creation aligned with the template

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-project/README.md.

Task:
Bootstrap a new Flutter app named <app_name> with <state_choice> state management and CSV localization.

Deliver:
1. exact files to create
2. chosen skills
3. implementation order
4. validation checklist
```
