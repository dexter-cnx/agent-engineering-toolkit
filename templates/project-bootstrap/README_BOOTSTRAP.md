# Project Bootstrap

Use this template to bootstrap a consuming repository with the toolkit.

## Goal
End up with:
- one clear root contract
- one chosen overlay if relevant
- memory files
- explicit verification commands
- project-specific CI
- project-specific architecture constraints

## Required inputs
- project name
- project type
- primary stack
- expected deployment surface
- main verification commands
- known constraints

## Bootstrap steps
1. Add or reference `AGENTS.md`.
2. Choose exactly one overlay if the stack is known; omit overlays only if the repo is intentionally stack-neutral for now.
3. Copy the project memory templates.
4. Add project-specific architecture rules.
5. Add project-specific verification commands.
6. Add CI checks matching those commands.
7. Run one real feature through the canonical lifecycle.

## Example finished bootstrap state
- `AGENTS.md` exists in the consuming repo
- one overlay has been copied or referenced
- `project_memory/decisions.md`, `known_constraints.md`, and `patterns.md` exist
- README or local docs list verification commands
- CI runs those commands or documents a temporary manual verification path

## Exit criteria
A project is considered bootstrapped when:
- AI instructions are explicit
- one overlay is chosen or intentionally omitted
- verification commands are written down
- memory files exist
- CI exists or a temporary manual verification process is documented

## Optional helper
If you want a small helper that only adds the toolkit submodule and copies the memory templates, use `scripts/bootstrap-project-memory.sh`.

## Important note
Keep stack-specific rules in overlays and project-specific rules in the consuming repo.
Only move material back into the foundation if it is broadly reusable.
