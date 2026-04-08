# Repo Bootstrap

## Recommended bootstrap set for a new repo
Copy or link:
- `AGENTS.md`
- `templates/project-bootstrap/README_BOOTSTRAP.md`
- `templates/project_memory/decisions.md`
- `templates/project_memory/known_constraints.md`
- `templates/project_memory/patterns.md`
- one overlay if relevant

## Then add
- project-specific CI
- project-specific verification commands
- project-specific architecture constraints
- project-specific coding conventions
- public-release scaffold in the consuming repo if that repo will be public

## Optional helper
Use `scripts/bootstrap-project-memory.sh` if you want a small helper that adds the toolkit submodule and copies the memory templates.

## Goal
The consuming repo should end up with:
- general foundation from this toolkit
- one relevant overlay
- local instructions for project-specific reality
- explicit verification
- GitHub-facing scaffold if public release readiness matters
