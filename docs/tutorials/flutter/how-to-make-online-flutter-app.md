---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - online
aliases:
  - Online Flutter Tutorial
  - Flutter Online App
---

# วิธีทำ Flutter app แบบ online

ใช้ tutorial นี้เมื่อ Flutter app พึ่งพา server-backed features และ online API

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์และ initialize git
2. เพิ่ม toolkit และ project memory
3. เพิ่ม `AGENTS.md`
4. เลือก `mobile-flutter` overlay
5. ตัดสินใจ boundary ของ API ก่อนเริ่ม UI
6. สร้าง Flutter app shell
7. ติดตั้ง `dio` เป็นตัวอย่าง HTTP client
8. วาง network และ session logic ไว้หลัง adapter หรือ service
9. verify ด้วย checks ที่เน้น online
10. บันทึก memory สำหรับการตัดสินใจเรื่อง API และ transport

ตัวอย่าง bootstrap:

```bash
mkdir flutter-online-app
cd flutter-online-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add dio
```

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)
- [Mobile Flutter worked example](../../../overlays/mobile-flutter/examples/worked_example.md)

## skill ของ Mobile Flutter overlay ที่ควรอ่าน

- API boundary, adapter placement, transport layering: `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md`
- auth/session flow ถ้ามี login: `../../../overlays/mobile-flutter/skills/flutter-auth/skill.md`
- cache หรือ persistence ถ้าต้องเก็บข้อมูลชั่วคราว: `../../../overlays/mobile-flutter/skills/flutter-storage/skill.md`

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
- dio
- <state management>
- <routing>
- <api client>

## 3. Architecture Rules

- widgets stay thin
- API calls live outside widgets
- keep routes, state, and data boundaries explicit

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
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the mobile-flutter overlay.
Use dio as the HTTP client and keep it behind an adapter or service.
Use the prompt pipeline in order.
Keep API, state, and widget boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | API assumptions, risks, constraints |
| 3 | `prompts/design/architecture_review.md` | `skills/dependency-review/README.md` + `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md` | API boundary, adapter placement, provider risk |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` + `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md` | app shell, network layer, state flow |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` + `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md` | UI ต้องบางและไม่มี transport leakage |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` + `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md` | API smoke evidence และ uncertainty |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | `../../../overlays/mobile-flutter/skills/flutter-networking/skill.md` | durable API conventions |

## โครงแบบ online-first ที่ควรมี

แยก responsibility เหล่านี้ให้ชัด:

- presentation widgets
- feature หรือ state layer
- API service หรือ adapter
- domain/use-case layer

ตัวอย่าง `dio` ที่ใช้ในชั้น service หรือ adapter:

```dart
final dio = Dio(
  BaseOptions(
    baseUrl: 'https://api.example.com',
    connectTimeout: const Duration(seconds: 10),
    receiveTimeout: const Duration(seconds: 10),
  ),
);
```

ให้ใช้ `dio` เป็น HTTP client หลัง adapter/service แล้วค่อย map response ไปยัง model หรือ entity ในชั้นที่เหมาะสม

ถ้า auth, session หรือ retry behavior สำคัญ ให้เขียนไว้ใน architecture review ตั้งแต่ต้น

## การ verify

ใช้ Flutter checks ปกติร่วมกับ online smoke test ที่ repo ของคุณรองรับ:

```bash
flutter analyze
flutter test
```

ถ้ามี mock server หรือ staging API ให้เพิ่ม smoke check เล็ก ๆ เข้าไป

## pitfall

- ให้ widgets เรียก network API โดยตรง
- กระจาย API helper ไปทั่ว UI
- ทำให้ loading/error states หายไปใน component ที่ไม่เกี่ยว
- ปล่อยให้ auth/session handling เป็นเรื่องที่ไม่ถูกบันทึก

## memory notes

เก็บ decision ที่ควรจำถาวร เช่น:

- ความคาดหวังของ API contract
- กติกาเรื่อง auth/session
- retry และ error-handling behavior
- adapter boundary
