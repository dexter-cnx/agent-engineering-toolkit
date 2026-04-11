# AGENTS.md — toolkit-i18n

This tool is a reusable CLI for Flutter localization workflows driven by a CSV
source of truth.

## Operating rules

1. Use `toolkit-i18n doctor` first when checking the environment.
2. Use `toolkit-i18n validate <csv-path> --json` before generating files.
3. Use `toolkit-i18n diff <csv-path> --json` to inspect the expected output.
4. Use `toolkit-i18n generate <csv-path> --output <dir>` only for explicit file
   writes to the target output directory.
5. Use `toolkit-i18n keys list <csv-path> --json` to inspect defined keys.
6. Use `toolkit-i18n keys diff --used-file <file> --translations <csv-path>
   --json` to compare architecture exports against translations.csv.
7. Use `toolkit-i18n coverage --used-file <file> --translations <csv-path>
   --json` to summarize defined, used, missing, unused, and feature coverage.
8. Keep stdout compact and structured where practical.
9. Do not mutate the source CSV implicitly.
10. Keep dotted keys as nested JSON when generating language files.
11. Update the CLI contract, README, and companion skill if the command surface
   changes.

## Source expectations

- CSV files should include a `key` column.
- CSV files should include one or more language columns.
- Duplicate keys, malformed rows, missing values, and missing required columns
  should be reported clearly.
