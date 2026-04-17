# Tutorial

เส้นทางนี้แสดงวิธีสร้าง Next.js แอปที่ใช้ Server Actions, Prisma, Postgres, NextAuth.js และ Vercel แบบตรงไปตรงมา

## เป้าหมาย
สร้าง Next.js แอปเดียวที่ดูแล:
- UI
- route protection
- auth sessions
- server actions
- persistence ผ่าน Prisma
- deployment config ของ Vercel

## ขั้นตอน
1. เริ่มจาก repo ว่างหรือ branch ใหม่ที่สะอาด
2. เพิ่ม toolkit และ project memory files
3. อ่าน README ของ overlay หลัก
4. สร้าง Next.js app ด้วย App Router
5. กำหนด contract แรกใน `backend-common`
6. เพิ่ม Prisma schema และเชื่อมฐานข้อมูล
7. เพิ่ม NextAuth.js config และ protected route boundaries
8. เขียน server action แรกใน Next.js app
9. เชื่อม persistence ผ่าน adapter layer เล็ก ๆ
10. เพิ่ม tests สำหรับ path เสี่ยง
11. ตรวจ env vars และ deployment settings ของ Vercel
12. อัปเดต project memory ด้วยการตัดสินใจที่ใช้

## ฟีเจอร์แรกที่เหมาะ
เริ่มจาก authenticated profile update เพราะจะได้แตะ:
- protected routes
- session handling
- server actions
- Prisma writes
- validation

## สิ่งที่ต้องระวัง
- อย่าให้ client components เป็นเจ้าของ permission logic
- อย่าซ่อน validation ไว้ใน presentation-only code
- ให้ server actions สั้น
- แยก Prisma ให้อยู่หลัง boundary เล็ก ๆ
- ทำให้ config ที่ขึ้นกับ deployment ชัดเจน
