# สถาปัตยกรรมอ้างอิง

## การแบ่ง stack ที่แนะนำ
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend: `backend-common` + `python-service`

## ตัวอย่างโครงสร้าง repo
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
│     ├─ tests/
│     └─ scripts/
├─ contracts/
├─ docs/
└─ project_memory/
```

## ลำดับของ contract
1. นิยามความต้องการของ UI ใน `web-frontend-common`
2. ตัดสินใจ boundary ของ Next.js ใน `web-frontend-nextjs`
3. นิยาม API contract ใน `backend-common`
4. แมป contract ไปสู่รายละเอียดของ Python service ใน `python-service`

## ตัวอย่าง end-to-end
- auth flow: session state ฝั่ง frontend -> backend issuance ของ token/session -> route ที่ถูกป้องกัน
- CRUD flow: form ฝั่ง frontend -> contract ฝั่ง backend -> validation -> persistence
- upload flow: เลือกไฟล์ฝั่ง frontend -> file safety ฝั่ง backend -> storage และ audit
- async job flow: action ฝั่ง frontend -> enqueue งานฝั่ง backend -> worker ประมวลผล -> polling สถานะ

