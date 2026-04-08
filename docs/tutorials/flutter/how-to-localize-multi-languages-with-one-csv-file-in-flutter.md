---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - localization
aliases:
  - Flutter CSV Localization
  - Multi Language CSV in Flutter
---

# วิธีทำ localization หลายภาษาใน Flutter ด้วย CSV ไฟล์เดียว

ใช้ tutorial นี้เมื่อคุณต้องการให้ Flutter app ใช้ CSV ไฟล์เดียวเป็น source of truth สำหรับหลายภาษา

แพ็กเกจหลักที่ใช้:
- `easy_localization`
- `easy_localization_loader`

หมายเหตุ:
- `easy_localization` เป็นแพ็กเกจหลักสำหรับแปลภาษาใน Flutter
- ถ้าใช้ CSV เป็น source of truth ให้ใช้ `easy_localization_loader` และ `CsvAssetLoader()`
- หากต้องการ code generation แบบทางการของ `easy_localization` เอง เอกสารหลักรองรับ JSON เป็นหลัก ดังนั้น tutorial นี้จึงใช้ CSV loader แทน

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)

## skill ของ Mobile Flutter overlay ที่ควรอ่าน

- localization workflow, fallback policy, generation pipeline: `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md`

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** CSV-first Localization
**Localization:** CSV-first
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- easy_localization
- easy_localization_loader
- CSV asset file

## 3. Architecture Rules

- CSV is the source of truth
- keep localization setup in app/bootstrap layer
- do not hardcode translated strings in widgets

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify CSV coverage and fallback behavior
5. Update project memory after durable decisions
```

## ตัวอย่าง prompt เริ่มงาน

```text
Follow AGENTS.md strictly.
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the mobile-flutter overlay.
Use easy_localization with CsvAssetLoader().
Use the prompt pipeline in order and verify translation coverage.
```

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์โปรเจกต์
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `mobile-flutter` overlay
6. ตัดสินใจว่าจะ generate หรือ load locale assets จาก CSV อย่างไร
7. สร้างโครง Flutter และโฟลเดอร์ localization
8. ติดตั้งแพ็กเกจ localization ที่ต้องใช้
9. ตั้งค่า `EasyLocalization` ให้ใช้ `CsvAssetLoader()`
10. สร้าง script สำหรับ validate translation files
11. verify ความครบถ้วนของ key และ locale
12. บันทึก memory เรื่อง naming และ fallback

ตัวอย่าง bootstrap:

```bash
mkdir flutter-csv-localization
cd flutter-csv-localization
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory assets/i18n tool
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
```

ติดตั้งแพ็กเกจ:

```bash
flutter pub add easy_localization
flutter pub add easy_localization_loader
```

ตัวอย่างการตั้งค่าใน `main.dart`:

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:easy_localization_loader/easy_localization_loader.dart';
import 'package:flutter/material.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await EasyLocalization.ensureInitialized();
  runApp(
    EasyLocalization(
      supportedLocales: const [
        Locale('en', 'US'),
        Locale('th', 'TH'),
        Locale('ja', 'JP'),
      ],
      fallbackLocale: const Locale('en', 'US'),
      path: 'assets/i18n/translations.csv',
      assetLoader: CsvAssetLoader(),
      child: const MyApp(),
    ),
  );
}
```

## โครง CSV ที่แนะนำ

เก็บไฟล์เดียวไว้เป็น source of truth เช่น:

```text
key,en,th,ja
app.title,My App,แอปของฉัน,マイアプリ
home.welcome,Welcome,ยินดีต้อนรับ,ようこそ
```

กติกาที่ควรยึด:

- `key` ต้องเสถียรและอ่านง่าย
- แต่ละคอลัมน์คือ locale หนึ่งตัว
- อย่าแก้ข้อความโดยตรงใน generated files
- CSV ต้นฉบับต้องเป็นแหล่งที่ทีมเดียวกันยอมรับร่วมกัน

ตัวอย่างการใช้งานใน UI:

```dart
Text('home.welcome'.tr())
```

ถ้าต้องการเปลี่ยนภาษา:

```dart
context.setLocale(const Locale('th', 'TH'));
```

## prompts ที่ควรใช้

| Stage | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| Plan | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| Architecture | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` + `skills/dependency-review/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | localization boundary, file placement, package choice |
| Implement | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | CSV, loader, generated assets |
| Review | `prompts/review/review_change.md` | `skills/docs-update/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | string coverage, boundary clarity |
| Verify | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | key coverage, fallback checks, evidence |
| Finalize | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary, follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | none | durable localization rules |

## skills ที่ควรอ่าน

- `skills/skill-router/README.md`
- `skills/risk-scoring/README.md`
- `skills/architecture-review/README.md`
- `skills/dependency-review/README.md`
- `skills/safe-refactor/README.md`
- `skills/docs-update/README.md`
- `skills/verification-pass/README.md`
- `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md`

## scripts ที่ควรมีใน consuming repo

ไม่มี script กลางของ toolkit สำหรับ localization นี้ ให้สร้าง script ใน repo ปลายทางเอง เช่น:

```bash
flutter analyze
flutter test
```

คุณอาจเพิ่ม command สำหรับ validate CSV เช่น:

```bash
dart run tool/validate_localization_csv.dart
```

## โครง Flutter ที่แนะนำ

แยก responsibility ให้ชัด:

- CSV source
- loader configuration
- generated locale assets
- runtime localization loader
- fallback language handling

## pitfall

- ให้ generated file หรือ fallback config กลายเป็น source of truth
- ปล่อยให้ key drift ระหว่างภาษา
- hardcode string ลงใน UI โดยไม่ผ่าน localization layer
- ไม่ทดสอบ fallback language

## การ verify

- ตรวจว่า CSV มี key ครบทุกภาษา
- ตรวจว่า `CsvAssetLoader()` โหลดได้ครบ
- รัน `flutter analyze`
- รัน `flutter test`
- ถ้ามี command validate CSV ให้รันด้วย

## memory notes

เก็บ decision ถาวรเกี่ยวกับ:

- โครง CSV
- naming convention ของ key
- fallback language
- script ที่ใช้ generate หรือ validate
