# กรณีศึกษา

## กรณีศึกษา 1: อัปเดตโปรไฟล์แบบมี auth
1. frontend common กำหนด form และ error state
2. Next.js overlay วาง route และ protection
3. backend common กำหนด contract และ permission shape
4. backend-node ทำ token issuance, validation และ persistence
5. ตรวจว่า UI ไม่เป็นคนตัดสิน permission และ backend ปฏิเสธการอัปเดตที่ไม่ได้รับอนุญาต

## กรณีศึกษา 2: CRUD table สำหรับ admin
1. frontend common กำหนด list/detail และ loading state
2. Next.js overlay วางหน้าและ boundary ของ data fetch
3. backend common กำหนด contract ของ resource
4. backend-node ทำ API, repositories และ validation
5. ตรวจว่า filter, pagination และ error state อยู่ฝั่ง frontend และ validation อยู่ฝั่ง backend

## กรณีศึกษา 3: flow webhook/job
1. frontend common กำหนด trigger และ feedback state
2. Next.js overlay ดู boundary ของ UI
3. backend common กำหนดกฎความปลอดภัยของ job และ contract
4. backend-node ทำ handler, service orchestration และ async processing
5. ตรวจว่า queueing และ external calls อยู่หลัง service และ adapter boundary
