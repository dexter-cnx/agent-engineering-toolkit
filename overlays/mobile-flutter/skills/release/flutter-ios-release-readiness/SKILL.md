# flutter-ios-release-readiness

## Purpose

Prepare iOS release readiness, signing hygiene, and App Store-safe Flutter release configuration.

## Use when

- You need to ship an iOS build or TestFlight candidate
- The project needs signing or provisioning readiness
- You want a release checklist before handing the app to distribution

## Do NOT use when

- The task is only about Android
- You are not touching release or signing settings
- You plan to store signing secrets in git

## Inputs required

- Bundle identifier
- Signing state
- Distribution target
- Release timeline constraints

## Constraints

- Keep provisioning and signing material managed outside source control
- Verify release configuration, not only local debug runs
- Document the setup path for future maintainers
- Avoid platform-specific hacks in shared app code

## Step-by-step workflow

1. Confirm bundle identifier and signing ownership.
2. Review Xcode project readiness.
3. Document provisioning or automatic signing expectations.
4. Check release build and archive configuration.
5. Validate distribution steps such as TestFlight readiness.
6. Record unresolved signing risks.

## Output contract

- Readiness checklist
- Signing notes
- Xcode configuration reminders
- Release risk summary

## Validation checklist

- Bundle ID is correct
- Signing state is documented
- Archive path is understood
- No secret material is committed

## Related skills

- `flutter-android-signing-config`
- `flutter-performance-audit`

## References

- [`../../../examples/release-config-example.md`](../../../examples/release-config-example.md)
- [`../../../policies/secrets/README.md`](../../../policies/secrets/README.md)

## Real example

If a profile feature is ready for release, confirm the app archive succeeds in Xcode and that Flutter assets are included in the generated build.

## Real file output sample

```text
ios/Runner.xcodeproj/project.pbxproj
ios/Runner/Info.plist
ios/Runner.xcworkspace/contents.xcworkspacedata
```
