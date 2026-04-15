# ตัวอย่าง go_router Deep Linking

## เป้าหมาย

แสดง flow ที่มี route map, redirect และ deep-link wiring สำหรับ Flutter app ที่เปิดหน้าถูกต้องจาก external link

## ไฟล์อ้างอิง

- [`../../templates/feature-module-template.md`](../../templates/feature-module-template.md)
- [`../../skills/routing/flutter-go-router-route-map/SKILL.md`](../../skills/routing/flutter-go-router-route-map/SKILL.md)
- [`../../skills/routing/flutter-go-router-redirect-guard/SKILL.md`](../../skills/routing/flutter-go-router-redirect-guard/SKILL.md)
- [`../../skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`](../../skills/routing/flutter-go-router-deeplink-wireup/SKILL.md)

## Skill ที่ต้องใช้

- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-clean-architecture-audit`

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/examples/routing-example.md`
- `lib/app/router/`
- `lib/main.dart`

## ขั้นตอน

1. declare route tree ไว้ใน router file เดียว
2. เพิ่ม redirect หรือ guard logic ในไฟล์แยก
3. wire platform entry points สำหรับ deep link
4. keep page builders ให้ typed และ minimal
5. เพิ่ม tests หรือ manual verification สำหรับ direct links

## เอาต์พุตที่คาดหวัง

```text
lib/app/router/app_router.dart
lib/app/router/route_guards.dart
lib/app/router/deeplink_handler.dart
lib/main.dart
```

## ความผิดพลาดที่พบบ่อย

- รวม route tree, redirect rules และ deep-link parsing ไว้ไฟล์เดียว
- ลืม root entry point
- ให้ widget code เป็นเจ้าของ navigation rules

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-project/README.md or overlays/mobile-flutter/workflows/new-feature/README.md depending on scope.
Use overlays/mobile-flutter/examples/routing-example.md.

Task:
Implement go_router route map, redirect guard, and deep-link wiring.

Deliver:
1. route plan
2. redirect plan
3. deep-link entry plan
4. exact output paths
5. validation checklist
```

## English

ดู `go-router-deep-linking.md`
