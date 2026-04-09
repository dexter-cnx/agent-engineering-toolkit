---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - localization
aliases:
  - Flutter CSV Localization EN
  - Multi Language CSV in Flutter EN
---

# How to Localize Multiple Languages in Flutter with One CSV File

Use this tutorial when you want a Flutter app to use one CSV file as the source of truth for multiple languages.

Main packages:
- `easy_localization`
- `easy_localization_loader`

Notes:
- `easy_localization` is the core Flutter localization package.
- If CSV is your source of truth, use `easy_localization_loader` with `CsvAssetLoader()`.
- The official `easy_localization` code generation flow is JSON-oriented, so this tutorial uses the CSV loader approach.

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)

## Mobile Flutter overlay skills to read

- localization workflow, fallback policy, generation pipeline: `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md`

## AGENTS.md Example You Can Use

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
- keep localization setup in the app/bootstrap layer
- do not hardcode translated strings in widgets

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify CSV coverage and fallback behavior
5. Update project memory after durable decisions
```

## Example Prompt to Start

```text
Follow AGENTS.md strictly.
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the mobile-flutter overlay.
Use easy_localization with CsvAssetLoader().
Use the prompt pipeline in order and verify translation coverage.
```

## Start from a Blank Folder

1. Create the project folder.
2. Initialize git.
3. Add the toolkit and project memory.
4. Add `AGENTS.md`.
5. Choose the `mobile-flutter` overlay.
6. Decide how CSV will be loaded into locale assets.
7. Create the Flutter structure and localization folder.
8. Install the localization packages you need.
9. Configure `EasyLocalization` to use `CsvAssetLoader()`.
10. Add a script to validate translation files.
11. Verify key coverage and locale coverage.
12. Save memory about naming and fallback rules.

Example bootstrap:

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

Install packages:

```bash
flutter pub add easy_localization
flutter pub add easy_localization_loader
```

Example `main.dart` setup:

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

## Suggested CSV Shape

Keep one file as the source of truth, for example:

```text
key,en,th,ja
app.title,My App,แอปของฉัน,マイアプリ
home.welcome,Welcome,ยินดีต้อนรับ,ようこそ
```

Keep these rules:

- `key` values must be stable and readable
- each column is one locale
- do not edit generated files directly
- the CSV source must be the shared truth for the team

Example usage in UI:

```dart
Text('home.welcome'.tr())
```

To change locale:

```dart
context.setLocale(const Locale('th', 'TH'));
```

## Prompts to Use

| Stage | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| Plan | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| Architecture | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` + `skills/dependency-review/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | localization boundary, file placement, package choice |
| Implement | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | CSV, loader, generated assets |
| Review | `prompts/review/review_change.md` | `skills/docs-update/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | string coverage and boundary clarity |
| Verify | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` + `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md` | key coverage, fallback checks, evidence |
| Finalize | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | none | durable localization rules |

## Skills to Read

- `skills/skill-router/README.md`
- `skills/risk-scoring/README.md`
- `skills/architecture-review/README.md`
- `skills/dependency-review/README.md`
- `skills/safe-refactor/README.md`
- `skills/docs-update/README.md`
- `skills/verification-pass/README.md`
- `../../../overlays/mobile-flutter/skills/flutter-i18n-l10n/skill.md`

## Scripts to Keep in the Consuming Repo

There is no shared toolkit script for this. Create repo-local commands such as:

```bash
flutter analyze
flutter test
```

You may also add a CSV validation command:

```bash
dart run tool/validate_localization_csv.dart
```

## Suggested Flutter Shape

Separate these responsibilities clearly:

- CSV source
- loader configuration
- generated locale assets
- runtime localization loader
- fallback language handling

## Pitfalls

- letting generated files or fallback config become the source of truth
- drifting keys across languages
- hardcoding strings in the UI without a localization layer
- not testing fallback language behavior

## Verification

- check that the CSV contains all keys for every locale
- check that `CsvAssetLoader()` loads successfully
- run `flutter analyze`
- run `flutter test`
- run the CSV validation command if you add one

## Memory Notes

Store durable decisions about:

- CSV shape
- key naming convention
- fallback language
- the script used to generate or validate localization files
