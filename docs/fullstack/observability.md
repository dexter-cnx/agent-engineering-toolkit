# Observability

Async full-stack systems need visibility across frontend, API, queue, and worker layers.

## What to observe

- request ID
- correlation ID
- trace ID
- job ID
- queue wait time
- execution duration
- retry count
- terminal failure reason
- dead-letter state

## Logging

- log one structured event per state transition
- keep provider payloads out of logs unless sanitized
- do not hide retryable failures behind generic messages
- log dead-letter reasons with enough context to debug

## Metrics

Track:

- job submissions
- queue depth
- claim latency
- run duration
- retry rate
- dead-letter rate
- worker success rate

## Tracing

- propagate trace IDs from frontend to API to worker
- create spans around queue handoff and provider calls
- keep worker traces separate from request traces but link them through correlation IDs

## Operator visibility

The status page or admin view should expose:

- current status
- retry count
- last error
- last transition time
- correlation or trace reference

