# สร้างโปรเจกต์ใหม่ด้วย AI

## เป้าหมาย

เริ่ม Flutter app ใหม่จาก overlay โดยไม่ต้องเดาเรื่องโครงสร้าง, state choice หรือ routing layout

## สิ่งที่ต้องมี

- รู้ชื่อ app และ package name
- รู้ว่าจะใช้ Riverpod หรือ GetX เป็นค่าเริ่มต้น
- สามารถ copy starter template ไปยัง consuming repository ได้

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/starter-app-template/`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/translations.csv`
- `overlays/mobile-flutter/ci/validate_skills.sh`

## ขั้นตอน

1. อ่าน `workflows/new-project/README.md`
2. copy `starter-app-template/` ไปยัง consuming repository ใหม่
3. ใช้ `project-bootstrap-template.md` ยืนยันโฟลเดอร์ที่คาดหวัง
4. ใช้ `feature-module-template.md` ตรวจรูปแบบ feature แรก
5. ตั้งค่า routing, state และ localization ตาม default ของ overlay
6. เพิ่ม tests สำหรับ bootstrap shell และ feature slice แรก
7. รัน overlay validation ก่อนประกาศว่า bootstrap เสร็จ

## ควรใช้ skill อะไร

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton` หรือ `flutter-getx-controller-skeleton`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-localization-csv-sync`
- `flutter-performance-audit`

## อินพุตที่คาดหวัง

- ชื่อ app
- package name
- state management ที่เลือก
- route list
- locale list
- ต้องรองรับ web หรือไม่

## เอาต์พุตที่คาดหวัง

- app shell และ folder tree
- route map และ redirect rule แรก
- localization baseline
- test baseline
- starter structure ที่พร้อม release

## ความผิดพลาดที่พบบ่อย

- เริ่มจาก feature code ก่อนมี bootstrap shell
- ปน Riverpod กับ GetX ใน pass แรก
- ลืมไฟล์ localization และ test baseline
- มองข้าม web shell ทั้งที่ต้องรันบน web

## วิธีแก้ปัญหา

- ถ้า scope กว้างเกินไป ให้สร้างแค่ shell, router และ feature เดียวก่อน
- ถ้าใช้ GetX อย่าสร้างไฟล์ Riverpod state
- ถ้า routing fail ให้สร้าง route map ก่อนเชื่อม deep link

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-project/README.md.
Copy overlays/mobile-flutter/starter-app-template/ into the target repo.

Task:
Bootstrap a new Flutter app with the overlay defaults.

Deliver:
1. starter structure
2. routing plan
3. state choice
4. localization baseline
5. test baseline
6. validation checklist
```

## English

ดู `build-a-new-project-with-ai.md` สำหรับเวอร์ชันภาษาอังกฤษ
