# AGENTS.overlay.md

## Overlay Purpose

This overlay equips an agent to design, scaffold, implement, review, and harden Flutter applications using a production-oriented workflow.

## Default assumptions

- Use Flutter stable and Dart 3.
- Prefer Material 3.
- Prefer Clean Architecture.
- Prefer `go_router` for navigation.
- Prefer Riverpod unless the task clearly requires GetX or the project already uses GetX.
- Use `dio` for HTTP unless a project standard says otherwise.
- Use `easy_localization` with CSV as the source of truth for translations when localization is needed.
- Keep business logic out of widgets.
- Treat testing, error handling, and release readiness as part of feature delivery.

## Entry points

### 1. General delivery
Start with `skills/flutter-dev/SKILL.md`.

### 2. Architecture decisions
Start with `skills/flutter-architect/SKILL.md`.

### 3. Code review or refactor
Start with `skills/flutter-code-reviewer/SKILL.md`.

### 4. Release checks
Start with `skills/flutter-release-reviewer/SKILL.md`.

## Skill-routing rules

- New project setup -> `guide-new-flutter-project-bootstrap`
- New feature -> `guide-new-feature-flow`
- Feature layering -> `guide-clean-architecture-feature`
- Routing/deep links -> `flutter-navigation-go-router`
- Riverpod state -> `flutter-state-riverpod`
- GetX state -> `flutter-state-getx`
- Forms -> `flutter-forms-validation`
- Networking -> `flutter-network-dio`
- Localization -> `flutter-localization-csv` + `policy-translation-csv`
- Web startup/loading -> `guide-flutter-web-loading`
- Performance -> `guide-performance-audit`
- Testing -> `flutter-testing-widget` and `flutter-testing-integration`
- Permissions -> `flutter-permissions`
- Maps/location -> `flutter-maps-geolocator`
- Push notifications -> `flutter-fcm-notifications`
- CI enforcement -> `flutter-ci-checks` + `policy-commit-pr-checks`

## Required delivery behavior

When generating or modifying Flutter code:

1. Respect folder and dependency rules from the policy skills.
2. Keep architecture explicit.
3. Add or update tests when the task changes behavior.
4. Update localization files when user-facing strings change.
5. Keep platform setup steps documented when mobile/web integrations are involved.
6. Prefer small, composable widgets and typed models.
7. Do not introduce hidden framework choices; state them clearly.

## Output expectations

- Produce implementation plans before large changes.
- Use feature-oriented structure.
- Surface tradeoffs when selecting state management or persistence.
- Default to repo-safe, CI-safe output.
- Keep markdown docs Obsidian-friendly when generating `.md` files.
