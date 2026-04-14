---
tags:
  - agent-engineering-toolkit
  - tutorial
  - example
  - patterns
  - adoption
  - obsidian
aliases:
  - Adoption Patterns
---

# รูปแบบการนำ toolkit ไปใช้

ใช้รูปแบบเหล่านี้เมื่อนำ toolkit เข้าไปใน repo

## สถานการณ์ที่พบบ่อย

- bootstrap repo ใหม่
- retrofit repo เดิม
- นำเข้าแบบ submodule
- นำเข้าแบบคัดลอกเฉพาะไฟล์ที่เลือก

## ลำดับที่แนะนำ

1. อ่าน `AGENTS.md`
2. อ่าน `docs/prompt-pipeline.md`
3. เลือก overlay ที่เกี่ยวข้อง
4. เพิ่มหรืออัปเดต project memory
5. ค่อยเพิ่ม design หรือสัญญาเฉพาะ stack เมื่อ foundation เสถียรแล้ว

## สิ่งที่ไม่ควรทำ

- เอากฎเฉพาะ stack ไปปนในเอกสาร foundation root
- ข้ามการตรวจสอบ
- ปล่อยให้บันทึกการ adoption กำกวม หรือเป็นแค่ข้อความสร้างแรงบันดาลใจ
