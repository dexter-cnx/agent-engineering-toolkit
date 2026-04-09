# วิธีใช้ Toolkit นี้

## โมเดลแบบ foundation-first

เริ่มจาก foundation ก่อน:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

จากนั้นค่อยเพิ่ม overlay เมื่อ repository ที่ใช้งานจริงต้องการกฎเฉพาะทางของ stack

## การใช้ overlay

ให้เลือก overlay ที่ตรงกับ stack หรือ capability ที่กำลังทำ แล้วอ่าน:
- `README.md` ของ overlay นั้น
- `AGENTS.overlay.md` ของ overlay นั้น
- catalog หรือ index ภายใน overlay ถ้ามี

overlay ปัจจุบัน:
- `overlays/backend-node/README.md`
- `overlays/mobile-flutter/README.md`
- `overlays/unity/README.md`
- `overlays/python-service/README.md`
- `overlays/web-frontend/README.md`

### ขั้นตอนเลือก skill

1. นิยามผลลัพธ์ของ feature
2. เลือกชุด skill ภายใน overlay ที่น้อยที่สุดแต่เพียงพอ
3. อ่าน README ของแต่ละ skill
4. ใช้ `skill.md` และ prompt ในการลงมือทำ
5. ตรวจงานด้วย checklist ของ skill
6. บันทึก convention ที่เสถียรลง project memory

## Catalog ของ capability

overlay แต่ละตัวกำหนดรูปแบบ skill catalog ของตัวเอง โดย foundation docs ควรชี้ไปที่ catalog แทนการอธิบายรูปแบบซ้ำ

เมื่อมีการเพิ่มหรือแก้ skill:
- อัปเดตรายการใน catalog ของ overlay
- อัปเดต tutorial ถ้า workflow เปลี่ยน
- หลีกเลี่ยงการอ้างถึงไฟล์ที่ไม่มีอยู่จริง
- แยกไฟล์ภาพรวมสำหรับคนอ่านออกจากไฟล์กฎสำหรับ AI
