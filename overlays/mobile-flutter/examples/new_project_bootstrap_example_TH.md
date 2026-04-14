# ตัวอย่างเริ่มโปรเจกต์ใหม่

## สถานการณ์

ทีมต้องเริ่ม Flutter app ใหม่ด้วย default ที่พร้อมใช้งานจริง:

- Flutter stable และ Dart 3
- Material 3
- Clean Architecture
- Riverpod
- `go_router`
- `dio`
- localization แบบ CSV

## Skill ที่แนะนำ

- `flutter-dev`
- `guide-new-flutter-project-bootstrap`
- `guide-clean-architecture-feature`
- `policy-folder-structure`
- `policy-testing-minimum`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/guide-new-flutter-project-bootstrap/SKILL.md`
- `overlays/mobile-flutter/prompts/new_project.md`
- `overlays/mobile-flutter/skills/policy-folder-structure/SKILL.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-dev
- guide-new-flutter-project-bootstrap
- policy-folder-structure
- policy-testing-minimum

Reference files:
- overlays/mobile-flutter/skills/guide-new-flutter-project-bootstrap/SKILL.md
- overlays/mobile-flutter/prompts/new_project.md
- overlays/mobile-flutter/templates/project-bootstrap-template.md

Task:
Bootstrap a new mobile Flutter app with a clear folder structure, router
scaffold, localization baseline, and first-pass tests.

Deliver:
1. project structure
2. bootstrap notes
3. boundary decisions
4. verification checklist
```

## สิ่งที่ควรได้

- app shell ที่สะอาด
- route registry
- localization baseline
- test baseline
- รายการ decisions ที่ต้องรักษาไว้ในงานถัดไป

## Review notes

- bootstrap code ต้องบางและต่อยอดง่าย
- app shell ไม่ควรยัด business logic
- default state management ต้องชัด ไม่ใช่ implicit

## Verification notes

- ตรวจว่ามีจุดเริ่มจาก `flutter-dev`
- ตรวจว่า prompt อยู่ใน `overlays/mobile-flutter/prompts/`
- ตรวจว่า folder structure ตรงกับ policy
