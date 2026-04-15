# Routing Example

Example feature: guarded profile route with deep-link support.

## Output tree

```text
lib/app/router/app_router.dart
lib/app/router/route_guards.dart
lib/features/profile/presentation/pages/profile_page.dart
lib/features/auth/presentation/pages/sign_in_page.dart
```

## Flutter-specific implementation

```dart
final appRouter = GoRouter(
  routes: [
    GoRoute(
      path: '/profile/:id',
      builder: (context, state) =>
          ProfilePage(userId: state.pathParameters['id']!),
    ),
  ],
  redirect: (context, state) {
    final signedIn = false;
    if (!signedIn && state.matchedLocation.startsWith('/profile')) {
      return '/sign-in';
    }
    return null;
  },
);
```

## Validation

- Deep links resolve to the correct route.
- Guards are deterministic.
- The router is declared once and injected from the app shell.
