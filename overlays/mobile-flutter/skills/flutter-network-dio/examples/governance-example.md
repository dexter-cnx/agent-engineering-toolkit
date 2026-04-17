# flutter-network-dio Governance Example

## Example scenario

An app needs a single HTTP boundary with Dio interceptors, typed response mapping, retry
behavior, and clear error handling.

## Example outcome

The skill keeps transport concerns behind the Dio boundary, avoids widget leakage, and
records the verification path before any promotion run.
