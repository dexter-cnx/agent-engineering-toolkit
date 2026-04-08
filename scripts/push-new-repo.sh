#!/usr/bin/env bash
set -e

git init
git branch -M main
git remote add origin git@github.com:dexter-cnx/agent-engineering-toolkit.git
git add .
git commit -m "Initial public release: agent-engineering-toolkit"
git push -u origin main
