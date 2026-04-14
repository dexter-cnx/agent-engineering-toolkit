---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - frontend
  - react
  - vite
aliases:
  - วิธีสร้าง React + Vite Web Frontend จากโฟลเดอร์เปล่า
  - React Vite Thai Tutorial
---

# วิธีทำ Web Frontend ด้วย React + Vite จากโฟลเดอร์เปล่า

ใช้ tutorial นี้เมื่อทีมต้องการ SPA ที่เบา, เร็ว, และคุม architecture เองได้ชัด

## เหมาะกับ

- แอปที่เป็น single-page หรือ dashboard
- ทีมที่อยากควบคุม routing และ data flow เอง
- โปรเจกต์ที่อยากแยก feature, service, state, และ design-system ให้ชัด

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์โปรเจกต์
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `web-frontend` overlay
6. สร้างโปรเจกต์ React + Vite
7. สร้างโครง `src/` ให้แยก page, components, features, services, state, design-system
8. ใส่ routing, state, networking, forms, auth, และ i18n ทีละชั้น
9. verify ด้วย lint, test, build
10. บันทึก memory สำหรับ decision ถาวร

ตัวอย่าง bootstrap:

```bash
mkdir react-vite-web-app
cd react-vite-web-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
npm create vite@latest . -- --template react-ts
```

## โครงที่แนะนำ

```text
src/
  main.tsx
  app/
  routes/
  pages/
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

- ใช้ `react-router` หรือ router ที่ทีมมาตรฐานเลือก
- route guard, layout, และ navigation state ต้องอยู่ที่ routing layer
- อย่าฝัง route decision ไว้ใน reusable component

### 2. State

- ใช้ local state สำหรับ UI ชั่วคราว
- ใช้ shared state เฉพาะเมื่อหลายหน้าใช้ข้อมูลเดียวกัน
- mutation ต้องอยู่ใน state layer หรือ store ที่ชัดเจน

### 3. Networking

- รวม API access ไว้ใน service หรือ data hook
- แยก request/response mapping ออกจาก UI
- เตรียม loading, empty, error, retry ให้ชัด

### 4. Auth

- แยก session/auth state ออกจาก presentation
- route protection ควรอยู่ที่ router layer หรือ guard component
- session/token handling ต้องไม่กระจายไปทุก component

### 5. Forms

- แยก validation ออกจาก view surface
- แสดง error ใกล้ field ที่เกี่ยวข้อง
- ระวัง keyboard flow, focus state, submit state

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
**Type:** React + Vite Web Frontend
**Architecture:** Page / Feature / Component / Service / State / Design System
**Localization:** i18n-first
**Target:** <target users>

## Rules

- pages own screen orchestration
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

- route และ guard อยู่ที่ router layer
- state mutation ไม่อยู่ใน leaf component
- networking ไม่ซ่อนอยู่ใน presentation primitive
- auth flow มี boundary ชัด
- forms มี validation และ error handling
- i18n keys ไม่ drift
- design-style ใช้ token หรือ shared primitives
- lint, test, build ผ่าน
