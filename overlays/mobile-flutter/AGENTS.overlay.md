# AGENTS.overlay.md

## Overlay purpose

This overlay equips an agent to plan, build, review, verify, and release Flutter applications using atomic skills and explicit orchestration.

## Foundation assumptions

- Keep the foundation domain-agnostic; Flutter specialization stays in this overlay.
- Prefer Flutter stable and Dart 3.
- Prefer Clean Architecture at the feature boundary.
- Prefer Riverpod unless the task explicitly calls for GetX or the project already uses GetX.
- Prefer `go_router` for routing and deep links.
- Keep external services behind adapters and repositories.
- Keep business logic out of widgets.
- Keep localization, testing, and release readiness part of delivery, not afterthoughts.

## Active v2 routing

### Architecture

- `skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- `skills/architecture/flutter-feature-folder-scaffold/SKILL.md`
- `skills/architecture/flutter-feature-contract-scaffold/SKILL.md`

### State

- `skills/state/flutter-riverpod-state-skeleton/SKILL.md`
- `skills/state/flutter-getx-controller-skeleton/SKILL.md`

### Routing

- `skills/routing/flutter-go-router-route-map/SKILL.md`
- `skills/routing/flutter-go-router-redirect-guard/SKILL.md`
- `skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`

### Firebase

- `skills/firebase/flutter-firebase-auth-adapter/SKILL.md`
- `skills/firebase/flutter-firebase-auth-state/SKILL.md`
- `skills/firebase/flutter-firestore-repository/SKILL.md`

### Web

- `skills/web/flutter-web-loading-shell/SKILL.md`

### Release

- `skills/release/flutter-android-signing-config/SKILL.md`
- `skills/release/flutter-android-release-validate/SKILL.md`
- `skills/release/flutter-ios-release-readiness/SKILL.md`

### Testing

- `policies/testing/README.md`
- `ci/validate_skills.sh`

### Performance

- `skills/performance/flutter-performance-audit/SKILL.md`

### Tooling

- `skills/tooling/flutter-design-token-map/SKILL.md`
- `skills/tooling/flutter-localization-csv-sync/SKILL.md`

## Orchestration rules

- New project -> `workflows/new-project/README.md`
- New feature -> `workflows/new-feature/README.md`
- Release -> `workflows/release-app/README.md`
- Migration -> `workflows/migrate-project/README.md`

## Delivery rules

1. Pick the smallest active skill that covers the task.
2. Compose multiple skills through a workflow when the task spans architecture, implementation, and release.
3. Update templates and examples when the expected file shape changes.
4. Update policies when the operating standard changes.
5. Validate active skills through the CI checker before calling the overlay production-ready.

## Agent contribution rules

- Prefer updating an existing skill over creating a duplicate.
- If a new skill is needed, justify the new boundary before writing files.
- Use `tools/skillgen/` to scaffold, validate, sync the index, and check overlap.
- Fill every schema field completely and link examples plus templates.
- Keep workflow docs orchestration-only and keep policies out of skills.
- Treat legacy skill files outside the active v2 router as compatibility stubs. Do not expand them; migrate behavior into the active router, workflows, policies, templates, or tutorials.

## Output discipline

- State assumptions before major changes.
- Keep architecture and implementation separate for non-trivial work.
- Verify structural correctness, obvious edge cases, and docs consistency.
- Call out what was not verified.

## Reference layers

- Canonical baselines live in `canonical/`.
- Scaffolding lives in `templates/`.
- Worked examples live in `examples/`.
- Tutorials live in `docs/tutorials/`.
- Policy constraints live in `policies/`.
- Contribution rules live in `AGENT_CONTRIBUTION_RULES.md`.
