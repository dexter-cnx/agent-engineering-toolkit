# How To Use

## Minimal flow

1. Read `AGENTS.overlay.md`.
2. Select the active skill in `SKILLS_INDEX.md`.
3. Follow the matching workflow in `workflows/`.
4. Use templates from `templates/` and examples from `examples/`.
5. Use `tools/skillgen/` when adding or splitting skills.
6. Validate active skills with `ci/validate_skills.sh`.

## Typical commands

- New app: `workflows/new-project/README.md`
- New feature: `workflows/new-feature/README.md`
- Release: `workflows/release-app/README.md`
- Migration: `workflows/migrate-project/README.md`

## Quick examples

- Build a Flutter app from scratch by chaining scaffold, state, routing, localization, and release readiness skills.
- Add a secure feature by chaining architecture audit, feature scaffold, state, repository, and routing skills.
- Prepare a release by chaining platform readiness, signing, performance, and CI checks.

## Claude Code / Codex loading

- Open `overlays/mobile-flutter/README.md` first.
- Then open `AGENTS.overlay.md` and `SKILLS_INDEX.md`.
- Use the relevant workflow doc instead of reading every skill.
- When contributing a new skill, read `AGENT_CONTRIBUTION_RULES.md` and `docs/tutorials/add-a-new-skill.md`.
