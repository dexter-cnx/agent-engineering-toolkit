# App Log and Production Logging

## Purpose

แนะนำเส้นทางที่สั้นและปลอดภัยที่สุดสำหรับเพิ่ม app-level production logging ใน Flutter repository

## Prerequisites

- รู้ว่าตอนนี้มี logger อยู่แล้วหรือยัง
- รู้ว่าต้อง handoff ไป crash reporting หรือ analytics ไหม
- มีไฟล์ logger หรือ bootstrap entrypoint ที่จะใช้เป็นจุดเริ่มต้น

## Exact repository paths

- `overlays/mobile-flutter/skills/architecture/flutter-production-logging/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-crash-reporting/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-analytics/SKILL.md`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/prompts/new_feature.md`

## Step-by-step instructions

1. เปิด `skills/architecture/flutter-production-logging/SKILL.md` แล้วยืนยัน boundary ของ logging
2. ตัดสินใจว่าไฟล์ไหนเป็นเจ้าของ logger interface, context model, และ formatter
3. wire logger ที่ app bootstrap layer ไม่ใช่ใน widgets
4. เพิ่ม crash reporting หรือ analytics adapter เฉพาะเมื่อจำเป็น
5. redact secrets และ personal data ก่อน log ออกจาก boundary
6. เพิ่ม tests สำหรับ formatting, redaction, และ fallback behavior
7. อัปเดต `HOW_TO_USE.md` หรือ feature prompt ที่เกี่ยวข้องถ้า path ของ logging เปลี่ยน

## What skills to use

- `flutter-production-logging`
- `flutter-crash-reporting` ถ้า logs ต้อง handoff ไป crash tooling
- `flutter-analytics` ถ้า event หรือ breadcrumb เป็น requirement
- `flutter-clean-architecture-audit` ถ้า ownership ของ logging ยังไม่ชัด

## Expected inputs

- ประเภทของ log event
- redaction rules
- sink destinations
- ความต้องการ integration กับ crash reporting หรือ analytics
- release verbosity rules

## Expected outputs

- Logger interface และ context model ที่รองรับ
- Formatter และ redaction helpers
- Bootstrap wiring สำหรับ logging boundary
- Tests สำหรับการจัดการข้อมูล sensitive

## Common mistakes

- ใส่ logger call ลงใน widgets โดยตรง
- log token, email, หรือข้อมูล sensitive อื่น ๆ
- ผสม adapter ของ crash reporting เข้าไปใน UI layer
- ปล่อยให้ release verbosity noisy เกินไป

## Troubleshooting

- ถ้าแค่ debug ชั่วคราว ใช้ `print()` แบบ local และยังไม่ต้องเพิ่ม boundary เต็มรูปแบบ
- ถ้า logger noisy เกินไป ลด release verbosity และเก็บ detail ไว้เฉพาะ debug build
- ถ้า crash reporting มีอยู่แล้ว ให้ logging boundary โฟกัสที่ formatting และ redaction

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/docs/tutorials/app-log-and-production-logging.md.
Use overlays/mobile-flutter/skills/architecture/flutter-production-logging/SKILL.md.

Task:
Add production logging to the Flutter app.

Deliver:
1. logger boundary plan
2. exact files to update
3. integration points
4. verification checklist
```

## Thai

ดู `app-log-and-production-logging.md` สำหรับเวอร์ชันภาษาอังกฤษ
