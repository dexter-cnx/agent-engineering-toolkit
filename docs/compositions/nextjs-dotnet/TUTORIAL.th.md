# บทเรียนการใช้งาน

## สถานการณ์
สร้าง flow สำหรับจัดการบัญชีผู้ใช้ด้วย overlay ทั้งสี่ตัว

## ขั้นตอนทีละขั้น
1. เริ่มจาก `web-frontend-common` เพื่อกำหนด state ของหน้า ฟอร์ม และพฤติกรรม loading
2. ใช้ `web-frontend-nextjs` เพื่อวาง route และแยกงาน server กับ client
3. ใช้ `backend-common` เพื่อกำหนด contract, validation และ permission
4. ใช้ `backend-dotnet` เพื่อทำ auth, persistence, middleware และ health checks
5. ตรวจ request/response shape แบบ end-to-end
6. เพิ่ม test ในชั้นที่พฤติกรรมอาจพัง

## สิ่งที่ต้องตรวจ
- ownership ของ route และ page
- ความเสถียรของ contract
- permission บังคับที่ backend
- ความปลอดภัยของไฟล์หรือข้อมูลถ้า flow ใช้อัปโหลด

