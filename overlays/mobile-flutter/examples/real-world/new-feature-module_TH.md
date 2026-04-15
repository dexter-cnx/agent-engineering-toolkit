# ตัวอย่าง Feature Module ใหม่

## เป้าหมาย

แสดง flow จริงของ feature module สำหรับ profile feature ที่มี layered structure และ Riverpod state

## ไฟล์อ้างอิง

- [`../../templates/feature-module-template.md`](../../templates/feature-module-template.md)
- [`../../templates/repository-template.md`](../../templates/repository-template.md)
- [`../../skills/architecture/flutter-feature-folder-scaffold/SKILL.md`](../../skills/architecture/flutter-feature-folder-scaffold/SKILL.md)
- [`../../skills/architecture/flutter-feature-contract-scaffold/SKILL.md`](../../skills/architecture/flutter-feature-contract-scaffold/SKILL.md)
- [`../../skills/state/flutter-riverpod-state-skeleton/SKILL.md`](../../skills/state/flutter-riverpod-state-skeleton/SKILL.md)

## Skill ที่ต้องใช้

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-firestore-repository`
- `flutter-go-router-route-map`

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `lib/features/profile/`
- `test/features/profile/`

## ขั้นตอน

1. audit boundary ของ feature
2. scaffold `lib/features/profile/` ตาม layered template
3. เพิ่ม domain contract และ repository contract
4. เพิ่ม Riverpod state skeleton สำหรับ profile loading
5. implement repository ที่ data layer
6. เพิ่ม route wiring เฉพาะกรณีที่ feature ต้องนำทางได้
7. เพิ่ม widget และ unit tests

## เอาต์พุตที่คาดหวัง

```text
lib/features/profile/
  data/repositories/profile_repository_impl.dart
  domain/entities/profile.dart
  domain/repositories/profile_repository.dart
  presentation/controllers/profile_controller.dart
  presentation/pages/profile_page.dart
test/features/profile/profile_controller_test.dart
```

## ความผิดพลาดที่พบบ่อย

- ข้าม contract layer
- ใส่ repository call ใน page โดยตรง
- เพิ่ม route logic ก่อนมี module

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.
Use overlays/mobile-flutter/templates/feature-module-template.md and overlays/mobile-flutter/examples/full-feature-implementation.md.

Task:
Implement a profile feature module with clean boundaries and tests.

Deliver:
1. file plan
2. architecture plan
3. exact output paths
4. validation checklist
```

## English

ดู `new-feature-module.md`
