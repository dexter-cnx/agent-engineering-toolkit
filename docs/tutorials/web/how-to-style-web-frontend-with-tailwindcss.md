---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - tailwindcss
  - design-tokens
  - flutter
aliases:
  - Tailwind CSS Design Token Flutter Bridge
  - Web Frontend Styling and Token Bridge
---

# How to Style Web Frontend with Tailwind CSS + Design Tokens + Flutter Design System Bridge

Use this tutorial when you want a web frontend that stays visually consistent with a Flutter app, or when you want both platforms to derive UI decisions from a shared token source.

## Purpose

This tutorial standardizes three connected concerns:

1. Tailwind CSS as the default styling layer for web frontend projects.
2. Design tokens as the canonical source of visual rules.
3. A Flutter bridge so web and Flutter can share the same semantic design decisions.

Use this when your team wants:
- faster UI implementation
- stronger design consistency
- less drift between web and Flutter
- a path from design file to production code

## Architecture Role

```text
Design Source
  -> Design Tokens
    -> Web Mapping
      -> Tailwind Theme / Utility Usage
    -> Flutter Mapping
      -> ThemeData / Extensions / Semantic Tokens
```

The critical rule is:

- design tokens define visual meaning
- Tailwind consumes tokens on web
- Flutter consumes the same semantics in app code
- feature code must not invent ad-hoc styling rules without updating the token contract

## When to Use

Use this tutorial when:
- the project has both web and Flutter surfaces
- the design system should be shared across platforms
- the team wants repeatable theming rules
- the team wants AI agents to follow one styling contract

## What to Read First

- [Start from a Blank Folder](../00-common-start.md)
- [AGENTS.md and prompt guide](../agents-and-prompts.md)
- [How to Make Web Frontend](./how-to-make-web-frontend.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)

## Core Principles

### 1. Tokens are semantic first

Prefer semantic tokens over raw values.

Bad:
```json
{ "blue500": "#2563eb" }
```

Better:
```json
{
  "color": {
    "action": {
      "primary": "#2563eb"
    }
  }
}
```

### 2. Tailwind stays presentational

Tailwind is the implementation layer for web UI, not the source of truth for design decisions.

### 3. Flutter consumes the same semantics

Flutter should map the same token meaning into:
- `ColorScheme`
- `ThemeData`
- `ThemeExtension`
- spacing, radius, elevation, typography wrappers

### 4. Shared meaning, platform-specific implementation

The semantic layer should match across platforms, while the implementation details may differ.

Example:
- `color.action.primary` may map to Tailwind utilities on web
- the same token may map to `AppColors.actionPrimary` in Flutter

### 5. Component APIs should speak semantics

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

docs/
  tutorials/
    web/
      how-to-style-web-frontend-with-tailwindcss.md
      how-to-style-web-frontend-with-tailwindcss_EN.md
      how-to-style-web-frontend-with-tailwindcss_TH.md

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

## Token Categories to Standardize

Start with these categories:

- color
- spacing
- radius
- typography
- shadow or elevation
- breakpoints
- motion
- z-index if needed

Do not start with dozens of token groups. Make the contract small and durable first.

## Suggested Token Shape

```json
{
  "color": {
    "surface": {
      "base": "#ffffff",
      "muted": "#f8fafc",
      "inverse": "#0f172a"
    },
    "text": {
      "primary": "#0f172a",
      "secondary": "#475569",
      "inverse": "#ffffff"
    },
    "action": {
      "primary": "#2563eb",
      "primaryHover": "#1d4ed8",
      "danger": "#dc2626"
    },
    "border": {
      "default": "#e2e8f0",
      "strong": "#94a3b8"
    }
  },
  "spacing": {
    "xs": 4,
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24
  },
  "radius": {
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24
  }
}
```

## Web Mapping Strategy

Map semantic tokens into Tailwind through one controlled layer.

### Example `tailwind.config.ts`

```ts
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./pages/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        surface: {
          base: "var(--color-surface-base)",
          muted: "var(--color-surface-muted)",
          inverse: "var(--color-surface-inverse)",
        },
        text: {
          primary: "var(--color-text-primary)",
          secondary: "var(--color-text-secondary)",
          inverse: "var(--color-text-inverse)",
        },
        action: {
          primary: "var(--color-action-primary)",
          "primary-hover": "var(--color-action-primary-hover)",
          danger: "var(--color-action-danger)",
        },
        border: {
          DEFAULT: "var(--color-border-default)",
          strong: "var(--color-border-strong)",
        },
      },
      spacing: {
        xs: "var(--space-xs)",
        sm: "var(--space-sm)",
        md: "var(--space-md)",
        lg: "var(--space-lg)",
        xl: "var(--space-xl)",
      },
      borderRadius: {
        sm: "var(--radius-sm)",
        md: "var(--radius-md)",
        lg: "var(--radius-lg)",
        xl: "var(--radius-xl)",
      },
    },
  },
  plugins: [],
};

export default config;
```

### Example `src/styles/globals.css`

```css
:root {
  --color-surface-base: #ffffff;
  --color-surface-muted: #f8fafc;
  --color-surface-inverse: #0f172a;

  --color-text-primary: #0f172a;
  --color-text-secondary: #475569;
  --color-text-inverse: #ffffff;

  --color-action-primary: #2563eb;
  --color-action-primary-hover: #1d4ed8;
  --color-action-danger: #dc2626;

  --color-border-default: #e2e8f0;
  --color-border-strong: #94a3b8;

  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 12px;
  --space-lg: 16px;
  --space-xl: 24px;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;
}
```

## Flutter Mapping Strategy

