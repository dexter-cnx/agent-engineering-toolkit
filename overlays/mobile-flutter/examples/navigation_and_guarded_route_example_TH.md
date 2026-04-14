# ตัวอย่าง Navigation และ guarded routes

## สถานการณ์

แอปต้องมี auth-aware navigation และ guarded routes

ตัวอย่างการเปลี่ยนแปลง:

- login gate
- dashboard ที่ protected
- flow ที่รองรับ deep link
- redirect หลัง sign-in

## Skill ที่แนะนำ

- `flutter-auth`
- `flutter-navigation-go-router`
- `flutter-dev`
- `guide-clean-architecture-feature`
- `policy-no-business-logic-in-widget`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/flutter-navigation-go-router/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-auth/SKILL.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/policy-no-business-logic-in-widget/SKILL.md`
- `overlays/mobile-flutter/skills/policy-folder-structure/SKILL.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-auth
- flutter-navigation-go-router
- flutter-dev

Reference files:
- overlays/mobile-flutter/skills/flutter-navigation-go-router/SKILL.md
- overlays/mobile-flutter/prompts/add_auth_feature.md
- overlays/mobile-flutter/prompts/new_feature.md

Task:
Add an auth-gated dashboard route with redirect handling and route registry
updates.

Deliver:
1. route plan
2. auth boundary plan
3. files to update
4. verification checklist
```

## Expected output

- route guards อยู่ข้างนอก widgets
- auth state อยู่ใน layer ที่มั่นคง
- redirects deterministic และ testable
- navigation rules inspect ได้ง่าย

## Review notes

- อย่า parse auth state ใน presentation widgets
- อย่าปน route registration กับ feature UI
- keep redirect rules small and explicit

## Verification notes

- ตรวจว่า route guards ไม่ได้อยู่ใน widget
- ตรวจว่า auth state ถูกเก็บใน layer ที่เหมาะสม
- ตรวจว่า redirect logic มี test
