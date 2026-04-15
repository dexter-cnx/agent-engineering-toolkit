# Navigation and Guarded Routes Example

## Scenario

The app needs auth-aware navigation with guarded routes.

Example change:

- login gate
- protected dashboard
- deep-link-safe route flow
- redirect behavior after sign-in

## Recommended skills

- `flutter-clean-architecture-audit`
- `flutter-firebase-auth-adapter`
- `flutter-firebase-auth-state`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`

## Reference files

- `overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-redirect-guard/SKILL.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`
- `overlays/mobile-flutter/skills/firebase/flutter-firebase-auth-adapter/SKILL.md`
- `overlays/mobile-flutter/skills/firebase/flutter-firebase-auth-state/SKILL.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`
- `overlays/mobile-flutter/prompts/new_feature.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-clean-architecture-audit
- flutter-firebase-auth-adapter
- flutter-firebase-auth-state
- flutter-go-router-route-map
- flutter-go-router-redirect-guard

Task:
Add an auth-gated dashboard route with redirect handling and route registry
updates.

Deliver:
1. route plan
2. auth boundary plan
3. files to update
4. verification checklist
```

## Expected output

- route guards live outside widgets
- auth state is owned in a stable layer
- redirects are deterministic and testable
- navigation rules are easy to inspect

## Review notes

- do not parse auth state inside presentation widgets
- do not mix route registration with feature UI code
- keep redirect rules small and explicit

## Verification notes

- confirm route guards are outside widgets
- confirm auth state lives in a stable layer
- confirm redirects are deterministic and testable
