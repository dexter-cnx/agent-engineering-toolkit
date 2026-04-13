#!/usr/bin/env bash
set -euo pipefail

echo "== Flutter starter bootstrap =="
flutter pub get
python3 tooling/generate_feature.py sample_feature || true
python3 tooling/register_feature.py sample_feature || true
python3 tooling/seed_translation_keys.py || true
python3 tooling/apply_web_loader.py .
echo "Bootstrap complete."
echo "Next:"
echo "1. Review generated sample_feature"
echo "2. Review route registry"
echo "3. Review translations.csv"
echo "4. Run flutter test"
echo "5. Run flutter build web --release"
