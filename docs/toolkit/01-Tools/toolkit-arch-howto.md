# 🔧 toolkit-arch

Use toolkit-arch to scan architecture boundaries and connect code structure to
localization coverage.

Flow:
doctor → i18n-usage → i18n-layer-check → i18n-coverage

Example:
toolkit-arch i18n-usage --target . --output artifacts/i18n-used-keys.json --json
toolkit-arch i18n-layer-check --target . --json
toolkit-arch i18n-coverage --target . --translations assets/i18n/translations.csv --json
