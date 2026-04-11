# toolkit-i18n CLI Contract

## Purpose

Validate and generate localization outputs from a CSV source of truth for Flutter projects.

## Required commands

- `toolkit-i18n doctor`
- `toolkit-i18n validate <csv-path> --json`
- `toolkit-i18n diff <csv-path> --json`
- `toolkit-i18n generate <csv-path> --output <dir>`

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

### validate

Returns compact findings such as:

- missing key column
- duplicate keys
- empty values by language
- malformed rows

### diff

Returns compact summary of what would be generated.

### generate

Writes per-language JSON files to the target output directory and reports the file paths.

## Safety rules

- no implicit overwrite of source-of-truth CSV
- generated files go to the requested output directory
- no live mutation unless an explicit apply-style command is added later

## Verification requirements

Prove:

1. command resolves from outside the source folder
2. help or usage is understandable
3. doctor works
4. validate works
5. generate writes files to the requested directory
