#!/usr/bin/env bash
set -e

echo "Run these commands after creating a new remote repository:"
echo "git init"
echo "git branch -M main"
echo "git remote add origin <your-remote-url>"
echo "git add ."
echo "git commit -m 'Initial release: agent-engineering-toolkit'"
echo "git push -u origin main"
