# How To Use This Overlay

This overlay has two usage layers.

## Layer A - Toolkit source of truth
Use these docs inside Agent Engineering Toolkit:
- `START_HERE.md`
- `INDEX_CANONICAL.md`
- `INDEX_PROMPTS.md`
- `INDEX_COMPANION.md`
- `INDEX_CHECKLISTS.md`

## Layer B - Repo-facing integration
Use `companion-pack/` inside a real web frontend repository.

## Recommended workflow
### For a new repo
1. Start from `web-dev`
2. Add only the required capabilities
3. Scaffold one feature at a time
4. Run review and verification gates

### For an existing repo
1. Read `repo-customization/REPO_ADAPTATION_CHECKLIST.md`
2. Add capabilities incrementally
3. Migrate one feature or one screen first
4. Keep the changed-file scope tight

## Catalog discipline
Use the overlay-local index as the catalog entry point.
Do not duplicate the catalog shape in foundation docs.
