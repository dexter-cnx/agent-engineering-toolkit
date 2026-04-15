# การประกอบ Next.js + Python Service

ชั้น composition นี้อธิบายการใช้ร่วมกันของ:
- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/python-service/`

ใช้เป็น reference ที่พร้อมใช้งานสำหรับงาน Next.js frontend คู่กับ Python service backend

## โครงสร้างที่แนะนำ
```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  │  ├─ app/
│  │  ├─ components/
│  │  ├─ features/
│  │  └─ services/
│  └─ backend-python/
│     ├─ app/
│     │  ├─ routers/
│     │  ├─ services/
│     │  ├─ repositories/
│     │  ├─ domain/
│     │  ├─ adapters/
│     │  └─ schemas/
│     ├─ tests/
│     └─ scripts/
├─ contracts/
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## ตารางจับคู่ feature กับ skill
| Feature | Frontend skills | Backend skills |
| --- | --- | --- |
| Auth/login | `auth-ux`, `nextjs-auth-integration`, `middleware-protected-routes` | `auth-token-concepts`, `refresh-token-strategy`, `role-permission-model` |
| CRUD screen | `loading-error-empty-states`, `forms-validation-ux`, `api-consumption-patterns` | `api-contracts`, `crud-resource-design`, `validation-error-handling`, `backend-testing-strategy` |
| Async job flow | `loading-error-empty-states`, `api-consumption-patterns` | `api-contracts`, `backend-testing-strategy` |

## เช็กลิสต์ตรวจโค้ดที่ AI สร้าง
- [ ] state ฝั่ง frontend ชัดเจน
- [ ] contract ถูกกำหนดก่อน implementation
- [ ] permission rules ถูกบังคับที่ backend
- [ ] โค้ดที่ AI สร้างตรงกับโครงสร้างโฟลเดอร์
- [ ] มี test ครอบคลุมเส้นทางเสี่ยง

## อ่านก่อน
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
