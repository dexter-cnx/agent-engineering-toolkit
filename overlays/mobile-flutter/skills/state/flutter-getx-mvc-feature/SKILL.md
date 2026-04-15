# flutter-getx-mvc-feature

## Purpose

Implement a feature with GetX MVC-style controllers, bindings, and observable state.

## Use when

- The project already uses GetX
- The team selected GetX for this feature
- The app needs lightweight controller-driven state with simple bindings

## Do NOT use when

- The app standard is Riverpod and the team wants consistency
- You are trying to hide architecture issues in a controller
- The feature has complex domain workflows that need richer state modeling

## Inputs required

- Feature name
- Controller responsibilities
- Binding scope
- Navigation entry point

## Constraints

- Keep repository access out of the view
- Keep bindings explicit and local to the feature
- Use observables for UI state only
- Add tests for controller behavior when non-trivial

## Step-by-step workflow

1. Define the controller responsibility.
2. Add the binding or dependency registration.
3. Create the view and connect observables.
4. Add repository or service adapters behind the controller.
5. Add tests for state mutations and side effects.

## Output contract

- Controller file
- Binding file
- View file
- Controller test file

## Validation checklist

- The controller owns the feature flow
- The view only renders and forwards events
- Dependencies are injected through bindings
- External SDK usage stays behind adapters

## Related skills

- `flutter-feature-scaffold`
- `flutter-clean-architecture-audit`
- `flutter-firestore-repository`

## References

- [`../../../../templates/state-management-template.md`](../../../../templates/state-management-template.md)
- [`../../../../examples/full-feature-implementation.md`](../../../../examples/full-feature-implementation.md)

## Real example

`ProfileController` exposes `RxBool isLoading` and `Rxn<Profile> profile`; the page binds a button to `controller.loadProfile()`.

## Real file output sample

```text
lib/features/profile/presentation/controllers/profile_controller.dart
lib/features/profile/presentation/bindings/profile_binding.dart
lib/features/profile/presentation/pages/profile_page.dart
```
