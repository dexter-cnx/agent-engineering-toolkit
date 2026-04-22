# Prompt: New Feature

## Intent

Add one Flutter feature module to an existing app without violating architecture, routing, or state boundaries.

## When to use

- Adding a feature slice to an existing consuming app
- Creating a new module under `lib/features/`
- You need the smallest safe implementation plan before coding

## Required inputs

- Feature name
- Feature goal
- Target feature path
- State choice
- Data source choice

## Optional inputs

- Route requirements
- Localization keys
- Test scope
- Analytics or logging needs

## Expected outputs

- Feature folder plan
- Domain contract plan
- State holder plan
- Repository plan
- Test plan

## Repo paths to inspect

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `overlays/mobile-flutter/templates/state-management-template.md`
- `overlays/mobile-flutter/examples/full-feature-implementation.md`
- `overlays/mobile-flutter/examples/firebase-integration-example.md`

## Related skills and workflows

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-getx-controller-skeleton`
- `flutter-firestore-repository`
- `flutter-firebase-auth-adapter`
- `flutter-production-logging`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `workflows/new-feature/README.md`

## Guardrails

- Do not put SDK calls in widgets
- Do not register routes inside presentation files
- Do not add state and repository logic in the same layer
- Keep the feature atomic and reusable

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.

Task:
Add <feature_name> to the app with <state_choice> and <data_source_choice>.

Deliver:
1. exact files to create or update
2. skill selection
3. implementation order
4. validation checklist
```
