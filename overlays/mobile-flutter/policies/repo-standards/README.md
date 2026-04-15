# Repo Standards Policy

## Rules

- Keep overlay-local docs in overlay-local paths.
- Keep reusable examples in `examples/` and templates in `templates/`.
- Keep skill files atomic and task-based.
- Keep active skill names stable once published.
- Prefer explicit file paths in every skill output.

## File standards

- Use ASCII unless an existing file clearly requires Unicode.
- Use short, path-based names that are easy to route.
- Avoid duplicating the same guidance across many docs.

## Change standards

- Update the router when a new active skill is added.
- Update examples when a skill changes its output contract.
- Update CI when schema rules change.
