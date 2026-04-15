# Migration To V2

This document explains how `overlays/mobile-flutter` changed from the older broad catalog to the current v2 overlay.

## What changed from the old structure

- The overlay now uses an active v2 router instead of a flat skill list.
- Skills are atomic and task-based.
- Workflows own multi-step orchestration.
- Policies live outside skills.
- Templates own reusable file shapes.
- Tutorials own explanations and walkthroughs.
- The CI gate validates schema, overlap, docs sync, and index sync.

## Where content moved

- Architecture and feature boundaries -> `skills/architecture/`
- State scaffolds -> `skills/state/`
- Routing and deep-linking -> `skills/routing/`
- Firebase boundaries -> `skills/firebase/`
- Web startup UX -> `skills/web/`
- Release readiness -> `skills/release/`
- Performance audits -> `skills/performance/`
- Design token and localization sync -> `skills/tooling/`
- Orchestration -> `workflows/`
- Constraints -> `policies/`
- File shapes -> `templates/`
- Operator guidance -> `docs/tutorials/`
- Reusable prompts -> `prompts/`

## How to find equivalent skills and workflows now

Use `SKILLS_INDEX.md` first.

Common mappings:

- Old feature bootstrap guides -> `workflows/new-project/README.md`
- Old new feature guides -> `workflows/new-feature/README.md`
- Old release guides -> `workflows/release-app/README.md`
- Old migration guides -> `workflows/migrate-project/README.md`
- Old Firebase auth bundles -> `skills/firebase/flutter-firebase-auth-adapter/SKILL.md` and `skills/firebase/flutter-firebase-auth-state/SKILL.md`
- Old routing bundles -> `skills/routing/flutter-go-router-route-map/SKILL.md`, `skills/routing/flutter-go-router-redirect-guard/SKILL.md`, and `skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`
- Old clean architecture guides -> `skills/architecture/flutter-clean-architecture-audit/SKILL.md`

## How to update old references

When you find an old reference such as `guide-*`, `policy-*`, or a deprecated umbrella skill:

1. Replace it with the active atomic skill or workflow.
2. If the content is explanatory, move it to a tutorial.
3. If the content is a file shape, move it to a template.
4. If the content is a constraint, move it to a policy.
5. If the content requires step ordering, move it to a workflow.

## Reference patterns

- Use `SKILLS_INDEX.md` for skill selection.
- Use `AGENTS.overlay.md` for routing rules.
- Use `HOW_TO_USE.md` for quick operator navigation.
- Use `docs/validation/skills-boundary-audit.md` for the latest boundary decisions.

## Practical rule

If a reference names an umbrella skill that no longer exists in the active router, replace it with the smallest active skill plus a workflow if sequencing is required.
