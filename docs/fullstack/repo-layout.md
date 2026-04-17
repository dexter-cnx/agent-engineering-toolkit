# Full-Stack Repo Layout

This repository is still foundation-first. The full-stack layer is a workspace-style subset
inside the larger toolkit.

## Layout map

```text
repo/
├─ apps/
│  ├─ nextjs-fullstack-app/      # canonical single-app starter
│  └─ nextjs-dotnet-app/         # canonical split starter
├─ packages/
│  ├─ contracts/                 # shared schema-first contracts
│  └─ fullstack-client/          # typed client helpers
├─ tools/
│  ├─ contract-check/            # contract automation
│  └─ fullstack-audit/           # repo integrity audit
├─ docs/fullstack/               # workflow, layout, and selection docs
├─ docs/compositions/            # composition references and Karpathy integration
├─ overlays/                     # capability overlays and skill contracts
└─ README.md                     # public front page and quick path
```

## How to navigate it

- Start at `README.md` for the public-facing quick path.
- Use `docs/fullstack/getting-started.md` when you need path selection.
- Use `docs/fullstack/dev-workflow.md` when you need commands.
- Use `docs/fullstack/selection-matrix.md` when the business shape is the deciding factor.

## What is canonical

- The starter apps are canonical runnable references.
- The contracts package is the canonical schema source for those starters.
- The client package is the canonical typed fetch pattern.
- The tools package checks repository integrity and consumer alignment.

## What is not canonical

- Overlay examples remain overlay-specific.
- Composition docs remain reference paths, not runnable starters.
- Tooling scripts are guards, not product features.
