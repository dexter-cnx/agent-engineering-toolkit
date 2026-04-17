# วิธีใช้งาน Composition นี้

## มันคืออะไร

นี่คือเส้นทางอ้างอิงสำหรับการสร้าง frontend แบบ Next.js คู่กับ backend แบบ Node โดยใช้ระบบ overlay แบบโมดูลาร์

## อ่านก่อน

1. README ของ overlay ทั้งสี่
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `CURRICULUM.md`
5. `overlays/backend-common/docs/backend-node-reuse-analysis.md` ถ้าต้องเทียบกับแนวคิดเฉพาะของ Node

## ขั้นตอนการใช้งานจริง

1. เลือก overlay ของ frontend และ backend
2. อ่าน overlay แบบ common ก่อน
3. เลือก skill เฉพาะ stack
4. จับ feature เข้ากับ skill ที่ต้องใช้
5. ทำ contract ก่อนรายละเอียด UI หรือ persistence
6. ตรวจ flow แบบ end-to-end ก่อนปล่อยงาน

## ลำดับทั่วไป

- ขอบเขต frontend
- API contract
- auth และ permission shape
- persistence และ adapter shape
- integration และ test

## Scaffold โปรเจกต์ใหม่

1. สร้างโฟลเดอร์หลัก:
   - `apps/frontend-nextjs/`
   - `apps/backend-node/`
   - `contracts/api/`
   - `project_memory/`
2. สร้างโครง App Router ฝั่ง frontend
3. สร้างโครง src ฝั่ง Node backend
4. เขียน API contract แรกใน `backend-common`
5. ทำ feature map ฝั่ง frontend ให้ตรงกับ contract
6. ลงมือ implement ใน `backend-node`
7. เชื่อม frontend เข้ากับ contract

## ลำดับ feature ที่ควรทำ

### Auth

1. กำหนด auth UX ใน `web-frontend-common`
2. วาง protected route ใน `web-frontend-nextjs`
3. กำหนด token และ permission shape ใน `backend-common`
4. ทำ token และ middleware flow ใน `backend-node`

### CRUD

1. กำหนด list/detail และ form state ใน `web-frontend-common`
2. วาง route และ boundary ใน `web-frontend-nextjs`
3. กำหนด request/response contract ใน `backend-common`
4. ทำ routes, services, repositories และ adapters ใน `backend-node`

## รีวิวโค้ดที่ AI สร้างอย่างปลอดภัย

- ตรวจว่า tree ของไฟล์ตรงกับ scaffold
- ตรวจว่า state ของ frontend อยู่ใน overlay ฝั่ง frontend
- ตรวจว่า contract และ permission อยู่ใน backend-common
- ตรวจว่า detail เฉพาะ Node อยู่ใน backend-node เท่านั้น
- ยืนยันว่ามี test สำหรับ path ที่เสี่ยง
