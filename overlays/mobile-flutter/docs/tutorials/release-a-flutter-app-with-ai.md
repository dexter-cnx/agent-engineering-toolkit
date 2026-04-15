# Release a Flutter App With AI

## Purpose

Prepare a Flutter app for Android and iOS release with signing, validation, and CI-aware checks.

## Prerequisites

- You know the target platforms
- You know the app identifiers and signing state
- The app already builds locally

## Exact repository paths

- `overlays/mobile-flutter/workflows/release-app/README.md`
- `overlays/mobile-flutter/ci/github-actions/validate-skills.yml`
- `overlays/mobile-flutter/ci/github-actions/flutter_overlay_ci.yml`
- `overlays/mobile-flutter/examples/release-config-example.md`
- `overlays/mobile-flutter/policies/secrets/README.md`
- `overlays/mobile-flutter/templates/pull_request_checklist.md`

## Step-by-step instructions

1. Read `workflows/release-app/README.md`.
2. Confirm Android signing paths and iOS readiness requirements.
3. Update `android/app/build.gradle` and `android/key.properties` only if signing config is missing.
4. Confirm iOS signing and bundle settings in `ios/Runner.xcodeproj` and `ios/Runner/Info.plist`.
5. Use the release validation skill to check the release path.
6. Keep secrets out of git and document secret placement only.
7. Run the overlay validation command before release handoff.

## What skills to use

- `flutter-android-signing-config`
- `flutter-android-release-validate`
- `flutter-ios-release-readiness`
- `flutter-performance-audit`
- `flutter-web-loading-shell` if the release also includes web

## Expected inputs

- Platform target
- Bundle ID or application ID
- Signing state
- Release timeline
- CI expectations

## Expected outputs

- Signing config plan
- Release validation checklist
- iOS readiness notes
- CI updates if needed
- Risk list before shipping

## Common mistakes

- Mixing signing setup and release validation in one step
- Committing secret values
- Forgetting iOS readiness when Android is already configured
- Skipping performance checks before release

## Troubleshooting

- If signing is unclear, fix Android signing before validation.
- If CI fails, check path references and secret handling first.
- If the app ships web, include web loading verification in the release pass.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/release-app/README.md and overlays/mobile-flutter/examples/release-config-example.md.

Task:
Prepare the Flutter app for release on <platforms>.

Deliver:
1. signing plan
2. release validation plan
3. exact files to review
4. CI updates needed
5. release risks
```

## Thai

ดู `release-a-flutter-app-with-ai_TH.md` สำหรับเวอร์ชันภาษาไทย
