# Contract Usage

Use `packages/job-contracts` for the shared job envelope, status, retry, error, and result
shapes.

Frontend code submits job payloads.
API code validates and persists the envelope.
Worker code consumes the same contract and returns result updates.
