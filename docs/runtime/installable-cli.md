# Installable CLI

The Agent Engineering OS CLI is installable from this repository via the package `bin` mapping.

## Runtime prerequisites

- Node.js 22+
- npm 10+

## Local development workflow

From a fresh clone:

```bash
npm install
npm run os:validate
npm run os:test
```

Run commands directly during development:

```bash
npm run os -- overlays list
npm run os -- run backend-node
npm run os -- validate
```

## Install-and-run workflow

Install the CLI entrypoint from this repository:

```bash
npm link
os validate
os overlays list
os run backend-node
```

Root `package.json` maps the `os` bin to `tools/os/bin/os.js`, which dispatches into `tools/os/cli.ts` using Node strip-types mode.

## Release-readiness notes

Before shipping CLI changes:

1. Run `npm run os:test`.
2. Run governance checks (`python3 tools/ci/*.py` and CI TypeScript checks).
3. Confirm `os validate` output contract remains stable.
4. Keep CLI behavior additive and non-breaking for automation users.


## Related release-candidate docs

- `docs/runtime/publishable-cli.md`
- `docs/runtime/command-output-contracts.md`
