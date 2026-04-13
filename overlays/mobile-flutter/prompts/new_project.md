# Prompt: New Flutter Project

Use the `mobile-flutter` overlay to bootstrap a production-grade Flutter project.

## Load these skills first
- `flutter-dev`
- `guide-new-flutter-project-bootstrap`
- `policy-folder-structure`
- `policy-clean-architecture`
- `flutter-material-3`
- `flutter-navigation-go-router`
- `flutter-network-dio`
- `flutter-state-riverpod`
- `flutter-localization-csv`
- `policy-testing-minimum`

## Working assumptions
- Flutter stable
- Dart 3
- Material 3
- Clean Architecture
- `go_router`
- `dio`
- `easy_localization`
- CSV localization at `assets/i18n/translations.csv`
- Riverpod as the default state management solution

## Required output
1. Explain the proposed project structure.
2. Create the minimal production-ready bootstrap.
3. Add environment, routing, networking, localization, and error-handling setup.
4. Add at least one sample feature vertically sliced through presentation/domain/data.
5. Add baseline test targets.
6. List commands needed to run, test, and build.
7. Keep business logic out of widgets.
8. Keep all user-facing strings localizable.

## Optional repo-specific overrides
Replace defaults when the repository already standardizes on:
- GetX instead of Riverpod
- another HTTP client
- another localization format
- another CI workflow
