# Prompt: Fix Architecture

## Intent

Repair a boundary violation, dependency leak, or layer mismatch without rewriting the app.

## When to use

- A widget calls SDKs or repositories directly
- A route file contains logic that should live elsewhere
- A module mixes presentation, domain, and data responsibilities

## Required inputs

- Broken file path
- Current dependency direction
- Target boundary
- Current state and routing choice

## Optional inputs

- Error logs
- Diff or patch snippet
- Suggested refactor scope

## Expected outputs

- Violation summary
- File move/edit plan
- Restored boundary description
- Test updates

## Repo paths to inspect

- `overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `overlays/mobile-flutter/policies/architecture/README.md`
- `overlays/mobile-flutter/workflows/migrate-project/README.md`

## Related skills and workflows

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-getx-controller-skeleton`
- `flutter-firestore-repository`
- `flutter-firebase-auth-adapter`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `workflows/migrate-project/README.md`

## Guardrails

- Fix the boundary, not just the symptom
- Keep refactors small and reversible
- Do not move route or SDK logic into widgets
- Avoid full rewrites unless explicitly requested

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md first.

Task:
Fix the architecture violation in <file_or_feature_path>.

Deliver:
1. violation summary
2. exact files to move or edit
3. boundary to restore
4. test updates
5. re-audit checklist
```
