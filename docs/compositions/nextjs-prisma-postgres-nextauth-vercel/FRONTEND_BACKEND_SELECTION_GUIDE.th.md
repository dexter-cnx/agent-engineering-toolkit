# คู่มือเลือกฝั่ง Frontend และ Backend

## เมื่อไหร่ควรใช้ชุดไหน
- `web-frontend-common` อย่างเดียว: ออกแบบ UI pattern หรือ prototype flow โดยยังไม่ยึด framework
- `web-frontend-common` + `web-frontend-nextjs`: กำลังสร้าง frontend ของ Next.js จริง
- `web-frontend-common` + `web-frontend-nextjs` + `backend-common`: กำลังสร้าง Next.js แบบ one-app ที่มี auth และ persistence rules
- คอมโพซิชันนี้: ต้องการ one-app path พร้อม Prisma, Postgres, NextAuth.js และ Vercel เป็น production stack หลัก

## ตัวอย่างสถานการณ์
- product MVP -> ใช้คอมโพซิชันนี้เพื่อให้ auth, persistence และ deployment เดินไปด้วยกัน
- internal admin panel -> ใช้เมื่อแอปต้องดูแล CRUD และ access control เอง
- SaaS starter -> ใช้เมื่อมี session, membership ที่ผูกฐานข้อมูล และ deploy บน Vercel
- frontend-first prototype -> เริ่มจาก overlay ฝั่ง frontend แล้วค่อยขยับมาชุดนี้เมื่อ data และ auth เป็นเรื่องจริง
- separate backend project -> ใช้ composition path อื่นแทน

## จุดเริ่มต้นที่ควรอ่าน
| สถานการณ์ | เปิดก่อน |
| --- | --- |
| product MVP | `web-frontend-common/README.md` |
| frontend-first prototype | `web-frontend-common/README.md` |
| SaaS starter | `docs/compositions/nextjs-prisma-postgres-nextauth-vercel/README.md` |
| backend-first API project | `backend-common/README.md` |
