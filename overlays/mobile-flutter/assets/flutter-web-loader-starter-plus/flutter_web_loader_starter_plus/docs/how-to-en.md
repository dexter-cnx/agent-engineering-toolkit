# Flutter Web Loader Starter Plus (EN)

## What is new
- 3 themes: `minimal`, `dark`, `enterprise`
- scripts to create a fresh Flutter project and apply the loader automatically
- apply scripts support theme selection

## New project
### macOS / Linux
```bash
bash tool/create_flutter_web_app.sh my_app enterprise
```

### Windows PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File .\tool\create_flutter_web_app.ps1 -AppName my_app -Theme enterprise
```

## Existing project
### macOS / Linux
```bash
bash tool/apply_web_loader.sh . dark
```

### Windows PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File .\tool\apply_web_loader.ps1 -ProjectDir . -Theme dark
```

## Suggested theme usage
- `minimal` for general apps
- `dark` for modern or dev-focused products
- `enterprise` for CRM, admin panels, and B2B apps

## Recommended workflow
- keep this pack in a central starter repo
- always use `create_flutter_web_app.*` for new Flutter web projects
- re-apply after regenerating the web shell
