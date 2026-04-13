#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="${1:-.}"
THEME="${2:-minimal}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE_DIR="$ROOT_DIR/templates/$THEME"

if [ ! -d "$TEMPLATE_DIR" ]; then
  echo "Unknown theme: $THEME"
  echo "Available themes: minimal, dark, enterprise"
  exit 1
fi

mkdir -p "$PROJECT_DIR/web"

cp "$TEMPLATE_DIR/index.html" "$PROJECT_DIR/web/index.html"
cp "$TEMPLATE_DIR/style.css" "$PROJECT_DIR/web/style.css"
cp "$TEMPLATE_DIR/flutter_bootstrap.js" "$PROJECT_DIR/web/flutter_bootstrap.js"

echo "Applied Flutter web loader"
echo "Project: $PROJECT_DIR"
echo "Theme: $THEME"
