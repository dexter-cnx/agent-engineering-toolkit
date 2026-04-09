# Tutorial

## เป้าหมาย

เรียนรู้การใช้ foundation ร่วมกับ overlay โดยไม่ทำให้ repository นี้กลายเป็น toolkit ที่ผูกกับ stack ใด stack หนึ่ง

## ขั้นตอนที่ 1: เริ่มจาก foundation

อ่าน:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

## ขั้นตอนที่ 2: เข้า overlay ที่ใช้งานจริง

อ่าน README และ `AGENTS.overlay.md` ของ overlay ที่ตรงกับ stack ที่ใช้งานจริง

## ขั้นตอนที่ 3: เลือกชุด skill

ตัวอย่าง:
- เลือกชุด skill ภายใน overlay ที่น้อยที่สุดแต่เพียงพอ
- จัดกลุ่ม capability ตาม catalog ของ overlay นั้น
- อย่าสร้างสมมติฐานเฉพาะ stack เพิ่มใน foundation layer

## ขั้นตอนที่ 4: ใช้ skill หนึ่งตัวแบบครบวงจร

สำหรับ skill ที่เลือก:
1. อ่าน `README.md`
2. อ่าน `skill.md`
3. เริ่มจาก `prompts/add_*.md`
4. ปรับ `templates/*.template.md`
5. ตรวจด้วย `checklists/`
6. เทียบกับ `examples/`

## ขั้นตอนที่ 5: ตรวจและบันทึก

ก่อน push:
- ตรวจว่าทุกไฟล์ที่เอกสารอ้างถึงมีอยู่จริง
- ตรวจว่า overlay catalog ตรงกับ skill ที่มีจริง
- อย่าใช้ชื่อ skill ที่ lock กับ provider มากเกินไป
