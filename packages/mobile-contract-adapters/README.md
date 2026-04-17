# Mobile Contract Adapters

This package documents how shared backend contracts map into Flutter and Dart models.

## Purpose

- keep mobile code aligned with the shared schema-first contract layer
- show the mapping shape for session, error, pagination, and post payloads
- give mobile teams a safe reference when they consume the same API as web clients

## Naming guidance

- keep adapter names close to the shared contract names
- prefer `Dto` or `ApiModel` for transport shapes
- prefer domain names for UI-facing models
- keep the adapter layer separate from widgets and repositories

## Mapping guidance

- map JSON to transport DTOs first
- map DTOs to UI/domain models second
- keep envelope parsing in the adapter layer
- keep formatting and display logic out of the mapping layer

## Error envelope mapping

- surface `code`, `message`, and `field` in a structured error object
- keep error codes machine-readable
- convert unknown payloads to a generic network failure
- treat auth failures as a sign-out trigger when appropriate

## Pagination mapping

- map `items` and `pagination` together
- keep page metadata explicit in the mobile model
- do not infer pagination behavior from list length alone

## Auth/session mapping

- map the session envelope into a storage-friendly session model
- keep access and refresh tokens grouped together
- store the session through a secure-storage adapter
- expose a clear invalidation path for sign-out and auth expiry

## Breaking-change handling

- treat removed fields or renamed fields as breaking changes
- prefer additive contract evolution
- keep the adapter layer version-aware when the backend contract version changes
- do not silently coerce incompatible payloads

## Examples

- `examples/naming.md`
- `examples/error-envelope-mapping.md`
- `examples/pagination-mapping.md`
- `examples/auth-session-mapping.md`
- `examples/post-mapping.md`

## Read next

- `docs/fullstack/mobile-backend-integration.md`
- `docs/fullstack/auth-cross-platform.md`
- `apps/flutter-api-client-reference/README.md`
