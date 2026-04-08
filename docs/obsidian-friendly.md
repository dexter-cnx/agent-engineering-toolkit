---
tags:
  - agent-engineering-toolkit
  - obsidian
  - ai-workflow
aliases:
  - Toolkit MOC
  - Toolkit Reference
---

# Obsidian-Friendly Reference

โน้ตนี้รวบรวมวิธีใช้ toolkit แบบเปิดอ่านใน Obsidian ได้ง่าย โดยใช้เป็น MOC หรือหน้า index หลักของ repo ได้เลย

## Read First

อ่านไฟล์เหล่านี้ก่อนเสมอ:

| File | Why it matters |
| --- | --- |
| `AGENTS.md` | สัญญาหลักของ repo และกติกาที่ AI ต้องตาม |
| `docs/prompt-pipeline.md` | ลำดับ lifecycle ที่เป็น source of truth |
| `docs/agent-team-system.md` | โมเดลบทบาทของทีม AI |
| `docs/how-to-use.md` | คู่มือใช้งาน canonical ภาษาอังกฤษ |
| `docs/how-to-use_TH.md` | คู่มือใช้งาน canonical ภาษาไทย |
| `docs/tutorial.md` | walkthrough แบบ step-by-step |
| `docs/tutorial_TH.md` | walkthrough ภาษาไทย |
| `docs/tutorials/team/how-to-use-team-agents.md` | guide การใช้ team agents |
| `docs/tutorials/team/how-to-use-team-agents_EN.md` | guide การใช้ team agents (English) |
| `docs/tutorials/index.md` | hub สำหรับ tutorial ภาษาไทย |
| `docs/tutorials/index_EN.md` | hub สำหรับ tutorial ภาษาอังกฤษ |
| `docs/tutorials/agents-and-prompts.md` | guide สำหรับ AGENTS.md และ prompt flow |
| `docs/tutorials/agents-and-prompts_EN.md` | guide สำหรับ AGENTS.md และ prompt flow (English) |
| `docs/overlays.md` | วิธีเลือกและใช้งาน overlays |
| `docs/repo-bootstrap.md` | วิธี bootstrap เข้า repo ใหม่ |
| `docs/public-repo-checklist.md` | checklist ก่อนเปิด public |
| `docs/release-process.md` | แนวทาง release |

## How To Use

### รูปแบบการ adopt

| Pattern | ใช้เมื่อ | สิ่งที่ควรทำ |
| --- | --- | --- |
| Standalone toolkit repo | ต้องการ repo กลางของ toolkit | ใช้ repo นี้เป็น foundation หลัก |
| Git submodule | ต้องการให้หลาย repo consume toolkit เดียวกัน | เพิ่ม toolkit เป็น submodule แล้วอ้างอิงจาก consuming repo |
| Copy selected files | ทีมยังไม่พร้อมใช้ submodule | คัดเฉพาะ governance, prompts, templates ที่จำเป็น |

### ลำดับใช้งาน

1. อ่าน `AGENTS.md`
2. อ่าน `docs/prompt-pipeline.md`
3. อ่าน `docs/agent-team-system.md`
4. เลือก overlay ถ้า repo ปลายทางมี stack ชัดเจน
5. ใช้ lifecycle เดิมกับงานจริง
6. อัปเดต project memory เมื่อมี decision ที่ต้องจำ

### สิ่งที่ไม่ควรลืม

- root ต้อง stack-agnostic
- stack-specific rules อยู่ใน overlays เท่านั้น
- review ไม่ใช่ verification
- prompts ต้องไม่ข้าม `AGENTS.md`

## Tutorial Map

นี่คือภาพย่อของ `docs/tutorial.md` และ tutorial hub ที่แยกตาม platform:

| Step | What happens |
| --- | --- |
| 1 | อ่านไฟล์ขั้นต่ำก่อนเริ่มงาน |
| 2 | เลือก adoption path |
| 3 | เลือก overlay ที่ตรงกับ repo ปลายทาง |
| 4 | เขียน plan ให้ชัด |
| 5 | วาง architecture และ boundary |
| 6 | implement ตาม plan |
| 7 | review ผลลัพธ์ |
| 8 | verify ด้วยคำสั่งจริง |
| 9 | finalize deliverable |
| 10 | update memory |
| 11 | audit ด้วย prompt ที่เหมาะสม |

