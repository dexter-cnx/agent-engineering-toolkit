# toolkit-i18n

A repository CLI for Flutter localization workflows.

## Purpose

`toolkit-i18n` helps coding agents and maintainers validate and generate localization files from a CSV source of truth.

Initial target workflow:

- validate translation CSV structure
- detect missing values and malformed rows
- compare generated output expectations
- generate per-language JSON files into an output directory

## Current command surface

- `toolkit-i18n doctor`
- `toolkit-i18n validate <csv-path> --json`
- `toolkit-i18n diff <csv-path> --json`
- `toolkit-i18n generate <csv-path> --output <dir>`

## Design goals

- non-interactive by default
- compact output
- machine-readable where practical
- safe by default
- output files written to a target directory instead of mutating source files silently

## Typical usage

```bash
toolkit-i18n doctor
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n diff assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n/