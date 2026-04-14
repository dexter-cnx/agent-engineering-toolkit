# Navigation and Guarded Routes Example

## Scenario

The app needs auth-aware navigation with guarded routes.

Example change:

- login gate
- protected dashboard
- deep-link-safe route flow
- redirect behavior after sign-in

## Recommended skills

- `flutter-auth`
- `flutter-navigation-go-router`
- `flutter-dev`
- `guide-clean-architecture-feature`
- `policy-no-business-logic-in-widget`

## Reference files

- `overlays/mobile-flutter/skills/flutter-navigation-go-router/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-auth/SKILL.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/policy-no-business-logic-in-widget/SKILL.md`
- `overlays/mobile-flutter/skills/policy-folder-structure/SKILL.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-auth
- flutter-navigation-go-router
- flutter-dev

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
