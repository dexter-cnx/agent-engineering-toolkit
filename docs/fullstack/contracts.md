# Full Stack Contracts

The contract package is the shared schema layer for the canonical starters.

## Why schema-first

- both frontend and backend can validate the same payload shape
- contract changes are visible before implementation changes
- runtime errors are reduced because the envelope and payload shape are explicit
- future OpenAPI or client generation can build from the same source of truth

## Package purpose

`packages/contracts` defines the canonical shapes for:

- auth login, register, and session payloads
- post create, update, and list payloads
- success envelopes
- error envelopes
- pagination metadata

`packages/fullstack-client` wraps these schemas with fetch, auth, and parsing helpers for
the starter apps and future consumers.

## Versioning strategy

- Follow semver at the package level.
- Increment patch for fixes that do not change shape.
- Increment minor for additive, non-breaking fields.
- Increment major for any breaking shape change.

## Breaking vs non-breaking changes

Non-breaking:

- adding optional fields
- adding new envelope metadata
- adding new request or response types

Breaking:

- removing a required field
- changing a field type
- renaming a field in a shipped contract
- changing the envelope shape

## Codegen readiness

The package already uses Zod schemas, which makes it suitable for later OpenAPI generation,
TypeScript inference, and backend DTO mapping.

Keep schema names stable and avoid ad hoc envelope shapes in implementation code.

## Frontend consumption pattern

Frontend code should:

1. import the schema and inferred type from `packages/contracts`
2. use `packages/fullstack-client` for fetch, auth, and parsing helpers
3. validate request payloads before sending
4. validate response payloads after receiving
5. keep UI code free of raw transport shapes

## Backend mapping pattern

Backend code should:

1. map domain entities into the contract shapes
2. validate incoming payloads against the same business rules
3. return the canonical success or error envelope
4. keep transport DTOs small and explicit

## Error envelope standard

The standard error envelope carries:

- `success: false`
- a stable `code`
- a short `message`
- an optional `field`
- optional structured `details`

Do not return plain strings for machine-handled failures.

## Pagination standard

The standard pagination response contains:

- `items`
- `page`
- `pageSize`
- `total`
- `totalPages`
- `hasNextPage`
- `hasPreviousPage`

Use one pagination shape everywhere so list endpoints stay predictable across compositions.
