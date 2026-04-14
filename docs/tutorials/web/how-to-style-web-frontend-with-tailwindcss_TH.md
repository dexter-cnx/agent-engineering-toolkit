---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - tailwindcss
  - design-tokens
  - flutter
aliases:
  - วิธีใช้ Tailwind CSS Design Token Flutter Bridge
  - Web Frontend Styling Bridge ภาษาไทย
---

# วิธีใช้ Tailwind CSS + Design Tokens + Flutter Design System Bridge

ใช้ tutorial นี้เมื่อคุณต้องการให้ web frontend กับ Flutter app ใช้ภาษาดีไซน์เดียวกัน และลดอาการ design drift ระหว่างสองฝั่ง

## เป้าหมาย

tutorial นี้คุม 3 เรื่องพร้อมกัน:

1. ใช้ Tailwind CSS เป็น styling layer หลักของฝั่งเว็บ
2. ใช้ design tokens เป็น source of truth ของ visual semantics
3. ทำ Flutter bridge เพื่อให้ app ใช้ semantic เดียวกับเว็บ

เหมาะเมื่อทีมต้องการ:
- ทำ UI เร็ว
- คุมหน้าตาให้สม่ำเสมอ
- แชร์ design language ระหว่าง web กับ Flutter
- ให้คนและ AI agents อ่านกติกาชุดเดียวกัน

## บทบาทในสถาปัตยกรรม

```text
Design Source
  -> Design Tokens
    -> Web Mapping
      -> Tailwind Theme / Utility Usage
    -> Flutter Mapping
      -> ThemeData / Extensions / Semantic Tokens
```

กติกาหลักคือ:
- token เป็นคนบอกความหมาย
- Tailwind เป็นคนเอา token ไปใช้ใน web
- Flutter เป็นคนเอาความหมายเดียวกันไปใช้ใน app
- feature code ห้าม invent visual semantics ใหม่แบบเงียบ ๆ

## ใช้เมื่อไร

- มีทั้ง web frontend และ Flutter app
- ต้องการ design system ที่ sync กัน
- ต้องการ theme rules ที่ขยายต่อได้
- ต้องการให้ agent ทำงานตาม contract เดียวกัน

## สิ่งที่ควรอ่านก่อน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [วิธีทำ web-frontend](./how-to-make-web-frontend.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)

## หลักการสำคัญ

### 1. token ต้องเป็น semantic ก่อน

ไม่ดี:
```json
{ "blue500": "#2563eb" }
```

ดีกว่า:
```json
{
  "color": {
    "action": {
      "primary": "#2563eb"
    }
  }
}
```

### 2. Tailwind เป็น presentation layer

Tailwind ไม่ใช่ source of truth ของดีไซน์ แต่เป็น implementation layer ของฝั่งเว็บ

### 3. Flutter ต้องใช้ semantic เดียวกัน

ฝั่ง Flutter ควร map ความหมายเดียวกันเข้า:
- `ColorScheme`
- `ThemeData`
- `ThemeExtension`
- spacing, radius, elevation, typography wrappers

### 4. ความหมายร่วมกัน แต่ implementation แยกได้

semantic layer ต้องตรงกัน แต่ implementation ราย platform ต่างกันได้

ตัวอย่าง:
- `color.action.primary` map เป็น utility classes ฝั่งเว็บ
- semantic เดียวกัน map เป็น `AppColors.actionPrimary` ใน Flutter

### 5. API ของ component ต้องพูดด้วย semantics

ควรใช้:
- `variant="primary"`
- `tone="danger"`
- `size="sm"`

ไม่ควรใช้:
- `isBlue`
- `useRounded14`
- `paddingValue=13`

## โครงสร้าง repo ที่แนะนำ

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

## หมวด token ที่ควรเริ่มก่อน

เริ่มจาก:
- color
- spacing
- radius
- typography
- shadow หรือ elevation
- breakpoints
- motion
- z-index ถ้าจำเป็น

อย่าเริ่มด้วย token จำนวนมากเกินไป ให้เริ่มจาก contract ที่เล็กแต่ทนก่อน

