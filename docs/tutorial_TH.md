# Tutorial

## เป้าหมาย

เรียนรู้การใช้ foundation ร่วมกับ Mobile Flutter overlay โดยไม่ทำให้ repository นี้กลายเป็น Flutter-only toolkit

## ขั้นตอนที่ 1: เริ่มจาก foundation

อ่าน:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

## ขั้นตอนที่ 2: เข้า Flutter overlay

อ่าน:
- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`

## ขั้นตอนที่ 3: เลือกชุด skill

ตัวอย่าง:
- login flow: `flutter-auth`, `flutter-storage`, `flutter-networking`
- map flow: `flutter-permissions`, `flutter-geolocation`, `flutter-maps`
- release flow: `flutter-build-flavors`, `flutter-web-deployment`, `flutter-ci-cd-mobile`

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
