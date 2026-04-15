# Workflow: Migrate Project

## Goal

Move a legacy Flutter codebase toward the overlay's production architecture without freezing delivery.

## Execution order

1. `flutter-clean-architecture-audit`
2. `flutter-feature-scaffold`
3. `flutter-riverpod-feature-state` or `flutter-getx-mvc-feature`
4. `flutter-go-router-deeplink`
5. `flutter-firestore-repository` or `flutter-firebase-auth-flow` when applicable
6. `flutter-performance-audit`

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