`docs/tutorials/index.md` และ `docs/tutorials/index_EN.md` จัด tutorial ตาม platform folder:
- `docs/tutorials/flutter/`
- `docs/tutorials/web/`
- `docs/tutorials/services/`
- `docs/tutorials/team/`

ก่อนเริ่มแต่ละ tutorial ให้เปิด `docs/tutorials/agents-and-prompts.md` หรือ `docs/tutorials/agents-and-prompts_EN.md` เพื่อเลือก AGENTS.md และ prompt flow ที่เหมาะกับ stack นั้น

## Skills

ทุก skill เป็น capability แบบ narrow และ reusable ใช้เมื่อ task ตรงกับหน้าที่ของ skill นั้นจริง ๆ

| Skill | Use when | Output | Notes |
| --- | --- | --- | --- |
| `skills/architecture-review/README.md` | งานเปลี่ยน boundary, layer, interface | boundary assessment, risks, structural direction | ไม่ใช่ตัว implement |
| `skills/bug-investigation/README.md` | มี bug แต่ root cause ยังไม่ชัด | likely causes, proposed checks, root-cause path | ห้ามเดาโดยไม่มี evidence |
| `skills/dependency-review/README.md` | เพิ่มหรือเปลี่ยน dependency | risk summary, adapter recommendations, adoption cautions | ช่วยกัน lock-in |
| `skills/docs-update/README.md` | behavior หรือ workflow เปลี่ยนและ docs ต้องตาม | updated docs list, missing-doc warnings, suggested edits | ใช้เพื่อคุม doc drift |
| `skills/repo-audit/README.md` | audit ระดับ repo ก่อน release | issues by severity, file-by-file notes, readiness assessment | มี `skills/repo-audit/checklist.md` เป็น checklist เสริม |
| `skills/risk-scoring/README.md` | task ใหญ่, ข้อมูลยังไม่ชัด, ต้องเลือกระดับความเข้ม | risk level, why it is risky, rigor level | ใช้ก่อนวางงานใหญ่ |
| `skills/safe-refactor/README.md` | refactor โดยไม่เปลี่ยน intended behavior | refactor plan, safety notes, cautions | ไม่ใช่ feature work |
| `skills/skill-router/README.md` | ยังไม่แน่ใจว่าควรใช้ skill ไหนก่อน | suggested skill order, why | ใช้เพื่อจัดลำดับการคิด |
| `skills/verification-pass/README.md` | งานใกล้จบ ต้องสรุปความมั่นใจ | verification summary, uncertainty, confidence level | ห้ามอ้าง check ที่ไม่ได้รัน |

## Prompts

prompts เป็น stage-oriented workflows ให้เลือก prompt ตามบทบาทและ stage ของงาน

| Prompt | Role | Use when | Output |
| --- | --- | --- | --- |
| `prompts/adoption/adopt_toolkit_in_repo.md` | LEAD + ARCHITECT | รับ repo ใหม่เข้าระบบ toolkit | adoption path, overlay, bootstrap files, verification guidance |
| `prompts/design/architecture_review.md` | ARCHITECT | ต้องการโครงสร้างที่ปลอดภัยก่อน implement | boundaries, proposed structure, guardrails |
| `prompts/review/audit_repo.md` | REVIEWER + VERIFIER | audit repo แบบ public readiness | severity findings, file-by-file notes, verdict |
| `prompts/finalization/finalize_change.md` | FINALIZER | review และ verification พอแล้ว | final summary, readiness, follow-ups |
| `prompts/implementation/implement_change.md` | BUILDER | ถึงขั้นลงมือแก้ไฟล์แล้ว | files changed, implementation notes, deviations |
| `prompts/investigation/investigate_bug.md` | REVIEWER + VERIFIER | bug หรือ regression ที่ต้องไล่ root cause | bug restatement, evidence, likely cause, fix strategy |
| `prompts/planning/plan_change.md` | LEAD | งานยังไม่ชัด ต้องแตกเฟสก่อน | restatement, facts, assumptions, constraints, phases |
| `prompts/review/review_change.md` | REVIEWER | มี implementation แล้วต้อง critique | strengths, blocking issues, non-blocking issues |
| `prompts/adoption/scaffold_overlay.md` | ARCHITECT + BUILDER | สร้างหรือปรับ overlay | updated overlay docs, verification examples, rejection criteria |
| `prompts/memory/update_project_memory.md` | MEMORY | มี decision หรือ constraint ที่ต้องจำ | decisions, constraints, patterns, reminders |
| `prompts/verification/verification_pass.md` | VERIFIER | ต้องสรุปสิ่งที่ตรวจจริง | checks, evidence, uncertainty, confidence |

