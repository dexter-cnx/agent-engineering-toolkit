# วิธีใช้งาน agent-engineering-toolkit (ฉบับละเอียด)

เอกสารนี้คือคู่มือการใช้งาน `agent-engineering-toolkit` แบบละเอียด

จะอธิบายว่า:
- toolkit นี้คืออะไร
- ควรคิดกับมันอย่างไร
- จะนำไปใช้กับ repo จริงอย่างไร
- จะใช้กับ Codex, Claude Code และเครื่องมือ AI coding อื่นอย่างไร
- จะใช้ overlays อย่างไร
- จะดูแล project memory อย่างไร
- จะ review และ verify งานให้ดีอย่างไร

---

## 1. toolkit นี้จริง ๆ คืออะไร

toolkit นี้ **ไม่ใช่** แค่ prompt pack

และก็ **ไม่ใช่** แค่ไฟล์ `AGENTS.md`

มันคือ operating layer ที่ใช้ซ้ำได้สำหรับ AI-assisted engineering  
operating layer นี้ประกอบด้วย:

- governance
- workflow
- prompts
- roles
- skills
- templates
- overlays
- วินัยด้านเอกสาร
- วินัยด้าน memory

ถ้าใช้แค่บางชิ้น เช่นใช้ prompt ตัวเดียว คุณจะได้ประโยชน์แค่บางส่วน

คุณค่าจริงจะเกิดเมื่อใช้ toolkit นี้เป็น “ระบบ”

---

## 2. mental model ที่ควรใช้

ให้คิดว่า toolkit นี้มี 5 ชั้น:

### ชั้นที่ 1 — Governance
ไฟล์:
- `AGENTS.md`
- `core/rules/*`

หน้าที่:
- กำหนดว่างานที่ดีหน้าตาเป็นอย่างไร
- กำหนด lifecycle ที่คาดหวัง
- ป้องกันการใช้ AI แบบกระจัดกระจายเกินไป

### ชั้นที่ 2 — Orchestration
ไฟล์:
- `prompts/*`
- `agent_team/*`

หน้าที่:
- กำหนดว่า flow งานจะเดินอย่างไร
- แยก role และ stage
- ทำให้ output deterministic มากขึ้น

### ชั้นที่ 3 — Capability
ไฟล์:
- `skills/*`

หน้าที่:
- ให้ ability แบบแคบที่ reusable
- ลดการทำงานซ้ำ
- ช่วยให้แก้ปัญหาแบบ focused มากขึ้น

### ชั้นที่ 4 — Specialization
ไฟล์:
- `overlays/*`

หน้าที่:
- ทำให้ foundation ยังคง stack-agnostic
- เก็บ assumption ที่เฉพาะ stack ไว้นอก root

### ชั้นที่ 5 — Continuity
ไฟล์:
- `project_memory/*`
- `templates/project_memory/*`

หน้าที่:
- เก็บบริบทถาวร
- ป้องกันไม่ให้ run รอบต่อไปลืม decision สำคัญ

---

## 3. lifecycle หลัก

toolkit นี้แนะนำ lifecycle นี้:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

### PLAN
ใช้เมื่อ:
- งานไม่ trivial
- scope หรือ risk ยังไม่ชัด
- คำขอสามารถแตกทางได้หลายแบบ

คำถามหลัก:
- โจทย์จริง ๆ คืออะไร?
- เรากำลังสมมติอะไรอยู่?
- constraint คืออะไร?
- risk หลักคืออะไร?

### DESIGN
ใช้เมื่อ:
- architecture มีผล
- boundary มีผล
- กำลังแตะเรื่อง structure, module, service, feature หรือ abstraction

คำถามหลัก:
- solution ควรมี shape แบบไหน?
- responsibility ควรอยู่ตรงไหน?
- อะไรควรถูกแยกไม่ให้ coupling กัน?

### IMPLEMENT
ใช้เมื่อ:
- plan และ design ชัดพอแล้ว
- ทิศทางไม่ ambiguous แล้ว

คำถามหลัก:
- artifact ไหนที่ต้องเปลี่ยนจริง?
- จะทำ implementation ให้ตรงกับ plan อย่างไร?

### REVIEW
ใช้เมื่อ:
- มี implementation แล้ว
- ต้องการ critique ก่อนอ้างว่างานเสร็จ

คำถามหลัก:
- output ถูกต้องไหม?
- อ่านง่ายไหม?
- ดูแลง่ายไหม?
- มี hidden coupling หรือ technical debt ซ่อนอยู่ไหม?

### VERIFY
ใช้เมื่อ:
- กำลังจะถือว่าผลลัพธ์น่าเชื่อถือ
- ต้องการ confidence ไม่ใช่แค่ output

คำถามหลัก:
- เช็กอะไรไปแล้วจริง?
- อะไรยังไม่ได้เช็ก?
- มั่นใจแค่ไหน?

### FINALIZE
ใช้เมื่อ:
- งานถูกต้องพอจะจัดส่ง
- ต้องเก็บ wording, docs, structure และ presentation

