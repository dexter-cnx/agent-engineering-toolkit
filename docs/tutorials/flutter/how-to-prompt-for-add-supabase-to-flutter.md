---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - prompts
  - supabase
aliases:
  - Prompt Supabase for Flutter
  - Flutter Supabase Prompt Tutorial
---

# วิธี prompt เพื่อเพิ่ม Supabase ให้ Flutter

ใช้ tutorial นี้เมื่อคุณมี Flutter app อยู่แล้ว และอยากสั่ง AI ให้เพิ่ม Supabase โดยคุม boundary ให้ชัด

## ใช้เมื่อไร

- ต้องการเพิ่ม Supabase แบบค่อย ๆ ทำ ไม่ใช่เขียนตรงจาก widget
- ต้องการให้ AI วาง package, auth flow, database access, และ verification ก่อน
- ต้องการคุม repo ให้ยังอยู่ใน clean architecture หรือ layered architecture

## เริ่มจากสิ่งที่ควรมี

1. มี Flutter repo อยู่แล้ว
2. มี `AGENTS.md` ที่ root
3. เลือก `mobile-flutter` overlay
4. อ่าน `docs/prompt-pipeline.md`
5. ตัดสินใจว่าจะใช้ Supabase feature อะไรบ้าง

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** Online App / Clean Architecture
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- supabase_flutter
- <state management>
- <routing>

## 3. Architecture Rules

- Supabase access must stay behind adapter or service layers
- widgets stay thin
- auth/session logic must be explicit
- keep repository boundaries clean

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify before finalizing
5. Update project memory after durable decisions
```

## ตัวอย่าง prompt เริ่มงาน

```text
Follow AGENTS.md strictly.
We already have a Flutter app.
Add Supabase behind adapter and service layers only.
Start by proposing the package list, files to create, and verification steps.
Do not put Supabase calls directly inside widgets.
Keep auth, data, and UI boundaries explicit.
```

## prompt flow ที่แนะนำ

| Stage | Prompt | ใช้ทำอะไร |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | ตรวจว่า repo ใช้ toolkit และ overlay อย่างไร |
| Plan | `prompts/planning/plan_change.md` | ระบุว่าจะเพิ่ม Supabase ตรงไหน |
| Architecture | `prompts/design/architecture_review.md` | วาง Supabase boundary, auth flow, data ownership |
| Implement | `prompts/implementation/implement_change.md` | เพิ่ม package, adapter, service, provider |
| Review | `prompts/review/review_change.md` | ตรวจว่า Supabase ไม่รั่วเข้า widget |
| Verify | `prompts/verification/verification_pass.md` | ยืนยันว่า analysis, test, smoke check ผ่าน |
| Finalize | `prompts/finalization/finalize_change.md` | สรุปผลและ follow-up |
| Memory | `prompts/memory/update_project_memory.md` | บันทึก rules ที่ควรจำถาวร |

## ตัวอย่าง prompt ที่เจาะ Supabase

```text
Add Supabase to this Flutter app.
Use supabase_flutter only if needed.
Keep Supabase behind adapter or service layers.
Update the repo structure first, then list the files to modify, then verify with flutter analyze and flutter test.
```

## โครงที่ควรคงไว้

- `presentation/` สำหรับ UI
- `domain/` สำหรับ use cases
- `data/` สำหรับ Supabase repository implementation
- `services/` หรือ `adapters/` สำหรับ Supabase client integration

## pitfall

- สั่งให้ AI ใส่ Supabase call ลง widget ตรง ๆ
- ลืมกำหนด auth/session flow
- ผสม package install กับ architecture decision โดยไม่แยก
- ไม่บอก verification step

