# Android Setup

## Firebase
1. Add `google-services.json` to `android/app/`
2. Add Google services Gradle plugin as required by the FlutterFire setup
3. Ensure minSdk / compileSdk values match selected dependencies

## Notifications
- Add notification permission for newer Android versions if required
- Configure launcher/background behavior carefully
- Verify default notification channel strategy

## Maps
- Add Google Maps API key in Android manifest or runtime config strategy
- Restrict the key in Google Cloud Console
