# HOW TO USE

This overlay has two usage layers.

## Layer A — Toolkit source of truth
Use these docs inside Agent Engineering Toolkit:
- `START_HERE.md`
- `INDEX_CANONICAL.md`
- `INDEX_PROMPTS.md`
- `INDEX_CHECKLISTS.md`

## Layer B — Repo-facing integration
Use `companion-pack/` inside a real Flutter app repository.

## Recommended workflow

### For a new repo
1. Start from `generic_app`
2. Add only required capabilities
3. Scaffold one feature at a time
4. Run policy check and CI

### For an existing repo
1. Read `companion-pack/migration/older_vault_cleanup.md`
2. Add capabilities incrementally
3. Migrate one feature or one screen first
4. Keep changed files scope tight

## Example commands in a real app repo

```bash
python3 tooling/flutter_overlay_cli_v7.py init generic_app
python3 tooling/flutter_overlay_cli_v7.py add-capabilities riverpod localization dio
python3 tooling/flutter_overlay_cli_v7.py scaffold-capability dio
python3 tooling/flutter_overlay_cli_v7.py create-feature home riverpod
python3 tooling/flutter_overlay_cli_v7.py check-policy
```
