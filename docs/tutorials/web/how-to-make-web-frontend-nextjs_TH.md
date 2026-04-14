---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - frontend
  - nextjs
aliases:
  - วิธีสร้าง Next.js Web Frontend จากโฟลเดอร์เปล่า
  - Next.js Thai Tutorial
---

# วิธีทำ Web Frontend ด้วย Next.js จากโฟลเดอร์เปล่า

ใช้ tutorial นี้เมื่อทีมต้องการ file-based routing, page/layout composition, SSR/SSG,
หรือ route protection ที่ผูกกับ framework

## เหมาะกับ

- แอปที่ต้องการ server rendering หรือ static generation
- ทีมที่อยากใช้ App Router หรือ Pages Router เป็นแกน
- โปรเจกต์ที่ route, layout, และ guard ควรอยู่ใกล้ framework boundary

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์โปรเจกต์
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `web-frontend` overlay
6. สร้างโปรเจกต์ Next.js
7. แยก app/layout/page ออกจาก feature, service, state, และ design-system
8. เติม routing, state, networking, auth, forms, i18n, และ design-style ทีละชั้น
9. verify ด้วย lint, test, build
10. บันทึก memory สำหรับ decision ถาวร

ตัวอย่าง bootstrap:

```bash
mkdir nextjs-web-app
cd nextjs-web-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
npx create-next-app@latest . --ts --eslint --app
```

## โครงที่แนะนำ

```text
app/
  layout.tsx
  page.tsx
  (routes)/
src/
  components/
  features/
  services/
  state/
  design-system/
tests/
e2e/
project_memory/
```

## ลำดับลง capability

### 1. Routing

- ใช้ App Router หรือ Pages Router ตามมาตรฐานของโปรเจกต์
- page/layout เป็นตัวกำหนด boundary ของ route
- route guard และ protected area ควรถูกจัดไว้ใกล้ routing layer

### 2. State

- ใช้ local state สำหรับ UI ชั่วคราว
- ใช้ shared state เฉพาะเมื่อหลาย route หรือหลาย component ต้องใช้ข้อมูลเดียวกัน
- อย่าให้ mutation ปนอยู่ใน presentational component

### 3. Networking

- แยก API access ให้อยู่ใน service หรือ server-facing layer ที่ชัด
- แยก request/response mapping ออกจาก UI
- เตรียม loading, empty, error, retry ให้ชัด

### 4. Auth

- ถ้าใช้ middleware, server component, หรือ route guard ให้ระบุ boundary ชัด
- session/auth state ต้องไม่กระจายไปทั่ว component tree
- แยก protected content ออกจาก public content ให้ชัด

### 5. Forms

- แยก validation ออกจาก view surface
- ใช้ form state ที่ชัดเจน
- แสดง error ใกล้ field ที่เกี่ยวข้อง

### 6. i18n

- วาง key ให้ stable และ feature-scoped
- ไม่ hardcode string ที่ผู้ใช้เห็นใน component โดยตรง
- ถ้าทีมใช้หลายภาษา ให้เตรียม fallback language ให้ชัด

### 7. Design-style / Design system

- ตั้ง token ของสี, spacing, typography, radius, shadow, และ motion ให้ชัด
- ใช้ shared primitives สำหรับ button, input, card, modal, table, empty state
- อย่าปล่อยให้ page-specific styling ล้นเข้า component ที่ควร reuse ได้

## ตัวอย่าง AGENTS.md สั้น

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Next.js Web Frontend
**Architecture:** Page / Feature / Component / Service / State / Design System
**Localization:** i18n-first
**Target:** <target users>

## Rules

- routes own screen orchestration
- features own business behavior
- components stay reusable
- services own API and external integration
- state mutations stay in the state layer
- design-system primitives stay feature-free
- forms and validation stay explicit
- translations come from the localization layer
```

## prompt ที่ควรใช้

| Stage | Prompt | สิ่งที่ควรทำ |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | เลือก overlay และ startup path |
| Plan | `prompts/planning/plan_change.md` | สรุป scope, risk, และ boundary |
| Architecture | `prompts/design/architecture_review.md` | ล็อก routing, state, service, design-system |
| Implement | `prompts/implementation/implement_change.md` | สร้างโครงและ wire capability ทีละชั้น |
| Review | `prompts/review/review_change.md` | เช็ก leakage, drift, และ missing tests |
| Verify | `prompts/verification/verification_pass.md` | ยืนยัน lint/test/build และ edge cases |
| Finalize | `prompts/finalization/finalize_change.md` | สรุปงานและ follow-up |
| Memory | `prompts/memory/update_project_memory.md` | เก็บ decision ถาวร |

## สิ่งที่ต้อง verify

- route, layout, และ guard อยู่ใกล้ framework boundary
- state mutation ไม่อยู่ใน leaf component
- networking ไม่ซ่อนอยู่ใน presentation primitive
- auth flow มี boundary ชัด
- forms มี validation และ error handling
- i18n keys ไม่ drift
- design-style ใช้ token หรือ shared primitives
- lint, test, build ผ่าน
