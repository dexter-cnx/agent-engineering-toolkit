# วิธีใช้งาน (ภาษาไทย)

คู่มือนี้อธิบายวิธีใช้ `agent-engineering-toolkit` กับโปรเจกต์จริง

## 1. toolkit นี้คืออะไร

รีโปนี้คือ operating system สำหรับการทำ AI-assisted engineering

ให้มองว่าเป็นชุดของ:
- governance
- execution flow
- prompts
- roles
- skills
- templates
- overlays
- กฎการดูแลเอกสาร

มันไม่ใช่ app starter สำเร็จรูปในตัวเอง  
แต่มันคือ layer ที่ช่วยให้คุณสร้างและดูแล repo อื่นอย่างสม่ำเสมอ

---

## 2. รูปแบบการนำไปใช้ที่แนะนำ

### แบบ A — ใช้เป็น reference repo แยกเดี่ยว
เหมาะเมื่อ:
- อยากเรียนรู้ระบบก่อน
- อยากมีที่เก็บ prompts และ rules กลาง
- อยากแชร์ toolkit ให้ทั้งทีม

### แบบ B — ใช้เป็น Git submodule
เหมาะเมื่อ:
- อยากให้แต่ละโปรเจกต์ดึง toolkit ไปใช้ตรง ๆ
- อยากให้ overlays และ templates อยู่ใน repo ปลายทาง
- อยากอัปเดตจาก toolkit กลางได้

ตัวอย่าง:
```bash
git submodule add <toolkit-repo-url> toolkit
```

### แบบ C — คัดลอกเฉพาะบางไฟล์เข้าโปรเจกต์
เหมาะเมื่อ:
- ทีมยังไม่พร้อมใช้ submodule
- โปรเจกต์ต้องการ setup เบากว่า
- ต้องการแค่ AGENTS.md, prompts และ templates

---

## 3. lifecycle หลัก

lifecycle ที่แนะนำคือ:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

### PLAN
ทำความเข้าใจ scope, constraint, assumption และ risk

### DESIGN
กำหนด architecture, boundary, flow หรือแนวทางโครงสร้าง

### IMPLEMENT
ลงมือทำหลังจาก plan และ design ชัดเจนแล้ว

### REVIEW
ตรวจ correctness, structure, clarity และ maintainability

### VERIFY
ยืนยันด้วย check, test, smoke path หรือ manual validation

### FINALIZE
เก็บความเรียบร้อยของ wording, docs, naming และความพร้อมใช้งาน

### MEMORY
อัปเดตความรู้ถาวรที่ควรรักษาไว้ข้าม run

---

## 4. team model เริ่มต้น

toolkit นี้ตั้งสมมติฐาน role ไว้ดังนี้:

### LEAD
ดูแลการแตกงาน, การวางกรอบโจทย์, ลำดับงาน และการประสานงาน

### ARCHITECT
ดูแลโครงสร้าง, boundary, interface และความเสี่ยงด้าน design

### BUILDER
รับผิดชอบ implementation ให้ตรงกับ plan/design

### REVIEWER
รับผิดชอบ critique, correctness review, structure review และ maintainability review

### VERIFIER
รับผิดชอบ validation และระดับความมั่นใจของผลลัพธ์

### FINALIZER
รับผิดชอบการเก็บงานสุดท้าย, shaping output และความพร้อมสำหรับ release

### MEMORY
รับผิดชอบ durable notes และ continuity ของระบบ

---

## 5. โฟลเดอร์แต่ละส่วนเอาไว้ทำอะไร

## `prompts/`
prompt ทั่วไปสำหรับแต่ละ stage

## `agent_team/`
คำอธิบาย role และ role-specific prompt patterns

## `skills/`
capability แบบแคบและเรียกใช้ซ้ำได้ เช่น:
- repo audit
- architecture review
- safe refactor
- dependency review
- docs update
- bug investigation
- verification pass
- risk scoring
- skill routing

## `core/`
วัสดุ framework กลาง:
- rules
- routing
- verification
- review discipline
- architecture discipline

## `templates/`
ไฟล์ template สำหรับคัดลอกเข้า repo จริง:
- AGENTS starter
- memory files
- runbooks
- review templates
- verification templates

