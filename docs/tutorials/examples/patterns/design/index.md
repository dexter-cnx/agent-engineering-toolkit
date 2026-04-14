---
tags:
  - agent-engineering-toolkit
  - tutorial
  - example
  - patterns
  - design
  - obsidian
aliases:
  - Design Usage Patterns
---

# รูปแบบการใช้ DESIGN.md

ใช้รูปแบบเหล่านี้เมื่อ `DESIGN.md` เป็นส่วนหนึ่งของ workflow

## เทมเพลตที่เกี่ยวข้อง

- [เทมเพลต DESIGN.md สำหรับ Flutter](../../templates/flutter/design-md-flutter-template.md)
- [เทมเพลต DESIGN.md สำหรับ Web Frontend](../../templates/web/design-md-web-frontend-template.md)

## สถานการณ์ที่พบบ่อย

- เพิ่มกฎ design ให้ repo ใหม่
- retrofit กฎ design เข้าไปในแอปเดิม
- ขอให้ AI เคารพ design contract

## ลำดับที่แนะนำ

1. ตัดสินว่า `DESIGN.md` จะอยู่ที่ไหน
2. อัปเดต `AGENTS.md` ให้ชี้ไปหาไฟล์นั้น
3. เลือก overlay ที่เหมาะ
4. ใช้เทมเพลตจาก `templates/`
5. ตรวจ UI เทียบกับ contract

## สิ่งที่ไม่ควรทำ

- ทำให้ `DESIGN.md` เป็นไฟล์เลือกใส่ได้ ถ้า repo ต้องพึ่งมัน
- ปล่อยให้เทมเพลตกับ contract ของ repo ไม่ตรงกัน
- ซ่อนกฎ accessibility หรือ responsive
