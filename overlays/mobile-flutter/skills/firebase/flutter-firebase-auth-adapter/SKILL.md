# flutter-firebase-auth-adapter

## Purpose

Create the Firebase Auth data adapter for one Flutter feature or app auth boundary.

## Use when

- Firebase Auth SDK calls need to be isolated
- A repository or state layer will consume auth methods
- You need sign-in or sign-out SDK wrappers

## Do NOT use when

- You only need route guards
- The project does not use Firebase Auth
- You need session state or UI wiring in the same pass

## Inputs required

- Auth methods to wrap
- Current Firebase setup
- Domain auth model shape

## Constraints

- Keep SDK calls in the adapter
- Return typed auth objects or primitives
- Do not wire router logic here

## Step-by-step workflow

1. Identify the Firebase Auth methods needed.
2. Wrap each method in a data adapter.
3. Map SDK user objects to typed outputs.
4. Keep the adapter free of UI and routing.
5. Return the adapter file list.

## Output contract

- Firebase Auth adapter file
- Mapping helper if needed
- Auth method summary

## Validation checklist

- SDK calls are isolated
- Adapter methods are typed
- No route or UI code was added
- Errors are surfaced clearly

## Related skills

- `flutter-firebase-auth-state`
- `flutter-go-router-redirect-guard`
- `flutter-firestore-repository`

## References

- [`../../../../examples/firebase-integration-example.md`](../../../../examples/firebase-integration-example.md)
- [`../../../../policies/secrets/README.md`](../../../../policies/secrets/README.md)

## Real example

`signInWithEmail` wraps `FirebaseAuth.signInWithEmailAndPassword`.

## Real file output sample

```text
lib/features/auth/data/datasources/firebase_auth_data_source.dart
```
