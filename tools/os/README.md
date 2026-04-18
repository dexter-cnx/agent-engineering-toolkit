# OS CLI (workspace entrypoint)

Installable CLI entrypoint for the Agent Engineering OS runtime surface (wired from root package bin).

## Purpose

- list manifest-backed overlays
- run simulation-mode prompt execution for an overlay
- validate runtime/overlay registration contract

## Install (local workspace)

```bash
npm install
npm link
os validate
```

## Commands

- `os overlays list [--json]`
- `os run <overlay> [--json]`
- `os validate`
