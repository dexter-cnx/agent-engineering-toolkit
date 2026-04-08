---
tags:
  - tutorial
  - flutter
  - full-example
aliases:
  - Flutter End to End Example
---

# ตัวอย่างเต็ม: Flutter project

หน้านี้สรุปว่า ถ้าจะใช้ toolkit กับ Flutter project จริงหนึ่งตัว ควรเดินอย่างไรตั้งแต่ต้นจนจบ

## สถานการณ์ตัวอย่าง

คุณมี repo เปล่า และอยากได้ Flutter app ที่มี:

- clean architecture
- state management ชัด
- routing ชัด
- localization ชัด
- one feature แรกที่ verify ได้

## เส้นทางแนะนำ

### Phase 1: Bootstrap
ใช้:

- [เริ่มจากโฟลเดอร์เปล่า](./00-common-start.md)
- [เส้นทางหลัก 10 นาทีแรก](./01-golden-path.md)

เป้าหมาย:
- ตั้ง repo
- ใส่ toolkit
- สร้าง AGENTS.md
- เลือก `mobile-flutter` overlay
- เตรียม project memory

### Phase 2: Mental model + workflow
ใช้:

- [Mental model ของระบบ Agent](./02-agent-mental-model.md)
- [Workflow ของจริงแบบ Lead → Architecture → Feature](./03-real-workflow.md)

เป้าหมาย:
- เข้าใจ stage
- ไม่สั่งงานแบบก้อนเดียว

### Phase 3: Flutter-specific build
ใช้ tutorial ใน `docs/tutorials/flutter/`

เริ่มจาก:
- basic Flutter app
- clean architecture + Riverpod / GetX / BLoC
- localization
- DESIGN.md integration ตามต้องการ

### Phase 4: First production feature
ใช้:
- [วิธีสร้าง feature แบบ production](./04-build-production-feature.md)

เลือก feature แรกที่เล็กแต่สำคัญ เช่น:
- login
- profile
- settings
- onboarding

### Phase 5: Multi-agent ถ้างานใหญ่ขึ้น
ใช้:
- [วิธีใช้ multi-agent execution](./07-multi-agent-execution.md)

เช่น:
- UI agent
- state/domain agent
- backend integration agent
- QA / verification agent

### Phase 6: Debug และทำให้ workflow เสถียร
ใช้:
- [วิธี debug agent run ที่พัง](./06-debugging-agent-runs.md)

## prompt starter สำหรับ Flutter repo ใหม่

```text
We are starting from a blank folder for a Flutter app.

Read AGENTS.md first.
Adopt the toolkit into this repository.
Choose the mobile-flutter overlay.
Create a short but production-usable AGENTS.md.
Set up project memory.
Use the canonical lifecycle in order.

Initial goal:
- production-shaped Flutter project structure
- explicit architecture boundaries
- chosen state management and routing
- one small verified feature
- no unnecessary extras
```

## สิ่งที่ควรได้เมื่อจบ example นี้

- Flutter repo ที่มี boundary ชัด
- tutorial path ที่ทีมใหม่ตามได้
- prompt usage ที่ predictable
- verification discipline
- memory discipline
