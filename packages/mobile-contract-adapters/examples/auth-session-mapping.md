# Auth and Session Mapping

```dart
class SessionDto {
  final String accessToken;
  final String refreshToken;
  final DateTime expiresAt;
  final String userId;
  final String email;

  SessionDto({
    required this.accessToken,
    required this.refreshToken,
    required this.expiresAt,
    required this.userId,
    required this.email,
  });
}
```

Store the session through secure storage, keep the adapter boundary explicit, and clear the
session on auth failure or sign-out.
