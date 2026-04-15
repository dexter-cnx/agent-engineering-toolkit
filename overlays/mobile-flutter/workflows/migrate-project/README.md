# Workflow: Migrate Project

## Goal

Move a legacy Flutter codebase toward the overlay's production architecture without freezing delivery.

## Execution order

1. `flutter-clean-architecture-audit`
2. `flutter-feature-folder-scaffold`
3. `flutter-feature-contract-scaffold`
4. `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton`
5. `flutter-go-router-route-map`
6. `flutter-go-router-redirect-guard`
7. `flutter-go-router-deeplink-wireup`
8. `flutter-firestore-repository` or `flutter-firebase-auth-adapter` when applicable
9. `flutter-firebase-auth-state` when route guards depend on auth
10. `flutter-performance-audit`

## Expected outputs

- Violation inventory
- Migration slices
- Refactor order
- Verification checklist

## Example result

```text
lib/features/profile/
lib/app/router/app_router.dart
test/features/profile/profile_page_test.dart
```