คำถามหลัก:
- deliverable coherent ไหม?
- docs ตรงกันไหม?
- follow-up ถูกบอกไว้ชัดไหม?

### MEMORY
ใช้เมื่อ:
- มี durable decision เกิดขึ้น
- มี recurring pattern ที่ควรรักษาไว้
- มี constraint ที่ควรส่งผลต่อรอบต่อไป

คำถามหลัก:
- อะไรที่ห้ามลืม?
- อะไรที่รอบต่อไปควรรู้ทันที?

---

## 4. รูปแบบการใช้งานที่แนะนำ

## แบบ A — ใช้เป็น toolkit repo แยกเดี่ยว
เหมาะเมื่ออยากได้:
- repo กลางที่เป็น canonical toolkit
- prompts และ overlays รวมศูนย์
- base repo ที่ใช้ข้ามหลายโปรเจกต์

## แบบ B — ใช้เป็น submodule ใน project จริง
เหมาะเมื่ออยากได้:
- source of truth เดียว
- แต่ละโปรเจกต์ consume toolkit ตรง ๆ
- reuse ข้ามหลาย repo ได้ง่าย

ตัวอย่าง:

```bash
git submodule add <toolkit-repo-url> toolkit
```

## แบบ C — คัดลอกเฉพาะบางไฟล์
เหมาะเมื่อ:
- ทีมยังไม่พร้อมใช้ submodule
- โปรเจกต์ต้องการ setup ที่เบากว่า
- ต้องการแค่ governance, prompts หรือ templates

---

## 5. โฟลเดอร์หลักแต่ละส่วนมีไว้ทำอะไร

## `AGENTS.md`
นี่คือ root contract

มันควรบอก AI ว่า:
- repo นี้คืออะไร
- ต้องเดิน lifecycle แบบไหน
- อะไรที่ห้าม assume
- ควรคิดเรื่อง boundary, docs, verification และ memory อย่างไร

ให้ถือว่านี่คือไฟล์แรกที่ AI ควรอ่าน

## `docs/`
อธิบายเรื่อง usage, architecture, adoption และวินัยด้าน release

ถ้า toolkit เปลี่ยนอย่างมีนัยสำคัญ docs ก็ควรถูกอัปเดต

## `prompts/`
นี่คือ stage-oriented prompts

ไม่ใช่ไฟล์ convenience แบบสุ่ม ๆ  
แต่มัน encode workflow ที่แนะนำไว้

## `agent_team/`
define role model เริ่มต้น:
- lead
- architect
- builder
- reviewer
- verifier
- finalizer
- memory

## `skills/`
เป็น capability แบบแคบและ reusable

ตัวอย่าง:
- repo audit
- architecture review
- verification pass
- dependency review
- bug investigation

## `core/`
เป็นวัสดุเชิงแนวคิดที่ใช้ร่วมกัน:
- rules
- verification baseline
- review checklist
- skill routing
- risk model

## `templates/`
ช่วยให้เอา toolkit ไป apply กับ repo อื่นได้ง่าย

## `overlays/`
ช่วย specialize foundation ให้เข้ากับ stack จริง

## `examples/`
แสดงตัวอย่างการใช้งานจริงและ prompt shape

## `project_memory/`
เป็นโครง baseline สำหรับ durable memory

---

## 6. วิธีใช้กับ Codex

คำสั่งเริ่มต้นที่แนะนำ:

```text
Follow AGENTS.md strictly.
Use the lifecycle:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
Use prompts and skills from the toolkit when relevant.
Do not introduce stack-specific assumptions into the foundation layer.
```

### รูปแบบการใช้ Codex ที่ดี
1. ให้ Codex อ่าน `AGENTS.md`
2. ให้มันอ่าน docs ที่เกี่ยวข้อง:
   - `docs/how_to_use.md`
   - `docs/architecture.md`
   - `docs/overlays.md`
3. ให้มันเลือก overlay ที่เหมาะ ถ้าเป็น consuming project
4. ให้มันทำงานผ่าน lifecycle
5. ให้มันอัปเดต memory เมื่อมี durable decision

### รูปแบบการใช้ Codex เพื่อตรวจทาน
ใช้:
- `docs/codex-review-prompt.md`
- `scripts/codex-final-review-prompt.txt`

---

## 7. วิธีใช้กับ Claude Code

Claude Code ทำงานได้ดีมากกับ role model

ลำดับที่แนะนำ:
1. LEAD วางกรอบงาน
2. ARCHITECT วางโครงสร้าง
3. BUILDER ลงมือทำ
4. REVIEWER ตรวจ
5. VERIFIER validate
6. FINALIZER เก็บงาน
7. MEMORY บันทึก durable note

ตัวอย่างคำสั่ง:

```text
Use AGENTS.md as the system contract.

Simulate this role sequence:
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY

Do not collapse roles unless the task is trivial.
```

---

## 8. วิธีเลือก overlay

