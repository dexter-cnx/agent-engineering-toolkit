# Mobile Flutter Overlay

Use this overlay when the consuming repository is a Flutter application or a mobile-first application that also targets web.

## Purpose

This overlay extends the foundation toolkit with Flutter-specific operational guidance. It keeps the repository foundation domain-agnostic while making the Flutter overlay practical for day-to-day implementation, review, migration, and release work.

## Recommended structure

```text
repo/
├─ lib/
│  ├─ presentation/
│  ├─ domain/
│  ├─ data/
│  ├─ app/
│  └─ core/
├─ test/
└─ project_memory/
```

## Responsibilities

- top-level UI or transport layer owns entry concerns only
- business orchestration stays in a dedicated feature, service, or domain layer
- external integrations stay behind service or adapter boundaries
- project memory captures recurring stack-specific conventions
- overlay skills add focused capability guidance without redefining foundation identity

## Skill catalog

### Core
- `flutter-auth`
- `flutter-permissions`
- `flutter-geolocation`
- `flutter-maps`
- `flutter-storage`
- `flutter-networking`
- `flutter-deep-link`
- `flutter-push-notifications`
- `flutter-i18n-l10n`

### Product
- `flutter-analytics`
- `flutter-crash-reporting`
- `flutter-feature-flags`
- `flutter-offline-first`
- `flutter-remote-config`

### Release
- `flutter-web-deployment`
- `flutter-build-flavors`
- `flutter-app-signing-release`
- `flutter-ci-cd-mobile`

### Device
- `flutter-camera-media`
- `flutter-file-upload-download`
- `flutter-biometric-auth`
- `flutter-background-tasks`
- `flutter-contacts-sharing`

## Skill usage model

1. Start from the foundation rules in `AGENTS.md`.
2. Apply this overlay through `AGENTS.overlay.md`.
3. Pull one or more skills from `overlays/mobile-flutter/skills/`.
4. Use the skill `README.md` for human orientation.
5. Use the skill `skill.md` plus prompt files for AI-assisted execution.
6. Use skill checklists during code review and release preparation.

## Examples

- `examples/worked_example.md`
- `skills/index.md`

## Verification examples

```bash
flutter analyze
flutter test
```

## Review guidance

Reject changes when:
- presentation leaks domain rules
- the data layer bypasses domain contracts
- navigation or localization logic is scattered across unrelated modules
- external SDK calls bypass adapter or repository boundaries
- a skill README references files that do not exist in the same skill folder

## Overlay rule

This overlay extends the foundation. It must not redefine the repository identity.
