---
tags:
  - tutorial
  - workflow
  - lead-agent
aliases:
  - Lead to Feature
---

# Workflow ของจริงแบบ Lead → Architecture → Feature

tutorial นี้ตอบคำถามที่เจอบ่อยที่สุด:

> เวลาทำจริง ต้องเริ่มจาก lead แล้วค่อย architecture แล้วค่อย feature ใช่ไหม

คำตอบคือ: **โดยมากใช่**
แต่สำคัญกว่านั้นคือ ต้องรู้ว่าแต่ละ stage มี output อะไร และ stage ถัดไปรับอะไรต่อ

## โครง workflow ที่แนะนำ

```text
Request
  ↓
Lead / Planning
  ↓
Architecture / Boundary Review
  ↓
Implementation
  ↓
Review
  ↓
Verification
  ↓
Finalize
  ↓
Memory
```

## Stage 1: Lead / Planning

เป้าหมาย:

- แปลง request ให้เป็นแผนงาน
- แตก scope
- ระบุความเสี่ยง
- เสนอไฟล์ที่จะเปลี่ยน

ตัวอย่าง prompt:

```text
Read AGENTS.md first.
Use the planning stage of the canonical lifecycle.

Task:
Add a login feature to the Flutter app.

Need:
- scope breakdown
- architecture impact
- files likely to change
- risks
- recommended order of implementation

Do not implement yet.
```

output ที่ควรได้:

- งานนี้ใหญ่แค่ไหน
- มี dependency อะไร
- ควรแยก sub-task ไหม
- งานไหน risky

## Stage 2: Architecture

เป้าหมาย:

- ตัดสิน boundary
- ห้าม leakage
- เลือก adapter / abstraction
- ตัดสินเรื่อง state, routing, persistence ถ้าจำเป็น

ตัวอย่าง prompt:

```text
Read AGENTS.md first.
Use the architecture stage of the canonical lifecycle.

We already have the plan.
Review the boundary for a login feature.

Decide:
- presentation/domain/data split
- auth abstraction boundary
- navigation impact
- state management impact
- testing and verification expectations

Do not implement yet.
```

output ที่ควรได้:

- boundary decision
- guardrails
- things that must not happen

## Stage 3: Implement

เป้าหมาย:

- สร้างหรือแก้ไฟล์ตามแผน
- ไม่หลุด boundary
- ไม่ขยาย scope เอง

ตัวอย่าง prompt:

```text
Read AGENTS.md first.
Use the implementation stage of the canonical lifecycle.

Implement the approved login feature.
Stay within the agreed boundaries.
Do not add unrelated improvements.
```

## Stage 4: Review

เป้าหมาย:

- หาจุดผิด
- หาจุดที่ over-engineered
- หา leakage หรือ missing verification

## Stage 5: Verify

เป้าหมาย:

- บอกว่าตรวจอะไรแล้ว
- บอกอะไรที่ยังไม่ได้ตรวจ
- ห้ามแสร้งบอกว่าผ่านหมด ถ้ายังไม่ได้รันจริง

## Stage 6: Finalize + Memory

เป้าหมาย:

- สรุปผลแบบส่งต่อได้
- บันทึกเฉพาะ decision ที่ควรจำระยะยาว

## workflow แบบไหนที่ไม่ควรทำ

### แบบก้อนเดียว
ขอให้ AI วางแผน ออกแบบ เขียนโค้ด review และ verify ใน prompt เดียว
ผลคือมักสับสนและตรวจย้อนกลับยาก

### แบบข้าม architecture
ใช้ได้กับงาน trivial มาก ๆ เท่านั้น
ถ้างานแตะ boundary ควรมี architecture stage

### แบบไม่มี review และ verify
งานจะดูเสร็จเร็ว แต่ quality จะ random

## rule of thumb

- งานเล็กมาก: plan + implement + verify อาจพอ
- งานแตะ architecture: ต้องมี architecture stage
- งานหลายระบบ: ใช้ multi-agent หรืออย่างน้อยแตก sub-task ให้ชัด

## ไปต่อ

- [วิธีสร้าง feature แบบ production](./04-build-production-feature.md)
- [วิธีใช้ multi-agent execution](./07-multi-agent-execution.md)
