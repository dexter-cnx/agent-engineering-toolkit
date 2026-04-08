---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - prompts
  - firebase
aliases:
  - Prompt Firebase Services for Flutter
  - Flutter Firebase Prompt Tutorial
---

# วิธี prompt เพื่อเพิ่ม Firebase services ให้ Flutter

ใช้ tutorial นี้เมื่อคุณมี Flutter app อยู่แล้ว และอยากสั่ง AI ให้เพิ่ม Firebase services โดยคุม boundary ให้ชัด

## ใช้เมื่อไร

- ต้องการเพิ่ม Firebase แบบค่อย ๆ ทำ ไม่ใช่เขียนตรงจาก widget
- ต้องการให้ AI วาง package, adapter, auth flow, และ verification ก่อน
- ต้องการคุม repo ให้ยังอยู่ใน clean architecture หรือ layered architecture

## skill ของ Mobile Flutter overlay ที่ควรอ่านก่อน

เลือก skill ให้ตรงกับ Firebase capability ที่จะเพิ่ม:

- auth/session: `../../../overlays/mobile-flutter/skills/flutter-auth/skill.md`
- data API หรือ transport boundary: `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md`
- cache หรือ local persistence: `../../../overlays/mobile-flutter/skills/flutter-storage/skill.md`
- analytics: `../../../overlays/mobile-flutter/skills/flutter-analytics/skill.md`
- crash reporting: `../../../overlays/mobile-flutter/skills/flutter-crash-reporting/skill.md`
- push notifications: `../../../overlays/mobile-flutter/skills/flutter-push-notifications/skill.md`
- remote config: `../../../overlays/mobile-flutter/skills/flutter-remote-config/skill.md`
- feature flags: `../../../overlays/mobile-flutter/skills/flutter-feature-flags/skill.md`
- deep links: `../../../overlays/mobile-flutter/skills/flutter-deep-link/skill.md`

ถ้า feature ที่จะเพิ่มมีหลายส่วน ให้เปิด skill ตาม capability ที่เกี่ยวข้องก่อน แล้วค่อยใช้ prompt flow ด้านล่าง

## เริ่มจากสิ่งที่ควรมี

1. มี Flutter repo อยู่แล้ว
2. มี `AGENTS.md` ที่ root
3. เลือก `mobile-flutter` overlay
4. อ่าน `docs/prompt-pipeline.md`
5. ตัดสินใจว่าจะใช้ Firebase service อะไรบ้าง

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
- firebase_core
- firebase_auth
- cloud_firestore
- <state management>

## 3. Architecture Rules

- Firebase access must stay behind adapter or service layers
- widgets stay thin
- auth/session logic must be explicit
- keep repository boundary clean

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
Add Firebase services behind adapter and service layers only.
Start by proposing the package list, files to create, and verification steps.
Do not put Firebase calls directly inside widgets.
Keep auth, data, and UI boundaries explicit.
```

## prompt flow ที่แนะนำ

| Stage | Prompt | ใช้ทำอะไร |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | ตรวจว่า repo ใช้ toolkit และ overlay อย่างไร |
| Plan | `prompts/planning/plan_change.md` | ระบุว่าจะแทรก Firebase service ส่วนไหน |
| Architecture | `prompts/design/architecture_review.md` | วาง Firebase boundary, auth flow, data ownership |
| Implement | `prompts/implementation/implement_change.md` | เพิ่ม package, adapter, service, provider |
| Review | `prompts/review/review_change.md` | ตรวจว่า Firebase ไม่รั่วเข้า widget |
| Verify | `prompts/verification/verification_pass.md` | ยืนยันว่ามี analysis, test, และ smoke check |
| Finalize | `prompts/finalization/finalize_change.md` | สรุปผลและ follow-up |
| Memory | `prompts/memory/update_project_memory.md` | บันทึก rules ที่ควรจำถาวร |

## ตัวอย่าง prompt ที่เจาะ Firebase

```text
Add Firebase services to this Flutter app.
Use firebase_core, firebase_auth, and cloud_firestore only if needed.
Keep Firebase behind adapter or service layers.
Update the repo structure first, then list the files to modify, then verify with flutter analyze and flutter test.
```

## โครงที่ควรคงไว้

- `presentation/` สำหรับ UI
- `domain/` สำหรับ use cases
- `data/` สำหรับ Firebase repository implementation
- `services/` หรือ `adapters/` สำหรับ Firebase client integration

## pitfall

- สั่งให้ AI ใส่ Firebase call ลง widget ตรง ๆ
- ลืมกำหนด auth/session flow
- ผสม package install กับ architecture decision โดยไม่แยก
- ไม่บอก verification step
