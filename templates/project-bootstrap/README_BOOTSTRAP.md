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
2. Choose one overlay if relevant.
3. Copy the project memory templates.
4. Add project-specific architecture rules.
5. Add project-specific verification commands.
6. Add CI checks matching those commands.
7. Run one real feature through the canonical lifecycle.

## Exit criteria
A project is considered bootstrapped when:
- AI instructions are explicit
- one overlay is chosen or intentionally omitted
- verification commands are written down
- memory files exist
- CI exists or a temporary manual verification process is documented

## Notes
Keep project-specific rules in the consuming repo.
Only move material back into the foundation if it is broadly reusable.
