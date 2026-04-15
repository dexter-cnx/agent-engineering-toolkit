# flutter-riverpod-feature-state

## Purpose

Implement feature state with Riverpod using explicit providers, notifier classes, and testable state transitions.

## Use when

- The project standard is Riverpod
- The feature needs async loading or derived state
- You want one-direction state flow with clear repository boundaries

## Do NOT use when

- The project standard is GetX and the team has already committed to it
- The feature has no meaningful state
- You need only a one-off widget local state interaction

## Inputs required

- Feature name
- State events or user actions
- Repository or use case contracts
- Loading/error semantics

## Constraints

- Keep data fetches outside widgets
- Use typed state instead of unstructured maps
- Keep controller logic in providers or notifiers
- Add tests for loading, success, and error cases

## Step-by-step workflow

1. Define the state model.
2. Define the provider or notifier class.
3. Inject repository or use case dependencies.
4. Map events to state transitions.
5. Wire the page to read and react to state.
6. Add unit tests for the notifier or controller.

## Output contract

- Provider or notifier file
- State model file
- Page wiring file
- Test file for state transitions

## Validation checklist

- State transitions are deterministic
- The view does not call the repository directly
- Async loading and error states are explicit
- The provider can be tested without UI

## Related skills

- `flutter-feature-scaffold`
- `flutter-clean-architecture-audit`
- `flutter-firestore-repository`

## References

- [`../../../../templates/state-management-template.md`](../../../../templates/state-management-template.md)
- [`../../../../examples/full-feature-implementation.md`](../../../../examples/full-feature-implementation.md)

## Real example

`ProfileController` exposes `AsyncValue<Profile>` and fetches data through `LoadProfileUseCase`, not through a widget callback.

## Real file output sample

```text
lib/features/profile/presentation/controllers/profile_controller.dart
lib/features/profile/presentation/providers/profile_providers.dart
test/features/profile/profile_controller_test.dart
```
