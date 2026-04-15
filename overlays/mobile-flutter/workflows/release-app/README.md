# Workflow: Release App

## Goal

Prepare a Flutter app for Android and iOS release with signing, readiness checks, and CI enforcement.

## Execution order

1. `flutter-android-release-signing`
2. `flutter-ios-release-readiness`
3. `flutter-performance-audit`
4. `flutter-clean-architecture-audit` if release blockers are architectural
5. `flutter-web-loading-shell` if the release includes web

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
