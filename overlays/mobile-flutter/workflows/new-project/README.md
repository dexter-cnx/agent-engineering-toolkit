# Workflow: New Project

## Goal

Create a Flutter app from scratch with Clean Architecture, state management, routing, and localization.

## Execution order

1. `flutter-clean-architecture-audit` for target structure and constraints.
2. `flutter-feature-folder-scaffold` for the base feature layout.
3. `flutter-feature-contract-scaffold` for core domain contracts.
4. `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton` for state setup.
5. `flutter-go-router-route-map` for router declaration.
6. `flutter-go-router-redirect-guard` for guards and redirects.
7. `flutter-go-router-deeplink-wireup` for deep-link entry wiring.
8. `flutter-design-token-map` for theme/token alignment.
9. `flutter-localization-csv-sync` for CSV-driven localization.
10. `flutter-web-loading-shell` if the app targets web.
11. `flutter-performance-audit` before handoff.

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
