# flutter-go-router-deeplink

## Purpose

Add `go_router` navigation, guarded routes, and deep-link handling for Flutter apps.

## Use when

- A feature needs route paths or nested navigation
- The app needs auth guards or redirect logic
- The app must support deep links or web URLs

## Do NOT use when

- The app is a static single-screen demo
- The request is only about widget styling
- Navigation is already fully handled by another agreed routing stack

## Inputs required

- Route map
- Auth or onboarding guard rules
- Initial entrypoint
- Any shell or nested route requirements

## Constraints

- Prefer one router definition owned by the app shell
- Keep redirect logic deterministic
- Do not put routing logic inside pages unless unavoidable
- Preserve browser URL behavior on web

## Step-by-step workflow

1. Define the route hierarchy.
2. Add path parameters and shell routes if needed.
3. Add redirect or guard logic.
4. Wire the router into the app bootstrap.
5. Add route tests or smoke checks.
6. Validate web and mobile entry paths.

## Output contract

- Router file
- Guard or redirect helper if needed
- Page route wiring
- Test notes for navigation behavior

## Validation checklist

- Deep link reaches the intended page
- Auth guard redirects correctly
- Browser URL updates as expected
- Router is not recreated in multiple places

## Related skills

- `flutter-firebase-auth-flow`
- `flutter-web-loading-shell`
- `flutter-clean-architecture-audit`

## References

- [`../../../../examples/routing-example.md`](../../../../examples/routing-example.md)
- [`../../../../docs/tutorials/how-skills-work.md`](../../../../docs/tutorials/how-skills-work.md)

## Real example

Route `/profile/:id` should open `ProfilePage(userId: ...)` and redirect to `/sign-in` when the auth state is missing.

## Real file output sample

```text
lib/app/router/app_router.dart
lib/app/router/route_guards.dart
lib/features/profile/presentation/pages/profile_page.dart
```
