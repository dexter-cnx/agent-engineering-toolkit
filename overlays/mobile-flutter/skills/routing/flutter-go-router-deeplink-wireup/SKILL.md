# flutter-go-router-deeplink-wireup

## Purpose

Wire deep-link entry handling to an existing `go_router` route map.

## Use when

- The app should open a feature from a browser or platform link
- The route map already exists
- Another skill will handle route declarations or guards

## Do NOT use when

- The route map has not been created yet
- The task is only about UI or state
- You are not using deep links

## Inputs required

- Deep-link patterns
- Target route paths
- Platform entrypoints

## Constraints

- Use the existing router map
- Keep link parsing isolated
- Do not mix redirect policy here

## Step-by-step workflow

1. Map each deep-link pattern to a route path.
2. Add the parsing or normalization helper.
3. Wire the incoming link to the router.
4. Add notes for mobile and web entrypoints.
5. Return the entry handling file list.

## Output contract

- Deep-link parsing helper
- App entry wiring note
- Route mapping summary

## Validation checklist

- Link resolves to the intended route
- Parsing is isolated
- Router map remains the source of truth
- Web and mobile entry behavior is documented

## Related skills

- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-web-loading-shell`

## References

- [`../../../examples/routing-example.md`](../../../examples/routing-example.md)

## Real example

`myapp://profile/123` resolves to `/profile/123`.

## Real file output sample

```text
lib/app/router/deeplink_router.dart
lib/app/router/app_router.dart
```
