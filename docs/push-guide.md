# Push Guide

## Create a new GitHub repository
Create an empty repository named `agent-engineering-toolkit`.

## Push from local
```bash
unzip agent-engineering-toolkit-final-public.zip
cd agent-engineering-toolkit-final-public

git init
git branch -M main
git remote add origin git@github.com:dexter-cnx/agent-engineering-toolkit.git
git add .
git commit -m "Initial public release: agent-engineering-toolkit"
git push -u origin main
```

## Optional next steps
- enable GitHub Discussions
- create first tag such as `v0.1.0`
- create first GitHub Release
- update CODEOWNERS if more maintainers are added
