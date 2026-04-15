# โอเวอร์เลย์ Backend Node

ใช้อโอเวอร์เลย์นี้เมื่อ repository ปลายทางเป็น Node backend, API service หรือ job processor

## ใช้ร่วมกับ
- `overlays/backend-common/` สำหรับแนวคิด backend แบบกลาง runtime
- `docs/compositions/README.md` สำหรับตัวเลือกการประกอบ full-stack
- `docs/compositions/nextjs-nodebackend/` สำหรับ Next.js + Node backend
- `overlays/backend-common/docs/backend-node-reuse-analysis.md` สำหรับดูว่าควรนำแนวคิดใดไปใช้ซ้ำ

## ครอบคลุมอะไรบ้าง
- route handler ที่บาง
- service สำหรับ orchestration
- repository และ adapter ที่แยกชัด
- แนวคิดการเก็บ project memory สำหรับ conventions ระยะยาว

## ไม่ครอบคลุม
- รายละเอียดเฉพาะของ Next.js
- รายละเอียดเฉพาะของ Python service
- รายละเอียดเฉพาะของ ASP.NET Core

