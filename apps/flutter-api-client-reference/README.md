# Flutter API Client Reference

This is a minimal but production-shaped Flutter reference for consuming the shared backend
contracts from the toolkit.

## What it demonstrates

- API client layer with envelope parsing
- DTO mapping layer for posts and sessions
- auth token handling through secure storage
- pagination handling for list endpoints
- CRUD flow for posts
- protected screen pattern
- build-time environment configuration with `--dart-define`

## Recommended environment pattern

```bash
flutter pub get
flutter run --dart-define=API_BASE_URL=http://localhost:8080
```

## File map

- `lib/config/app_config.dart` - environment-driven API configuration
- `lib/core/api/api_client.dart` - request, response, and envelope handling
- `lib/core/api/api_models.dart` - session, post, pagination, and error DTOs
- `lib/core/auth/token_store.dart` - secure storage session handling
- `lib/features/auth/login_screen.dart` - sign-in flow example
- `lib/features/auth/protected_shell.dart` - protected screen example
- `lib/features/posts/posts_repository.dart` - CRUD and pagination repository
- `lib/features/posts/posts_screen.dart` - posts list and create/delete example

## Verification

```bash
node scripts/check-structure.mjs
```
