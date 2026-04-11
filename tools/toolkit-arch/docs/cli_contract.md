# toolkit-arch CLI Contract

## Purpose

Validate repository architecture guardrails and connect source structure to localization coverage.

## Required commands

- `toolkit-arch doctor`
- `toolkit-arch scan --target <path> --json`
- `toolkit-arch violations --target <path> --json --limit 20`
- `toolkit-arch export --target <path> --output <file>`
- `toolkit-arch i18n-usage --target <path> --output <file> --json`
- `toolkit-arch i18n-layer-check --target <path> --json`
- `toolkit-arch i18n-coverage --target <path> --translations <csv-path> --json`

## Output expectations

### i18n-usage

Returns compact usage information with:

- target
- used_keys
- source matches
- output file path when exported

Exports a JSON report that downstream localization tooling can read.

### i18n-layer-check

Returns compact architecture findings with:

- forbidden_usages
- review_usages
- exception_usages when repository-approved exceptions are detected

### i18n-coverage

Returns a combined localization coverage summary with:

- defined_keys
- used_keys
- missing_keys
- unused_keys
- feature_coverage

## Safety rules

- no implicit source mutation
- no live write behavior unless an explicit output path is provided
- keep command output compact and machine-readable
