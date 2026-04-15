# flutter-android-release-validate

## Purpose

Validate the Android release path without changing the signing configuration.

## Use when

- The Android signing config already exists
- You need a release build readiness check
- CI should confirm the release path

## Do NOT use when

- You need to create the signing config itself
- The task is about iOS
- The request is not release-related

## Inputs required

- Android release target
- CI expectations
- Build artifact type

## Constraints

- Do not modify secret material
- Do not add iOS config
- Focus on validation and verification only

## Step-by-step workflow

1. Check the release build command.
2. Confirm artifact type and environment.
3. Validate CI steps for Android release.
4. Return the validation checklist and file references.

## Output contract

- Android release validation checklist
- CI verification notes
- Artifact target summary

## Validation checklist

- Release build path is clear
- CI confirms the build path
- Signing config is not rewritten here

## Related skills

- `flutter-android-signing-config`
- `flutter-ios-release-readiness`

## References

- [`../../../../examples/release-config-example.md`](../../../../examples/release-config-example.md)

## Real example

`flutter build appbundle --release` is the validation target for Play Store delivery.

## Real file output sample

```text
ci/github-actions/flutter-release.yml
```
