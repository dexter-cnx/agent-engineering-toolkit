# CLI Contract Governance

This policy governs machine-readable CLI contract evolution.

## Scope

Machine-readable outputs are contract surfaces for:

- `os validate`
- `os overlays list --json`
- `os run <overlay> --json`
- machine-readable error payloads emitted when `--json` is used

## Contract versioning expectations

- Payloads include `contractVersion`.
- Additive changes may keep the same major version.
- Breaking changes require a major contract version increment and release notes.

## Additive vs breaking changes

### Additive (non-breaking)

- Adding optional fields
- Adding new machine-readable commands
- Expanding enum sets where existing values remain valid

### Breaking

- Removing fields
- Renaming fields
- Changing field types
- Changing exit code semantics
- Changing default command mode from human to machine or vice versa

## Release-note requirements

Any change to machine-readable payloads must include:

1. affected commands
2. before/after payload examples
3. compatibility impact (additive or breaking)
4. migration guidance for automation consumers

## Enforcement

- Contract regressions are guarded by `tests/runtime/runtime.test.mjs`.
- Publish-critical metadata and bin correctness are guarded by `tools/ci/check-package-metadata.ts`.
