# ตัวอย่าง Firebase Auth Flow

## เป้าหมาย

แสดง sign-in flow ที่ปลอดภัย โดยให้ Firebase SDK อยู่ใน data layer และ auth state แยกจาก routing

## ไฟล์อ้างอิง

- [`../../templates/repository-template.md`](../../templates/repository-template.md)
- [`../../templates/state-management-template.md`](../../templates/state-management-template.md)
- [`../../skills/firebase/flutter-firebase-auth-adapter/SKILL.md`](../../skills/firebase/flutter-firebase-auth-adapter/SKILL.md)
- [`../../skills/firebase/flutter-firebase-auth-state/SKILL.md`](../../skills/firebase/flutter-firebase-auth-state/SKILL.md)

## Skill ที่ต้องใช้

- `flutter-firebase-auth-adapter`
- `flutter-firebase-auth-state`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-route-map`

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/examples/firebase-integration-example.md`
- `lib/features/auth/`
- `lib/app/router/`
- `test/features/auth/`

## ขั้นตอน

1. wrap Firebase Auth calls ไว้ใน data adapter
2. เพิ่ม auth session state ที่ consume adapter
3. เก็บ redirect logic ไว้ใน routing ไม่ใช่ใน page
4. เพิ่มหน้า sign-in และ sign-out
5. เพิ่ม tests สำหรับ adapter mapping และ route behavior

## เอาต์พุตที่คาดหวัง

```text
lib/features/auth/data/datasources/firebase_auth_data_source.dart
lib/features/auth/data/repositories/auth_repository_impl.dart
lib/features/auth/presentation/controllers/auth_controller.dart
lib/app/router/route_guards.dart
test/features/auth/auth_controller_test.dart
```

## ความผิดพลาดที่พบบ่อย

- เรียก Firebase SDK จาก widget โดยตรง
- เอา auth state มาปนกับ UI state
- ใส่ redirect logic ใน screen

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md and overlays/mobile-flutter/examples/firebase-integration-example.md.

Task:
Implement a Firebase Auth flow with adapter, auth state, and guarded routing.

Deliver:
1. auth boundary plan
2. exact files to create or update
3. route guard plan
4. validation checklist
```

## English

ดู `firebase-auth-flow.md`
