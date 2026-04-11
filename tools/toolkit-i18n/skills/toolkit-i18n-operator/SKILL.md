---
name: toolkit-i18n-operator
description: Use the toolkit-i18n CLI for repeated Flutter localization workflows with compact outputs, CSV validation, generated JSON exports, and safe non-mutating behavior.
---

# When to use

Use this skill when the task involves Flutter localization files generated from a CSV source of truth.

# Preferred workflow

1. `toolkit-i18n doctor`
2. `toolkit-i18n validate <csv-path> --json`
3. `toolkit-i18n diff <csv-path> --json`
4. `toolkit-i18n generate <csv-path> --output <dir>`

# Output rules

- keep stdout compact
- prefer structured output where practical
- write generated language files to a target directory
- always report generated file paths

# Safety

- do not overwrite source CSV implicitly
- do not add or run live write behavior unless explicitly requested

# Common prompts

- Use toolkit-i18n-operator to validate assets/i18n/translations.csv and summarize the top issues.
- Use toolkit-i18n-operator to generate localization JSON files into artifacts/i18n and report the file paths.