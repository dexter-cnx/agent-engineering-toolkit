# AI Workflow Reference

This reference shows how a frontend, API, and Python worker coordinate through shared job
contracts.

## What it demonstrates

- submit job flow from a frontend surface
- polling-based job status updates
- job status page pattern
- retry and failure UI pattern
- traceability through correlation IDs and trace IDs
- worker runtime boundaries for AI provider calls

## Canonical boundary rule

Frontend code submits jobs and renders status.
API code validates, queues, and records jobs.
Worker code executes AI-heavy or long-running work.
AI provider integration belongs in the worker runtime, not in UI routes.

## Reference layout

```text
apps/ai-workflow-reference/
├─ api/
│  └─ submit-job.route.ts
├─ frontend/
│  └─ job-status.page.tsx
├─ worker/
│  └─ process-job.py
├─ contracts/
│  └─ usage.md
├─ examples/
│  ├─ submit-job.ts
│  ├─ job-status.page.tsx
│  └─ worker-task.py
└─ scripts/
   └─ check-structure.mjs
```

## Job flow

1. The frontend submits a typed job request.
2. The API validates the payload against `packages/job-contracts`.
3. The API stores the job envelope and enqueues the job.
4. The worker reads the envelope, performs the task, and updates status.
5. The frontend polls for status or consumes updates from an event stream.
6. Failure states are visible to both operators and end users.

## Read next

- `docs/fullstack/ai-worker-architecture.md`
- `docs/fullstack/async-jobs.md`
- `docs/fullstack/observability.md`
- `docs/fullstack/failure-recovery.md`
- `packages/job-contracts/README.md`
