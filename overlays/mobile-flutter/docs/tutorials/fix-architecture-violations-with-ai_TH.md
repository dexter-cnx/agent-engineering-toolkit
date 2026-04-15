# แก้ architecture violation ด้วย AI

## เป้าหมาย

แก้ปัญหา layering, dependency direction และ boundary violation โดยไม่ต้อง rewrite แอปทั้งหมด

## สิ่งที่ต้องมี

- มีไฟล์หรือโฟลเดอร์ที่สงสัยว่า boundary แตก
- รู้ว่า feature หรือ module ไหนเป็นเจ้าของปัญหา
- เปิดหรือ inspect แอปในเครื่องได้

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/migrate-project/README.md`
- `overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `overlays/mobile-flutter/policies/architecture/README.md`

## ขั้นตอน

1. อ่าน `flutter-clean-architecture-audit` ก่อน
2. ระบุ path ของไฟล์ที่ boundary พัง
3. ย้าย SDK calls ออกจาก widgets ไปไว้ใน adapter หรือ repository
4. ย้าย state logic ไปยัง state layer ที่เลือก
5. ย้าย route rules ไปยัง routing files ไม่ใช่ UI files
6. อัปเดต tests และ docs ถ้า boundary เปลี่ยน
7. รัน audit ใหม่เพื่อยืนยันว่าการแก้ไขเล็กกว่าการ rewrite

## ควรใช้ skill อะไร

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton` หรือ `flutter-getx-controller-skeleton`
- `flutter-firestore-repository`
- `flutter-firebase-auth-adapter`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`

## อินพุตที่คาดหวัง

- path ที่มีปัญหา
- current imports หรือ dependency graph
- layer ที่ถือ logic อยู่ตอนนี้
- target layer ที่ควรเป็นเจ้าของ logic

## เอาต์พุตที่คาดหวัง

- violation list
- แผนย้ายไฟล์
- adapter หรือ repository ที่อัปเดตแล้ว
- tests ที่อัปเดต
- ผล audit ที่สะอาด

## ความผิดพลาดที่พบบ่อย

- ย้าย code แต่ไม่เปลี่ยน ownership
- แก้อาการใน widget แทนที่จะแก้ boundary
- ทิ้ง import เก่าไว้หลังย้ายไฟล์
- rewrite ทั้งระบบทั้งที่แก้ boundary เดียวพอ

## วิธีแก้ปัญหา

- ถ้า boundary ยังไม่ชัด ให้ audit feature ก่อนแก้
- ถ้าการแก้แตะ routing ให้แยก route map ออกจาก redirect logic
- ถ้าการแก้แตะ Firebase ให้ isolate SDK use หลัง adapter

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md first.

Task:
Fix the architecture violation in <file or feature path>.

Deliver:
1. violation summary
2. exact files to move or edit
3. boundary that must be restored
4. test updates
5. re-audit checklist
```

## English

ดู `fix-architecture-violations-with-ai.md` สำหรับเวอร์ชันภาษาอังกฤษ
