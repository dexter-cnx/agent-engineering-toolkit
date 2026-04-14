# Maps and Notifications Example

## Scenario

A customer-facing mobile app needs location-aware maps and notification routing.

Example change:

- current-location support
- map-based branch selection
- push notification tap-to-route behavior
- deep-link handoff into the right page

## Recommended skills

- `flutter-geolocation`
- `flutter-maps`
- `flutter-push-notifications`
- `flutter-deep-link`
- `flutter-dev`
- `policy-no-business-logic-in-widget`

## Reference files

- `overlays/mobile-flutter/skills/flutter-geolocation/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-maps/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-push-notifications/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-deep-link/SKILL.md`
- `overlays/mobile-flutter/prompts/add_maps_feature.md`
- `overlays/mobile-flutter/prompts/add_notifications_feature.md`
- `overlays/mobile-flutter/prompts/add_customer_visit_map.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-geolocation
- flutter-maps
- flutter-push-notifications
- flutter-deep-link
- flutter-dev

Task:
Implement a branch finder flow with location permission handling, map selection,
and notification tap routing.

Deliver:
1. capability boundaries
2. route plan
3. permission plan
4. verification checklist
```

## Expected output

- permission handling stays separate from map rendering
- notification payload parsing stays outside widgets
- route decisions are deterministic and testable
- location and deep-link boundaries are explicit

## Review notes

- keep navigation intent parsing out of UI widgets
- keep platform permission code isolated
- do not let the map widget own business rules

## Verification notes

- confirm permission handling is not in the map widget
- confirm notification payload parsing is outside presentation code
- confirm route decisions are testable and deterministic