### เลือก `mobile-flutter` ถ้า:
- โปรเจกต์เป็น Flutter app
- app layers มีผล
- localization, navigation และ UI state สำคัญ

### เลือก `backend-node` ถ้า:
- โปรเจกต์เป็น API หรือ backend service
- ต้องการวินัยเรื่อง service/adapters/contracts

### เลือก `web-frontend` ถ้า:
- โปรเจกต์เป็น web UI หนัก
- hierarchy ของ component และ design system สำคัญ

### เลือก `python-service` ถ้า:
- โปรเจกต์เป็น FastAPI service, worker, automation tool หรือ integration layer

### กฎสำคัญ
overlay มีไว้ “ต่อยอด” foundation  
ไม่ใช่เขียนทับ identity ของ foundation

---

## 9. วิธี bootstrap repo ใหม่ด้วย toolkit นี้

แนวทางที่แนะนำ:

### Step 1
เพิ่ม toolkit เป็น submodule หรือคัดลอกไฟล์ที่เลือก

### Step 2
เพิ่มหรืออ้างอิง:
- `AGENTS.md`
- `templates/project-bootstrap/README_BOOTSTRAP.md`

### Step 3
เพิ่มไฟล์ project memory:
- `templates/project_memory/decisions.md`
- `templates/project_memory/known_constraints.md`
- `templates/project_memory/patterns.md`

### Step 4
เลือก overlay ที่เหมาะหนึ่งตัวถ้าจำเป็น

### Step 5
เพิ่ม project-specific verification commands

### Step 6
เพิ่ม project-specific CI

### Step 7
ลองรัน feature จริงหนึ่งอันผ่าน lifecycle เต็ม

---

## 10. วิธีใช้ project memory ให้ถูก

project memory ควรเก็บ:
- durable decisions
- approved patterns
- known constraints
- recurring pitfalls
- future reminders

project memory ไม่ควรกลายเป็น:
- noisy logs
- random observations
- temporary scratchpad ที่รก

ตัวอย่าง memory entry ที่ดี:
- Decision: ใช้ adapter boundary สำหรับ payment gateway
- Why: ป้องกัน vendor lock-in และทำให้ domain logic สะอาด
- Consequence: code ของ payment provider ทั้งหมดต้องอยู่หลัง adapter interface

ตัวอย่างที่ไม่ดี:
- “วันนี้คุยกันว่าอาจจะเปลี่ยนอะไรบางอย่างทีหลัง”

---

## 11. วิธี review ให้ดีด้วย toolkit นี้

review ที่ดีควรตรวจ:
- correctness
- clarity
- maintainability
- architecture fit
- verification evidence
- doc alignment

review ที่อ่อนจะพูดว่า:
- “Looks good”

review ที่ดีจริงจะบอกว่า:
- อะไรดี
- อะไรเสี่ยง
- อะไรยังไม่ verify
- อะไรควรแก้ก่อน approve

---

## 12. วิธี verify ให้ดีด้วย toolkit นี้

verification ต้องซื่อตรง

ควรบอกชัดว่า:
- เช็กอะไร
- เช็กอย่างไร
- อะไรยังไม่แน่ใจ

อย่าแกล้งทำเหมือน verified แล้ว ทั้งที่เป็นแค่การ reasoning

---

## 13. ความผิดพลาดที่เจอบ่อย

### Mistake 1
เอา assumption ของ Flutter หรือ Node ไปใส่ใน root ของ toolkit

### Mistake 2
ใช้ prompts โดยไม่อ่าน `AGENTS.md`

### Mistake 3
ข้าม memory update หลังมี decision สำคัญ

### Mistake 4
ทำเหมือน review กับ verification คืออย่างเดียวกัน

### Mistake 5
ปล่อยให้ overlays ไปเขียนทับ identity ของ foundation

---

## 14. แบบฝึกหัดแรกที่แนะนำ

ลองทำ sequence นี้กับโปรเจกต์จริงหนึ่งตัว:

1. เพิ่ม toolkit เป็น submodule
2. เลือก overlay หนึ่งตัว
3. คัดลอก memory templates
4. ขอให้ AI ทำ feature ขนาดกลางหนึ่งอัน
5. บังคับให้มันผ่าน:
   - plan
   - design
   - implement
   - review
   - verify
   - finalize
   - memory
6. ประเมินคุณภาพ output
7. ปรับ overlay หรือ local repo rules ตามสิ่งที่ได้เรียนรู้

---

## 15. คำแนะนำสุดท้าย

ใช้ toolkit นี้เป็น “ระบบ” ไม่ใช่เป็นถุงรวมไฟล์

คุณค่าหลักไม่ได้อยู่ที่ prompt ตัวใดตัวหนึ่ง  
แต่อยู่ที่การรวมกันของ:
- governance ที่ explicit
- flow แบบแยก stage
- role ที่แยกกันชัด
- skills ที่ reusable
- verification ที่ซื่อตรง
- durable memory
