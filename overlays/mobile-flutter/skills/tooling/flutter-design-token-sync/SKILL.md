# flutter-design-token-sync

## Purpose

Sync design tokens into Flutter theme files and keep app colors, typography, and spacing aligned with the source of truth.

## Use when

- The design system changed and Flutter must follow it
- Tokens live in CSV, JSON, or another structured source
- Theme values are drifting across screens

## Do NOT use when

- You only need a one-off widget color tweak
- There is no design token source of truth
- The request is about runtime behavior, not theme mapping

## Inputs required

- Token source
- Theme target files
- Naming rules
- Any platform-specific token overrides

## Constraints

- Keep the token source explicit
- Avoid hard-coded colors when a token exists
- Keep generated values stable and reviewable
- Do not embed policy text in the generated theme

## Step-by-step workflow

1. Map source tokens to Flutter theme concepts.
2. Identify the target files to update.
3. Generate or update theme constants and `ThemeData`.
4. Cross-check naming and fallback values.
5. Add or update examples showing the new tokens in use.

## Output contract

- Token mapping table
- Updated theme or constants files
- Example usage paths
- Validation checklist

## Validation checklist

- Token names are consistent
- Theme values are not duplicated manually
- The generated output is easy to review
- Example output compiles against the target theme structure

## Related skills

- `flutter-feature-scaffold`
- `flutter-performance-audit`

## References

- [`../../../../templates/state-management-template.md`](../../../../templates/state-management-template.md)
- [`../../../../examples/full-feature-implementation.md`](../../../../examples/full-feature-implementation.md)

## Real example

Map a `brand.primary` token to `ColorScheme.primary` and update `lib/app/theme/app_theme.dart` plus any shared button styles that consume it.

## Real file output sample

```text
lib/app/theme/app_theme.dart
lib/app/theme/app_colors.dart
lib/app/theme/app_text_styles.dart
```
