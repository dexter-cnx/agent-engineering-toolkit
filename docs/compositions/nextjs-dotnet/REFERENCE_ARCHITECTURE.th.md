# สถาปัตยกรรมอ้างอิง

## การแบ่ง stack ที่แนะนำ
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend: `backend-common` + `backend-dotnet`

## ตัวอย่างโครงสร้าง repo
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
├─ docs/
└─ project_memory/
```

## ลำดับของ contract
1. นิยามความต้องการของ UI ใน `web-frontend-common`
2. ตัดสินใจ boundary ของ Next.js ใน `web-frontend-nextjs`
3. นิยาม API contract ใน `backend-common`
4. แมป contract ไปสู่รายละเอียด ASP.NET Core ใน `backend-dotnet`

## ตัวอย่าง end-to-end
- auth flow: session state ฝั่ง frontend -> token issuance ฝั่ง backend -> route ที่ถูกป้องกัน
- CRUD flow: form ฝั่ง frontend -> contract ฝั่ง backend -> validation -> persistence
- upload flow: เลือกไฟล์ฝั่ง frontend -> file safety ฝั่ง backend -> storage และ audit
- permission flow: การแสดงผลฝั่ง frontend -> authorization ฝั่ง backend -> audit trail

