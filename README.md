# agent-engineering-toolkit

A production-ready, domain-agnostic toolkit for structured AI-assisted software engineering.

This repository is a foundation toolkit that can be reused across:
- mobile projects
- backend services
- web frontends
- AI and agent systems
- monorepos
- internal engineering platforms

It is intentionally not tied to mobile. Mobile is treated as an overlay, not the default identity of the toolkit.

## Canonical references

- Lifecycle source of truth: `docs/prompt-pipeline.md`
- Role model source of truth: `docs/agent-team-system.md`
- Prompt hub: `prompts/index.md`
- Prompt hub (English): `prompts/index_EN.md`
- Adoption guide: `docs/how-to-use.md`
- Tutorial: `docs/tutorial.md`
- Overlay strategy: `docs/overlays.md`

## Mobile Flutter overlay status

The mobile Flutter overlay now includes a structured catalog of 23 reusable capability skills under `overlays/mobile-flutter/skills/`.

### Mobile Flutter skill groups

#### Core
- `flutter-auth`
- `flutter-permissions`
- `flutter-geolocation`
- `flutter-maps`
- `flutter-storage`
- `flutter-networking`
- `flutter-deep-link`
- `flutter-push-notifications`
- `flutter-i18n-l10n`

#### Product
- `flutter-analytics`
- `flutter-crash-reporting`
- `flutter-feature-flags`
- `flutter-offline-first`
- `flutter-remote-config`

#### Release
- `flutter-web-deployment`
- `flutter-build-flavors`
- `flutter-app-signing-release`
- `flutter-ci-cd-mobile`

#### Device
- `flutter-camera-media`
- `flutter-file-upload-download`
- `flutter-biometric-auth`
- `flutter-background-tasks`
- `flutter-contacts-sharing`

## Start here

- `README_START_HERE.md`
- `docs/how-to-use.md`
- `docs/tutorial.md`
- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/skills/index.md`

## Documentation

- `docs/how-to-use.md`
- `docs/how-to-use_TH.md`
- `docs/tutorial.md`
- `docs/tutorial_TH.md`
- `docs/tutorials/index.md`
- `docs/tutorials/index_EN.md`
- `docs/overlays.md`

## Worked examples

- `examples/worked_examples/foundation_feature_flow.md`
- `overlays/mobile-flutter/examples/worked_example.md`

## License

MIT
