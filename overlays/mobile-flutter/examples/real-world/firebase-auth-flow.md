# Firebase Auth Flow Example

## Purpose

Show a safe sign-in flow where Firebase SDK calls stay in the data layer and auth state stays separate from routing.

## Reference files

- [`../../templates/repository-template.md`](../../templates/repository-template.md)
- [`../../templates/state-management-template.md`](../../templates/state-management-template.md)
- [`../../skills/firebase/flutter-firebase-auth-adapter/SKILL.md`](../../skills/firebase/flutter-firebase-auth-adapter/SKILL.md)
- [`../../skills/firebase/flutter-firebase-auth-state/SKILL.md`](../../skills/firebase/flutter-firebase-auth-state/SKILL.md)

## Skills to use

- `flutter-firebase-auth-adapter`
- `flutter-firebase-auth-state`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-route-map`

## Exact repository paths

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/examples/firebase-integration-example.md`
- `lib/features/auth/`
- `lib/app/router/`
- `test/features/auth/`

## Step-by-step

1. Wrap Firebase Auth calls in a data adapter.
2. Add auth session state that consumes the adapter.
3. Keep redirect logic in routing, not in the page.
4. Add sign-in and sign-out pages.
5. Add tests for adapter mapping and route behavior.

## Expected output

```text
lib/features/auth/data/datasources/firebase_auth_data_source.dart
lib/features/auth/data/repositories/auth_repository_impl.dart
lib/features/auth/presentation/controllers/auth_controller.dart
lib/app/router/route_guards.dart
test/features/auth/auth_controller_test.dart
```

## Common mistakes

- Calling Firebase SDK directly from widgets
- Mixing auth state with UI state
- Putting redirect logic inside the screen

## Copy-paste prompt

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md and overlays/mobile-flutter/examples/firebase-integration-example.md.

Task:
Implement a Firebase Auth flow with adapter, auth state, and guarded routing.

Deliver:
1. auth boundary plan
2. exact files to create or update
3. route guard plan
4. validation checklist
```

## Thai

ดู `firebase-auth-flow_TH.md`
