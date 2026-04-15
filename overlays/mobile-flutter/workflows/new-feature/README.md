# Workflow: New Feature

## Goal

Add a feature module without violating architecture, state, or policy boundaries.

## Execution order

1. `flutter-clean-architecture-audit`
2. `flutter-feature-folder-scaffold`
3. `flutter-feature-contract-scaffold`
4. `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton`
5. `flutter-firestore-repository` or `flutter-firebase-auth-adapter` if the feature needs Firebase
6. `flutter-firebase-auth-state` if route guards need auth state
7. `flutter-go-router-route-map` if the feature adds routes
8. `flutter-go-router-redirect-guard` if the feature needs auth or onboarding gates
9. `flutter-go-router-deeplink-wireup` if the feature must open from a link
10. `flutter-performance-audit` if the feature is visually or data heavy

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
