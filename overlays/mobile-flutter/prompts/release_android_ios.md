# Prompt: Release Android + iOS

## Intent

Prepare a Flutter app for Android and iOS release with signing, validation, and CI-safe checks.

## When to use

- The app is ready for a production release
- Signing and readiness must be verified
- Release steps need to be separated from app implementation

## Required inputs

- Platform targets
- Application ID or bundle ID
- Signing state
- Release timeline

## Optional inputs

- Web release scope
- Flavor or environment setup
- Store submission requirements
- CI provider details

## Expected outputs

- Signing plan
- Validation plan
- iOS readiness notes
- Release risk list
- CI update notes if needed

## Repo paths to inspect

- `overlays/mobile-flutter/workflows/release-app/README.md`
- `overlays/mobile-flutter/examples/release-config-example.md`
- `overlays/mobile-flutter/skills/release/flutter-android-signing-config/SKILL.md`
- `overlays/mobile-flutter/skills/release/flutter-android-release-validate/SKILL.md`
- `overlays/mobile-flutter/skills/release/flutter-ios-release-readiness/SKILL.md`
- `overlays/mobile-flutter/policies/secrets/README.md`
- `overlays/mobile-flutter/ci/github-actions/flutter_overlay_ci.yml`

## Related skills and workflows

- `flutter-android-signing-config`
- `flutter-android-release-validate`
- `flutter-ios-release-readiness`
- `flutter-performance-audit`
- `flutter-web-loading-shell`
- `workflows/release-app/README.md`

## Guardrails

- Do not commit secret values
- Keep signing setup separate from release validation
- Do not skip iOS readiness when Android is already configured
- Confirm performance and test checks before release handoff

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/release-app/README.md and overlays/mobile-flutter/examples/release-config-example.md.

Task:
Prepare the app for Android and iOS release.

Deliver:
1. signing plan
2. release validation plan
3. exact files to review
4. release risks
```
