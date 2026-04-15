# flutter-riverpod-state-skeleton

## Purpose

Create the Riverpod state skeleton for one Flutter feature.

## Use when

- The project standard is Riverpod
- The feature needs a provider or notifier scaffold
- Another skill will handle routing, repository, or UI wiring

## Do NOT use when

- The project standard is GetX
- You only need a one-line local widget state
- You need the repository implementation in the same pass

## Inputs required

- Feature name
- State model name
- Trigger methods or state events

## Constraints

- Create only the Riverpod state shell
- Keep data fetching delegated to injected contracts
- Do not add routing or platform code

## Step-by-step workflow

1. Define the state model.
2. Define the provider or notifier class.
3. Wire the dependency injection surface.
4. Add the minimal page-facing state entrypoint.
5. Return the file list and next-step note.

## Output contract

- Provider/notifier file
- State model file
- Optional provider export file

## Validation checklist

- Provider compiles on its own
- State is typed
- No repository implementation was created
- No widget logic leaked into the notifier

## Related skills

- `flutter-feature-contract-scaffold`
- `flutter-go-router-route-map`
- `flutter-firestore-repository`

## References

- [`../../../../templates/state-management-template.md`](../../../../templates/state-management-template.md)
- [`../../../../examples/full-feature-implementation.md`](../../../../examples/full-feature-implementation.md)

## Real example

`ProfileController` exposes `AsyncValue<Profile>` backed by a repository contract.

## Real file output sample

```text
lib/features/profile/presentation/controllers/profile_controller.dart
lib/features/profile/presentation/providers/profile_providers.dart
```
