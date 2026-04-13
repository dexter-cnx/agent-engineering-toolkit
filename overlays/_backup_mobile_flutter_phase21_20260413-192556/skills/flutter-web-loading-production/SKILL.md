# SKILL: flutter-web-loading-production

## Purpose
Apply a production-friendly loading experience to Flutter Web so users do not see a blank screen during startup.

## Requirements
- show visible progress or loading state before Flutter paints first frame
- keep HTML/CSS loader lightweight
- do not hardcode app-specific branding unless repo policy requires it
- preserve compatibility with the selected Flutter web bootstrap path
- test with release builds, not just debug

## Deliverables
- `web/index.html` starter markup
- `web/style.css`
- `web/flutter_bootstrap.js` or equivalent loader-aware bootstrap
- integration guide
- review checklist

## Review points
- first paint is visible immediately
- loader disappears cleanly when Flutter takes over
- no obvious layout shift
- works in slow network simulations
