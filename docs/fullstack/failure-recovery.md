# Failure Recovery

This guide explains how the worker layer should fail closed and recover predictably.

## Failure classes

- validation failure
- auth failure
- queue submission failure
- worker execution failure
- provider failure
- retry exhaustion
- dead-letter state

## Recovery rules

- fail fast on invalid job envelopes
- retry only transient worker and provider failures
- treat repeated auth or policy failures as terminal
- move exhausted jobs into dead-letter state
- make manual replay explicit rather than automatic

## Backoff and replay

- use bounded backoff for retries
- keep replay idempotent
- do not automatically replay jobs that need human review
- preserve the original failure reason when replaying

## Operator workflow

1. inspect the job envelope and terminal error
2. confirm whether the failure is transient or permanent
3. replay only if the job is safe to re-run
4. document the recovery action in the audit trail

## What not to do

- do not swallow worker failures
- do not convert retry exhaustion into success
- do not hide dead-letter jobs from status views
- do not make provider calls in UI routes to avoid queue setup
