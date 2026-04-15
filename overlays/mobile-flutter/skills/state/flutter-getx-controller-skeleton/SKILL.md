# flutter-getx-controller-skeleton

## Purpose

Create the GetX controller skeleton for one Flutter feature.

## Use when

- The project standard is GetX
- The feature needs a controller and binding scaffold
- Another skill will handle data access and routing

## Do NOT use when

- The project standard is Riverpod
- You only need a UI tweak
- You need repository or platform setup in the same pass

## Inputs required

- Feature name
- Controller name
- Observable fields or actions

## Constraints

- Create only controller-facing GetX scaffolding
- Keep bindings explicit
- Do not add data-source implementation here

## Step-by-step workflow

1. Define the controller class.
2. Define observable state fields.
3. Add a binding file if needed.
4. Add the minimal page-facing action surface.
5. Return the file list and next-step note.

## Output contract

- Controller file
- Binding file if needed
- Optional view-facing export file

## Validation checklist

- Controller compiles independently
- Observable fields are typed
- No repository implementation was created
- View logic remains outside the controller

## Related skills

- `flutter-feature-contract-scaffold`
- `flutter-go-router-route-map`
- `flutter-firestore-repository`

## References

- [`../../../../templates/state-management-template.md`](../../../../templates/state-management-template.md)
- [`../../../../examples/full-feature-implementation.md`](../../../../examples/full-feature-implementation.md)

## Real example

`ProfileController` exposes `isLoading` and `profile` observables.

## Real file output sample

```text
lib/features/profile/presentation/controllers/profile_controller.dart
lib/features/profile/presentation/bindings/profile_binding.dart
```
