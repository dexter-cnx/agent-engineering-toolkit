# Runtime CLI Usage

Entrypoint: `tools/os/cli.ts`

## Commands

### `os overlays list`

- Lists registered overlays as tab-separated lines.
- Exit code: `0` on success.

### `os run <overlay>`

- Resolves overlay from manifest-backed registry.
- Runs simulation mode execution with compiled prompt.
- Output:
  - summary line (`overlay=... mode=... prompt=...`)
  - simulated output preview line
- Exit code: `0` on success.

### `os validate`

- Emits machine-friendly JSON:
  - `{"status":"pass","overlays":<n>,"source":"docs/overlays.manifest.json"}`
- Exit code: `0` on success.

## Failure behavior

- Invalid usage returns exit code `1`.
- Runtime errors return exit code `2` with `OS_CLI_FAIL:` stderr prefix.
