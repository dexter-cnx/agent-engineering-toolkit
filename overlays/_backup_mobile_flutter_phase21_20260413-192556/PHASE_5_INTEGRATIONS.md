# Phase 5: Integrations + Generator Layer

This phase adds repo-ready integration scaffolding for the starter app without forcing a single backend vendor at compile time.

## Added in this phase

- Firebase auth adapter template
- Maps feature template for field CRM / customer visit routing
- Push notification service abstractions and Firebase Messaging template
- Environment configuration template
- Feature generator script for repeatable module scaffolding
- Overlay audit script for local repo validation

## Why templates instead of hardwired packages?

The overlay should remain safe to copy into multiple repositories. Some teams use Firebase, some Supabase, some custom APIs. For that reason, the concrete vendor integrations are delivered as `.template.dart` files and onboarding docs instead of being wired into the starter app by default.

## Recommended next step after copying into a real repo

1. Pick your auth backend
2. Pick your maps provider
3. Pick your notifications provider
4. Rename the selected `*.template.dart` files to `.dart`
5. Add required packages to `pubspec.yaml`
6. Wire the repository implementations into `lib/core/di/app_providers.dart`
7. Enable CI checks for generated localization and feature policy
