# Flutter Web Deployment Checklist

## Build
- `flutter build web --release` succeeds
- no missing assets in output
- base href is correct for hosting target

## Runtime
- loader appears before first frame
- initial route loads
- deep links / refresh behavior work
- fonts/assets do not visibly break startup

## Hosting
- correct cache policy chosen
- SPA fallback or routing strategy confirmed
- CDN/static host paths verified

## Verification
- test in Chrome
- test in Safari if relevant
- test mobile browser startup
- test with slow network throttling
