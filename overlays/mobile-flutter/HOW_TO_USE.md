# How To Use

## What this overlay is

`overlays/mobile-flutter` is the Flutter-specific operating overlay for the Agent Engineering Toolkit.
Use it to build, review, migrate, and release Flutter apps with atomic skills, workflows, policies, templates, and examples.

## When to use skills

Use a skill when the task has one clear responsibility.

- Audit boundaries: `skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- Scaffold a feature: `skills/architecture/flutter-feature-folder-scaffold/SKILL.md`
- Build state: `skills/state/flutter-riverpod-state-skeleton/SKILL.md` or `skills/state/flutter-getx-controller-skeleton/SKILL.md`
- Route behavior: `skills/routing/flutter-go-router-route-map/SKILL.md`
- Firebase boundaries: `skills/firebase/flutter-firebase-auth-adapter/SKILL.md`
- Release checks: `skills/release/flutter-android-release-validate/SKILL.md`

## When to use workflows

Use a workflow when the task needs multiple ordered skills.

- New project: `workflows/new-project/README.md`
- New feature: `workflows/new-feature/README.md`
- Release app: `workflows/release-app/README.md`
- Migrate project: `workflows/migrate-project/README.md`

## When to read policies

Read policies when you need constraints, not execution.

- Architecture rules: `policies/architecture/README.md`
- Repo standards: `policies/repo-standards/README.md`
- Testing rules: `policies/testing/README.md`
- Secrets handling: `policies/secrets/README.md`

## Minimal onboarding steps

1. Read `README.md`.
2. Read `AGENTS.overlay.md`.
3. Open `SKILLS_INDEX.md` and pick the smallest skill.
4. Open the matching workflow if the task spans multiple steps.
5. Use `templates/` and `examples/` to match the expected file shape.
6. Validate with `ci/validate_skills.sh`.

## 5 common tasks

| Task | Use |
|---|---|
| Create a new project | `workflows/new-project/README.md` + `flutter-clean-architecture-audit` |
| Add a new feature | `workflows/new-feature/README.md` + `flutter-feature-folder-scaffold` + `flutter-feature-contract-scaffold` |
| Integrate Firebase auth | `flutter-firebase-auth-adapter` + `flutter-firebase-auth-state` + `workflows/new-feature/README.md` |
| Add deep link routing | `flutter-go-router-route-map` + `flutter-go-router-redirect-guard` + `flutter-go-router-deeplink-wireup` |
| Prepare release | `workflows/release-app/README.md` + `flutter-android-signing-config` + `flutter-ios-release-readiness` |

## Copy-paste prompts

### Create new project

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-project/README.md.
Pick the smallest skills from overlays/mobile-flutter/SKILLS_INDEX.md.

Task:
Bootstrap a new Flutter app with clean architecture, routing, state, and localization.

Deliver:
1. exact files to create
2. chosen skills
3. implementation order
4. validation checklist
```

### Add new feature

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.
Use overlays/mobile-flutter/templates/feature-module-template.md.

Task:
Add a <feature name> feature module to the Flutter app.

Deliver:
1. file plan
2. boundary plan
3. chosen skills
4. validation checklist
```

### Integrate Firebase auth

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.
Use overlays/mobile-flutter/examples/firebase-integration-example.md.

Task:
Integrate Firebase Auth with adapter, auth state, and guarded routing.

Deliver:
1. auth boundary plan
2. exact files to update
3. route guard plan
4. validation checklist
```

### Add deep link routing

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/examples/routing-example.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md if the feature is new.

Task:
Add go_router route map, redirect guard, and deep-link wiring.

Deliver:
1. route plan
2. deep-link entry plan
3. exact files to update
4. validation checklist
```

### Prepare release

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/release-app/README.md.
Use overlays/mobile-flutter/examples/release-config-example.md.

Task:
Prepare the app for Android and iOS release.

Deliver:
1. signing plan
2. release validation plan
3. exact files to review
4. release risks
```

## Quick troubleshooting

- If the task is boundary-heavy, start with `flutter-clean-architecture-audit`.
- If the task touches routing, split route map, redirects, and deep links.
- If the task touches auth, keep Firebase SDK calls in an adapter.
- If the task is too broad, use a workflow before editing code.
- If validation fails, check file paths and references first.

## Repository navigation map

- `README.md` -> overlay summary and start point
- `AGENTS.overlay.md` -> active routing and operating rules
- `SKILLS_INDEX.md` -> choose the smallest skill
- `SKILL_SCHEMA.md` -> required skill format
- `workflows/` -> multi-skill orchestration
- `policies/` -> constraints only
- `templates/` -> file shape and scaffolding
- `examples/` -> worked output examples
- `docs/tutorials/` -> operational guides
- `ci/validate_skills.sh` -> overlay validation

