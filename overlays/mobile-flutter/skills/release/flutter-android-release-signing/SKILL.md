# flutter-android-release-signing

## Purpose

Prepare Android signing, release artifacts, and CI-safe release configuration for a Flutter app.

## Use when

- You need to ship an Android release build
- The app requires a keystore, signing config, or bundle release path
- CI must build or verify Android release output

## Do NOT use when

- The task is unrelated to Android release delivery
- You need only debug a local debug build
- You plan to commit secrets into the repository

## Inputs required

- Android application ID
- Keystore strategy
- CI target
- Release artifact type: APK or AAB

## Constraints

- Never commit keystore material
- Keep signing config documented but secret values external
- Validate release mode, not only debug mode
- Keep release setup consistent with CI

## Step-by-step workflow

1. Define release artifact target.
2. Add or update Gradle signing config.
3. Document keystore and secret handling.
4. Wire CI to build or at least validate release readiness.
5. Verify bundle or APK generation locally.
6. Record the final setup path.

## Output contract

- Signing plan
- Gradle or property file edits
- CI notes
- Release verification checklist

## Validation checklist

- Signing material stays outside git
- Release build succeeds
- Artifact target matches distribution channel
- CI can reproduce the release validation path

## Related skills

- `flutter-ios-release-readiness`
- `flutter-performance-audit`

## References

- [`../../../../examples/release-config-example.md`](../../../../examples/release-config-example.md)
- [`../../../../policies/secrets/README.md`](../../../../policies/secrets/README.md)

## Real example

Use `android/key.properties` locally, wire `signingConfig` in `android/app/build.gradle`, and keep the keystore password in CI secrets rather than source control.

## Real file output sample

```text
android/app/build.gradle
android/key.properties
ci/github-actions/flutter-release.yml
```
