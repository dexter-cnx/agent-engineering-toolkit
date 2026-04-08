#!/usr/bin/env bash
set -euo pipefail

REMOTE_URL=${1:-}

if [ -z "$REMOTE_URL" ]; then
  echo "Usage: $0 <git-remote-url>"
  exit 1
fi

git init
git branch -M main
git remote add origin "$REMOTE_URL"
git add .
git commit -m "Release: agent-engineering-toolkit"
git push -u origin main
