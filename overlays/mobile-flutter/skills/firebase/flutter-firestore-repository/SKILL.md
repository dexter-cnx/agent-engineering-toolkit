# flutter-firestore-repository

## Purpose

Build a Firestore-backed repository with explicit DTO mapping, query boundaries, and clean domain output.

## Use when

- A feature needs document or collection persistence
- You need query logic isolated from UI and domain
- The feature needs mapping between Firestore data and domain entities

## Do NOT use when

- The feature only needs in-memory state
- There is no Firestore dependency in the project
- You want to return `Map<String, dynamic>` directly to the presentation layer

## Inputs required

- Collection path
- Entity shape
- Query and pagination rules
- Offline or cache expectations

## Constraints

- Keep Firestore SDK calls in the data layer
- Map raw documents into typed DTOs before domain use
- Keep query rules explicit and documented
- Handle null and missing-field cases deliberately

## Step-by-step workflow

1. Define the repository contract in the domain layer.
2. Define DTOs and mappers in the data layer.
3. Implement Firestore queries in the datasource or repository adapter.
4. Convert raw documents into typed domain entities.
5. Add tests for mapping and query edge cases.
6. Document collection paths and indexing assumptions.

## Output contract

- Domain repository contract
- DTO and mapper files
- Firestore repository implementation
- Query or mapping tests

## Validation checklist

- Firestore documents are never exposed raw to UI
- Missing fields are handled safely
- Query scope is narrow and documented
- Mapper tests cover schema drift

## Related skills

- `flutter-firebase-auth-flow`
- `flutter-riverpod-feature-state`
- `flutter-clean-architecture-audit`

## References

- [`../../../../templates/repository-template.md`](../../../../templates/repository-template.md)
- [`../../../../examples/firebase-integration-example.md`](../../../../examples/firebase-integration-example.md)

## Real example

`profiles` collection documents map to a `Profile` entity via `ProfileDto.fromJson` and never leak `DocumentSnapshot` objects into presentation.

## Real file output sample

```text
lib/features/profile/data/datasources/profile_firestore_data_source.dart
lib/features/profile/data/repositories/profile_repository_impl.dart
lib/features/profile/data/dtos/profile_dto.dart
```
