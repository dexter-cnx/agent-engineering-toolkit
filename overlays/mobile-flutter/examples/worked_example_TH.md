# ตัวอย่าง Mobile Flutter แบบครบ flow

## สถานการณ์

แอป Flutter ที่ใช้งานจริงต้องมี:

- email/password authentication
- current-location support
- map-based branch selection
- notification tap-to-route
- web deployment สำหรับ internal QA

## Skill ที่แนะนำ

- `flutter-auth`
- `flutter-geolocation`
- `flutter-maps`
- `flutter-push-notifications`
- `flutter-deep-link`
- `guide-flutter-web-loading`
- `flutter-web-deployment`
- `guide-clean-architecture-feature`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/flutter-auth/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-geolocation/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-maps/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-push-notifications/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-deep-link/SKILL.md`
- `overlays/mobile-flutter/skills/guide-flutter-web-loading/SKILL.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`
- `overlays/mobile-flutter/prompts/add_maps_feature.md`
- `overlays/mobile-flutter/prompts/add_notifications_feature.md`
- `overlays/mobile-flutter/prompts/add_customer_visit_map.md`
- `overlays/mobile-flutter/prompts/prepare_flutter_web_release.md`
- `overlays/mobile-flutter/prompts/apply_flutter_web_loading.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-auth
- flutter-geolocation
- flutter-maps
- flutter-push-notifications
- flutter-deep-link
- guide-flutter-web-loading
- flutter-web-deployment

Reference files:
- overlays/mobile-flutter/skills/flutter-auth/SKILL.md
- overlays/mobile-flutter/prompts/add_auth_feature.md
- overlays/mobile-flutter/prompts/add_maps_feature.md

Task:
Implement a branch finder flow with guarded account access, notification tap
routing, and a QA web deployment plan.

Deliver:
1. file plan
2. route plan
3. capability boundaries
4. implementation notes
5. verification checklist
6. release risks
```

## Expected output

```text
$ myapp doctor
OK  Flutter stable
OK  Dart 3
OK  router configured

$ myapp plan branch-finder --json
{
  "features":["auth","location","maps","notifications","web"],
  "boundaries":["auth-state","permission-handling","payload-parsing","web-startup"]
}

$ myapp verify branch-finder
PASS route guard is outside widget tree
PASS location permission flow is isolated
PASS notification routing uses a dedicated resolver
PASS web release checklist is attached
```

## Review notes

- auth state ต้องไม่อยู่แค่ใน screen
- location permission handling ต้องแยกจาก map rendering
- notification payload parsing ต้องไม่อยู่ใน widget
- web deployment rules ต้องตรงกับ router strategy

## Verification notes

- ตรวจว่า permission handling ถูก isolate
- ตรวจว่า notification intent parsing ถูก isolate
- ตรวจว่า release checklist ครอบคลุม web startup และ deployment
