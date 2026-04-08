# agent-engineering-toolkit

Toolkit ระดับ production สำหรับทำ **AI-assisted software engineering แบบมีโครงสร้าง** และไม่ยึดติดกับ stack ใด stack หนึ่ง

รีโปนี้ถูกออกแบบให้เป็น **foundation toolkit** ที่ใช้ซ้ำได้กับ:
- mobile project
- backend service
- web frontend
- ระบบ AI/agent
- monorepo
- internal engineering platform

แนวคิดสำคัญคือ **ไม่ให้ mobile เป็นแกนกลางของระบบอีกต่อไป**  
mobile จะเป็นเพียง **overlay** ตัวหนึ่งเท่านั้น

---

## รีโปนี้มีไว้ทำอะไร

ระบบ AI coding ทั่วไปมักจบแค่ “โยน prompt แล้วให้ generate code”

แต่ toolkit นี้ตั้งใจยกระดับให้เป็น:

- workflow ที่ชัดเจน
- แยก planning, architecture, implementation, review, verification และ memory ออกจากกัน
- ทำ output ให้ deterministic มากขึ้น
- reuse knowledge ข้าม repo ได้
- รองรับหลาย AI surface เช่น Codex CLI, Claude Code, OpenClaw และอื่น ๆ ในอนาคต

รีโปนี้คือ **foundation layer**  
ส่วน rule ที่เฉพาะกับ project ใด project หนึ่งควรไปอยู่ใน overlay หรือ repo ที่ consume toolkit นี้

---

## โมเดลการทำงานหลัก

lifecycle หลัก:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

team model หลัก:

```text
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY
```

---

## มีอะไรให้ในชุดนี้

### Governance
- `AGENTS.md`
- operating rules ที่ใช้ซ้ำได้
- expectation ด้าน architecture และ verification

### Prompt pipeline
- prompt สำหรับ plan
- prompt สำหรับ architecture
- prompt สำหรับ implementation
- prompt สำหรับ review
- prompt สำหรับ verification
- prompt สำหรับ finalize
- prompt สำหรับ memory update

### Skill system
- capability แบบแคบและ reusable
- ตัวช่วย audit และ architecture review
- guidance สำหรับ skill router และ risk model

### Templates
- template สำหรับ bootstrap project
- template สำหรับ runbook
- template สำหรับ project memory
- template สำหรับ review
- template สำหรับ verification

### Overlays
- `mobile-flutter`
- `backend-node`
- `web-frontend`
- `python-service`

### Examples
- ตัวอย่าง prompt
- ตัวอย่าง workflow
- ตัวอย่าง integration

### CI
- workflow เบื้องต้นสำหรับ validate ตัว toolkit เอง

---

## โครงสร้างรีโป

```text
agent-engineering-toolkit/
├─ AGENTS.md
├─ README.md
├─ README_TH.md
├─ docs/
├─ prompts/
├─ agent_team/
├─ skills/
├─ core/
├─ templates/
├─ overlays/
├─ examples/
├─ project_memory/
├─ scripts/
└─ .github/workflows/
```

---

## เริ่มใช้งานเร็ว

### 1) ใช้เป็น toolkit repo เดี่ยว
clone แล้ว push เป็นรีโปใหม่ได้เลย

### 2) ใช้เป็น submodule ใน repo อื่น
```bash
git submodule add <toolkit-repo-url> toolkit
```

### 3) ใช้กับ AI coding surface
เริ่มด้วยคำสั่งแนวนี้:

```text
Follow AGENTS.md strictly.
Use the full pipeline:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

---

## use case ที่เหมาะ

### use case 1: ฐานสำหรับ mobile toolkit
ใช้รีโปนี้เป็นฐาน แล้วค่อย apply:
- `overlays/mobile-flutter`
- rule ที่เฉพาะ Flutter
- verification ของ Flutter
- prompt ของ Flutter

### use case 2: backend platform
ใช้:
- `overlays/backend-node` หรือ `overlays/python-service`
- กฎด้าน API และ service architecture
- แนวทาง adapter-based integration

### use case 3: web product
ใช้:
- `overlays/web-frontend`
- กฎของ design system ฝั่ง frontend
- convention สำหรับ operator dashboard

### use case 4: internal engineering platform
ใช้:
- team model เต็ม
- skill router
- runbook templates
- memory system
- verification gates

---

## ลำดับการนำไปใช้ที่แนะนำ

### Phase 1 — Foundation adoption
นำไปใช้ก่อน:
- `AGENTS.md`
- prompt pipeline
- project memory
- repo audit และ architecture review skills

### Phase 2 — Team workflow
ค่อยเพิ่ม:
- role แบบ lead/architect/builder/reviewer/verifier
- runbooks
- verification gate
- review templates

### Phase 3 — Overlay specialization
เพิ่ม:
- mobile/backend/web/python overlay
- คำสั่งเฉพาะ repo
- verification และ CI ที่เฉพาะ project

### Phase 4 — Platform integration
เชื่อมกับ:
- Codex CLI
- Claude Code Agent Teams
- OpenClaw gateway
- CI/CD pipeline
- internal dashboard

---

## เอกสาร

- `docs/how-to-use.md` — คู่มือภาษาอังกฤษแบบละเอียด
- `docs/how-to-use_TH.md` — คู่มือภาษาไทยแบบละเอียด
- `docs/architecture.md` — โมเดล architecture
- `docs/agent-team-system.md` — อธิบายระบบ agent team
- `docs/prompt-pipeline.md` — flow ของ prompt
- `docs/overlays.md` — กลยุทธ์การใช้ overlay
- `docs/real-world-integration.md` — แนวทางเชื่อมกับงานจริง
- `docs/repo-bootstrap.md` — วิธีเอา toolkit ไปเริ่ม repo ใหม่
- `docs/roadmap.md` — แนวทางต่อยอด

---

## Checklist ก่อน push

ก่อน push ขึ้นจริง ควรแก้:
- URL ของ repo
- metadata ของผู้เขียน
- license
- ถ้อยคำที่เฉพาะกับองค์กรของคุณ
