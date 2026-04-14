# unity-save-system Skill

Use this skill when the project needs persistence, migration, or save-file conventions.

## Rules

- Version save data from the start.
- Separate schema migration from runtime state mutation.
- Keep save I/O behind a dedicated service or adapter.
- Prefer predictable fallback behavior when save data is missing or corrupt.
- Treat sensitive data and tamper risk as part of the design.

## Deliverables

- save schema plan
- migration notes
- fallback behavior
- verification checklist
