# เริ่มต้นใช้งาน

## เป้าหมาย

ใช้ overlay นี้ได้ตั้งแต่ต้นจนจบโดยไม่ต้องมี context มาก่อน เหมาะสำหรับงานที่ต้องเลือก skill ทำงานตาม workflow และส่งมอบอย่างปลอดภัย

## สิ่งที่ต้องมี

- clone repository ไว้ในเครื่อง
- เข้าถึง `overlays/mobile-flutter/`
- รู้เป้าหมายงานชัดเจน: new app, new feature, release หรือ architecture fix

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `overlays/mobile-flutter/SKILL_SCHEMA.md`
- `overlays/mobile-flutter/workflows/`
- `overlays/mobile-flutter/examples/`
- `overlays/mobile-flutter/templates/`
- `overlays/mobile-flutter/ci/validate_skills.sh`

## ขั้นตอน

1. อ่าน [README.md](../../README.md) เพื่อยืนยันเป้าหมายของ overlay
2. อ่าน [AGENTS.overlay.md](../../AGENTS.overlay.md) เพื่อดู rules การทำงาน
3. เปิด [SKILLS_INDEX.md](../../SKILLS_INDEX.md) แล้วเลือก skill ที่เล็กที่สุดที่ใช้ได้
4. ถ้างานต้องใช้มากกว่าหนึ่ง skill ให้เปิด workflow ที่ตรงใน `../../workflows/`
5. เปิด example และ template ที่ถูกอ้างถึงก่อนเริ่มแก้ code
6. แก้ไฟล์ให้น้อยที่สุดแต่ตรงกับ output ของ workflow
7. รัน `bash overlays/mobile-flutter/ci/validate_skills.sh` ก่อนส่งงาน

## ควรใช้ skill อะไร

- ใช้ `SKILLS_INDEX.md` เพื่อเลือก active skill ที่เล็กที่สุด
- ใช้ `workflows/new-project/README.md` สำหรับสร้าง app ใหม่
- ใช้ `workflows/new-feature/README.md` สำหรับ feature module
- ใช้ `workflows/release-app/README.md` สำหรับ release readiness
- ใช้ `workflows/migrate-project/README.md` สำหรับ refactor legacy project

## อินพุตที่คาดหวัง

- คำอธิบายงาน
- พาธของ repository เป้าหมาย
- ชื่อ feature หรือ app
- state management ที่ต้องใช้ถ้ามี
- platform scope ถ้ามี

## เอาต์พุตที่คาดหวัง

- เลือก skill ได้ชัดเจน
- รายการไฟล์ที่ต้องแก้
- docs หรือ template ที่ต้องอัปเดตถ้าจำเป็น
- ผล validation จาก overlay checker

## ความผิดพลาดที่พบบ่อย

- อ่านทุก skill ก่อนเริ่มทำ
- ใช้ workflow ทั้งที่ skill เดียวพอ
- แก้ code ก่อนตรวจ path ของ overlay
- ข้าม validation command

## วิธีแก้ปัญหา

- ถ้างานยังไม่ชัด ให้เริ่มจาก `flutter-clean-architecture-audit`
- ถ้าโปรเจกต์ใช้ GetX ให้เลือก skill ของ GetX แทน Riverpod
- ถ้างานแตะ routing ให้แยก route map, redirect และ deep link เป็นคนละ skill
- ถ้า validation fail ให้แก้ path ของไฟล์ก่อน แล้วค่อยรัน checker ใหม่

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/SKILLS_INDEX.md to select the smallest active skill.
If the task spans multiple steps, use the matching workflow from overlays/mobile-flutter/workflows/.

Task:
<describe the change>

Deliver:
1. assumptions
2. exact files to update
3. chosen skills
4. implementation plan
5. validation checklist
```

## English

ดู `getting-started.md` สำหรับเวอร์ชันภาษาอังกฤษ
