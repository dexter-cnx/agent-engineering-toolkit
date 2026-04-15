# เพิ่มฟีเจอร์ใหม่ด้วย AI

## เป้าหมาย

เพิ่ม feature module เดียวใน Flutter app ที่มีอยู่ โดยไม่ทำให้ architecture หรือ route boundary แตก

## สิ่งที่ต้องมี

- consuming app มีอยู่แล้ว
- รู้ชื่อ feature และ boundary ของ layer
- รู้ว่าจะใช้ Riverpod หรือ GetX

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `overlays/mobile-flutter/templates/state-management-template.md`
- `overlays/mobile-flutter/examples/full-feature-implementation.md`
- `overlays/mobile-flutter/examples/firebase-integration-example.md`

## ขั้นตอน

1. อ่าน `workflows/new-feature/README.md`
2. อ่าน `overlays/mobile-flutter/templates/feature-module-template.md` และ `overlays/mobile-flutter/templates/repository-template.md`
3. ใช้ `flutter-clean-architecture-audit` เพื่อตรวจ boundary
4. สร้าง feature folder และ contract files
5. เพิ่ม state skeleton และ repository adapter
6. wire routes เฉพาะกรณีที่ feature เพิ่ม navigation
7. เพิ่ม tests และ validate tree กับ template

## ควรใช้ skill อะไร

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton` หรือ `flutter-getx-controller-skeleton`
- `flutter-firestore-repository` หรือ `flutter-firebase-auth-adapter` ถ้า feature ใช้ Firebase
- `flutter-firebase-auth-state` ถ้า feature เปลี่ยน auth state
- `flutter-go-router-route-map` ถ้า feature เพิ่ม routes
- `flutter-go-router-redirect-guard` ถ้า feature ต้องมี auth/onboarding gate
- `flutter-go-router-deeplink-wireup` ถ้า feature ต้องเปิดจากลิงก์
- `flutter-performance-audit` ถ้า feature หนักหรือช้า

## อินพุตที่คาดหวัง

- ชื่อ feature
- เป้าหมายของ feature
- พาธเป้าหมายใน consuming app
- state choice
- data source choice
- route requirements

## เอาต์พุตที่คาดหวัง

- feature folder tree
- contract และ repository files
- state holder และ page wiring
- route หรือ guard update ถ้าจำเป็น
- tests สำหรับ behavior ที่ไม่ trivial

## ความผิดพลาดที่พบบ่อย

- สร้าง page ก่อน contract และ state shape
- เอา Firebase SDK call ไปไว้ใน widgets
- ปน route registration กับ feature implementation
- ข้ามขั้น audit ตอน boundary ยังไม่ชัด

## วิธีแก้ปัญหา

- ถ้า feature แตะ auth ให้แยก SDK wrapper ออกจาก auth state
- ถ้า feature แตะ routes ให้แยก route map, redirect และ deep-link wiring
- ถ้า feature กว้างเกินไป ให้ตัดให้เหลือหนึ่ง module และหนึ่ง responsibility

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.
Use overlays/mobile-flutter/templates/feature-module-template.md and overlays/mobile-flutter/examples/full-feature-implementation.md.

Task:
Add <feature name> to the existing Flutter app.

Deliver:
1. architecture boundary plan
2. exact files to create or update
3. selected skills
4. implementation order
5. validation checklist
```

## English

ดู `add-a-new-feature-with-ai.md` สำหรับเวอร์ชันภาษาอังกฤษ
