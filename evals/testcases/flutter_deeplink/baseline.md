# flutter-go-router-deeplink-wireup

## Purpose
Wire up a deep link entry point in a Flutter app that uses go_router, so that an incoming URI is routed to the correct feature screen.

## Use when
- A feature screen must be reachable via an external URI (e.g., a push notification tap or a web link)
- The app already uses go_router and you need to add a new deep link without disrupting existing routes
- You need to handle both cold-start and warm-start deep link scenarios in a single configuration
- Platform-specific intent filters (Android) or URL schemes (iOS) must be registered alongside the in-app route

## Do NOT use when
- The app does not use go_router — use the appropriate routing adapter skill for the active router
- You only need to add a regular navigation route without any external URI entry — use flutter-go-router-route-map instead
- The deep link requires custom authentication before showing the destination screen — add the guard separately after wireup
- You are migrating from a non-go_router router to go_router

## Inputs required
- The URI pattern for the deep link (e.g., `/orders/:id`)
- The target feature screen widget class name
- The current `AppRouter` or `GoRouter` configuration file path
- The platform target (Android, iOS, or both)

## Constraints
- Do not add deep link handling logic inside presentation widgets — keep it in the router configuration
- Do not hardcode URI schemes in Dart — read them from the platform configuration files
- Do not add a new GoRoute without checking for path conflicts in the existing route tree
- Keep the Android intent filter and iOS URL scheme registrations in sync with the Dart route pattern

## Step-by-step workflow
1. Identify the target feature screen and its widget path in `lib/features/<feature>/presentation/pages/`.
2. Open `lib/app/router/app_router.dart` and locate the GoRouter routes list.
3. Add a new GoRoute with the correct path and builder pointing to the feature screen and register it with the route registry.
4. Update `android/app/src/main/AndroidManifest.xml` with an intent filter for the URI scheme and host.
5. Update `ios/Runner/Info.plist` with the URL scheme under `CFBundleURLSchemes`.
6. Run the app on both platforms and trigger the deep link to confirm routing.
7. Write or update a widget test in `test/routing/` that navigates via the URI and asserts the correct page is displayed.

## Output contract
- A new GoRoute entry in `lib/app/router/app_router.dart`
- An updated `android/app/src/main/AndroidManifest.xml` with the correct intent filter
- An updated `ios/Runner/Info.plist` with the URL scheme entry
- A widget test file at `test/routing/deep_link_<feature>_test.dart`

## Validation checklist
- Run `flutter test test/routing/` and confirm exit code 0
- Open the Android emulator and run `adb shell am start -W -a android.intent.action.VIEW -d "<uri>"` — confirm correct screen opens
- Confirm no path conflicts by running `flutter analyze` and checking for router errors in the output
- Review `app_router.dart` and ensure the new route does not import any Firebase SDK directly

## Related skills
- `flutter-go-router-route-map` — for adding a standard navigation route
- `flutter-go-router-redirect-guard` — for adding auth or permission guards to the new route
- `flutter-clean-architecture-audit` — to verify the deep link handling does not violate layer boundaries

## References
- [`../../examples/flutter_deeplink_full_cycle.md`](../../examples/flutter_deeplink_full_cycle.md)
- [`../../../overlays/mobile-flutter/skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`](../../../overlays/mobile-flutter/skills/routing/flutter-go-router-deeplink-wireup/SKILL.md)

## Real example
Adding a deep link `/orders/:id` that opens `OrderDetailPage`. The GoRoute is added to `app_router.dart` with `path: '/orders/:id'` and `builder: (context, state) => OrderDetailPage(id: state.pathParameters['id']!)`. The intent filter in `AndroidManifest.xml` uses `scheme="https"`, `host="app.example.com"`, `pathPrefix="/orders"`.

## Real file output sample
```text
lib/app/router/app_router.dart
android/app/src/main/AndroidManifest.xml
ios/Runner/Info.plist
test/routing/deep_link_orders_test.dart
```
