# บทเรียนการใช้งาน

## สถานการณ์
สร้างหน้า account settings ที่ถูกป้องกันด้วย auth ใน Next.js พร้อม server-side data loading และ client-side form editing

## ขั้นตอนทีละขั้น
1. เริ่มจาก common overlay เพื่อกำหนด state และฟอร์ม
2. ใช้ skill เรื่อง App Router เพื่อวางหน้าให้ถูกตำแหน่ง
3. แยก server/client boundary ให้ชัด
4. ป้องกัน route ด้วย middleware
5. ตรวจ loading, error และ failure state

