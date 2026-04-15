# Release Config Example

Example feature: Android and iOS release readiness setup.

## Output tree

```text
android/app/build.gradle
android/key.properties
ios/Runner.xcodeproj
ios/Runner/Info.plist
ci/github-actions/flutter-release.yml
```

## Flutter-specific implementation

```gradle
def keystoreProperties = new Properties()
def keystorePropertiesFile = rootProject.file('key.properties')
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}
```

## Validation

- Signing material is not committed.
- CI runs analysis, format, and tests before release artifacts.
- Platform documentation describes local setup and secret placement.
