# toolkit-i18n CLI Contract

## Purpose

Validate and generate localization outputs from a CSV source of truth for Flutter projects.

## Required commands

- `toolkit-i18n doctor`
- `toolkit-i18n validate <csv-path> --json`
- `toolkit-i18n diff <csv-path> --json`
- `toolkit-i18n generate <csv-path> --output <dir>`
- `toolkit-i18n keys list <csv-path> --json`
- `toolkit-i18n keys diff --used-file <file> --translations <csv-path> --json`
- `toolkit-i18n coverage --used-file <file> --translations <csv-path> --json`

## Input expectations

The CSV file is expected to:

- contain a key column
- contain one or more language columns
- support dotted keys for nested JSON generation

## Output expectations

### doctor

Returns:

- command availability
- runtime assumptions
- basic environment readiness

Supports `--json` for compact machine-readable output.

### validate

Returns compact findings such as:

- missing key column
- duplicate keys
- empty values by language
- malformed rows

Use `--json` in agent workflows so the output stays easy to parse.

### diff

Returns compact summary of what would be generated.

Includes the expected per-language output file names and row counts.

### generate

Writes per-language JSON files to the target output directory and reports the file paths.

Uses dotted keys to build nested JSON objects.

Supports `--json` for compact machine-readable output.

### keys list

Returns the unique keys defined in `translations.csv`.

Use `--output` when the full key list is large.

### keys diff

Compares used localization keys exported by `toolkit-arch i18n-usage` against `translations.csv`.

Returns missing keys, unused keys, and matched keys in compact form.

The preferred flags are `--used-file` and `--translations`. Legacy aliases may
still be accepted for compatibility.

### coverage

Summarizes defined, used, missing, unused, and feature coverage.

Supports the same `--used-file` JSON input as `keys diff`.

## Safety rules

- no implicit overwrite of source-of-truth CSV
- generated files go to the requested output directory
- no live mutation unless an explicit apply-style command is added later
- dotted keys must remain nested in output JSON

## Verification requirements

Prove:

1. command resolves from outside the source folder
2. help or usage is understandable
3. doctor works
4. validate works
5. generate writes files to the requested directory
