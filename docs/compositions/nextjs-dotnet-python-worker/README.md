# Next.js + .NET + Python Worker Composition

This composition layer shows how to combine:
- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/backend-dotnet/`
- `overlays/python-service/`
- `packages/job-contracts/`
- `apps/ai-workflow-reference/`

Use it when the frontend is Next.js, the core backend is .NET, and Python handles the AI
or batch worker lane.

## Read first

1. `overlays/web-frontend-common/README.md`
2. `overlays/web-frontend-nextjs/README.md`
3. `overlays/backend-common/README.md`
4. `overlays/backend-dotnet/README.md`
5. `overlays/python-service/README.md`
6. `docs/fullstack/ai-worker-architecture.md`
7. `docs/fullstack/async-jobs.md`
8. `docs/fullstack/observability.md`
9. `docs/fullstack/failure-recovery.md`
10. `packages/job-contracts/README.md`
11. `apps/ai-workflow-reference/README.md`

## Overlay combination

- `web-frontend-common` owns shared UX state and error handling.
- `web-frontend-nextjs` owns routing, server/client boundaries, and status pages.
- `backend-common` owns contract and validation shape.
- `backend-dotnet` owns auth, policy enforcement, persistence, and API ownership.
- `python-service` owns worker execution, queues, and AI adapters.
- `packages/job-contracts` owns the async job envelope and task schemas.

## When to use it

- the product needs strong API control plus worker-based async AI processing
- the backend must enforce enterprise auth, validation, or audit behavior
- the worker lane should stay isolated from the web request path
- the team wants a long-lived core backend with a separate async runtime

## System boundaries

- synchronous paths handle auth, CRUD, and job submission
- the .NET backend owns identity, policy, persistence, and queue handoff
- the Python worker owns AI provider calls and batch processing
- the frontend only submits jobs and presents status and recovery states

## Queue and job flow

1. The frontend submits a typed request.
2. The .NET backend validates the request and creates a job envelope.
3. The backend writes the job and enqueues the async work item.
4. The Python worker consumes the job and executes the task.
5. The worker reports progress, retry state, and terminal outcomes.
6. The frontend renders status through polling or event updates.

## Contract ownership

- shared job payloads live in `packages/job-contracts`
- backend DTOs should map to the same envelope and status model
- worker adapters own provider-specific IO and serialization details
- frontend contracts stay focused on submit/status/review views

## Retry and failure patterns

- keep idempotency keys stable across submit and retry
- retry transient worker failures with bounded backoff
- dead-letter jobs that exhaust the retry ceiling
- surface actionable error codes for operators and reviewers

## Observability expectations

- propagate correlation IDs into the .NET backend and Python worker
- record queue wait time, worker runtime, and retry count
- expose terminal failure reasons in the UI and logs
- keep human review checkpoints explicit when outputs are sensitive

## Scaling triggers

- worker throughput becomes independent of API throughput
- generation tasks exceed the request-response budget
- queue depth or retry pressure becomes operationally visible
- auditability or human review becomes mandatory

## Related paths

- `docs/compositions/nextjs-python-worker/README.md`
- `docs/fullstack/ai-worker-architecture.md`
- `docs/fullstack/async-jobs.md`
