# Case Studies

## กรณีศึกษา 1: อัปเดตโปรไฟล์หลังล็อกอิน

1. frontend common กำหนด form และ error states
2. Next.js overlay วาง route และ protection
3. backend common กำหนด session และ permission shape
4. แอป Next.js implement NextAuth.js checks, server action และ Prisma update
5. review: UI ต้องไม่เป็นเจ้าของ permissions; server ต้อง reject คำสั่งที่ไม่ได้สิทธิ์

## กรณีศึกษา 2: CRUD admin table

1. frontend common กำหนด list/detail และ loading states
2. Next.js overlay วาง page และ server-action boundary
3. backend common กำหนด resource contract
4. แอป Next.js implement validation, Prisma queries และ mutation handling
5. review: frontend ดูแล filters, pagination และ errors; server ดูแล data integrity

## กรณีศึกษา 3: organization access control

1. frontend common กำหนด gated UI states
2. Next.js overlay วาง protected route
3. backend common กำหนด role และ membership rule
4. แอป Next.js ตรวจ session และโหลดเฉพาะข้อมูลที่อนุญาต
5. review: access control ต้องอยู่ฝั่ง server ไม่ใช่การเดาจาก client state
