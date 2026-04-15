# flutter-go-router-route-map

## Purpose

Create the `go_router` route map for one Flutter app or feature slice.

## Use when

- Routes need to be declared
- A route hierarchy or shell route is missing
- Another skill will handle guards or deep-link wiring

## Do NOT use when

- You only need a redirect rule
- The task is purely about state or UI
- The app does not use `go_router`

## Inputs required

- Route list
- Shell route requirements
- Initial entrypoint

## Constraints

- Define route objects only
- Keep redirect rules out of this skill
- Do not add widget business logic

## Step-by-step workflow

1. List the route paths.
2. Create the `GoRoute` tree.
3. Add shell routes if needed.
4. Wire page builders to typed parameters.
5. Return the router file and the route list.

## Output contract

- Router file
- Route tree summary
- Page builder path list

## Validation checklist

- Route paths are typed
- The router tree is singular
- No guard logic was mixed in
- Deep links can target the declared routes

## Related skills

- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-firebase-auth-state`

## References

- [`../../../../examples/routing-example.md`](../../../../examples/routing-example.md)
- [`../../../../templates/feature-module-template.md`](../../../../templates/feature-module-template.md)

## Real example

Route `/profile/:id` maps to `ProfilePage(userId: ...)`.

## Real file output sample

```text
lib/app/router/app_router.dart
lib/features/profile/presentation/pages/profile_page.dart
```
