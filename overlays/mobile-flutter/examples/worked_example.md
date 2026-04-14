# Mobile Flutter Worked Example

## Scenario

A consuming Flutter application needs:

- email and password authentication
- current-location support
- map-based branch selection
- push notification tap-to-route behavior
- Flutter web deployment for internal QA

## Recommended skills

- `flutter-auth`
- `flutter-geolocation`
- `flutter-maps`
- `flutter-push-notifications`
- `flutter-deep-link`
- `guide-flutter-web-loading`
- `flutter-web-deployment`
- `guide-clean-architecture-feature`

## Reference files

- `overlays/mobile-flutter/skills/flutter-auth/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-geolocation/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-maps/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-push-notifications/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-deep-link/SKILL.md`
- `overlays/mobile-flutter/skills/guide-flutter-web-loading/SKILL.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`
- `overlays/mobile-flutter/prompts/add_maps_feature.md`
- `overlays/mobile-flutter/prompts/add_notifications_feature.md`
- `overlays/mobile-flutter/prompts/add_customer_visit_map.md`
- `overlays/mobile-flutter/prompts/prepare_flutter_web_release.md`
- `overlays/mobile-flutter/prompts/apply_flutter_web_loading.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-auth
- flutter-geolocation
- flutter-maps
- flutter-push-notifications
- flutter-deep-link
- guide-flutter-web-loading
- flutter-web-deployment

Reference files:
- overlays/mobile-flutter/skills/flutter-auth/SKILL.md
- overlays/mobile-flutter/prompts/add_auth_feature.md
- overlays/mobile-flutter/prompts/add_maps_feature.md
- overlays/mobile-flutter/prompts/add_notifications_feature.md

Task:
Implement a branch finder flow with guarded account access, notification tap
routing, and a QA web deployment plan.

Deliver:
1. file plan
2. route plan
3. capability boundaries
4. implementation notes
5. verification checklist
6. release risks
```

## Expected output

- auth state should not live only inside screens
- location permission handling should stay separate from map rendering
- notification payload parsing should not sit inside widgets
- web deployment rules should match router strategy

## Review notes

- keep platform boundaries explicit
- keep routing logic outside presentation widgets
- keep web loading and deployment decisions documented

## Verification notes

- confirm permission handling is isolated
- confirm notification intent parsing is isolated
- confirm release checklist covers web startup and deployment paths
