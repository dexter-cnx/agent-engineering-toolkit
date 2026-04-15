# flutter-go-router-redirect-guard

## Purpose

Create the redirect or guard logic for a `go_router` app.

## Use when

- Routes need auth or onboarding redirects
- A router map already exists
- Another skill will handle page and route declaration

## Do NOT use when

- You need the route tree itself
- The app does not require redirects
- The feature does not have navigation guards

## Inputs required

- Guard condition
- Redirect targets
- State source for the condition

## Constraints

- Keep the redirect deterministic
- Do not declare route paths here
- Avoid hidden side effects in the guard

## Step-by-step workflow

1. Identify the guard condition.
2. Define the allowed and blocked paths.
3. Implement the redirect function or guard helper.
4. Document the dependency on state.
5. Return the guard file and behavior summary.

## Output contract

- Redirect helper or router redirect block
- Path behavior summary
- Test note for the redirect rule

## Validation checklist

- Blocked paths redirect correctly
- Allowed paths remain accessible
- Guard does not create loops
- The condition source is documented

## Related skills

- `flutter-go-router-route-map`
- `flutter-firebase-auth-state`
- `flutter-go-router-deeplink-wireup`

## References

- [`../../../examples/routing-example.md`](../../../examples/routing-example.md)
- [`../../../examples/firebase-integration-example.md`](../../../examples/firebase-integration-example.md)

## Real example

When auth is missing, `/profile/123` redirects to `/sign-in`.

## Real file output sample

```text
lib/app/router/route_guards.dart
lib/app/router/app_router.dart
```
