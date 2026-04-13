# Mobile Flutter Worked Example

## Scenario

A consuming Flutter application needs:
- email and password authentication
- staged rollout of a new dashboard
- current-location support
- map-based branch selection
- push notification tap-to-route behavior
- Flutter web deployment for internal QA

## Recommended skill set

- `flutter-auth`
- `flutter-feature-flags`
- `flutter-geolocation`
- `flutter-maps`
- `flutter-push-notifications`
- `flutter-deep-link`
- `flutter-web-deployment`

## Example invocation

```text
Follow AGENTS.md strictly.
Apply overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-auth
- flutter-geolocation
- flutter-maps
- flutter-push-notifications
- flutter-deep-link
- flutter-web-deployment

Task:
Implement a branch finder flow with guarded account access, notification tap routing, and a QA web deployment plan.

Deliver:
1. file plan
2. route plan
3. capability boundaries
4. implementation notes
5. verification checklist
6. release risks
```

## Review notes

- authentication state must not live only inside screens
- location permission handling must stay separate from map rendering
- notification payload parsing must not sit inside widgets
- web deployment rules must match router strategy
