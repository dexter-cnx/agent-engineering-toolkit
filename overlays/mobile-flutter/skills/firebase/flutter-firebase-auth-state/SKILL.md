# flutter-firebase-auth-state

## Purpose

Create the auth session state layer that consumes a Firebase Auth adapter.

## Use when

- You need session state, not SDK wrapping
- Route guards depend on auth status
- A controller or provider must react to sign-in state

## Do NOT use when

- You need the Firebase SDK wrapper itself
- The feature does not affect auth state
- You need route declarations in the same pass

## Inputs required

- Auth state source
- Signed-in and signed-out states
- Consumer type: Riverpod, GetX, or router guard

## Constraints

- Keep session state typed
- Do not call Firebase SDKs directly
- Do not create routes here

## Step-by-step workflow

1. Define the session state model.
2. Consume the auth adapter stream or methods.
3. Expose sign-in, sign-out, and session data.
4. Document the consumer surface.
5. Return the state file list.

## Output contract

- Session state file
- Optional provider or controller file
- Auth state summary

## Validation checklist

- Session state is typed
- SDK access remains behind the adapter
- Route guard consumers are documented
- No router tree was created

## Related skills

- `flutter-firebase-auth-adapter`
- `flutter-go-router-redirect-guard`
- `flutter-riverpod-state-skeleton`

## References

- [`../../../examples/firebase-integration-example.md`](../../../examples/firebase-integration-example.md)

## Real example

`authStateProvider` exposes `AsyncValue<User?>` to the router guard.

## Real file output sample

```text
lib/features/auth/presentation/controllers/auth_controller.dart
lib/features/auth/presentation/providers/auth_providers.dart
```
