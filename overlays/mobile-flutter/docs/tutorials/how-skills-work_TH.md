# skill ทำงานอย่างไร

## เป้าหมาย

อธิบายวิธีเลือก skill ที่เล็กที่สุด วิธีใช้หลาย skill ร่วมกัน และเมื่อไรควรใช้ workflow แทนการเรียงขั้นตอนเอง

## สิ่งที่ต้องมี

- อ่าน [Getting Started](getting-started.md) แล้ว
- เปิด `overlays/mobile-flutter/SKILLS_INDEX.md` ได้
- รู้เป้าหมายงานว่าเป็น app, feature, release หรือ architecture fix

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/workflows/release-app/README.md`
- `overlays/mobile-flutter/workflows/migrate-project/README.md`
- `overlays/mobile-flutter/examples/real-world/`

## ขั้นตอน

1. ระบุ goal ของงานและไฟล์ที่คาดว่าจะเปลี่ยน
2. ดู `SKILLS_INDEX.md` แล้วหา skill ที่เล็กที่สุดที่ตรงกับ goal
3. ตรวจ `Use when` และ `Do NOT use when` ของ skill นั้น
4. ถ้างานต้องทำตามลำดับ ให้ใช้ workflow จาก `workflows/`
5. ใช้ policy เป็นข้อจำกัด ไม่ใช่ขั้นตอนทำงาน
6. ใช้ example เพื่อยืนยันรูปแบบไฟล์ output

## ควรใช้ skill อะไร

- `flutter-clean-architecture-audit` สำหรับตรวจ boundary
- `flutter-feature-folder-scaffold` สำหรับสร้าง feature tree
- `flutter-feature-contract-scaffold` สำหรับสร้าง domain contracts
- `flutter-riverpod-state-skeleton` หรือ `flutter-getx-controller-skeleton` สำหรับ state
- `flutter-go-router-route-map`, `flutter-go-router-redirect-guard`, `flutter-go-router-deeplink-wireup` สำหรับ routing ที่แยก responsibility
- `flutter-firebase-auth-adapter` และ `flutter-firebase-auth-state` สำหรับแยก auth
- `flutter-android-signing-config`, `flutter-android-release-validate`, `flutter-ios-release-readiness` สำหรับ release

## อินพุตที่คาดหวัง

- เป้าหมายของ feature หรือ workflow
- พาธ repo เป้าหมาย
- การเลือก state management
- platform scope
- ความเสี่ยงหรือข้อจำกัดที่รู้แล้ว

## เอาต์พุตที่คาดหวัง

- skill เดี่ยวหรือ sequence ของ workflow
- ชุดไฟล์ที่ต้องแก้แบบชัดเจน
- boundary ที่ไม่หลุดเข้า widgets
- แผน validation ที่ตรงกับ output

## ความผิดพลาดที่พบบ่อย

- ใช้ skill สองตัวที่แก้ responsibility เดียวกัน
- ใส่ policy text ลงใน skill capsule
- ใช้ workflow doc เป็น implementation file
- เลือก workflow ทั้งที่ skill เดียวพอ

## วิธีแก้ปัญหา

- ถ้า skill สองตัวซ้อนกัน ให้เลือกตัวที่แคบกว่าแล้วดึง rule ร่วมไปไว้ใน workflow
- ถ้า skill ไฟล์ใหญ่เกินไป ให้ split ก่อนขยาย workflow
- ถ้า router หรือ example ไม่ตรง ให้ update `SKILLS_INDEX.md` และ example docs พร้อมกัน

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Read overlays/mobile-flutter/SKILLS_INDEX.md and choose the smallest skill that fits.
If the task needs ordering, follow the matching workflow in overlays/mobile-flutter/workflows/.

Task:
<describe the change>

Deliver:
1. chosen skill or workflow
2. why it is the smallest fit
3. exact files to update
4. output contract
5. validation checklist
```

## English

ดู `how-skills-work.md` สำหรับเวอร์ชันภาษาอังกฤษ
