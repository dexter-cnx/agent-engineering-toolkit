# Workflow: New Project

## Goal

Create a Flutter app from scratch with Clean Architecture, state management, routing, and localization.

## Execution order

1. `flutter-clean-architecture-audit` for target structure and constraints.
2. `flutter-feature-scaffold` for the base feature layout.
3. `flutter-riverpod-feature-state` or `flutter-getx-mvc-feature` for state setup.
4. `flutter-go-router-deeplink` for router and startup flow.
5. `flutter-design-token-sync` for theme/token alignment.
6. `flutter-web-loading-shell` if the app targets web.
7. `flutter-performance-audit` before handoff.

## Expected outputs

- App folder structure
- Feature scaffold
- Router shell
- Theme/token bridge
- Localization-ready entry points

## Example result

```text
lib/app/router/app_router.dart
lib/features/home/presentation/pages/home_page.dart
lib/features/home/presentation/controllers/home_controller.dart
```
