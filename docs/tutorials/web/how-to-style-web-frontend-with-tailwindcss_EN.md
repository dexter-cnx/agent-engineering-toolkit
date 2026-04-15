---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - tailwindcss
  - design-tokens
  - flutter
aliases:
  - Tailwind CSS Design Token Flutter Bridge EN
  - Web Frontend Styling Bridge EN
---

# How to Use Tailwind CSS + Design Tokens + Flutter Design System Bridge

Use this tutorial when you want web frontend and Flutter app surfaces to share one design language and one semantic contract.

## Goal

This tutorial aligns three layers:

1. Tailwind CSS as the default styling layer on web.
2. Design tokens as the visual source of truth.
3. A Flutter bridge so mobile uses the same semantic meanings.

It is a good fit when your team wants:
- fast UI delivery
- consistent visual behavior
- less drift between web and Flutter
- one contract for humans and agents

## Architecture Role

```text
Design Source
  -> Design Tokens
    -> Web Mapping
      -> Tailwind Theme / Utility Usage
    -> Flutter Mapping
      -> ThemeData / Extensions / Semantic Tokens
```

## Core Rules

- tokens define meaning
- Tailwind consumes token-backed values on web
- Flutter consumes the same semantics in app code
- feature code must not invent new visual semantics silently

## When to Use

- the project has both web and Flutter surfaces
- the team wants a shared design system
- the team wants durable theming rules
- the team wants agents to work from one contract

## What to Read First

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [How to Make Web Frontend](./how-to-make-web-frontend_EN.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)

## Best Practices

### Use semantic tokens first

Prefer:
```json
{
  "color": {
    "action": {
      "primary": "#2563eb"
    }
  }
}
```

Avoid:
```json
{ "blue500": "#2563eb" }
```

### Keep Tailwind presentational

Tailwind is not the source of truth for design intent.

### Keep Flutter aligned semantically

Flutter should map the same meaning into:
- `ColorScheme`
- `ThemeData`
- `ThemeExtension`
- spacing, radius, elevation, typography wrappers

### Keep component APIs semantic

Prefer:
- `variant="primary"`
- `tone="danger"`
- `size="sm"`

Avoid:
- `isBlue`
- `useRounded14`
- `paddingValue=13`

## Recommended Repository Shape

```text
design/
  tokens/
    core.json
    semantic.json
    light.json
    dark.json

src/
  components/
    ui/
  features/
  styles/
    globals.css
  lib/
    cn.ts

flutter_app/
  lib/
    theme/
      app_colors.dart
      app_spacing.dart
      app_radius.dart
      app_typography.dart
      app_theme.dart
      theme_extensions.dart
```

## Suggested Token Scope

Start with:
- color
- spacing
- radius
- typography
- shadow or elevation
- breakpoints
- motion
- z-index if needed

## Example Web Mapping

Use CSS variables and Tailwind theme extension for controlled mapping.

```ts
colors: {
  surface: {
    base: "var(--color-surface-base)",
  },
  action: {
    primary: "var(--color-action-primary)",
  },
}
```

## Example Flutter Mapping

```dart
abstract final class AppColors {
  static const actionPrimary = Color(0xFF2563EB);
}
```

## Cross-Platform Naming Contract

| Semantic meaning | Web token intent | Flutter symbol |
| --- | --- | --- |
| Primary action | `color.action.primary` | `AppColors.actionPrimary` |
| Base surface | `color.surface.base` | `AppColors.surfaceBase` |
| Primary text | `color.text.primary` | `AppColors.textPrimary` |
| Medium radius | `radius.md` | `AppRadius.md` |
| Large spacing | `spacing.lg` | `AppSpacing.lg` |

## Agent Rule Snippet

```md
## Tailwind and Token Rules

- Tailwind CSS is the default styling system for web frontend.
- Design tokens are the source of truth for visual semantics.
- Web and Flutter should share semantic token names where practical.
- Repeated utility patterns must be extracted into reusable UI primitives.
- Hard-coded visual values require justification.
```

## Verification Checklist

- semantic token names are stable
- Tailwind maps to token-backed values
- Flutter maps to the same semantics
- repeated styling is extracted
- no feature-specific styling leaks into base primitives
- light and dark theme rules are explicit if supported
- lint, test, and build pass
