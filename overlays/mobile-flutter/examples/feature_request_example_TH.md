# ตัวอย่าง Feature request

## สถานการณ์

ใช้ `mobile-flutter` เพื่อเพิ่มฟีเจอร์ profile ที่มี:

- profile view page
- แก้ display name ได้
- avatar placeholder
- load/save ผ่าน repository
- Riverpod providers
- localization สำหรับทุก string
- widget tests สำหรับหน้า
- unit tests สำหรับ validation logic

## Skill ที่แนะนำ

- `flutter-dev`
- `guide-new-feature-flow`
- `guide-clean-architecture-feature`
- `flutter-state-riverpod`
- `flutter-localization-csv`
- `policy-translation-csv`
- `policy-testing-minimum`
- `policy-no-business-logic-in-widget`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md`
- `overlays/mobile-flutter/skills/guide-clean-architecture-feature/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-state-riverpod/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md`
- `overlays/mobile-flutter/skills/policy-translation-csv/SKILL.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`
- `overlays/mobile-flutter/skills/policy-no-business-logic-in-widget/SKILL.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-dev
- guide-new-feature-flow
- guide-clean-architecture-feature
- flutter-state-riverpod
- flutter-localization-csv
- policy-translation-csv
- policy-testing-minimum
- policy-no-business-logic-in-widget

Reference files:
- overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md
- overlays/mobile-flutter/prompts/new_feature.md
- overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md

Task:
Implement a profile feature with clean boundaries, localization, and tests.

Deliver:
1. feature plan
2. file plan
3. dependency boundaries
4. localization plan
5. implementation notes
6. test plan
```

## Expected output

```text
$ myapp plan feature profile --json
{
  "feature":"profile",
  "layers":["presentation","domain","data"],
  "localization":"assets/i18n/translations.csv",
  "tests":["widget","unit"]
}

$ myapp verify feature profile
PASS repository boundaries are isolated
PASS widget tree has no business logic
PASS localization keys added through CSV
PASS validation logic covered by unit tests
```

## Review notes

- อย่าย้าย business rules ไปไว้ใน widgets
- อย่าทำ repository/use case/UI ให้ปนกัน
- ทำ feature ให้ modular พอสำหรับ reuse

## Verification notes

- ตรวจว่าใช้ workflow skill ที่ถูก
- ตรวจว่า localization ผูกกับ CSV source of truth
- ตรวจว่ามี unit test และ widget test ตาม scope
