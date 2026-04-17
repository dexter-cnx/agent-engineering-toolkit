# Mobile Flutter Overlay Phase 6

Production Flutter operating overlay for the Agent Engineering Toolkit.

This overlay keeps the foundation general and pushes Flutter-specific execution into smaller atomic skills, workflows, policies, templates, examples, and generator tooling.

## Start here

- If you are new, read `HOW_TO_USE.md` first, then `docs/tutorials/getting-started.md`.
- `HOW_TO_USE.md`
- `AGENTS.overlay.md`
- `SKILLS_INDEX.md`
- `SKILL_SCHEMA.md`

## What changed in v2

- The catalog is routed through a generated decision index instead of a flat list.
- Skills are atomic execution capsules with explicit single responsibilities.
- Generator tooling creates new skills from a standard template.
- Policies live outside skills.
- Workflows orchestrate multiple skills in a fixed order.
- CI validates schema, overlap, docs sync, and index synchronization.

## Active architecture

```text
overlays/mobile-flutter/
  AGENTS.overlay.md
  README.md
  SKILLS_INDEX.md
  SKILL_SCHEMA.md
  skills/
  workflows/
  policies/
  canonical/
  templates/
  examples/
  checklists/
  ci/
  starter-app-template/
```

## Default stack

- Flutter stable
- Dart 3
- Clean Architecture
- Riverpod by default
- GetX when explicitly selected
- `go_router` for navigation
- Firebase adapters behind repository boundaries
- CSV-driven localization when localization is needed

## Operating rule

Use `SKILLS_INDEX.md` to select the smallest skill that can finish the task, then compose workflows when the work spans multiple execution units. Use `tools/skillgen/` to add or sync skills safely.

## Karpathy integration

- Governed exemplar: `skills/flutter-network-dio/SKILL.md`
- Contract: `skills/flutter-network-dio/skill.contract.yaml`
- Eval case: `skills/flutter-network-dio/eval/cases/governance-smoke/README.md`

## Archive assets

The overlay retains older catalog material in place for reference, but only the v2 skill set is considered active and CI-validated.

## Related docs

- `docs/tutorials/README.md`
- `docs/tutorials/getting-started.md`
- `docs/tutorials/how-skills-work.md`
- `docs/tutorials/add-a-new-skill.md`
- `examples/README.md`
- `examples/real-world/README.md`
- `prompts/new_project.md`
- `prompts/new_feature.md`
- `prompts/fix_architecture.md`
- `prompts/integrate_firebase_auth.md`
- `prompts/add_go_router_deeplink.md`
- `prompts/release_android_ios.md`
- `docs/tutorials/build-a-new-project-with-ai.md`
- `docs/tutorials/add-a-new-feature-with-ai.md`
- `docs/tutorials/release-a-flutter-app-with-ai.md`
- `docs/tutorials/fix-architecture-violations-with-ai.md`
- `docs/tutorials/real-use-cases.md`
- `AGENT_CONTRIBUTION_RULES.md`
- `CONTRIBUTING_SKILLS.md`
- `MAINTAINER_REVIEW_GUIDE.md`
- `MIGRATION_TO_V2.md`
- `workflows/new-project/README.md`
- `workflows/new-feature/README.md`
- `workflows/release-app/README.md`
- `workflows/migrate-project/README.md`
## Overlay OS contract

### Purpose
Provide specialization for **mobile-flutter** while keeping the repository root stack-neutral.

### When to use
Use this overlay for Flutter-first mobile delivery and app architecture standards.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
