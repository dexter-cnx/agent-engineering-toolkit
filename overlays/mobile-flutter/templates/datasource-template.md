# Datasource Template

```text
lib/features/<feature_name>/data/datasources/<feature_name>_remote_data_source.dart
lib/features/<feature_name>/data/datasources/<feature_name>_local_data_source.dart
```

## Example

```dart
class ProfileRemoteDataSource {
  Future<Map<String, dynamic>> fetchRawProfile(String userId) async {
    // Adapter boundary only
    return <String, dynamic>{'id': userId};
  }
}
```

## Output sample

- `lib/features/profile/data/datasources/profile_remote_data_source.dart`
- `lib/features/profile/data/datasources/profile_local_data_source.dart`
