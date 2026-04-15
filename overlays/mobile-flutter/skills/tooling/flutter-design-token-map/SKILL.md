# flutter-design-token-map

## Purpose

Map design system tokens to Flutter theme targets without applying unrelated UI changes.

## Use when

- The source design tokens changed
- You need a mapping from tokens to Flutter theme values
- Another skill will apply the concrete theme file updates

## Do NOT use when

- You only need a local widget color tweak
- The task is about state, routing, or release work
- There is no design token source of truth

## Inputs required

- Token source
- Target theme targets
- Naming rules

## Constraints

- Output only the mapping
- Do not rewrite widgets
- Do not add runtime behavior

## Step-by-step workflow

1. Read the token source.
2. Match tokens to Flutter theme targets.
3. Record any gaps or naming conflicts.
4. Return the mapping table and follow-up note.

## Output contract

- Token-to-theme mapping table
- Gap list
- Next-step note for theme application

## Validation checklist

- Every mapped token has a target
- Gaps are explicit
- No widget files changed

## Related skills

- `flutter-feature-contract-scaffold`
- `flutter-performance-audit`

## References

- [`../../../examples/full-feature-implementation.md`](../../../examples/full-feature-implementation.md)

## Real example

`brand.primary` maps to `ColorScheme.primary`.

## Real file output sample

```text
docs/design/token-map.md
lib/app/theme/app_theme_tokens.dart
```
