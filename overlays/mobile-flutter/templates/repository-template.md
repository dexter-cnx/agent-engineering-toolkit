# Repository Template

```text
lib/features/<feature_name>/data/repositories/<feature_name>_repository_impl.dart
lib/features/<feature_name>/domain/repositories/<feature_name>_repository.dart
```

## Contract shape

```dart
abstract class ProfileRepository {
  Future<Profile> loadProfile(String userId);
}
```

## Implementation shape

```dart
class ProfileRepositoryImpl implements ProfileRepository {
  ProfileRepositoryImpl(this._remoteDataSource);

  final ProfileRemoteDataSource _remoteDataSource;

  @override
  Future<Profile> loadProfile(String userId) {
    return _remoteDataSource.fetchProfile(userId);
  }
}
```

## Output sample

- `lib/features/profile/data/repositories/profile_repository_impl.dart`
- `lib/features/profile/domain/repositories/profile_repository.dart`
