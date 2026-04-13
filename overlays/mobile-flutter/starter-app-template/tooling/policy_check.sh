#!/usr/bin/env bash
set -euo pipefail

fail() {
  echo "[policy-check] $1" >&2
  exit 1
}

[[ -f pubspec.yaml ]] || fail "pubspec.yaml not found"
[[ -d lib ]] || fail "lib directory not found"
[[ -f assets/i18n/translations.csv ]] || fail "assets/i18n/translations.csv missing"
[[ -f lib/app/router/app_router.dart ]] || fail "router file missing"
[[ -d lib/features ]] || fail "features directory missing"

grep -q "go_router" pubspec.yaml || fail "go_router dependency missing"
grep -q "flutter_riverpod" pubspec.yaml || fail "flutter_riverpod dependency missing"
grep -q "easy_localization" pubspec.yaml || fail "easy_localization dependency missing"

echo "[policy-check] OK"
