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

## ตัวอย่างที่มีอยู่แล้ว

- [Worked example](./worked_example.md)
- [Feature request example](./feature_request_example.md)

## เวอร์ชันภาษา

- ไฟล์ภาษาอังกฤษใช้ชื่อเดิมในโฟลเดอร์นี้
- ไฟล์ภาษาไทยใช้ basename เดียวกันและเติม `_TH.md`
- ฮับภาษาอังกฤษอยู่ที่ [README.md](./README.md)
