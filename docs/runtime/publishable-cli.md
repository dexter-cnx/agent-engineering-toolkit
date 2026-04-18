# Publishable CLI (Release Candidate)

The CLI is prepared for package distribution through the repository root `package.json` bin mapping.

## Package intent

- Package: `agent-engineering-toolkit`
- Entrypoint: `tools/os/bin/os.js`
- Runtime: Node.js 22+ (strip-types execution mode)

## Install methods

### Local repository workflow

```bash
npm install
npm run os:validate
npm run os:test
```

### Link install workflow

```bash
npm run os:link
os validate
```

### Packaging dry-run

```bash
npm run os:pack:dryrun
```

## Publish-readiness expectations

- Root `package.json` must retain accurate `bin.os` mapping and engine constraints.
- `os validate` output contract must remain stable for automation users.
- Runtime tests and governance checks must pass before release candidate tags.
- No real provider execution is introduced in this RC phase (simulation mode only).


## Release checklist

- `docs/runtime/release-candidate-checklist.md`
- `docs/runtime/cli-contract-governance.md`
