# Feature Module Template

Use this as the default shape for a new feature.

```text
lib/features/<feature_name>/
  data/
    datasources/
    dtos/
    mappers/
    repositories/
  domain/
    entities/
    repositories/
    usecases/
  presentation/
    controllers/
    providers/
    pages/
    widgets/
```

## Minimum files to consider
- one page or screen
- one state holder (Riverpod provider / GetX controller)
- one domain use case
- one repository contract
- one repository implementation
- one mapper if network or storage models differ from domain entities
- one widget test for the page
- one unit test for non-trivial domain logic
- localization keys for all user-facing text

## Notes
- Put orchestration in controllers/providers/use cases, not widgets.
- Keep DTOs out of the presentation layer.
- Prefer typed models over `Map<String, dynamic>` crossing layers.
