#!/usr/bin/env bash
set -euo pipefail

echo "== Overlay Phase 21 policy check =="

fail=0
required_files=(
  "pubspec.yaml"
  "lib/app/router/route_registry.dart"
  "assets/i18n/translations.csv"
  "docs/overlay/repo_integration.md"
)

for f in "${required_files[@]}"; do
  if [ ! -f "$f" ]; then
    echo "Missing required file: $f"
    fail=1
  fi
done

if [ -d "lib/features" ]; then
  for dir in lib/features/*; do
    if [ -d "$dir" ]; then
      for req in domain data presentation; do
        if [ ! -d "$dir/$req" ]; then
          echo "Feature missing $req/: $dir"
          fail=1
        fi
      done
    fi
  done
fi

if [ "$fail" -ne 0 ]; then
  echo "Policy check failed."
  exit 1
fi

echo "Policy check passed."
