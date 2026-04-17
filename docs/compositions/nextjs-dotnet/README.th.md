# การประกอบ Next.js + .NET

ชั้น composition นี้อธิบายการใช้ร่วมกันของ:
- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/backend-dotnet/`

ใช้เป็นเส้นทางอ้างอิงสำหรับ full-stack แบบพร้อมใช้งานในงานจริง

## โครงสร้างที่แนะนำ
```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  │  ├─ app/
│  │  ├─ components/
│  │  ├─ features/
│  │  └─ services/
│  └─ backend-dotnet/
│     ├─ src/
│     ├─ tests/
│     └─ Api/
├─ contracts/
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## ตารางจับคู่ feature กับ skill
| Feature | Frontend skills | Backend skills |
| --- | --- | --- |
| Auth/login | `auth-ux`, `nextjs-auth-integration`, `middleware-protected-routes` | `auth-token-concepts`, `jwt-auth-dotnet`, `refresh-token-dotnet`, `role-permission-model` |
| CRUD screen | `loading-error-empty-states`, `forms-validation-ux`, `api-consumption-patterns` | `api-contracts`, `crud-resource-design`, `validation-error-handling`, `efcore-basics` |
| File upload | `loading-error-empty-states`, `api-consumption-patterns` | `file-handling-safety`, `validation-error-handling`, `efcore-basics` |

## เช็กลิสต์ตรวจโค้ดที่ AI สร้าง
- [ ] state ฝั่ง frontend ชัดเจน
- [ ] contract ถูกกำหนดก่อน implementation
- [ ] auth และ permission บังคับที่ backend
- [ ] โค้ดที่ AI สร้างตรงกับโครงสร้างโฟลเดอร์
- [ ] มี test ครอบคลุมเส้นทางเสี่ยง

## อ่านก่อน
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
