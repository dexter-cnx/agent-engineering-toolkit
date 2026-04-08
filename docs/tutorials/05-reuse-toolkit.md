---
tags:
  - tutorial
  - reuse
  - adoption
aliases:
  - Reuse Patterns
---

# วิธี reuse toolkit

repo นี้มีคุณค่าเมื่อมันถูก reuse ได้ง่ายและไม่ทำให้ repo ปลายทางสกปรก

tutorial นี้ช่วยเลือก adoption pattern ให้เหมาะกับงาน

## วิธี A: ใช้เป็น submodule

เหมาะเมื่อ:

- อยากตาม upstream ง่าย
- อยากแยก foundation ออกจาก business repo
- อยากอัปเดต toolkit เป็น version

ข้อดี:

- boundary ชัด
- update ง่าย
- ลดการ copy drift

ข้อเสีย:

- ต้องเข้าใจ submodule workflow
- contributor ใหม่อาจงงช่วงแรก

## วิธี B: คัดลอกเฉพาะส่วนที่ต้องใช้

เหมาะเมื่อ:

- repo ปลายทางเล็ก
- ไม่อยากมี dependency แบบ submodule
- เอาแค่ prompt, template, หรือ docs บางส่วน

ข้อดี:

- เริ่มง่าย
- ไม่มี submodule overhead

ข้อเสีย:

- drift เร็ว
- ต้องดูแลเองทั้งหมด

## วิธี C: ใช้ repo นี้เป็น foundation repo

เหมาะเมื่อ:

- คุณจะสร้าง toolkit fork / derivative ของตัวเอง
- มีทีมที่ใช้ workflow นี้ซ้ำหลาย repo
- ต้องการองค์กรของตัวเองบน foundation เดิม

ข้อดี:

- คุมมาตรฐานได้มาก
- เหมาะกับทีม/องค์กร

ข้อเสีย:

- ต้องมี release discipline
- ต้องดูแล docs และ audit เองจริงจัง

## วิธีเลือกแบบเร็ว

ใช้คำถามนี้:

- ต้อง sync upstream ไหม
- ทีมรับ submodule ได้ไหม
- อยากได้ foundation กลางของตัวเองไหม
- ต้องการ copy แค่ prompt บางตัวหรือทั้งระบบ

## คำแนะนำเชิงปฏิบัติ

### สำหรับโปรเจกต์ลูกค้า / โปรเจกต์ใหม่รายตัว
เริ่มที่ **submodule**

### สำหรับ prototype สั้นมาก
copy เฉพาะส่วนที่ต้องใช้ได้

### สำหรับการทำ platform ภายใน
สร้าง foundation repo ของตัวเองบนแนวทางนี้

## สิ่งที่ควรแยกเสมอ

- foundation rules
- stack overlays
- project-specific AGENTS.md
- project memory ของ repo ปลายทาง

## สิ่งที่ไม่ควรทำ

- เอาเรื่อง business-specific มาใส่ใน foundation root
- copy ทุกอย่างทั้ง repo ทั้งที่ใช้จริงน้อยมาก
- fork แล้วไม่วาง release/update policy
