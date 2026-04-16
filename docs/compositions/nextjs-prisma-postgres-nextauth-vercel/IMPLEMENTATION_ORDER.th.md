# ลำดับการทำงาน

## ลำดับที่แนะนำ
1. กำหนด scenario และ scope
2. ใช้ `web-frontend-common` เพื่อกำหนด state และ form behavior
3. ใช้ `web-frontend-nextjs` เพื่อวาง routes และ boundaries
4. ใช้ `backend-common` เพื่อกำหนด contract, validation, auth และ permissions
5. ออกแบบ Prisma schema และ migration path
6. เพิ่ม NextAuth.js config และ session shape
7. Implement server actions, services และ Prisma adapters
8. เพิ่ม tests และตรวจ deployment config สำหรับ Vercel

## เหตุผลที่เรียงแบบนี้
- contracts มาก่อน code
- auth และ persistence สอดคล้องกับ data model
- server actions สั้น
- constraints ของ deployment เห็นชัดก่อนงานบาน
- review ง่ายขึ้นเพราะแต่ละชั้นมีหน้าที่เดียว