## Thai

### overlay นี้คืออะไร

`overlays/mobile-flutter` คือ Flutter-specific operating overlay ของ Agent Engineering Toolkit
ใช้สำหรับ build, review, migrate และ release Flutter app ด้วย atomic skills, workflows, policies, templates และ examples

### เมื่อไรควรใช้ skill

ใช้ skill เมื่อ task มี responsibility เดียวชัดเจน

- ตรวจ boundary: `skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- สร้าง feature folder: `skills/architecture/flutter-feature-folder-scaffold/SKILL.md`
- ทำ state: `skills/state/flutter-riverpod-state-skeleton/SKILL.md` หรือ `skills/state/flutter-getx-controller-skeleton/SKILL.md`
- ทำ routing: `skills/routing/flutter-go-router-route-map/SKILL.md`
- ทำ Firebase boundary: `skills/firebase/flutter-firebase-auth-adapter/SKILL.md`
- ตรวจ release: `skills/release/flutter-android-release-validate/SKILL.md`

### เมื่อไรควรใช้ workflow

ใช้ workflow เมื่องานต้องใช้หลาย skill ตามลำดับ

- new project: `workflows/new-project/README.md`
- new feature: `workflows/new-feature/README.md`
- release app: `workflows/release-app/README.md`
- migrate project: `workflows/migrate-project/README.md`

### เมื่อไรควรอ่าน policy

อ่าน policy เมื่อต้องการข้อจำกัด ไม่ใช่ขั้นตอนทำงาน

- architecture rules: `policies/architecture/README.md`
- repo standards: `policies/repo-standards/README.md`
- testing rules: `policies/testing/README.md`
- secrets handling: `policies/secrets/README.md`

### ขั้นตอนเริ่มต้นแบบสั้น

1. อ่าน `README.md`
2. อ่าน `AGENTS.overlay.md`
3. เปิด `SKILLS_INDEX.md` แล้วเลือก skill ที่เล็กที่สุด
4. ถ้างานหลายขั้นตอน ให้เปิด workflow ที่ตรง
5. ใช้ `templates/` และ `examples/` เป็นตัวอย่างรูปแบบไฟล์
6. validate ด้วย `ci/validate_skills.sh`

### 5 งานที่พบบ่อย

| งาน | ใช้อะไร |
|---|---|
| สร้างโปรเจกต์ใหม่ | `workflows/new-project/README.md` + `flutter-clean-architecture-audit` |
| เพิ่ม feature ใหม่ | `workflows/new-feature/README.md` + `flutter-feature-folder-scaffold` + `flutter-feature-contract-scaffold` |
| ใส่ Firebase auth | `flutter-firebase-auth-adapter` + `flutter-firebase-auth-state` + `workflows/new-feature/README.md` |
| เพิ่ม deep link routing | `flutter-go-router-route-map` + `flutter-go-router-redirect-guard` + `flutter-go-router-deeplink-wireup` |
| เตรียม release | `workflows/release-app/README.md` + `flutter-android-signing-config` + `flutter-ios-release-readiness` |

### Prompt สำหรับคัดลอกไปใช้

ดูส่วน English ด้านบน แล้วใช้ prompt blocks เดียวกันได้ทันที

### วิธีแก้ปัญหาเร็ว ๆ

- ถ้า boundary ซับซ้อน ให้เริ่มจาก `flutter-clean-architecture-audit`
- ถ้าแตะ routing ให้แยก route map, redirects และ deep links
- ถ้าแตะ auth ให้เก็บ Firebase SDK calls ไว้ใน adapter
- ถ้างานกว้างเกินไป ให้ใช้ workflow ก่อนแก้ code
- ถ้า validation fail ให้เช็ก path และ references ก่อน

### แผนที่ repository

- `README.md` -> ภาพรวมและจุดเริ่ม
- `AGENTS.overlay.md` -> rules และ active routing
- `SKILLS_INDEX.md` -> เลือก skill ที่เล็กที่สุด
- `SKILL_SCHEMA.md` -> รูปแบบ skill ที่ต้องมี
- `workflows/` -> orchestration หลาย skill
- `policies/` -> ข้อจำกัด
- `templates/` -> โครงไฟล์
- `examples/` -> ตัวอย่างผลลัพธ์
- `docs/tutorials/` -> คู่มือใช้งาน
- `ci/validate_skills.sh` -> ตรวจ overlay
