# Tutorial (ภาษาไทย) — คู่มือสอนใช้งานแบบ Step-by-Step

tutorial นี้แสดงตัวอย่างการใช้งานครั้งแรกแบบครบวงจรหนึ่งรอบ

## เป้าหมาย
เมื่อจบคู่มือนี้ คุณควรจะ:
- เลือก overlay ได้ถูก
- พางานผ่าน canonical lifecycle ได้
- ไม่เอา rule เฉพาะ stack ไปปนใน foundation
- บันทึก memory ที่เป็น durable note ได้

## Scenario
repo ที่ consume toolkit ต้องเพิ่ม capability สำหรับ account preferences

ให้ใช้ toolkit เป็นโครงหลักของ workflow แล้วเลือก overlay ใน repo ที่จะใช้งานจริง

## Step 1 — อ่านชุดไฟล์ขั้นต่ำ
อ่านไฟล์เหล่านี้ก่อน:
1. `README.md`
2. `AGENTS.md`
3. `docs/how-to-use.md`
4. `docs/architecture.md`
5. `docs/overlays.md`
6. `docs/agent-team-system.md`
7. `docs/prompt-pipeline.md`
8. `docs/tutorials/index.md`
9. `docs/tutorials/agents-and-prompts.md`

tutorial hub ถูกแยกเป็น platform folders ดังนี้:
- `docs/tutorials/flutter/`
- `docs/tutorials/web/`
- `docs/tutorials/services/`
- `docs/tutorials/team/`

## Step 2 — เลือกวิธี adopt
เลือกหนึ่งแบบ:
- toolkit repo กลาง
- submodule ในโปรเจกต์จริง
- คัดลอกเฉพาะบางไฟล์

ถ้าเป็น repo จริง วิธีที่พบบ่อยคือ:
```bash
git submodule add <toolkit-repo-url> toolkit
```

## Step 3 — เลือก overlay
อ่าน overlay ที่ตรงกับ repo:
- `overlays/mobile-flutter/README.md`
- `overlays/backend-node/README.md`
- `overlays/web-frontend/README.md`
- `overlays/python-service/README.md`

ถ้าไม่มีอันไหนตรง ให้คง foundation ไว้และเก็บ rule เฉพาะ stack ไว้ใน consuming repo

## Step 4 — วางแผน
รูปแบบ output ของ planning ควรมี:
- restatement ของ task: เพิ่ม account preferences capability
- facts: repo นี้ใช้ toolkit เป็น foundation
- assumptions: stack จะชัดหลังเลือก overlay
- constraints: root ต้อง stack-agnostic
- risks: boundary leak, ownership ไม่ชัด, verification ไม่พอ
- next prompt: architecture review

## Step 5 — กำหนดโครงสร้าง
architecture output ควรบอก layer ให้ชัด

ตัวอย่างโครงสร้างสำหรับ consuming repo:
- transport layer: route, handler หรือ controller
- orchestration layer: service หรือ use-case
- persistence layer: repository หรือ data-access
- adapter layer: boundary ของ external provider

Builder guardrails:
- อย่าใส่ business rule ไว้ใน transport code
- อย่าเรียก external provider ตรงจากโมดูลที่ไม่เกี่ยว
- อย่าให้ repository ทำ response shaping

## Step 6 — Implement
builder แก้ artifact ใน consuming repo

ตัวอย่าง implementation note:
- files changed: transport, service, repository และ adapter layers
- deviations: เฉพาะที่ architecture review อนุมัติ

## Step 7 — Review
reviewer ต้องแยก strengths กับปัญหาให้ชัด

ตัวอย่างผล review:
- strength: handler บางและชัด
- blocking issue: repository มี business logic
- non-blocking issue: ยังไม่มี example coverage
- architecture fit: ผ่านได้ก็ต่อเมื่อแก้ blocking issue แล้ว

## Step 8 — Verify
verification ต้องบอกว่ารันอะไรไปจริง

ตัวอย่าง checks:
```bash
bash scripts/check-public-repo.sh
```

ถ้าคุณกำลังเช็ก toolkit repository นี้ ให้รัน public-repo gate
ใน consuming repo ให้รัน stack checks ของตัวเองด้วย เช่น lint, tests หรือ startup sanity

ตัวอย่าง verification summary:
- checks performed: public-repo gate, local tests, startup sanity
- evidence: output ของ command และไฟล์ที่เปลี่ยน
- remaining uncertainty: integration coverage ยังไม่ครบ
- confidence: medium หรือ high ตาม evidence

## Step 9 — Finalize
finalizer ควรสรุปงานให้ชัด

ตัวอย่าง final summary:
- เพิ่ม account preferences capability โดยคง boundary ให้ชัด
- review กับ verification แยกจากกัน
- follow-up ที่เหลือ: เพิ่ม integration test 1 ตัว

## Step 10 — Update memory
เก็บเฉพาะ note ที่ durable

ตัวอย่าง memory entry:
- account preference handlers ต้องบาง
- response shaping ต้องอยู่นอก repository
- overlay ที่เลือกสำหรับ repo นี้คือ `<chosen-overlay>`

## Step 11 — Audit
ใช้ prompt แบบ role-based เมื่ออยากให้อีก agent ทำ audit:
- `prompts/review/audit_repo.md`

ใช้ invocation template เมื่ออยากได้ prompt แบบ paste ได้ทันที:
- `docs/strict-audit-prompt.md`

## helper เสริม
ถ้าอยากมี helper สำหรับ bootstrap memory templates ให้ใช้ script นี้:
```bash
bash scripts/bootstrap-project-memory.sh
```
