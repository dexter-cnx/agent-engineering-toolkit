# flutter-android-signing-config

## Purpose

Create the Android signing configuration only.

## Use when

- The app needs a keystore-based Android release setup
- Another skill will handle the release checklist or CI validation
- You need Gradle signing properties and file locations

## Do NOT use when

- The task is about iOS
- You only need release validation
- You plan to store secret values in git

## Inputs required

- Application ID
- Keystore path strategy
- Secret handling strategy

## Constraints

- Do not commit secret values
- Keep the output focused on Android signing files
- Do not add release notes or iOS config here

## Step-by-step workflow

1. Identify the signing file locations.
2. Add the Gradle signing property wiring.
3. Document local secret placement.
4. Return the signing file list.

## Output contract

- Android signing config file paths
- Secret placement note
- Minimal verification checklist

## Validation checklist

- Keystore values are not committed
- Gradle signing references resolve
- Output only touches Android signing

## Related skills

- `flutter-ios-release-readiness`
- `flutter-performance-audit`

## References

- [`../../../../examples/release-config-example.md`](../../../../examples/release-config-example.md)
- [`../../../../policies/secrets/README.md`](../../../../policies/secrets/README.md)

## Real example

`android/app/build.gradle` reads from `android/key.properties`.

## Real file output sample

```text
android/app/build.gradle
android/key.properties
```
