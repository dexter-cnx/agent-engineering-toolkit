# ตัวอย่าง Web loading และ deployment

## สถานการณ์

แอป Flutter ตัวนี้ต้อง ship สำหรับ web ด้วย และต้องมี loading/deployment rules

ตัวอย่างการเปลี่ยนแปลง:

- loading shell ตอน startup
- web bootstrap behavior
- deployment checklist สำหรับ QA หรือ staging

## Skill ที่แนะนำ

- `guide-flutter-web-loading`
- `flutter-web-deployment`
- `flutter-dev`
- `guide-app-release-checklist`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/guide-flutter-web-loading/SKILL.md`
- `overlays/mobile-flutter/prompts/apply_flutter_web_loading.md`
- `overlays/mobile-flutter/prompts/prepare_flutter_web_release.md`
- `overlays/mobile-flutter/prompts/patch_existing_flutter_project_with_web_loader.md`
- `overlays/mobile-flutter/templates/flutter_web_loading_checklist.md`
- `overlays/mobile-flutter/templates/flutter_web_deployment_checklist.md`
- `overlays/mobile-flutter/skills/guide-app-release-checklist/SKILL.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- guide-flutter-web-loading
- flutter-web-deployment
- flutter-dev

Reference files:
- overlays/mobile-flutter/skills/guide-flutter-web-loading/SKILL.md
- overlays/mobile-flutter/prompts/apply_flutter_web_loading.md
- overlays/mobile-flutter/templates/flutter_web_loading_checklist.md

Task:
Prepare the app for web startup/loading and deployment validation.

Deliver:
1. loading strategy
2. deployment notes
3. files to check
4. release risks
```

## สิ่งที่ควรได้

- loading state ตั้งใจไว้ชัด และสั้น
- web bootstrap behavior ถูกอธิบาย
- deployment checks ชัดเจน
- release risks ถูกบอกก่อนปล่อย

## Review notes

- keep web startup rules separate from feature logic
- อย่าใส่ loading behavior แบบ ad hoc ใน leaf widgets
- document caveats ที่เฉพาะ web ให้ชัด

## Verification notes

- ตรวจว่า checklist สำหรับ loading ถูกอ้างถึง
- ตรวจว่า deployment steps ถูกเขียนไว้
- ตรวจว่า behavior เฉพาะ web แยกจาก feature logic
