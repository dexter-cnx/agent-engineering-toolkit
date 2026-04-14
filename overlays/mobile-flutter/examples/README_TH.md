# ตัวอย่าง Mobile Flutter

ตัวอย่างใช้งานจริงสำหรับ mobile Flutter overlay

ใช้หน้านี้เป็นจุดเริ่มต้นของงาน Flutter ที่ต้องคุมเรื่อง architecture,
testing, localization, route, web loading และ release readiness

## ลำดับการอ่านที่แนะนำ

1. [เริ่มโปรเจกต์ใหม่](./new_project_bootstrap_example_TH.md)
2. [ฟีเจอร์แบบ Clean Architecture](./feature_flow_clean_architecture_example_TH.md)
3. [Localization ด้วย CSV](./localization_csv_example_TH.md)
4. [Navigation และ guarded routes](./navigation_and_guarded_route_example_TH.md)
5. [Web loading และ deployment](./web_loading_and_deployment_example_TH.md)
6. [Review และ release](./review_and_release_example_TH.md)
7. [Maps และ notifications](./maps_and_notifications_example_TH.md)

## สิ่งที่ตัวอย่างชุดนี้สาธิต

- การเลือก skill ให้น้อยแต่พอ
- การเก็บ Flutter-specific assumptions ไว้ใน overlay
- การแยก business logic ออกจาก widgets
- การทำ localization และ tests ให้เป็นงานบังคับ
- การแยก route, permission และ integration ให้ชัด

## แผนภาพตัวอย่าง

| ตัวอย่าง | ใช้เมื่อ | Skill หลัก |
| --- | --- | --- |
| [เริ่มโปรเจกต์ใหม่](./new_project_bootstrap_example_TH.md) | เริ่ม Flutter app ใหม่ด้วย production defaults | `flutter-dev`, `guide-new-flutter-project-bootstrap`, `policy-folder-structure`, `policy-testing-minimum` |
| [ฟีเจอร์แบบ Clean Architecture](./feature_flow_clean_architecture_example_TH.md) | เพิ่มฟีเจอร์แบบ layered และมี tests | `flutter-dev`, `guide-new-feature-flow`, `guide-clean-architecture-feature`, `flutter-state-riverpod` |
| [Localization ด้วย CSV](./localization_csv_example_TH.md) | เก็บ translations ใน CSV เป็น source of truth | `flutter-localization-csv`, `policy-translation-csv`, `flutter-dev` |
| [Navigation และ guarded routes](./navigation_and_guarded_route_example_TH.md) | เพิ่ม route guards และ auth-aware navigation | `flutter-auth`, `flutter-navigation-go_router`, `policy-no-business-logic-in-widget` |
| [Web loading และ deployment](./web_loading_and_deployment_example_TH.md) | เตรียม web startup และ deployment readiness | `guide-flutter-web-loading`, `flutter-web-deployment`, `guide-app-release-checklist` |
| [Review และ release](./review_and_release_example_TH.md) | ทำ code review และ release review | `flutter-code-reviewer`, `flutter-release-reviewer`, `policy-commit-pr-checks` |
| [Maps และ notifications](./maps_and_notifications_example_TH.md) | เชื่อม location, maps, push และ deep-link routing | `flutter-geolocation`, `flutter-maps`, `flutter-push-notifications`, `flutter-deep-link` |
| [Worked example](./worked_example.md) | ส่งมอบ branch-finder flow แบบรวม | `flutter-auth`, `flutter-geolocation`, `flutter-maps`, `flutter-web-deployment` |
| [Feature request example](./feature_request_example.md) | สร้าง profile feature พร้อม localization และ tests | `guide-new-feature-flow`, `guide-clean-architecture-feature`, `flutter-localization-csv`, `flutter-state-riverpod` |

## ตัวอย่างที่มีอยู่แล้ว

- [Worked example](./worked_example.md)
- [Worked example TH](./worked_example_TH.md)
- [Feature request example](./feature_request_example.md)
- [Feature request example TH](./feature_request_example_TH.md)

## เวอร์ชันภาษา

- ไฟล์ภาษาอังกฤษใช้ชื่อเดิมในโฟลเดอร์นี้
- ไฟล์ภาษาไทยใช้ basename เดียวกันและเติม `_TH.md`
- ฮับภาษาอังกฤษอยู่ที่ [README.md](./README.md)
