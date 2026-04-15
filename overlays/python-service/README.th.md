# โอเวอร์เลย์ Python Service

ใช้อโอเวอร์เลย์นี้เมื่อ repository ปลายทางเป็น Python service, FastAPI application, worker, adapter layer หรือระบบ automation

## ใช้ร่วมกับ
- `overlays/backend-common/` สำหรับแนวคิด backend แบบกลาง runtime
- `docs/compositions/README.md` สำหรับตัวเลือกการประกอบ full-stack
- `docs/compositions/nextjs-python-service/` สำหรับ Next.js + Python service

## ครอบคลุมอะไรบ้าง
- โครงสร้างแยก router, service, repository, domain, adapter และ schema
- การรักษา route handler ให้บาง
- การดึง provider ภายนอกออกไปไว้ที่ adapter
- การเก็บ contract, retry และ background-job behavior ใน memory หรือเอกสารที่ชัดเจน

## ไม่ครอบคลุม
- รายละเอียดเฉพาะของ Next.js
- รายละเอียดเฉพาะของ ASP.NET Core
- ความรู้เฉพาะของ Node runtime

