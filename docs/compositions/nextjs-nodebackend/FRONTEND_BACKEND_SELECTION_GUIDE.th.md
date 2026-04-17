# คู่มือเลือก Frontend และ Backend

## เมื่อไรควรใช้ชุดไหน
- ใช้ `web-frontend-common` อย่างเดียว: เมื่อกำลังออกแบบ pattern UI หรือ prototype flow ฝั่ง frontend โดยยังไม่ผูกกับเฟรมเวิร์ก
- ใช้ `web-frontend-common` + `web-frontend-nextjs`: เมื่อกำลังสร้าง frontend Next.js จริง
- ใช้ `backend-common` อย่างเดียว: เมื่อกำลังนิยาม API หรือแนวคิดด้าน security โดยยังไม่ลง runtime
- ใช้ `backend-common` + `backend-node`: เมื่อกำลังสร้าง backend Node จริง
- ใช้ overlay ทั้งสี่ตัว: เมื่อกำลังสร้าง production full-stack app

## ตัวอย่างสถานการณ์
- โปรเจกต์สำหรับเรียนรู้ -> เริ่มจาก common overlays
- solo MVP -> ใช้ common overlays ทั้งสองฝั่งร่วมกับ overlay เฉพาะ stack
- internal admin panel -> ใช้เส้นทาง full-stack
- production SaaS starter -> ใช้ทั้งสี่ overlay และทำตามลำดับการลงมือ
- frontend-first prototype -> เริ่ม frontend ก่อน แล้วค่อย backend
- backend-first API project -> เริ่ม backend ก่อน แล้วค่อย frontend

