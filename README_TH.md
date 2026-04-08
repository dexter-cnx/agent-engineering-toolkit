# agent-engineering-toolkit

Toolkit ระดับ production สำหรับทำ AI-assisted software engineering แบบมีโครงสร้าง และไม่ยึดติดกับ stack ใด stack หนึ่ง

รีโปนี้ถูกออกแบบให้เป็น foundation toolkit ที่ใช้ซ้ำได้กับ:
- mobile project
- backend service
- web frontend
- ระบบ AI และ agent
- monorepo
- internal engineering platform

แนวคิดสำคัญคือไม่ให้ mobile เป็นแกนกลางของระบบอีกต่อไป mobile จะเป็นเพียง overlay ตัวหนึ่งเท่านั้น

## รีโปนี้มีไว้ทำอะไร

ระบบ AI coding ทั่วไปมักจบแค่ “โยน prompt แล้วให้ generate code”

แต่ toolkit นี้ตั้งใจยกระดับให้เป็น:
- operating model ที่ใช้ซ้ำได้
- prompt pipeline แบบเป็น stage
- agent team model
- skill แบบ reusable และเฉพาะทาง
- template สำหรับ bootstrap โปรเจกต์
- overlay สำหรับ specialization ตาม stack
- วินัยด้านเอกสารเพื่อให้ดูแลได้ยาว
- hygiene สำหรับ public repository

รีโปนี้คือ foundation layer ส่วน rule ที่เฉพาะกับ project ควรไปอยู่ใน overlay หรือ repo ที่ consume toolkit นี้

## lifecycle หลัก

canonical lifecycle ถูกกำหนดไว้ใน `docs/prompt-pipeline.md`

short form คือ:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

## team model หลัก

```text
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY
```

## มีอะไรให้ในชุดนี้

- `AGENTS.md` สำหรับ governance และความคาดหวังของระบบ
- `docs/` สำหรับคู่มือใช้งาน, architecture, adoption, release และ tutorial
- `prompts/` สำหรับ workflow ตาม stage
- `agent_team/` สำหรับคำอธิบาย role
- `skills/` สำหรับ capability แบบ reusable
- `core/` สำหรับ rules, routing, verification และ review discipline
- `templates/` สำหรับ bootstrap และ operational consistency
- `overlays/` สำหรับ stack-specific extensions
- `examples/` สำหรับ adoption patterns และ worked examples
- `.github/` สำหรับ CI, issue templates, PR template, CODEOWNERS และ security policy
- `.gitignore` สำหรับ hygiene ของ repo

## เริ่มใช้งานเร็ว

### ใช้เป็นรีโปหลักของ toolkit
push รีโปนี้ตรง ๆ แล้วใช้เป็นแหล่งกลาง

### ใช้เป็น submodule
```bash
git submodule add <toolkit-repo-url> toolkit
```

### ใช้กับ AI tooling
เริ่มด้วยคำสั่งแนวนี้:

```text
Follow AGENTS.md strictly.
Use the canonical lifecycle from docs/prompt-pipeline.md.
```

## เอกสาร

- `docs/how-to-use.md` — คู่มือภาษาอังกฤษหลัก
- `docs/how-to-use_TH.md` — คู่มือภาษาไทยหลัก
- `docs/tutorial.md` — tutorial ภาษาอังกฤษ
- `docs/tutorial_TH.md` — tutorial ภาษาไทย
- `docs/architecture.md` — architecture ของ foundation vs overlay
- `docs/agent-team-system.md` — คำอธิบายระบบ role
- `docs/prompt-pipeline.md` — canonical lifecycle reference
- `docs/overlays.md` — กลยุทธ์การใช้ overlay
- `docs/real-world-integration.md` — แนวทางใช้งานจริง
- `docs/repo-bootstrap.md` — วิธีเอา toolkit ไปเริ่ม repo ใหม่
- `docs/public-repo-checklist.md` — checklist ก่อน publish
- `docs/release-process.md` — วิธีจัด release
- `docs/codex-review-prompt.md` — prompt สำหรับให้ Codex ตรวจทานแบบเข้ม

## License

MIT
