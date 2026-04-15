# Workflow: Release App

## Goal

Prepare a Flutter app for Android and iOS release with signing, readiness checks, and CI enforcement.

## Execution order

1. `flutter-android-signing-config`
2. `flutter-android-release-validate`
3. `flutter-ios-release-readiness`
4. `flutter-performance-audit`
5. `flutter-clean-architecture-audit` if release blockers are architectural
6. `flutter-web-loading-shell` if the release includes web

## Expected outputs

- Release checklist
- Signing plan
- Platform setup notes
- CI job updates

## Example result

```text
android/key.properties
ios/Runner.xcodeproj/project.pbxproj
overlays/mobile-flutter/ci/github-actions/validate-skills.yml
```
