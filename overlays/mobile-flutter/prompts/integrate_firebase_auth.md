# Prompt: Integrate Firebase Auth

## Intent

Add Firebase Auth to a Flutter app with clean architecture, auth state, and guarded routing.

## When to use

- The app needs sign-in, sign-out, or session bootstrap
- Firebase Auth SDK must be isolated behind an adapter
- Route access depends on auth state

## Required inputs

- App auth flow
- Firebase project state
- Domain user model shape
- Route protection rules

## Optional inputs

- Email/password, SSO, or anonymous auth scope
- Sign-up flow requirements
- Password reset requirements
- Local session persistence rules

## Expected outputs

- Firebase Auth adapter
- Auth state layer
- Repository or use-case wiring
- Route guard plan
- Tests for mapping and redirect behavior

## Repo paths to inspect

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/examples/firebase-integration-example.md`
- `overlays/mobile-flutter/examples/real-world/firebase-auth-flow.md`
- `overlays/mobile-flutter/skills/firebase/flutter-firebase-auth-adapter/SKILL.md`
- `overlays/mobile-flutter/skills/firebase/flutter-firebase-auth-state/SKILL.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-redirect-guard/SKILL.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md`

## Related skills and workflows

- `flutter-firebase-auth-adapter`
- `flutter-firebase-auth-state`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-clean-architecture-audit`
- `workflows/new-feature/README.md`

## Guardrails

- Do not call Firebase SDKs from widgets
- Keep auth state separate from routing logic
- Keep redirect logic out of the view layer
- Keep the adapter boundary explicit

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/examples/firebase-integration-example.md.

Task:
Integrate Firebase Auth with adapter, auth state, and guarded routes.

Deliver:
1. auth boundary plan
2. exact files to update
3. route guard plan
4. validation checklist
```
