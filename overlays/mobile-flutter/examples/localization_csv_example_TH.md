# ตัวอย่าง Localization ด้วย CSV

## สถานการณ์

แอปเพิ่ม user-facing strings ใหม่ และต้องให้ CSV localization เป็น source of truth

ตัวอย่างการเปลี่ยนแปลง:

- เพิ่ม settings page
- เพิ่ม labels, helper text, validation messages
- อัปเดต `assets/i18n/translations.csv`

## Skill ที่แนะนำ

- `flutter-localization-csv`
- `policy-translation-csv`
- `flutter-dev`
- `policy-testing-minimum`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md`
- `overlays/mobile-flutter/skills/policy-translation-csv/SKILL.md`
- `overlays/mobile-flutter/templates/translations.csv`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-localization-csv
- policy-translation-csv
- flutter-dev

Reference files:
- overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md
- overlays/mobile-flutter/skills/policy-translation-csv/SKILL.md
- overlays/mobile-flutter/templates/translations.csv

Task:
Add localized strings for a new settings page and update the CSV source of
truth.

Deliver:
1. key list
2. CSV update plan
3. affected Dart files
4. verification checklist
```

## Expected output

- keys ใหม่ถูกเพิ่มใน CSV ก่อน
- generated localization artifacts ถูกอัปเดต
- Dart code ใช้ stable keys ไม่ hard-code text
- มี check เรื่อง fallback behavior เมื่อจำเป็น

## Review notes

- ตั้งชื่อ key ให้สม่ำเสมอและสื่อความ
- อย่าเพิ่ม key ชั่วคราวหรือ duplicate ลง source CSV
- update project memory เฉพาะ naming/fallback rules ที่ถาวร

## Verification notes

- ตรวจว่า CSV ยังเป็น source of truth
- ตรวจว่า artifacts ที่ generate ถูกอัปเดตหลังแก้ CSV
- ตรวจว่า code ใช้ keys ไม่ใช่ข้อความฝังตรง ๆ
