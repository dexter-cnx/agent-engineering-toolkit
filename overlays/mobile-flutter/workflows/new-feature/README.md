# Workflow: New Feature

## Goal

Add a feature module without violating architecture, state, or policy boundaries.

## Execution order

1. `flutter-clean-architecture-audit`
2. `flutter-feature-scaffold`
3. `flutter-riverpod-feature-state` or `flutter-getx-mvc-feature`
4. `flutter-firestore-repository` or `flutter-firebase-auth-flow` if the feature needs Firebase
5. `flutter-go-router-deeplink` if the feature adds routes
6. `flutter-performance-audit` if the feature is visually or data heavy

## Expected outputs

- Feature module folder
- Repository contract and implementation
- State holder and page wiring
- Tests for non-trivial behavior

## Example result

```text
lib/features/profile/data/repositories/profile_repository_impl.dart
lib/features/profile/presentation/pages/profile_page.dart
test/features/profile/profile_controller_test.dart
```
