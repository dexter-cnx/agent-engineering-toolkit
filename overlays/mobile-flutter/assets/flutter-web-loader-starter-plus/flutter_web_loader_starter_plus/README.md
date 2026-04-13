# Flutter Web Loader Starter Plus

ชุดพร้อมใช้สำหรับใส่ startup progress ให้ Flutter web ทุกโปรเจกต์

## Themes
- `minimal`
- `dark`
- `enterprise`

## Tools
- `tool/apply_web_loader.sh`
- `tool/apply_web_loader.ps1`
- `tool/create_flutter_web_app.sh`
- `tool/create_flutter_web_app.ps1`

## Quick start

### macOS / Linux
```bash
bash tool/create_flutter_web_app.sh my_app enterprise
```

### Windows PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File .\tool\create_flutter_web_app.ps1 -AppName my_app -Theme enterprise
```

## Apply to existing project

### macOS / Linux
```bash
bash tool/apply_web_loader.sh /path/to/project dark
```

### Windows PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File .\tool\apply_web_loader.ps1 -ProjectDir C:\path\to\project -Theme dark
```
