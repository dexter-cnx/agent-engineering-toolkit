# ปล่อย Flutter app ด้วย AI

## เป้าหมาย

เตรียม Flutter app สำหรับ release บน Android และ iOS โดยมี signing, validation และ CI-aware checks

## สิ่งที่ต้องมี

- รู้ว่า target platform คืออะไร
- รู้ app identifiers และสถานะ signing
- แอป build บนเครื่องได้แล้ว

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/workflows/release-app/README.md`
- `overlays/mobile-flutter/ci/github-actions/validate-skills.yml`
- `overlays/mobile-flutter/ci/github-actions/flutter_overlay_ci.yml`
- `overlays/mobile-flutter/examples/release-config-example.md`
- `overlays/mobile-flutter/policies/secrets/README.md`
- `overlays/mobile-flutter/templates/pull_request_checklist.md`

## ขั้นตอน

1. อ่าน `workflows/release-app/README.md`
2. ตรวจ path ของ Android signing และ requirement ของ iOS readiness
3. ถ้า signing config ยังไม่มี ค่อยแก้ `android/app/build.gradle` และ `android/key.properties`
4. ตรวจ iOS signing และ bundle settings ใน `ios/Runner.xcodeproj` และ `ios/Runner/Info.plist`
5. ใช้ release validation skill เพื่อตรวจเส้นทาง release
6. อย่าใส่ secret ลง git และให้บันทึกแค่ตำแหน่งของ secret
7. รัน overlay validation ก่อนส่งงาน release

## ควรใช้ skill อะไร

- `flutter-android-signing-config`
- `flutter-android-release-validate`
- `flutter-ios-release-readiness`
- `flutter-performance-audit`
- `flutter-web-loading-shell` ถ้า release รวม web ด้วย

## อินพุตที่คาดหวัง

- target platform
- bundle ID หรือ application ID
- signing state
- release timeline
- CI expectations

## เอาต์พุตที่คาดหวัง

- signing config plan
- release validation checklist
- iOS readiness notes
- CI update ถ้าจำเป็น
- risk list ก่อน ship

## ความผิดพลาดที่พบบ่อย

- เอา signing setup กับ release validation มาปนกัน
- commit secret values
- ลืมตรวจ iOS readiness ทั้งที่ Android พร้อมแล้ว
- ข้าม performance check ก่อน release

## วิธีแก้ปัญหา

- ถ้า signing ยังไม่ชัด ให้จัดการ Android signing ก่อน validation
- ถ้า CI fail ให้เช็ก path reference และ secret handling ก่อน
- ถ้าแอปรองรับ web ให้รวม web loading verification ใน pass นี้

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/release-app/README.md and overlays/mobile-flutter/examples/release-config-example.md.

Task:
Prepare the Flutter app for release on <platforms>.

Deliver:
1. signing plan
2. release validation plan
3. exact files to review
4. CI updates needed
5. release risks
```

## English

ดู `release-a-flutter-app-with-ai.md` สำหรับเวอร์ชันภาษาอังกฤษ
