# Flutter Web Loader Starter Plus (TH)

## มีอะไรเพิ่มจากชุดแรก
- 3 themes: `minimal`, `dark`, `enterprise`
- script สำหรับสร้างโปรเจกต์ใหม่แล้ว apply loader ให้อัตโนมัติ
- apply script รองรับการเลือก theme

## ใช้กับโปรเจกต์ใหม่

### macOS / Linux
```bash
bash tool/create_flutter_web_app.sh my_app minimal
bash tool/create_flutter_web_app.sh my_app dark
bash tool/create_flutter_web_app.sh my_app enterprise
```

### Windows PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File .\tool\create_flutter_web_app.ps1 -AppName my_app -Theme minimal
powershell -ExecutionPolicy Bypass -File .\tool\create_flutter_web_app.ps1 -AppName my_app -Theme dark
powershell -ExecutionPolicy Bypass -File .\tool\create_flutter_web_app.ps1 -AppName my_app -Theme enterprise
```

## ใช้กับโปรเจกต์เดิม
```bash
bash tool/apply_web_loader.sh . enterprise
```

หรือ

```powershell
powershell -ExecutionPolicy Bypass -File .\tool\apply_web_loader.ps1 -ProjectDir . -Theme enterprise
```

## คำแนะนำ
- `minimal` เหมาะกับ internal tool / dashboard ทั่วไป
- `dark` เหมาะกับ app สมัยใหม่หรือสาย dev tool
- `enterprise` เหมาะกับ CRM, admin, B2B portal

## workflow ที่ควรใช้
- เก็บชุดนี้ไว้ใน repo กลาง
- ใช้ `create_flutter_web_app.*` เป็นจุดเริ่มต้นทุกครั้ง
- ถ้าโดน `flutter create . --platforms web` เขียนทับ ให้ apply ใหม่ทันที
