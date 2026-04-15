# Prompt: Add go_router Deep Link

## Intent

Add route map, redirect, and deep-link wiring for a Flutter app that uses `go_router`.

## When to use

- The app must open from external links
- Route tree and redirect logic need separation
- You need deterministic navigation behavior across platforms

## Required inputs

- Target routes
- Deep-link patterns
- Guard or redirect rules
- Root entrypoint file

## Optional inputs

- Web-only vs mobile-only scope
- Auth gate requirements
- Initial route and shell route requirements

## Expected outputs

- Route map file
- Redirect guard file
- Deep-link wiring file
- Navigation verification notes

## Repo paths to inspect

- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/examples/routing-example.md`
- `overlays/mobile-flutter/examples/real-world/go-router-deep-linking.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-redirect-guard/SKILL.md`
- `overlays/mobile-flutter/skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`

## Related skills and workflows

- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-clean-architecture-audit`
- `workflows/new-project/README.md`
- `workflows/new-feature/README.md`

## Guardrails

- Keep route tree, redirect, and deep-link parsing in separate responsibilities
- Do not put navigation logic in widgets
- Keep typed route params and explicit entrypoints
- Validate the route file before wiring deep links

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/examples/routing-example.md.

Task:
Add go_router route map, redirect guard, and deep-link wiring for <app_name>.

Deliver:
1. route plan
2. deep-link entry plan
3. exact files to update
4. validation checklist
```