### Audit Note

- ใช้ `prompts/review/audit_repo.md` เมื่ออยากได้ prompt แบบ role-based
- ใช้ `docs/strict-audit-prompt.md` เมื่ออยากได้ prompt แบบ paste-ready
- ใช้ `prompts/index.md` หรือ `prompts/index_EN.md` เป็นทางเข้าหลักถ้าต้องการไล่ตาม stage

## Scripts

| Script / File | Use for | How to use | Pitfall |
| --- | --- | --- | --- |
| `scripts/bootstrap-project-memory.sh` | bootstrap submodule + memory templates | `bash scripts/bootstrap-project-memory.sh [target-dir] <toolkit-repo-url>` | ไม่ได้ทำ bootstrap ทั้งหมดให้ครบ ต้องทำ `AGENTS.md`, overlay, verification เอง |
| `scripts/check-public-repo.sh` | ตรวจว่า public-release files ครบ | `bash scripts/check-public-repo.sh` | ตรวจแค่ existence ไม่ได้ตรวจเนื้อหา |
| `scripts/check-public-repo.paths` | รายการ path ที่ public repo ต้องมี | แก้ไฟล์นี้เมื่อ public contract เปลี่ยน | ถ้าลืมอัปเดต gate จะเช็คผิดรายการ |
| `scripts/push-new-repo.sh` | สร้าง repo ใหม่แล้ว push ครั้งแรก | `bash scripts/push-new-repo.sh <git-remote-url>` | เป็น flow แบบ fresh repo เท่านั้น |
| `scripts/push-guide.md` | คู่มือ push แบบ manual | อ่านเป็น checklist ก่อน release | ไม่ใช่ script ที่ execute ได้ |

## Overlays

overlays คือที่เก็บ stack-specific assumptions และ stack-specific examples

| Overlay | Target stack | What it adds |
| --- | --- | --- |
| `overlays/mobile-flutter/` | Flutter mobile apps | boundary guidance, overlay AGENTS, Flutter examples |
| `overlays/backend-node/` | Node backends / APIs | backend-specific workflow and example structure |
| `overlays/web-frontend/` | browser UI repos | frontend-specific workflow and example structure |
| `overlays/python-service/` | Python services / workers / automation | Python service guidance and example structure |

### วิธีใช้ overlay

1. อ่าน foundation ก่อน
2. เลือก overlay ที่ตรงกับ consuming repo
3. คัดหรือ reference `AGENTS.overlay.md`
4. อ่าน `README.md` ของ overlay
5. ใช้ worked example ของ overlay เป็น pattern
6. อย่าเอา stack-specific rules ย้อนเข้ามาใน root

## Agent Team With Codex And Claude

### หลักการเดียวกัน

ทั้ง Codex และ Claude ควรใช้ workflow เดียวกัน:

1. อ่าน `AGENTS.md`
2. ใช้ `docs/prompt-pipeline.md` เป็น lifecycle หลัก
3. ใช้ `docs/agent-team-system.md` เป็น role model
4. แยก LEAD, ARCHITECT, BUILDER, REVIEWER, VERIFIER, FINALIZER, MEMORY ให้ชัด
5. อย่าข้าม verification
6. อย่าลืม memory เมื่อมี decision ถาวร

### ใช้กับ Codex

- เหมาะกับงานที่ต้องอ่าน repo, แก้ไฟล์, และรันคำสั่งตรวจสอบ
- ใช้ prompt ให้ตรง stage เช่น `plan_change`, `architecture_review`, `implement_change`, `review_change`, `verification_pass`
- ถ้างานใหญ่ ให้แยกบทบาทตาม sequence แทนการยัดทุกอย่างไว้ใน prompt เดียว

### ใช้กับ Claude

- ใช้ prompt และ role sequence เดียวกันกับ Codex
- ถ้าทำงานในครั้งเดียว ให้เขียนบทบาทที่กำลังทำอยู่ในแต่ละช่วงชัด ๆ
- ใช้ output sections เดิมเพื่อให้ review และ verification ไม่ปนกัน
- อย่าพึ่งชื่อเครื่องมือ ให้พึ่ง repo contract และ canonical docs

### Role cards

