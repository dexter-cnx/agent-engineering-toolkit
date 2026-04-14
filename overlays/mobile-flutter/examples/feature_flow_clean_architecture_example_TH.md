# ตัวอย่างฟีเจอร์แบบ Clean Architecture

## สถานการณ์

แอปต้องเพิ่มฟีเจอร์ใหม่โดยยังคง layered และทดสอบได้

ตัวอย่างฟีเจอร์:

- profile page
- แก้ display name ได้
- save ผ่าน repository
- ใช้ Riverpod providers
- widget tests
- unit tests สำหรับ validation

## Skill ที่แนะนำ

- `flutter-dev`
- `guide-new-feature-flow`
- `guide-clean-architecture-feature`
- `flutter-state-riverpod`
- `policy-no-business-logic-in-widget`
- `policy-testing-minimum`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md`
- `overlays/mobile-flutter/skills/guide-clean-architecture-feature/SKILL.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/flutter-state-riverpod/SKILL.md`
- `overlays/mobile-flutter/skills/policy-no-business-logic-in-widget/SKILL.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-dev
- guide-new-feature-flow
- guide-clean-architecture-feature
- flutter-state-riverpod
- policy-no-business-logic-in-widget
- policy-testing-minimum

Reference files:
- overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md
- overlays/mobile-flutter/prompts/new_feature.md
- overlays/mobile-flutter/templates/feature-module-template.md

Task:
Implement a profile feature with clean boundaries and tests.

Deliver:
1. feature plan
2. file plan
3. dependency boundaries
4. implementation notes
5. test plan
```

## Expected output

- domain, data, presentation แยกกันชัด
- widget code ไม่มี repository/validation logic
- provider wiring เล็กและมองเห็นได้
- tests ครอบคลุม behavior ที่สำคัญ

## Review notes

- อย่าย้าย business rules ไปไว้ใน widgets
- อย่าทำ repository/use case/UI ให้ปนกัน
- ทำ feature ให้ modular พอสำหรับ reuse

## Verification notes

- ตรวจว่าใช้ workflow skill ที่ถูก
- ตรวจว่ามีการอ้างถึง feature template
- ตรวจว่ามี unit test และ widget test ตาม scope
