---
tags:
  - tutorial
  - multi-agent
  - team
aliases:
  - Agent Team Execution
---

# วิธีใช้ multi-agent execution

เมื่อไหร่ที่งานควรแตกเป็นหลาย agent

คำตอบสั้น:

- เมื่องานมีหลาย boundary
- เมื่องานมีหลาย output type
- เมื่อต้องการลด context overload
- เมื่อต้องการ review แบบ role-specific

## โครงสร้างที่แนะนำ

```text
Lead Agent
 ├─ Architecture Agent
 ├─ Implementation Agent
 ├─ Review Agent
 └─ Verification Agent
```

หรือในงาน product จริง:

```text
Lead Agent
 ├─ UI Agent
 ├─ Backend Agent
 ├─ QA Agent
 └─ Docs Agent
```

## Lead Agent ต้องทำอะไร

- รับ request หลัก
- แตกงานเป็น sub-task
- กำหนด boundary ของแต่ละ agent
- ระบุ handoff artifact
- ตัดสินว่าอะไร sequential และอะไร parallel ได้

## สิ่งที่แต่ละ sub-agent ควรได้รับ

ทุกตัวควรได้รับอย่างน้อย:

- task statement
- in-scope
- out-of-scope
- files หรือ area ที่เกี่ยวข้อง
- output format
- verification expectation

## ตัวอย่าง handoff ที่ดี

```text
Sub-agent: UI Agent

In scope:
- login screen
- form validation UI
- loading/error/success state rendering

Out of scope:
- auth provider integration
- token persistence
- analytics

Output:
- list of UI files to create/change
- implementation summary
- UI-specific verification notes
```

## pitfall ที่พบบ่อย

- lead ไม่กำหนด out-of-scope
- sub-agent แก้ไฟล์ทับกันมั่ว
- ไม่มี handoff artifact
- verification ไม่รู้ว่าใครรับผิดชอบส่วนไหน
- แยก agent มากเกินไปจน overhead สูง

## rule of thumb

- งานเล็ก: agent เดียวพอ
- งานกลาง: lead + implementation + verify
- งานใหญ่: lead + role-based agents + final integrator

## เอกสารที่ควรอ่านคู่กัน

- `docs/agent-team-system.md`
- tutorial ใน `docs/tutorials/team/`
- [Workflow ของจริงแบบ Lead → Architecture → Feature](./03-real-workflow.md)
