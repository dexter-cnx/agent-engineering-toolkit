# ตัวอย่าง Maps และ notifications

## สถานการณ์

แอปมือถือสำหรับลูกค้าต้องมี location-aware maps และ notification routing

ตัวอย่างการเปลี่ยนแปลง:

- current-location support
- เลือกสาขาจาก map
- push notification tap-to-route
- deep-link handoff ไปยังหน้าที่ถูกต้อง

## Skill ที่แนะนำ

- `flutter-geolocation`
- `flutter-maps`
- `flutter-push-notifications`
- `flutter-deep-link`
- `flutter-dev`
- `policy-no-business-logic-in-widget`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/flutter-geolocation/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-maps/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-push-notifications/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-deep-link/SKILL.md`
- `overlays/mobile-flutter/prompts/add_maps_feature.md`
- `overlays/mobile-flutter/prompts/add_notifications_feature.md`
- `overlays/mobile-flutter/prompts/add_customer_visit_map.md`
- `overlays/mobile-flutter/prompts/add_auth_feature.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-geolocation
- flutter-maps
- flutter-push-notifications
- flutter-deep-link
- flutter-dev

Reference files:
- overlays/mobile-flutter/skills/flutter-geolocation/SKILL.md
- overlays/mobile-flutter/skills/flutter-maps/SKILL.md
- overlays/mobile-flutter/prompts/add_maps_feature.md
- overlays/mobile-flutter/prompts/add_notifications_feature.md

Task:
Implement a branch finder flow with location permission handling, map selection,
and notification tap routing.

Deliver:
1. capability boundaries
2. route plan
3. permission plan
4. verification checklist
```

## สิ่งที่ควรได้

- permission handling แยกจาก map rendering
- notification payload parsing อยู่นอก widgets
- route decisions deterministic และ testable
- location กับ deep-link boundaries ชัดเจน

## Review notes

- อย่า parse navigation intent ใน UI widgets
- keep platform permission code isolated
- อย่าให้ map widget เป็นเจ้าของ business rules

## Verification notes

- ตรวจว่า permission handling ไม่ได้อยู่ใน map widget
- ตรวจว่า notification payload parsing ไม่ได้อยู่ใน presentation code
- ตรวจว่า route decisions มี test และ deterministic
