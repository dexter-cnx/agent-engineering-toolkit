# flutter-feature-folder-scaffold

## Purpose

Create the feature folder tree for a Flutter module with the correct layer boundaries and file locations.

## Use when

- A new feature directory needs to be created
- You need the folder structure before adding code
- You want an output that other skills can build on

## Do NOT use when

- The feature folder already exists and only code changes are needed
- You need contracts, state, or routing code in the same pass
- The task is only an audit

## Inputs required

- Feature name
- Target layer layout
- Whether tests should be seeded now

## Constraints

- Create directories only, not implementation logic
- Keep the folder names feature-specific
- Do not invent route, state, or repository code here

## Step-by-step workflow

1. Create `lib/features/<feature_name>/`.
2. Create `data/`, `domain/`, and `presentation/`.
3. Create nested layer folders needed by the project standard.
4. Seed support files only if the caller requested them.
5. Return the created tree.

## Output contract

- A folder tree for the feature
- A path list of created directories
- A handoff note for follow-up skills

## Validation checklist

- The folder tree matches the feature name
- Layer directories exist
- No business logic was added
- No unrelated files were changed

## Related skills

- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-go-router-route-map`

## References

- [`../../../templates/feature-module-template.md`](../../../templates/feature-module-template.md)
- [`../../../examples/full-feature-implementation.md`](../../../examples/full-feature-implementation.md)

## Real example

For a `profile` feature, create:

```text
lib/features/profile/data/
lib/features/profile/domain/
lib/features/profile/presentation/
```

## Real file output sample

```text
lib/features/profile/data/
lib/features/profile/domain/
lib/features/profile/presentation/
```
