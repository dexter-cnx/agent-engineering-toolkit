---
tags:
  - agent-engineering-toolkit
  - tutorial
  - blank-folder
aliases:
  - Common Start
  - Blank Folder Bootstrap
---

# เริ่มจากโฟลเดอร์เปล่า

ใช้โน้ตนี้เมื่อคุณมีโฟลเดอร์ว่างและอยากเริ่มโปรเจกต์จริงด้วย toolkit

## เป้าหมาย

เมื่อจบขั้นตอนเริ่มต้นนี้ คุณควรได้:

- repo ที่ initialize แล้วในโฟลเดอร์เปล่า
- toolkit ที่อ้างอิงหรือคัดลอกเข้ามาแล้ว
- `AGENTS.md` ที่ root ของ repo
- project memory templates ที่พร้อมใช้งาน
- overlay ที่เลือกไว้แล้ว ถ้า stack ชัดเจน
- ลำดับ prompt ที่ชัดเจนสำหรับงานจริง

## ต้องทำอะไรก่อน

1. สร้างโฟลเดอร์ว่าง
2. initialize git
3. เพิ่ม toolkit ด้วย submodule หรือคัดลอกไฟล์ที่ต้องใช้
4. สร้างหรือปรับ `AGENTS.md` ที่ root ของ repo
5. คัดลอก project memory templates
6. เลือก overlay ที่ถูกต้อง
7. รันงานจริงหนึ่งชิ้นผ่าน lifecycle ให้ครบ

ตัวอย่างคำสั่ง bootstrap:

```bash
mkdir my-project
cd my-project
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
```

ถ้าคุณมี toolkit checkout อยู่แล้วในเครื่อง คุณค่อยใช้ helper script จาก checkout นั้นได้

- เพิ่ม toolkit repository
- สร้าง `project_memory/`
- คัดลอก `templates/project_memory/*`
- สร้าง `AGENTS.md`
- ตัดสินใจว่า overlay ไหนควรอยู่ใน repo นี้ ถ้า stack ของ repo ชัดเจนแล้ว

## prompts ที่ควรใช้

prompt เหล่านี้จะใช้บ่อยใน tutorial ชุดนี้:

| Stage | Prompt | ใช้ทำอะไร |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | ตัดสินว่า toolkit เข้ากับโฟลเดอร์เปล่านี้อย่างไร |
| Plan | `prompts/planning/plan_change.md` | แปลง request ให้เป็นแผนที่ชัดเจน |
| Architecture | `prompts/design/architecture_review.md` | กำหนด boundary และ guardrail |
| Implement | `prompts/implementation/implement_change.md` | ลงมือแก้ไฟล์จริง |
| Review | `prompts/review/review_change.md` | วิจารณ์ implementation |
| Verify | `prompts/verification/verification_pass.md` | บอกว่าตรวจอะไรไปแล้วและยังไม่แน่ใจอะไร |
| Finalize | `prompts/finalization/finalize_change.md` | จัดรูปผลลัพธ์ให้เรียบร้อย |
| Memory | `prompts/memory/update_project_memory.md` | เก็บเฉพาะ decision และ constraint ที่ควรจำ |

## skills ที่ควรอยู่ใกล้มือ

อ่าน skill cards เหล่านี้เมื่อ task ตรงกับหน้าที่ของมัน:

- `skills/skill-router/README.md`
- `skills/risk-scoring/README.md`
- `skills/architecture-review/README.md`
- `skills/verification-pass/README.md`
- `skills/docs-update/README.md`
- `skills/repo-audit/README.md`
- `skills/safe-refactor/README.md`

## scripts ที่ควรรู้จัก

- `scripts/bootstrap-project-memory.sh` สำหรับเพิ่ม submodule และคัดลอก memory templates
- `scripts/check-public-repo.sh` สำหรับตรวจ public-release hygiene ของ toolkit

## AGENTS.md ที่ควรสร้างก่อน

เริ่มจาก `AGENTS.md` แบบสั้นและใช้งานได้จริงก่อน แล้วค่อยเติม stack-specific rules ทีหลัง

สิ่งที่ควรมีอย่างน้อย:

- repository identity ว่า repo นี้คืออะไร
- default tech stack หรือ platform ที่ใช้
- architecture / boundary rules แบบสั้น
- workflow และ verification rules
- stack-specific notes แบบสั้น ๆ ว่าจะใช้ overlay ไหน

ถ้ารู้ platform แล้ว ให้เลือกทิศทางนี้:

- เลือก overlay ที่ตรงกับ stack นั้นจาก [docs/overlays.md](../overlays.md)
- ถ้ายังไม่ชัดเจน ให้เริ่ม foundation-only แล้วค่อยเพิ่ม overlay ทีหลังเมื่อ stack ตกผลึก

อ่านตัวอย่างและ prompt flow เพิ่มเติมได้ที่ [AGENTS.md และ prompt guide](./agents-and-prompts.md)

## pitfall ที่พบบ่อย

- ข้าม `AGENTS.md`
- ใส่ assumption แบบ stack-specific ลงใน foundation root
- สับสนระหว่าง review กับ verification
- คิดว่า helper script ทำทุกอย่างให้ครบ
- ลืมอัปเดต project memory เมื่อมี decision ที่ควรจำถาวร

## ขั้นต่อไป

เปิด tutorial เฉพาะ stack ในโฟลเดอร์นี้ แล้วไปต่อจากจุดนั้น