## `overlays/`
pack สำหรับ specialization ทับบน foundation

## `examples/`
ตัวอย่างการใช้งานจริงและ sample prompts

## `project_memory/`
โครงสร้างพื้นฐานสำหรับเก็บ decisions และ constraints

---

## 6. วิธีใช้ toolkit กับ AI coding tools

### Codex CLI
ใช้คำสั่งตั้งต้นประมาณนี้:

```text
Follow AGENTS.md strictly.
Use the full lifecycle:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
Prefer reusable toolkit prompts and templates when relevant.
```

### Claude Code
ใช้แนว role-driven:
- ให้ LEAD วางกรอบงาน
- ให้ ARCHITECT กำหนดโครงสร้าง
- ให้ BUILDER ลงมือทำ
- ให้ REVIEWER ตรวจ
- ให้ VERIFIER validate
- ให้ FINALIZER เก็บงาน
- ให้ MEMORY บันทึกบริบทถาวร

### OpenClaw
ใช้ toolkit นี้เป็นแหล่ง rules/prompt กลาง แล้ว map model roles ไปยัง:
- planning
- coding
- review
- verification

---

## 7. กลยุทธ์ overlay

foundation ควรเป็น general  
อย่าเอาสมมติฐาน Flutter-only หรือ Node-only ไปปนใน root rules

ให้เก็บสิ่งที่เฉพาะ stack ไว้ใน overlays

### `overlays/mobile-flutter`
ใช้เมื่อโปรเจกต์เป็น mobile/Flutter

### `overlays/backend-node`
ใช้เมื่อโปรเจกต์เป็น Node/Nest/Express/backend service

### `overlays/web-frontend`
ใช้เมื่อโปรเจกต์เป็น frontend/UI/product surface

### `overlays/python-service`
ใช้เมื่อโปรเจกต์เป็น Python/FastAPI/service/integration automation

---

## 8. วิธี bootstrap repo ใหม่

minimal bootstrap ที่แนะนำ:
1. copy หรือลิงก์ `AGENTS.md`
2. copy `templates/project-bootstrap/README_BOOTSTRAP.md`
3. copy `templates/project_memory/*`
4. เลือก overlay ถ้าจำเป็น
5. เพิ่มกฎ verification ของ repo นั้น
6. เพิ่ม CI ของ project นั้น

---

## 9. workflow ตัวอย่างกับ feature จริง

ตัวอย่าง: "เพิ่มหน้าตั้งค่า billing"

### Step 1
ใช้ `prompts/plan_change.md`

### Step 2
ใช้ `prompts/architecture_review.md`

### Step 3
ใช้ `prompts/implement_change.md`

### Step 4
ใช้ `prompts/review_change.md`

### Step 5
ใช้ `prompts/verification_pass.md`

### Step 6
ใช้ `prompts/finalize_change.md`

### Step 7
อัปเดต `project_memory/decisions.md` หรือ `project_memory/known_constraints.md`

---

## 10. วิธีเตรียมก่อน push public

ก่อน push ควร:
- เปลี่ยน URL placeholder
- เพิ่ม author/license
- เปลี่ยนชื่อไฟล์ที่เฉพาะองค์กรถ้าจำเป็น
- ตัดสินใจว่าจะเก็บ overlay ทั้งหมดไว้ repo เดียว หรือแยกบางส่วนออกไป

---

## 11. สิ่งที่รีโปนี้ไม่ได้ทำให้อัตโนมัติ

toolkit นี้ไม่ได้ทำให้อัตโนมัติ:
- รันโมเดลให้
- มี hosted orchestration ให้ทันที
- แทน CI/CD
- แทน project-specific rules
- แทนวิจารณญาณด้าน engineering

สิ่งที่มันให้คือ **โครงสร้าง** ที่ทำให้คุณต่อยอดสิ่งพวกนี้ได้ดี

---

## 12. next step หลัง push

- เพิ่ม license ที่ต้องการ
- เพิ่ม branding ของคุณถ้าต้องการ
- เอารีโปนี้ไปเป็น submodule ในโปรเจกต์จริงสักหนึ่งตัว
- ทดสอบ feature workflow แบบ end-to-end หนึ่งรอบ
- ปรับ overlays ตาม usage จริง
