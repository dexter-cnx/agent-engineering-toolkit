# HOW TO USE

This consolidated Phase 21 package is meant to be copied into:

```bash
cp -R overlays/mobile-flutter /path/to/agent-engineering-toolkit/overlays/
```

Then commit and push.

## Recommended usage modes

### Mode A — Toolkit source of truth
Use this overlay as the canonical Flutter overlay inside Agent Engineering Toolkit.

### Mode B — Repo companion source
Copy selected files from `companion-pack/` into a real Flutter app repo.

### Mode C — Team onboarding
Use:
- `START_HERE.md`
- `ONBOARDING_MINIMAL.md`
- `ONBOARDING_FULL.md`

## Fastest path
1. Read `START_HERE.md`
2. Choose `generic_app` unless you clearly need `field_service`
3. Use companion CLI in an app repo
4. Add capabilities incrementally
5. Run policy check and CI
