# AI Worker Architecture

This document defines when and how to add a worker lane to the toolkit's full-stack story.

## When to introduce a worker layer

Add a worker layer when the work is:

- AI-heavy
- long-running
- batch-oriented
- rate-limited by an external provider
- likely to retry or dead-letter
- better represented as a job than a single HTTP response

Do not add a worker lane just because the implementation uses an AI provider.
If the work is synchronous, bounded, and user-facing, keep it in the request path.

## Why not call AI providers directly from UI routes

- UI routes become fragile under long latency
- provider retries can outlive the request budget
- failures become harder to audit
- queue semantics and idempotency disappear
- human review checkpoints become awkward to model

## Job lifecycle

1. submit
2. validate
3. queue
4. claim
5. run
6. retry or fail
7. dead-letter or succeed
8. notify or poll status

## Boundary model

- frontend: submit job and show status
- API: validate, persist, authorize, and enqueue
- worker: execute provider calls and batch processing
- contracts: define the shared envelope, status, retry, and result shapes

## Contract ownership

- `packages/job-contracts` owns the shared async schema layer
- API DTOs map to and from the shared job envelope
- worker adapters map provider requests and provider responses
- UI code consumes job status only, not provider internals

## Human review checkpoints

Use review checkpoints when the output affects:

- regulated or customer-facing content
- document extraction with downstream consequences
- long-form generation that needs operator approval
- multi-step jobs where a terminal state should be gated

## Scale-up path

1. direct HTTP request
2. queued job with polling
3. queued job with event updates
4. multi-stage workflow with review checkpoints
5. separate worker fleet or queue partitioning

