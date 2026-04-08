# Tutorial (ภาษาไทย) — คู่มือสอนใช้งานแบบ Step-by-Step

tutorial นี้สอนผู้ใช้ใหม่ให้ใช้ toolkit นี้ตั้งแต่ศูนย์

## เป้าหมายของ tutorial
เมื่อจบคู่มือนี้ คุณควรจะ:
- เข้าใจโครงสร้าง repo
- ใช้ toolkit กับ repo จริงได้
- เลือก overlay เป็น
- รัน feature หนึ่งอันผ่าน lifecycle เต็มได้
- อัปเดต project memory ได้ถูกต้อง

## Part 1 — อ่านไฟล์ขั้นต่ำก่อน
อ่านไฟล์เหล่านี้ตามลำดับ:
1. `README.md`
2. `AGENTS.md`
3. `docs/how-to-use.md`
4. `docs/architecture.md`
5. `docs/overlays.md`
6. `docs/agent-team-system.md`
7. `docs/prompt-pipeline.md`

## Part 2 — ตัดสินใจว่าจะ adopt toolkit แบบไหน
เลือกหนึ่งแบบ:
- toolkit repo กลาง
- submodule ในโปรเจกต์จริง
- คัดลอกเฉพาะบางไฟล์

## Part 3 — เพิ่ม toolkit เข้า repo จริง
```bash
git submodule add <toolkit-repo-url> toolkit
```

## Part 4 — เลือก overlay
อ่าน overlay README และ AGENTS.overlay ที่ตรงกับ stack ของคุณ

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

## Part 6 — ลองรัน feature จริงหนึ่งอัน
ใช้ canonical prompt order จาก `docs/prompt-pipeline.md`

## Part 7 — ประเมิน output
ตรวจ:
- คุณภาพ planning
- คุณภาพ architecture
- คุณภาพ implementation
- คุณภาพ review
- คุณภาพ verification
- คุณภาพ memory

## Part 8 — ปรับปรุงจากสิ่งที่เรียนรู้
ปรับ:
- local repo rules
- wording ของ overlay
- โครงสร้าง project memory
- verification commands
- ความคาดหวังของ review

## Part 9 — ใช้ AI audit
ใช้:
- `docs/codex-review-prompt.md`
- `scripts/codex-final-review-prompt.txt`

## Part 10 — ทำซ้ำและพัฒนาให้ mature
หลังผ่านงานจริงหลายรอบ:
- ทำ overlay ให้คมขึ้น
- ทำ verification expectations ให้ชัดขึ้น
- ปรับ memory format
- update examples
- ตัดสิ่งที่ vague หรือซ้ำซ้อนออก
