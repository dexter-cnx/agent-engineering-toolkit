# Push Guide

## Create a new Git repository or remote repository
Create or choose a repository for the toolkit.

## Push from local
```bash
unzip <release-archive>.zip
cd <release-folder>

git init
git branch -M main
git remote add origin <your-remote-url>
git add .
git commit -m "Release: agent-engineering-toolkit"
git push -u origin main
```

## Optional next steps
- enable GitHub Discussions
- create a tag such as `v1.0.2`
- create a GitHub Release
- update `CODEOWNERS` if more maintainers are added
