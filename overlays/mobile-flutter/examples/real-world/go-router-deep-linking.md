# go_router Deep Linking Example

## Purpose

Show a route-map plus redirect plus deep-link wiring flow for a Flutter app that opens the correct page from an external link.

## Reference files

- [`../../templates/feature-module-template.md`](../../templates/feature-module-template.md)
- [`../../skills/routing/flutter-go-router-route-map/SKILL.md`](../../skills/routing/flutter-go-router-route-map/SKILL.md)
- [`../../skills/routing/flutter-go-router-redirect-guard/SKILL.md`](../../skills/routing/flutter-go-router-redirect-guard/SKILL.md)
- [`../../skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`](../../skills/routing/flutter-go-router-deeplink-wireup/SKILL.md)

## Skills to use

- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-clean-architecture-audit`

## Exact repository paths

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/examples/routing-example.md`
- `lib/app/router/`
- `lib/main.dart`

## Step-by-step

1. Declare the route tree in one router file.
2. Add redirect or guard logic in a separate file.
3. Wire platform entry points for deep links.
4. Keep page builders typed and minimal.
5. Add tests or manual verification for direct links.

## Expected output

```text
lib/app/router/app_router.dart
lib/app/router/route_guards.dart
lib/app/router/deeplink_handler.dart
lib/main.dart
```

## Common mistakes

- Combining route tree, redirect rules, and deep-link parsing in one file
- Forgetting the root entry point
- Letting widget code own the navigation rules

## Copy-paste prompt

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-project/README.md or overlays/mobile-flutter/workflows/new-feature/README.md depending on scope.
Use overlays/mobile-flutter/examples/routing-example.md.

Task:
Implement go_router route map, redirect guard, and deep-link wiring.

Deliver:
1. route plan
2. redirect plan
3. deep-link entry plan
4. exact output paths
5. validation checklist
```

## Thai

ดู `go-router-deep-linking_TH.md`