Create a stable semantic layer in Flutter.

### Example `app_colors.dart`

```dart
import 'package:flutter/material.dart';

abstract final class AppColors {
  static const surfaceBase = Color(0xFFFFFFFF);
  static const surfaceMuted = Color(0xFFF8FAFC);
  static const surfaceInverse = Color(0xFF0F172A);

  static const textPrimary = Color(0xFF0F172A);
  static const textSecondary = Color(0xFF475569);
  static const textInverse = Color(0xFFFFFFFF);

  static const actionPrimary = Color(0xFF2563EB);
  static const actionPrimaryHover = Color(0xFF1D4ED8);
  static const actionDanger = Color(0xFFDC2626);

  static const borderDefault = Color(0xFFE2E8F0);
  static const borderStrong = Color(0xFF94A3B8);
}
```

### Example `app_spacing.dart`

```dart
abstract final class AppSpacing {
  static const double xs = 4;
  static const double sm = 8;
  static const double md = 12;
  static const double lg = 16;
  static const double xl = 24;
}
```

### Example `app_radius.dart`

```dart
abstract final class AppRadius {
  static const double sm = 8;
  static const double md = 12;
  static const double lg = 16;
  static const double xl = 24;
}
```

### Example `app_theme.dart`

```dart
import 'package:flutter/material.dart';
import 'app_colors.dart';

ThemeData buildAppTheme() {
  const scheme = ColorScheme(
    brightness: Brightness.light,
    primary: AppColors.actionPrimary,
    onPrimary: AppColors.textInverse,
    secondary: AppColors.surfaceMuted,
    onSecondary: AppColors.textPrimary,
    error: AppColors.actionDanger,
    onError: AppColors.textInverse,
    surface: AppColors.surfaceBase,
    onSurface: AppColors.textPrimary,
  );

  return ThemeData(
    colorScheme: scheme,
    scaffoldBackgroundColor: AppColors.surfaceBase,
    useMaterial3: true,
  );
}
```

## Cross-Platform Naming Contract

Keep naming aligned across web and Flutter.

| Semantic meaning | Web token / class intent | Flutter symbol |
| --- | --- | --- |
| Primary action | `color.action.primary` | `AppColors.actionPrimary` |
| Base surface | `color.surface.base` | `AppColors.surfaceBase` |
| Primary text | `color.text.primary` | `AppColors.textPrimary` |
| Medium radius | `radius.md` | `AppRadius.md` |
| Large spacing | `spacing.lg` | `AppSpacing.lg` |

## Recommended Component Strategy

### Web
- use Tailwind utilities for page assembly
- extract repeated UI into `components/ui`
- use `clsx`, `tailwind-merge`, or `class-variance-authority` for variants

### Flutter
- expose semantic UI widgets only where repeated
- avoid hard-coding colors in feature widgets
- prefer theme-based access over raw values in leaf widgets

## Example Web Button

```tsx
type ButtonProps = {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "danger";
};

export function Button({ children, variant = "primary" }: ButtonProps) {
  const base =
    "inline-flex items-center justify-center rounded-lg px-lg py-sm text-sm font-medium transition";
  const styles =
    variant === "primary"
      ? "bg-action-primary text-text-inverse hover:bg-action-primary-hover"
      : variant === "danger"
        ? "bg-action-danger text-text-inverse"
        : "bg-surface-muted text-text-primary border border-border";

  return <button className={`${base} ${styles}`}>{children}</button>;
}
```

## Example Flutter Button Wrapper

```dart
import 'package:flutter/material.dart';
import '../theme/app_colors.dart';
import '../theme/app_radius.dart';
import '../theme/app_spacing.dart';

class AppPrimaryButton extends StatelessWidget {
  final String label;
  final VoidCallback? onPressed;

  const AppPrimaryButton({
    super.key,
    required this.label,
    this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.actionPrimary,
        foregroundColor: AppColors.textInverse,
        padding: const EdgeInsets.symmetric(
          horizontal: AppSpacing.lg,
          vertical: AppSpacing.sm,
        ),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppRadius.lg),
        ),
      ),
      onPressed: onPressed,
      child: Text(label),
    );
  }
}
```

## Workflow for Teams and Agents

1. Decide the semantic token contract first.
2. Create or update `design/tokens/semantic.json`.
3. Map tokens to web CSS variables and Tailwind theme extensions.
4. Map the same semantics to Flutter theme files.
5. Build a small set of shared primitives.
6. Add verification rules so ad-hoc styling gets caught in review.

## Suggested AGENTS.md Rules

```md
## Tailwind and Token Rules

- Tailwind CSS is the default styling system for web frontend.
- Design tokens are the source of truth for visual semantics.
- Web and Flutter must use the same semantic token names where practical.
- Repeated utility patterns must be extracted into reusable UI primitives.
- Feature code must not invent new visual semantics without updating the token contract.
- Hard-coded visual values require justification.
```

## Verification Checklist

- semantic token names are stable
- Tailwind maps to token-backed CSS variables
- Flutter maps to the same semantic meanings
- repeated styling is extracted
- no feature-specific styling leaks into base primitives
- light and dark theme rules are explicit if the project supports them
- lint, test, and build pass

## Common Pitfalls

- treating Tailwind config as the source of truth
- mapping raw colors directly into feature widgets
- letting web and Flutter drift into different semantic names
- introducing arbitrary values everywhere
- putting data fetching or business logic into UI primitives

## Related

- [How to Make Web Frontend](./how-to-make-web-frontend.md)
- [How to integrate DESIGN.md with Web Frontend](./how-to-integrate-design-md-to-existing-project-and-new-project-in-web-frontend.md)
