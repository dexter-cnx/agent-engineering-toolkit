# Mobile Flutter Overlay

Production Flutter specialization overlay for the stack-neutral Agent Engineering OS.

## Purpose

Provide Flutter-specific implementation guidance (skills, workflows, policies, templates, examples) while keeping root governance and onboarding canonical.

## When to use

Use this overlay when the consuming repository is Flutter-first and needs operational guidance for architecture, features, CI/CD, release, and platform integration.

## When not to use

- Do not use for root OS governance or onboarding authority.
- Do not use for non-Flutter stacks.
- Do not treat this overlay as canonical policy for backend/web/unity tracks.

## Canonical links

- Front door: [`README.md`](../../README.md)
- Canonical onboarding: [`docs/get-started.md`](../../docs/get-started.md) → [`docs/adoption-paths.md`](../../docs/adoption-paths.md)
- Overlay catalog and boundary: [`docs/overlays.md`](../../docs/overlays.md)
- Runtime role/workflow authority: [`agents/README.md`](../../agents/README.md)

## Expected consuming repository shape

```text
repo/
├─ lib/
│  ├─ app/
│  ├─ features/
│  ├─ shared/
│  └─ core/
├─ test/
├─ integration_test/
├─ android/
├─ ios/
├─ scripts/
└─ project_memory/
```

## Verify commands

```bash
python3 tools/ci/overlay_lint.py
python3 overlays/mobile-flutter/ci/verify_skill_schema.py
python3 overlays/mobile-flutter/ci/verify_docs_sync.py
```

## Examples and templates entrypoints

- Examples: `examples/README.md`, `examples/real-world/README.md`
- Workflows: `workflows/new-project/README.md`, `workflows/new-feature/README.md`, `workflows/release-app/README.md`
- Tutorials: `docs/tutorials/README.md`, `docs/tutorials/app-log-and-production-logging.md`
- Templates and generation: `templates/`, `tools/skillgen/`
- Starter reference: `starter-app-template/README.md`

## Memory conventions

Capture reusable Flutter decisions in project memory:
- state management choice and boundaries
- routing/deeplink strategy
- platform integration constraints
- release/signing constraints
- known regressions and rollout notes

## Review checklist

- Root identity stays stack-neutral and unchanged.
- Flutter details remain inside this overlay (not root docs/contracts).
- Skills/workflows are atomic and non-overlapping.
- Verify commands pass without manual edits to generated artifacts.
- Examples and templates remain aligned with active skills.

## Start here

- `HOW_TO_USE.md`
- `AGENTS.overlay.md`
- `SKILLS_INDEX.md`
- `SKILL_SCHEMA.md`
- `docs/tutorials/getting-started.md`

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
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
