# กรณีศึกษา

## กรณีศึกษา 1: อัปเดตโปรไฟล์แบบมี auth
1. frontend common กำหนด form และ error state
2. Next.js overlay วาง route และ protection
3. backend common กำหนด contract และ permission shape
4. python-service ทำ token/session, validation และ persistence
5. ตรวจว่า UI ไม่เป็นคนตัดสิน permission และ backend ปฏิเสธการอัปเดตที่ไม่ได้รับอนุญาต

## กรณีศึกษา 2: CRUD table สำหรับ admin
1. frontend common กำหนด list/detail และ loading state
2. Next.js overlay วางหน้าและ boundary ของ data fetch
3. backend common กำหนด contract ของ resource
4. python-service ทำ API, repository และ validation
5. ตรวจว่า filter, pagination และ error state อยู่ฝั่ง frontend และ validation อยู่ฝั่ง backend

## กรณีศึกษา 3: flow ประมวลผลไฟล์แบบ async
1. frontend common กำหนด input และ failure state
2. Next.js overlay ดู boundary ของ UI
3. backend common กำหนดกฎความปลอดภัยของไฟล์
4. python-service ทำ validation, queueing และ worker processing
5. ตรวจว่า file type และ size check เกิดก่อน queueing และ access rule อยู่บน backend
