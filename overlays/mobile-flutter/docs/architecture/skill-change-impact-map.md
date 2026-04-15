# Skill Change Impact Map

## When a skill changes

Updating one skill can affect:

- `SKILLS_INDEX.md`
- `workflows/`
- `docs/tutorials/`
- `examples/`
- `templates/`
- `ci/`
- `AGENTS.overlay.md`
- `AGENT_CONTRIBUTION_RULES.md`

## Impact rules

### Skills Index

- Update the index when a new active skill is added, removed, renamed, or re-categorized.
- Regenerate the index from skill metadata instead of editing rows manually.

### Workflows

- Update a workflow when its execution order changes or when a skill split creates a new atomic step.
- Keep workflows orchestration-only.

### Tutorials

- Update tutorials when contributor flow, validation flow, or usage assumptions change.
- Add a tutorial when a new generator or gate changes how agents should work.

### Examples

- Update examples when the output contract changes.
- Keep examples aligned with current active skill names.

### Templates

- Update templates when the skill scaffold or expected file shape changes.
- Template drift should fail CI.

### CI

- Update CI whenever schema rules, overlap rules, or docs-sync rules change.
- CI must fail if the active skill set is not in sync with the generated index.

## Maintenance reminder

- If a skill change touches more than one category, review whether it should be split before merging.
