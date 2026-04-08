---
tags:
  - tutorial
  - mental-model
  - agents
aliases:
  - Agent Thinking
---

# Mental model ของระบบ Agent

เอกสารชุดนี้จะใช้งานยากทันที ถ้ายังมองทุกอย่างเป็น “prompt ยาว ๆ ก้อนเดียว”

tutorial นี้มีไว้ทำให้เห็นว่า toolkit แยกของออกเป็นคนละชั้นอย่างไร

## ความต่างที่ต้องเข้าใจ

### 1. Agent
agent คือผู้ปฏิบัติงานตามบทบาท ไม่ใช่แค่ตัวตอบข้อความ

มันควรมี:

- ขอบเขตงาน
- กติกาการทำงาน
- ลำดับการตัดสินใจ
- รูปแบบ output

### 2. Prompt
prompt คือคำสั่งสำหรับ stage หนึ่ง ไม่ใช่ระบบทั้งหมด

ตัวอย่าง:

- adopt
- plan
- architecture
- implement
- review
- verify
- finalize
- memory

### 3. Skill
skill คือความสามารถเฉพาะทางที่หยิบมาใช้เมื่อจำเป็น

ตัวอย่าง:

- architecture review
- repo audit
- safe refactor
- docs update

skill ไม่ควรถูกเรียกใช้ทุกครั้งแบบอัตโนมัติ ถ้างานยังไม่ต้องใช้

### 4. Overlay
overlay คือชั้น specialization ของ stack หรือ platform

ตัวอย่าง:

- mobile-flutter
- web-frontend
- backend-node
- python-service

foundation toolkit ต้องไม่กลายเป็น Flutter repo โดยไม่ได้ตั้งใจ
เรื่องเฉพาะ stack ควรไปอยู่ใน overlay หรือ repo ปลายทาง

### 5. Project Memory
project memory มีไว้เก็บเฉพาะสิ่งที่ควรจำข้ามงาน

เช่น:

- architecture decision
- known constraints
- patterns ที่ทีมตกลงใช้

ไม่ควรเก็บ log ทุกอย่าง

## แผนภาพที่ควรนึกในหัว

```text
User Request
  ↓
AGENTS.md
  ↓
Prompt Pipeline
  ↓
Overlay Selection
  ↓
Optional Skills
  ↓
Verification
  ↓
Project Memory Update
```

## หลักคิดสำคัญ

### อย่าเริ่มที่ implementation
เริ่มที่ boundary ก่อนเสมอ

### อย่าคิดว่า prompt เดียวพอ
งานจริงต้องมี stage

### อย่าเอา stack-specific rule ไปปน foundation
จะทำให้ toolkit drift และ reuse ยาก

### อย่าจำทุกอย่าง
memory ควรเก็บเฉพาะ durable decisions

## checklist สั้นก่อนเริ่มงาน

- repo นี้คืออะไร
- ใช้ overlay ไหน
- architecture boundary คืออะไร
- ต้องใช้ skill อะไรเพิ่มหรือไม่
- จะ verify อย่างไร
- มี decision อะไรที่ต้องจำหลังจบงาน

## ไปต่ออ่านอะไรดี

- [Workflow ของจริงแบบ Lead → Architecture → Feature](./03-real-workflow.md)
- [วิธี debug agent run ที่พัง](./06-debugging-agent-runs.md)
- [วิธีใช้ multi-agent execution](./07-multi-agent-execution.md)
