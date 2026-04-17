# สถาปัตยกรรมอ้างอิง

## การแบ่ง stack ที่แนะนำ
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- Backend: `backend-common` + `backend-node`

## ตัวอย่างโครงสร้าง repo
```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  │  ├─ app/
│  │  ├─ components/
│  │  ├─ features/
│  │  └─ services/
│  └─ backend-node/
│     ├─ src/
│     ├─ test/
│     └─ project_memory/
├─ contracts/
├─ docs/
└─ project_memory/
```

## ลำดับของ contract
1. นิยามความต้องการของ UI ใน `web-frontend-common`
2. ตัดสินใจ boundary ของ Next.js ใน `web-frontend-nextjs`
3. นิยาม API contract ใน `backend-common`
4. แมป contract ไปสู่รายละเอียดของ Node backend ใน `backend-node`

## ตัวอย่าง end-to-end
- auth flow: session state ฝั่ง frontend -> token issuance ฝั่ง backend -> route ที่ถูกป้องกัน
- CRUD flow: form ฝั่ง frontend -> contract ฝั่ง backend -> validation -> persistence
- upload flow: เลือกไฟล์ฝั่ง frontend -> file safety ฝั่ง backend -> storage และ audit
- webhook/job flow: trigger ฝั่ง frontend -> handler ฝั่ง backend -> service orchestration -> async processing

## สิ่งที่นำกลับมาใช้จาก backend-node
- route handler ที่บาง
- orchestration แบบ service-oriented
- แยก repositories และ adapters
- วินัยเรื่อง boundary ระหว่าง handler, service และ repository

## อะไรที่เป็น Node-specific
- runtime และ package scripts
- framework ของ request/response
- กลไก middleware
- convention ด้าน module และ deployment ของ Node