## ตัวอย่าง token shape

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

## แนวทาง map ฝั่งเว็บ

ให้ map semantic tokens ผ่านชั้นกลางที่ควบคุมได้

### ตัวอย่าง `tailwind.config.ts`

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

### ตัวอย่าง `src/styles/globals.css`

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

## แนวทาง map ฝั่ง Flutter

ทำ semantic layer ให้ชัดและเสถียร

### ตัวอย่าง `app_colors.dart`

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

### ตัวอย่าง `app_spacing.dart`

```dart
abstract final class AppSpacing {
  static const double xs = 4;
  static const double sm = 8;
  static const double md = 12;
  static const double lg = 16;
  static const double xl = 24;
}
```

### ตัวอย่าง `app_radius.dart`

```dart
abstract final class AppRadius {
  static const double sm = 8;
  static const double md = 12;
  static const double lg = 16;
  static const double xl = 24;
}
```

### ตัวอย่าง `app_theme.dart`

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

## contract การตั้งชื่อข้าม platform

| ความหมาย | web token / class intent | Flutter symbol |
| --- | --- | --- |
| Primary action | `color.action.primary` | `AppColors.actionPrimary` |
| Base surface | `color.surface.base` | `AppColors.surfaceBase` |
| Primary text | `color.text.primary` | `AppColors.textPrimary` |
| Medium radius | `radius.md` | `AppRadius.md` |
| Large spacing | `spacing.lg` | `AppSpacing.lg` |

## กลยุทธ์ component

### ฝั่งเว็บ
- ใช้ Tailwind utility ตอนประกอบหน้า
- ถ้าซ้ำบ่อยให้ extract ไป `components/ui`
- ใช้ `clsx`, `tailwind-merge`, หรือ `class-variance-authority` สำหรับ variants

### ฝั่ง Flutter
- expose semantic UI widgets เฉพาะที่ใช้ซ้ำ
- อย่า hard-code color ใน feature widgets
- leaf widget ควรอิง theme มากกว่า raw values

## ตัวอย่าง Web Button

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

## ตัวอย่าง Flutter Button Wrapper

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

## workflow สำหรับทีมและ agent

1. ตกลง semantic token contract ก่อน
2. สร้างหรืออัปเดต `design/tokens/semantic.json`
3. map token ไป web CSS variables และ Tailwind theme
4. map semantics ชุดเดียวกันไป Flutter theme files
5. สร้าง shared primitives ชุดเล็กก่อน
6. เพิ่ม verify rules เพื่อกัน ad-hoc styling

## ตัวอย่าง rule สำหรับ `AGENTS.md`

```md
## Tailwind and Token Rules

- Tailwind CSS is the default styling system for web frontend.
- Design tokens are the source of truth for visual semantics.
- Web and Flutter must use the same semantic token names where practical.
- Repeated utility patterns must be extracted into reusable UI primitives.
- Feature code must not invent new visual semantics without updating the token contract.
- Hard-coded visual values require justification.
```

## Checklist

- semantic token names เสถียร
- Tailwind map ไป token-backed CSS variables
- Flutter map ไป semantic เดียวกัน
- style ที่ซ้ำถูก extract แล้ว
- base primitives ไม่มี feature-specific styling leak
- ถ้ารองรับ light/dark ต้องกำหนด explicit
- lint, test, build ผ่าน

## pitfall ที่พบบ่อย

- ใช้ Tailwind config เป็น source of truth แทน token
- map สีดิบลง feature widgets โดยตรง
- web กับ Flutter ใช้ semantic คนละชื่อ
- ใส่ arbitrary values เยอะเกิน
- เอา data fetching หรือ business logic ไปไว้ใน UI primitive

## อ่านต่อ

- [วิธีทำ web-frontend](./how-to-make-web-frontend.md)
- [วิธี integrate `DESIGN.md` กับ Web Frontend](./how-to-integrate-design-md-to-existing-project-and-new-project-in-web-frontend.md)
