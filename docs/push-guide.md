# Push Guide

## Create a new GitHub repository
Create an empty repository named `agent-engineering-toolkit`.

## Push from local
```bash
unzip agent-engineering-toolkit-release-v0.1.2.zip
cd agent-engineering-toolkit-release-v0.1.2

git init
git branch -M main
git remote add origin git@github.com:<your-org>/agent-engineering-toolkit.git
git add .
git commit -m "Initial public release: agent-engineering-toolkit"
git push -u origin main
```

## Optional next steps
- enable GitHub Discussions
- create a tag such as `v0.1.2`
- create the first GitHub Release
- update `CODEOWNERS` if more maintainers are added
