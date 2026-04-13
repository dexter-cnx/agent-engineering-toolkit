#!/usr/bin/env bash
set -euo pipefail

APP_NAME="${1:?Usage: create_flutter_web_app.sh <app_name> [theme] }"
THEME="${2:-minimal}"

flutter create "$APP_NAME"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$SCRIPT_DIR/apply_web_loader.sh" "$APP_NAME" "$THEME"

echo "Done. Next:"
echo "  cd $APP_NAME"
echo "  flutter run -d chrome"
