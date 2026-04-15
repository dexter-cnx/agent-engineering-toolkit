# flutter-feature-scaffold

## Purpose

Scaffold a production-ready Flutter feature module with clear layers, tests, and a stable folder shape.

## Use when

- A new feature needs to be created from scratch
- You want a repeatable folder layout before implementation starts
- The team needs a starter module for a clean architecture feature

## Do NOT use when

- You only need a small tweak inside an existing file
- The feature is intentionally a one-file prototype
- The request is purely about release or performance

## Inputs required

- Feature name
- State choice: Riverpod or GetX
- Data source type: API, Firestore, local storage, or mixed
- Route requirements

## Constraints

- Keep the feature module inside `lib/features/<feature_name>/`
- Create domain, data, and presentation folders
- Add at least one test target
- Keep UI text localizable when the feature contains user-facing strings

## Step-by-step workflow

1. Create the feature folder tree.
2. Add the domain entity and repository contract.
3. Add a repository implementation stub.
4. Add the selected state holder and page entry point.
5. Add tests for the first non-trivial behavior.
6. Add routing or localization hooks if needed.

## Output contract

- A feature tree ready for implementation
- Placeholder contracts and starter files
- A test file path
- A clear handoff checklist

## Validation checklist

- Folder names match the feature name
- Domain does not import data-layer SDKs
- Presentation owns widgets only
- The scaffold compiles once implementation lands

## Related skills

- `flutter-clean-architecture-audit`
- `flutter-riverpod-feature-state`
- `flutter-getx-mvc-feature`
- `flutter-go-router-deeplink`

## References

- [`../../../../templates/feature-module-template.md`](../../../../templates/feature-module-template.md)
- [`../../../../templates/repository-template.md`](../../../../templates/repository-template.md)
- [`../../../../examples/full-feature-implementation.md`](../../../../examples/full-feature-implementation.md)

## Real example

For a `profile` feature, create:

```text
lib/features/profile/domain/repositories/profile_repository.dart
lib/features/profile/presentation/pages/profile_page.dart
test/features/profile/profile_page_test.dart
```

## Real file output sample

```text
lib/features/profile/
  data/repositories/profile_repository_impl.dart
  domain/entities/profile.dart
  presentation/pages/profile_page.dart
```
