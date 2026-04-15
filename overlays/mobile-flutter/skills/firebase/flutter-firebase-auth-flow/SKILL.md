# flutter-firebase-auth-flow

## Purpose

Wire a Firebase Auth flow through repository boundaries, state management, and route guards.

## Use when

- The app needs sign in, sign up, sign out, or session restoration
- Auth state must control access to routes
- You need a production-safe Firebase Auth integration

## Do NOT use when

- The feature does not touch authentication
- You are only mocking login UI for a prototype
- Firebase is not part of the project standard

## Inputs required

- Auth provider choice and sign-in methods
- Route guard rules
- Session persistence requirements
- Firebase project configuration status

## Constraints

- Keep Firebase SDK calls in the data layer
- Expose auth state through a repository or stream abstraction
- Avoid reading auth state directly from widgets
- Keep secrets and config files out of source control

## Step-by-step workflow

1. Define the auth repository contract.
2. Implement Firebase Auth data-source methods.
3. Map Firebase user objects into domain models.
4. Expose a session state stream to the controller or provider.
5. Connect route guards to auth state.
6. Add tests for sign-in success, sign-out, and redirect behavior.

## Output contract

- Auth repository contract
- Firebase data source
- Session state provider or controller
- Guard-aware router wiring

## Validation checklist

- Firebase SDK code stays in the data layer
- Signed-out users are redirected deterministically
- Session restore does not duplicate logic in widgets
- Auth errors are surfaced clearly

## Related skills

- `flutter-go-router-deeplink`
- `flutter-firestore-repository`
- `flutter-clean-architecture-audit`

## References

- [`../../../../examples/firebase-integration-example.md`](../../../../examples/firebase-integration-example.md)
- [`../../../../policies/secrets/README.md`](../../../../policies/secrets/README.md)

## Real example

When the user signs out, the controller emits an unauthenticated state and the router redirects `/profile/123` to `/sign-in`.

## Real file output sample

```text
lib/features/auth/data/datasources/firebase_auth_data_source.dart
lib/features/auth/data/repositories/auth_repository_impl.dart
lib/features/auth/presentation/controllers/auth_controller.dart
```
