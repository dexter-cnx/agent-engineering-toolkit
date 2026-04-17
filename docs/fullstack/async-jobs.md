# Async Jobs

This guide covers the practical rules for job-based execution in the toolkit.

## Job shape

Every async task should carry:

- a stable job ID
- a job type
- a version
- a status
- retry metadata
- correlation and trace IDs
- a payload
- a terminal result or error

## Idempotency

- accept a submission key for create and retry paths
- deduplicate repeated submissions where the domain allows it
- keep retries safe to replay
- do not assume a queue guarantees exactly-once delivery

## Retry strategy

- retry only transient failures
- use bounded backoff
- keep the attempt ceiling explicit
- record the final failure reason before dead-lettering

## Dead-letter concepts

Move a job to dead-letter state when:

- attempts are exhausted
- the payload is invalid in a non-recoverable way
- the provider or worker error is permanent
- the job requires manual intervention

Dead-lettered jobs should remain observable and auditable.

## Rate limiting

- protect provider calls with worker-side throttling
- keep API requests independent from provider spikes
- surface queue depth when provider saturation is likely

## Timeout strategy

- keep API requests short and bounded
- let worker tasks have their own execution budget
- separate queue wait time from actual execution time
- time out provider calls before they consume the full worker budget

## Human review

Add review checkpoints when a human must approve:

- generated content
- extracted fields with business impact
- sensitive workflows
- release-impacting output

