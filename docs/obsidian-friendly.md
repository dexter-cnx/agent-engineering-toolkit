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

โน้ตนี้เป็น MOC แบบอ่านเร็ว ไม่ใช่ source of truth หลัก

ถ้าเอกสารหน้านี้กับเอกสาร canonical ขัดกัน ให้เชื่อ canonical docs ก่อนเสมอ

## Read First

อ่านไฟล์เหล่านี้ก่อนเสมอ:

| File | Why it matters |
| --- | --- |
| `AGENTS.md` | สัญญาหลักของ repo และกติกาที่ AI ต้องตาม |
| `docs/prompt-pipeline.md` | ลำดับ lifecycle ที่เป็น source of truth |
| `docs/agent-team-system.md` | โมเดลบทบาทของทีม AI |
| `docs/how-to-use.md` | คู่มือใช้งาน canonical ภาษาอังกฤษ |
| `docs/how-to-use_TH.md` | คู่มือใช้งาน canonical ภาษาไทย |
| `README_START_HERE.md` | เส้นทาง onboarding สั้นที่สุดของ repo |
| `docs/tutorial.md` | walkthrough แบบ step-by-step |
| `docs/tutorial_TH.md` | walkthrough ภาษาไทย |
| `docs/public-repo-checklist.md` | รายการตรวจ public release แบบ human-readable |
| `scripts/check-public-repo.paths` | source of truth แบบ machine-readable สำหรับ public gate |

## Use This Page

Treat this as a quick navigation map, not the canonical contract.

### Start here

1. `AGENTS.md`
2. `docs/prompt-pipeline.md`
3. `docs/agent-team-system.md`
4. `README_START_HERE.md`
5. `docs/how-to-use.md`
6. `docs/overlays.md`

### Primary hubs

- Tutorials: `docs/tutorials/index.md` and `docs/tutorials/index_EN.md`
- Tutorial setup: `docs/tutorials/agents-and-prompts.md` and `docs/tutorials/agents-and-prompts_EN.md`
- Examples: `docs/tutorials/examples/index.md` and `docs/tutorials/examples/index_EN.md`
- Prompts: `prompts/index.md` and `prompts/index_EN.md`
- Skills: `skills/`
- Overlays: `overlays/`
- Public release: `docs/public-repo-checklist.md`, `docs/release-process.md`, `scripts/check-public-repo.sh`

### Quick rules

- Root stays stack-agnostic.
- Stack-specific rules belong in overlays or consuming repos.
- Review is not verification.
- Project memory is for durable decisions only.
