# Feature Module Template

Use this as the default shape for a new Flutter feature.

```text
lib/features/<feature_name>/
  data/
    datasources/
    dtos/
    mappers/
    repositories/
  domain/
    entities/
    repositories/
    usecases/
  presentation/
    controllers/
    pages/
    widgets/
```

## Minimum files

- one page
- one state holder
- one repository contract
- one repository implementation
- one use case or controller entry point
- one mapper when data and domain models differ
- one widget test
- one unit test

## Example

- `lib/features/profile/presentation/pages/profile_page.dart`
- `lib/features/profile/presentation/controllers/profile_controller.dart`
- `lib/features/profile/domain/usecases/load_profile_usecase.dart`

## Output sample

```text
lib/features/profile/
  data/repositories/profile_repository_impl.dart
  domain/entities/profile.dart
  domain/usecases/load_profile_usecase.dart
  presentation/controllers/profile_controller.dart
  presentation/pages/profile_page.dart
```
