# Tutorial (ภาษาไทย) — คู่มือสอนใช้งานแบบ Step-by-Step

tutorial นี้สอนผู้ใช้ใหม่ให้ใช้ toolkit นี้ตั้งแต่ศูนย์

---

## เป้าหมายของ tutorial

เมื่อจบคู่มือนี้ คุณควรจะ:
- เข้าใจโครงสร้าง repo
- ใช้ toolkit กับ repo จริงได้
- เลือก overlay เป็น
- รัน feature หนึ่งอันผ่าน lifecycle เต็มได้
- อัปเดต project memory ได้ถูกต้อง

---

## Part 1 — อ่านไฟล์ขั้นต่ำก่อน

ก่อนทำอย่างอื่น ให้อ่านไฟล์เหล่านี้ตามลำดับ:

1. `README.md`
2. `AGENTS.md`
3. `docs/how_to_use.md`
4. `docs/architecture.md`
5. `docs/overlays.md`
6. `docs/agent-team-system.md`
7. `docs/prompt-pipeline.md`

สิ่งที่คุณจะได้:
- เข้าใจ identity ของ repo
- เข้าใจ workflow
- เข้าใจกลยุทธ์ overlay
- เข้าใจ role model
- เข้าใจ flow ของ prompt

---

## Part 2 — ตัดสินใจว่าจะ adopt toolkit แบบไหน

เลือกหนึ่งแบบ:

### Option A — ใช้เป็น toolkit repo กลาง
เหมาะกับทีมที่มีหลายโปรเจกต์

### Option B — เอาไปเป็น submodule
เหมาะกับโปรเจกต์จริงที่ต้อง consume toolkit ตรง ๆ

### Option C — คัดลอกเฉพาะบางไฟล์
เหมาะกับทีมเล็กหรือ setup เบา

สำหรับ tutorial นี้ ให้สมมติว่าใช้ Option B

---

## Part 3 — เพิ่ม toolkit เข้า repo จริง

ในโปรเจกต์จริงของคุณ:

```bash
git submodule add <toolkit-repo-url> toolkit
```

จากนั้น commit การเพิ่ม submodule

---

## Part 4 — เลือก overlay

เข้าไปดูใน `overlays/`

เลือกหนึ่งตัว:
- `mobile-flutter`
- `backend-node`
- `web-frontend`
- `python-service`

ตัวอย่าง:
- ถ้า repo จริงเป็น Flutter → เลือก `mobile-flutter`
- ถ้า repo เป็น FastAPI → เลือก `python-service`

อ่าน:
- `README.md` ของ overlay
- `AGENTS.overlay.md` ของ overlay

---

## Part 5 — bootstrap repo จริง

คัดลอกหรือดัดแปลง:
- `AGENTS.md`
- `templates/project-bootstrap/README_BOOTSTRAP.md`
- `templates/project_memory/decisions.md`
- `templates/project_memory/known_constraints.md`
- `templates/project_memory/patterns.md`

จากนั้นเพิ่ม:
- project-specific verification commands
- project-specific CI
- project-specific architecture constraints

กฎสำคัญ:
กติกาที่เฉพาะ project ให้อยู่ใน consuming repo

อย่าเอากลับมายัดใน foundation ถ้ามันไม่ได้ reusable กว้างพอ

---

## Part 6 — ลองรัน feature จริงหนึ่งอัน

ตัวอย่าง feature:
“เพิ่มหน้า profile settings”

ใช้ prompts ตามลำดับนี้:

1. `prompts/plan_change.md`
2. `prompts/architecture_review.md`
3. `prompts/implement_change.md`
4. `prompts/review_change.md`
5. `prompts/verification_pass.md`
6. `prompts/finalize_change.md`
7. `prompts/update_project_memory.md`

คุณจะทำแบบ:
- manual
- ผ่าน Codex
- ผ่าน Claude Code
- ผ่าน orchestration system อื่น

ก็ได้

---

## Part 7 — ประเมิน output

หลังรันเสร็จ ให้ถามว่า:

### คุณภาพของ planning
- assumptions explicit ไหม?
- scope ชัดไหม?
- risk ถูกเรียกชื่อไหม?

### คุณภาพของ architecture
- boundary ชัดไหม?
- coupling ลดลงไหม?
- โครงสร้างที่เสนอ sensible ไหม?

### คุณภาพของ implementation
- change ตรงกับ plan ไหม?
- readability ยังดีไหม?

### คุณภาพของ review
- review พูดอะไรที่มีความหมายไหม?
- ระบุ risk ได้ไหม?

### คุณภาพของ verification
- checks เป็นของจริงไหม?
- uncertainty ถูกบอกอย่างซื่อตรงไหม?

### คุณภาพของ memory
- durable decisions ถูกเก็บจริงไหม?

---

## Part 8 — ปรับปรุงจากสิ่งที่เรียนรู้

หลังจากลอง feature จริงหนึ่งอัน ให้ปรับ:
- local repo rules
- wording ของ overlay
- โครงสร้าง project memory
- verification commands
- ความคาดหวังของ review

จุดนี้สำคัญ:
toolkit จะโตจากการใช้งานจริง ไม่ใช่จากทฤษฎีอย่างเดียว

---

## Part 9 — ใช้ Codex ตรวจ toolkit หรือ consuming repo

ใช้:
- `docs/codex-review-prompt.md`
- `scripts/codex-final-review-prompt.txt`

สั่ง Codex ให้:
- หา foundation vs overlay leakage
- หา docs ที่ซ้ำหรือฟุ้ง
- หาจุดที่ prompt stages อ่อน
- หาไฟล์ที่ยังขาดหรือ adoption guidance ที่ยังไม่พอ

---

## Part 10 — ทำซ้ำและพัฒนาให้ mature

หลังผ่านงานจริงหลายรอบ:
- ทำ overlay ให้คมขึ้น
- ทำ verification expectations ให้ชัดขึ้น
- ปรับ memory format ให้ดีขึ้น
- update examples ตามสิ่งที่ใช้จริง
- ตัดสิ่งที่ vague หรือซ้ำซ้อนออก

นี่คือวิธีที่ทำให้ toolkit นี้ mature ในโลกจริง
