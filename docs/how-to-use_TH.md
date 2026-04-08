# วิธีใช้งาน (ภาษาไทย)

นี่คือคู่มือใช้งานหลักภาษาไทยของ `agent-engineering-toolkit`

เอกสารนี้อธิบาย:
- toolkit นี้คืออะไร
- จะนำไปใช้กับ repo จริงอย่างไร
- จะใช้กับ AI coding tools อย่างไร
- จะใช้ overlays อย่างไร
- จะดูแล project memory อย่างไร
- จะ review และ verify งานให้ดีอย่างไร

## 1. toolkit นี้คืออะไร

toolkit นี้ไม่ใช่แค่ prompt pack และไม่ใช่แค่ `AGENTS.md`

มันคือ operating layer ที่ใช้ซ้ำได้สำหรับ AI-assisted engineering ซึ่งประกอบด้วย:
- governance
- workflow
- prompts
- roles
- skills
- templates
- overlays
- วินัยด้านเอกสาร
- วินัยด้าน memory

## 2. mental model

ให้คิดว่า toolkit นี้มี 5 ชั้น:
- Governance
- Orchestration
- Capability
- Specialization
- Continuity

ควรใช้ `AGENTS.md`, `core/*`, `prompts/*`, `skills/*`, `overlays/*` และ `project_memory/*` ร่วมกันเป็นระบบ

## 3. lifecycle หลัก

ให้ถือ `docs/prompt-pipeline.md` เป็นแหล่งอ้างอิงเดียวของ lifecycle

ใช้ไฟล์นั้นเป็น source of truth สำหรับ:
- ลำดับ lifecycle
- stage ต่าง ๆ
- การ map ไปยัง prompts

## 4. รูปแบบการนำไปใช้

### แบบ A — toolkit repo กลาง
เหมาะเมื่ออยากมี canonical toolkit repository ใช้ร่วมกันหลายโปรเจกต์

### แบบ B — Git submodule
เหมาะเมื่ออยากให้แต่ละโปรเจกต์ consume toolkit ตรง ๆ

```bash
git submodule add <toolkit-repo-url> toolkit
```

### แบบ C — คัดลอกเฉพาะบางไฟล์
เหมาะเมื่อทีมยังไม่พร้อมใช้ submodule และต้องการแค่ governance, prompts หรือ templates

## 5. โฟลเดอร์หลัก

### `AGENTS.md`
root contract ที่บอก AI ว่า:
- repo นี้คืออะไร
- ต้องเดิน lifecycle แบบไหน
- อะไรที่ห้าม assume
- ควรคิดเรื่อง boundary, docs, verification และ memory อย่างไร

### `prompts/`
stage-oriented prompts

### `agent_team/`
role definitions สำหรับ lead, architect, builder, reviewer, verifier, finalizer และ memory

### `skills/`
capability แบบแคบและ reusable ที่มี contract ชัดเจน

### `overlays/`
extension ที่เฉพาะ stack

### `templates/`
template สำหรับ bootstrap, review, verification และ memory

## 6. วิธีใช้กับ AI tools

คำสั่งเริ่มต้นที่แนะนำ:

```text
Follow AGENTS.md strictly.
Use the canonical lifecycle from docs/prompt-pipeline.md.
Use prompts and skills from the toolkit when relevant.
Do not introduce stack-specific assumptions into the foundation layer.
```

ลำดับที่แนะนำ:
1. ให้เครื่องมือ AI อ่าน `AGENTS.md`
2. ให้มันอ่าน:
   - `docs/how-to-use.md`
   - `docs/architecture.md`
   - `docs/overlays.md`
   - `docs/prompt-pipeline.md`
3. ให้มันเลือก overlay ที่ถูกต้อง ถ้าเป็น consuming project
4. ให้มันทำงานผ่าน lifecycle
5. ให้มันอัปเดต memory เมื่อมี durable decision

## 7. วิธีใช้กับ Claude Code

ลำดับที่แนะนำ:
1. LEAD วางกรอบงาน
2. ARCHITECT วางโครงสร้าง
3. BUILDER ลงมือทำ
4. REVIEWER ตรวจ
5. VERIFIER validate
6. FINALIZER เก็บงาน
7. MEMORY บันทึก durable notes

## 8. วิธีเลือก overlay

### `mobile-flutter`
สำหรับ Flutter applications

### `backend-node`
สำหรับ Node-based API หรือ backend services

### `web-frontend`
สำหรับ web repos ที่ UI หนัก

### `python-service`
สำหรับ Python services, workers, automation tools หรือ integration layers

กฎสำคัญ:
overlay มีไว้ต่อยอด foundation ไม่ใช่เขียนทับ identity ของ foundation

## 9. วิธี bootstrap repo ใหม่

แนวทางที่แนะนำ:
1. เพิ่ม toolkit เป็น submodule หรือคัดลอกไฟล์ที่เลือก
2. เพิ่มหรืออ้างอิง `AGENTS.md`
3. คัดลอกไฟล์ project memory templates
4. เลือก overlay ที่เหมาะหนึ่งตัว
5. เพิ่ม project-specific verification commands
6. เพิ่ม project-specific CI
7. ลองรัน feature จริงหนึ่งอันผ่าน lifecycle เต็ม

helper เสริม:
```bash
bash scripts/bootstrap-project-memory.sh
```

## 10. project memory ที่ดี

project memory ควรเก็บ:
- durable decisions
- approved patterns
- known constraints
- recurring pitfalls
- future reminders

## 11. review และ verification

review ที่ดีควรตรวจ:
- correctness
- clarity
- maintainability
- architecture fit
- verification evidence
- doc alignment

verification ต้องบอกชัดว่า:
- เช็กอะไร
- เช็กอย่างไร
- อะไรยังไม่แน่ใจ

ถ้าจะ audit toolkit repository นี้แบบเข้ม:
- ใช้ `prompts/audit_repo.md` เมื่ออยากได้ prompt แบบ role-based
- ใช้ `docs/strict-audit-prompt.md` เมื่ออยากได้ invocation template แบบ paste ได้ทันที

## 12. ความผิดพลาดที่เจอบ่อย
- เอา assumption ของ Flutter หรือ Node ไปใส่ใน root
- ใช้ prompts โดยไม่อ่าน `AGENTS.md`
- ข้าม memory update หลังมี decision สำคัญ
- ทำเหมือน review กับ verification คืออย่างเดียวกัน
- ปล่อยให้ overlays เขียนทับ identity ของ foundation