| File | Role | Responsibility |
| --- | --- | --- |
| `agent_team/lead.md` | LEAD | frame, sequence, decide when structure is needed |
| `agent_team/architect.md` | ARCHITECT | boundaries, structure, interfaces, design integrity |
| `agent_team/builder.md` | BUILDER | implement faithfully to the plan |
| `agent_team/reviewer.md` | REVIEWER | critique correctness, maintainability, readability |
| `agent_team/verifier.md` | VERIFIER | state what was checked and what remains uncertain |
| `agent_team/finalizer.md` | FINALIZER | package the result clearly |
| `agent_team/memory.md` | MEMORY | preserve durable decisions and constraints |

## Tips And Pitfalls

- อ่าน `AGENTS.md` ก่อนเสมอ
- อย่าใส่ Flutter, Node, หรือ Python assumptions ลงใน root
- อย่าข้าม `docs/prompt-pipeline.md`
- อย่าสับสนระหว่าง review กับ verification
- อย่าใช้ `prompts/review/audit_repo.md` กับ `docs/strict-audit-prompt.md` แบบสลับกันโดยไม่ตั้งใจ
- อย่าปล่อย project memory กลายเป็น log
- อย่าลืมอัปเดต docs เมื่อ workflow เปลี่ยน
- อย่าลืมอัปเดต `docs/tree-manifest.txt` เมื่อมี audit file ใหม่
- อย่ารัน `scripts/check-public-repo.sh` แบบคิดว่าเช็คเนื้อหาทั้งหมดแล้ว
- อย่าปล่อย overlay ไป rewrite identity ของ foundation
- อย่าประกาศ verification ที่ไม่ได้ทำจริง

## Quick Index

| Area | Start here |
| --- | --- |
| Governance | `AGENTS.md`, `docs/prompt-pipeline.md`, `docs/agent-team-system.md` |
| Usage | `docs/how-to-use.md`, `docs/how-to-use_TH.md` |
| Tutorial | `docs/tutorial.md`, `docs/tutorial_TH.md`, `docs/tutorials/index.md`, `docs/tutorials/agents-and-prompts.md` |
| Agent Team | `docs/tutorials/team/how-to-use-team-agents.md`, `docs/tutorials/team/how-to-use-team-agents_EN.md` |
| Tutorial Examples | `docs/tutorials/examples/index.md`, `docs/tutorials/examples/index_EN.md` |
| Tutorial Example Patterns | `docs/tutorials/examples/patterns/index.md`, `docs/tutorials/examples/patterns/index_EN.md`, `docs/tutorials/examples/patterns/adoption/index.md`, `docs/tutorials/examples/patterns/adoption/index_EN.md`, `docs/tutorials/examples/patterns/prompting/index.md`, `docs/tutorials/examples/patterns/prompting/index_EN.md`, `docs/tutorials/examples/patterns/design/index.md`, `docs/tutorials/examples/patterns/design/index_EN.md` |
| Tutorial Example Templates | `docs/tutorials/examples/templates/index.md`, `docs/tutorials/examples/templates/index_EN.md`, `docs/tutorials/examples/templates/flutter/design-md-flutter-template.md`, `docs/tutorials/examples/templates/flutter/design-md-flutter-template_EN.md`, `docs/tutorials/examples/templates/web/design-md-web-frontend-template.md`, `docs/tutorials/examples/templates/web/design-md-web-frontend-template_EN.md` |
| Architecture | `docs/architecture.md`, `core/architecture/layering.md` |
| Overlays | `docs/overlays.md`, `overlays/*/README.md`, `overlays/*/AGENTS.overlay.md` |
| Prompts | `prompts/index.md`, `prompts/index_EN.md`, `prompts/adoption/index.md`, `prompts/adoption/index_EN.md`, `prompts/planning/index.md`, `prompts/planning/index_EN.md`, `prompts/design/index.md`, `prompts/design/index_EN.md`, `prompts/implementation/index.md`, `prompts/implementation/index_EN.md`, `prompts/review/index.md`, `prompts/review/index_EN.md`, `prompts/verification/index.md`, `prompts/verification/index_EN.md`, `prompts/finalization/index.md`, `prompts/finalization/index_EN.md`, `prompts/memory/index.md`, `prompts/memory/index_EN.md`, `prompts/investigation/index.md`, `prompts/investigation/index_EN.md` |
| Skills | `skills/*/README.md` |
| Templates | `templates/*` |
| Examples | `examples/*`, `overlays/*/examples/*` |
| Public release | `docs/public-repo-checklist.md`, `docs/release-process.md`, `scripts/check-public-repo.sh` |
