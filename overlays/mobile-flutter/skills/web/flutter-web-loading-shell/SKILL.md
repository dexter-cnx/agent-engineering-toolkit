# flutter-web-loading-shell

## Purpose

Add a visible, production-friendly loading shell for Flutter Web startup.

## Use when

- The web app shows a blank screen before Flutter renders
- You need a branded or neutral loading experience before first frame
- You are patching `web/index.html` or bootstrap scripts

## Do NOT use when

- The app is mobile-only
- The project already has a solved loading shell and no web changes are needed
- You only need an in-app progress bar after startup

## Inputs required

- Current web entry files
- Branding or neutral-loader rules
- Bootstrap path used by the project
- Any release-browser expectations

## Constraints

- Keep the loader lightweight
- Preserve compatibility with the Flutter bootstrap path
- Show visible loading before the first Flutter frame
- Avoid app-specific hard-coded branding unless required

## Step-by-step workflow

1. Inspect `web/index.html`, `web/style.css`, and bootstrap files.
2. Add a loading container visible before Flutter paints.
3. Ensure the loader is removed cleanly when Flutter takes over.
4. Verify no layout shift or blank-screen regression.
5. Test with a slow-network or release build.

## Output contract

- Updated web shell files
- Loader styling and bootstrap notes
- Verification checklist for release mode

## Validation checklist

- Loader is visible immediately
- Loader disappears cleanly
- App still boots in release mode
- No script or CSS dependency breaks startup

## Related skills

- `flutter-go-router-deeplink-wireup`
- `flutter-performance-audit`

## References

- [`../../../examples/release-config-example.md`](../../../examples/release-config-example.md)
- [`../../../canonical/web_loading.md`](../../../canonical/web_loading.md)

## Real example

Use a centered shell with text like `Loading app...` and a subtle progress indicator in `web/index.html` before `flutter_bootstrap.js` starts the app.

## Real file output sample

```text
web/index.html
web/style.css
web/flutter_bootstrap.js
```
