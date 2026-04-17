# Next.js + Python Worker Composition

This composition layer shows how to combine:
- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/python-service/`
- `packages/job-contracts/`
- `apps/ai-workflow-reference/`

Use it when the frontend is the primary user surface, the backend owns identity and CRUD,
and a Python worker handles AI-heavy or long-running async jobs.

## Read first

1. `overlays/web-frontend-common/README.md`
2. `overlays/web-frontend-nextjs/README.md`
3. `overlays/backend-common/README.md`
4. `overlays/python-service/README.md`
5. `docs/fullstack/ai-worker-architecture.md`
6. `docs/fullstack/async-jobs.md`
7. `docs/fullstack/observability.md`
8. `docs/fullstack/failure-recovery.md`
9. `packages/job-contracts/README.md`
10. `apps/ai-workflow-reference/README.md`

## Overlay combination

- `web-frontend-common` owns shared UX state and loading/error patterns.
- `web-frontend-nextjs` owns routing, server/client boundaries, and interaction surfaces.
- `backend-common` owns contracts, validation shape, auth policy, and permissions.
- `python-service` owns queue consumers, orchestration services, and AI adapters.
- `packages/job-contracts` owns the async job envelope and task schemas.

## When to use it

- AI work is asynchronous or batch-oriented
- the product needs a queue/job model instead of direct provider calls
- human review or retry behavior matters
- the web app should show job submission, progress, and recovery states

## System boundaries

- synchronous paths handle auth, CRUD, and job submission
- asynchronous paths handle provider calls, document processing, and generation work
- the UI never calls AI providers directly
- the backend never hides job state transitions behind ad hoc strings

## Queue and job flow

1. The frontend validates and submits a job request.
2. The backend validates the payload against `packages/job-contracts`.
3. The backend persists a job envelope and enqueues the job.
4. The worker consumes the queue item and executes the AI or batch task.
5. The worker writes progress, retry, failure, and result updates.
6. The frontend polls or subscribes to updates and renders the job state.

## Contract ownership

- API request and response shapes live in `packages/job-contracts`.
- Job retry metadata and trace metadata also live in `packages/job-contracts`.
- Worker-specific adapters own provider-specific request shaping.
- Frontend screens own display concerns only.

## Retry and failure patterns

- use idempotency keys for submission and worker retries
- retry transient failures with bounded backoff
- dead-letter jobs after the configured attempt ceiling
- keep human review explicit for high-risk outputs

## Observability expectations

- propagate correlation IDs from frontend to backend to worker
- log queue lag, retry count, and failure reason
- expose job state transitions in the status view
- make dead-lettered jobs easy to audit

## Scaling triggers

- worker latency grows beyond the API request budget
- provider rate limits become a product concern
- the job graph requires retries, dead-letter handling, or batching
- human review or auditability becomes a core flow

## Related paths

- `docs/compositions/nextjs-dotnet-python-worker/README.md`
- `docs/fullstack/ai-worker-architecture.md`
- `docs/fullstack/async-jobs.md`
