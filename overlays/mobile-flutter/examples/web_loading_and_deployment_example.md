# Web Loading and Deployment Example

## Scenario

The mobile Flutter app also ships for web and needs loading and deployment rules.

Example change:

- startup splash/loading shell
- web bootstrap behavior
- deployment checklist for QA or staging

## Recommended skills

- `guide-flutter-web-loading`
- `flutter-web-deployment`
- `flutter-dev`
- `guide-app-release-checklist`

## Reference files

- `overlays/mobile-flutter/skills/guide-flutter-web-loading/SKILL.md`
- `overlays/mobile-flutter/prompts/apply_flutter_web_loading.md`
- `overlays/mobile-flutter/prompts/prepare_flutter_web_release.md`
- `overlays/mobile-flutter/prompts/patch_existing_flutter_project_with_web_loader.md`
- `overlays/mobile-flutter/templates/flutter_web_loading_checklist.md`
- `overlays/mobile-flutter/templates/flutter_web_deployment_checklist.md`
- `overlays/mobile-flutter/skills/guide-app-release-checklist/SKILL.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- guide-flutter-web-loading
- flutter-web-deployment
- flutter-dev

Task:
Prepare the app for web startup/loading and deployment validation.

Deliver:
1. loading strategy
2. deployment notes
3. files to check
4. release risks
```

## Expected output

- loading state is deliberate and brief
- web bootstrap behavior is documented
- deployment checks are explicit
- release risks are called out before shipping

## Review notes

- keep web startup rules separate from feature logic
- avoid ad hoc loading behavior in leaf widgets
- document any web-only caveats clearly

## Verification notes

- confirm the loading checklist is referenced
- confirm deployment steps are documented
- confirm web-only behavior is isolated from feature logic
