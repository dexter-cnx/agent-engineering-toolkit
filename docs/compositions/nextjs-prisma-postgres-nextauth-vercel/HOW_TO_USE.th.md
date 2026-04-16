# วิธีใช้คอมโพซิชันนี้

## คืออะไร
เส้นทางอ้างอิงสำหรับ Next.js แอปเดียวที่ใช้ Server Actions, Prisma, Postgres, NextAuth.js และ Vercel

## อ่านก่อน
1. README ของ overlay หลัก
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `CURRICULUM.md`

## วิธีทำงานจริง
1. เลือก overlay ของ frontend
2. อ่าน contract และ auth rules ใน `backend-common`
3. กำหนด boundaries ของ App Router และ server actions ใน `web-frontend-nextjs`
4. กำหนด data model ใน Prisma ก่อนเขียน server actions
5. ใส่ auth, session และ permission ในแอป Next.js
6. แยก persistence ให้อยู่หลัง adapter หรือ repository ที่เล็กพอ
7. ตรวจรูปแบบ deployment บน Vercel ตั้งแต่ต้น

## ลำดับที่เหมาะสม
- scope ของ frontend
- contract และ validation
- auth และ permission shape
- Prisma schema และ migration strategy
- รูปแบบ server action
- รูปแบบ adapter และ service
- tests และ deployment config

## ตัวอย่างการเลือกใช้
- product MVP -> ใช้คอมโพซิชันนี้เพื่อให้ auth, persistence และ deployment เดินไปด้วยกัน
- internal admin panel -> ใช้เมื่อแอปต้องดูแล CRUD และ access control เอง
- SaaS starter -> ใช้เมื่อมี session, membership ที่ผูกฐานข้อมูล และ deploy บน Vercel

## สร้างโปรเจกต์ใหม่
1. สร้างโฟลเดอร์ร่วม:
   - `apps/web-nextjs/`
   - `contracts/api/`
   - `project_memory/`
2. สร้างโครงสร้าง App Router
3. เพิ่ม `prisma/schema.prisma` และ migration แรก
4. เพิ่ม `auth/` หรือ `auth.ts` สำหรับ NextAuth.js
5. กำหนด contract แรกใน `backend-common`
6. เขียน server action แรกและเชื่อมกับ Prisma
7. เพิ่ม protected route แรก
8. ตั้งค่า env vars และ deployment checks ของ Vercel
9. เพิ่ม tests สำหรับ path เสี่ยง

## ลำดับที่แนะนำสำหรับฟีเจอร์
### Auth
1. กำหนด UX ของ auth ใน `web-frontend-common`
2. วาง protected routes และ boundaries ใน `web-frontend-nextjs`
3. กำหนด session, role และ permission shape ใน `backend-common`
4. ใส่ NextAuth.js config และ server-side session checks

### CRUD
1. กำหนด list/detail และ form states ใน `web-frontend-common`
2. วาง routes และ boundaries ใน `web-frontend-nextjs`
3. กำหนด request/response contract ใน `backend-common`
4. เขียน server actions, Prisma access และ validation ใน Next.js app

### Deployment
1. ให้ logic ที่ไวต่อ runtime อยู่ฝั่ง server
2. ตรวจ env vars ในเครื่องก่อน
3. ยืนยันว่า migrations รันได้ตาม flow ที่ deploy
4. ตรวจว่า Vercel runtime เข้ากับ server-actions และ database strategy ที่เลือก

## ตรวจโค้ดจาก AI อย่างปลอดภัย
- ตรวจว่า tree ของไฟล์ตรงกับ scaffold
- ตรวจว่า auth และ permission อยู่ฝั่ง server
- ตรวจว่า Prisma ถูกใช้ผ่าน data layer ที่แคบ
- ตรวจว่า server actions ไม่ปน UI concerns กับ persistence details
- ตรวจว่ามี tests สำหรับ path เสี่ยง
