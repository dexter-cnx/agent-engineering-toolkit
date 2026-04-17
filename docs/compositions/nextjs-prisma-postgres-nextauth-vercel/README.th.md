# คอมโพซิชัน Next.js + Prisma + Postgres + NextAuth.js + Vercel

คอมโพซิชันนี้เป็นเส้นทางอ้างอิงสำหรับ Next.js แอปเดียวที่ใช้ Server Actions, Prisma, Postgres, NextAuth.js และ Vercel

ใช้เมื่อ:
- UI, mutation, auth และ persistence อยู่ใน deployment เดียว
- ต้องการใช้ server actions สำหรับ form submission และการแก้ไขข้อมูล
- ให้ Prisma เป็นขอบเขตของ database adapter
- ให้ NextAuth.js ดูแล session และการ sign-in
- ให้ Vercel เป็นเป้าหมายการ deploy หลัก

## แนวคิดร่วม
- state และ UX ของ frontend อยู่ใน `web-frontend-common`
- routing และ server/client boundaries ของ Next.js อยู่ใน `web-frontend-nextjs`
- contract, validation, auth shape และ permissions อยู่ใน `backend-common`
- server actions, auth handlers และการเข้าถึง Prisma อยู่ในแอป Next.js เอง

## โครงสร้างเริ่มต้นที่แนะนำ
```text
repo/
├─ apps/
│  └─ web-nextjs/
│     ├─ app/
│     │  ├─ api/
│     │  └─ (routes)/
│     ├─ auth/
│     ├─ db/
│     ├─ prisma/
│     ├─ server/
│     │  ├─ actions/
│     │  ├─ services/
│     │  └─ adapters/
│     ├─ components/
│     ├─ features/
│     └─ tests/
├─ contracts/
│  └─ api/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## แผนผังความสามารถ
| ความสามารถ | ฝั่ง frontend | ฝั่ง backend |
| --- | --- | --- |
| Login / auth | `nextjs-auth-integration`, `server-client-boundaries`, `middleware-protected-routes` | `auth-token-concepts`, `role-permission-model`, `nextauth-session-shape` |
| CRUD screen | `loading-error-empty-states`, `forms-validation-ux`, `api-consumption-patterns` | `api-contracts`, `validation-error-handling`, `prisma-schema-design`, `database-adapter-patterns` |
| Protected mutation | `server-client-boundaries`, `forms-validation-ux` | `api-contracts`, `role-permission-model`, `server-actions-boundary`, `prisma-repository-patterns` |
| Deploy บน Vercel | `deployment-ready-ui`, `runtime-constraints-awareness` | `env-var-management`, `build-time-safety`, `migration-strategy` |

## Checklist ตรวจทาน
- [ ] state ของ frontend ชัดเจน
- [ ] contract ถูกกำหนดก่อนเริ่ม implementation
- [ ] auth และ permission ถูกบังคับบน server
- [ ] server actions สั้นและเรียก service หรือ adapter
- [ ] Prisma ถูกแยกไว้หลัง boundary เล็ก ๆ
- [ ] config ของ Vercel ถูกบันทึกและทำซ้ำได้
- [ ] มี tests สำหรับ path เสี่ยง

## คอมโพซิชันที่เกี่ยวข้อง
- `docs/compositions/nextjs-fullstack/` ถ้าต้องการ path full-stack ที่ทั่วไปกว่า
- `docs/compositions/nextjs-dotnet/` ถ้าต้องการ Next.js คู่กับ ASP.NET Core
- `docs/compositions/nextjs-python-service/` ถ้าต้องการ Next.js คู่กับ Python
- `docs/compositions/nextjs-nodebackend/` ถ้าต้องการ Next.js คู่กับ Node

## อ่านก่อน
1. `HOW_TO_USE.md`
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `FRONTEND_BACKEND_SELECTION_GUIDE.md`
5. `CURRICULUM.md`
