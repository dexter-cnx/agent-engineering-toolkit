# Job Contracts

Schema-first job contracts for worker-backed full-stack compositions.

## What it provides

- a shared job envelope
- task status and retry metadata
- result and error shapes
- reusable task schemas for document analysis, report generation, and AI extraction
- correlation and trace guidance for async orchestration

## Why this package exists

The package gives frontend, API, and worker code a common contract layer for queued work.
It keeps async workflows explicit instead of burying them in provider-specific code.

## Commands

```bash
npm run check
npm run build
```

## Read next

- `docs/fullstack/ai-worker-architecture.md`
- `docs/fullstack/async-jobs.md`
- `docs/fullstack/observability.md`
- `docs/fullstack/failure-recovery.md`
- `apps/ai-workflow-reference/README.md`
