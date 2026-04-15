# flutter-feature-contract-scaffold

## Purpose

Create the minimal domain contract files for a Flutter feature, such as entities and repository interfaces.

## Use when

- The feature folder exists and the next step is domain contracts
- You need repository and entity definitions before implementation
- Another skill will handle the data or presentation layers

## Do NOT use when

- The task is only to create folders
- You need state, routing, or platform configuration in the same pass
- The domain model already exists unchanged

## Inputs required

- Feature name
- Entity names
- Repository interface names

## Constraints

- Create domain-only files
- Keep contracts independent of SDKs and UI
- Do not add data-layer implementation here

## Step-by-step workflow

1. Define the core entity type.
2. Define repository interfaces.
3. Define any domain use case names required by the feature.
4. Write minimal signatures only.
5. Return the created file list.

## Output contract

- Entity file path
- Repository interface path
- Optional use case file paths

## Validation checklist

- Domain files import no Flutter SDKs
- Interfaces are minimal and typed
- No data-source implementation is included
- File names match the feature vocabulary

## Related skills

- `flutter-feature-folder-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-firestore-repository`

## References

- [`../../../templates/repository-template.md`](../../../templates/repository-template.md)
- [`../../../templates/feature-module-template.md`](../../../templates/feature-module-template.md)

## Real example

For a `profile` feature:

```text
lib/features/profile/domain/entities/profile.dart
lib/features/profile/domain/repositories/profile_repository.dart
```

## Real file output sample

```text
lib/features/profile/domain/entities/profile.dart
lib/features/profile/domain/repositories/profile_repository.dart
```
