# วิธีใช้ Toolkit นี้

## โมเดลแบบ foundation-first

เริ่มจาก foundation ก่อน:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

จากนั้นค่อยเพิ่ม overlay เมื่อ repository ที่ใช้งานจริงต้องการกฎเฉพาะทางของ stack

## การใช้ Mobile Flutter overlay

ให้ใช้:
- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/skills/index.md`

### ขั้นตอนเลือก skill

1. นิยามผลลัพธ์ของ feature
2. เลือกชุด Flutter skill ที่น้อยที่สุดแต่เพียงพอ
3. อ่าน README ของแต่ละ skill
4. ใช้ `skill.md` และ prompt ในการลงมือทำ
5. ตรวจงานด้วย checklist ของ skill
6. บันทึก convention ที่เสถียรลง project memory

### ตัวอย่างการจับคู่ skill

- แอปที่มีระบบล็อกอิน: `flutter-auth` + `flutter-storage` + `flutter-networking`
- เลือกตำแหน่งบนแผนที่: `flutter-permissions` + `flutter-geolocation` + `flutter-maps`
- notification แล้วพาไปหน้าเฉพาะ: `flutter-push-notifications` + `flutter-deep-link`
- ปล่อย Flutter web: `flutter-web-deployment` + `flutter-build-flavors` + `flutter-ci-cd-mobile`

## วินัยด้านเอกสาร

เมื่อมีการเพิ่มหรือแก้ skill:
- อัปเดตรายการใน overlay catalog
- อัปเดต tutorial ถ้า workflow เปลี่ยน
- หลีกเลี่ยงการอ้างถึงไฟล์ที่ไม่มีอยู่จริง
- แยกไฟล์ภาพรวมสำหรับคนอ่านออกจากไฟล์กฎสำหรับ AI
