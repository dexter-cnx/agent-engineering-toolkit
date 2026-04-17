# ดัชนี Composition

ส่วนนี้รวมเส้นทาง full-stack reference ที่ประกอบจากระบบ overlay แบบโมดูลาร์

## Composition ที่มี
- [Next.js + ASP.NET Core](nextjs-dotnet/README.md)
- [Next.js Full Stack](nextjs-fullstack/README.md)
- [Next.js + Prisma + Postgres + NextAuth.js + Vercel](nextjs-prisma-postgres-nextauth-vercel/README.md)
- [Next.js + Python Service](nextjs-python-service/README.md)
- [Next.js + Node Backend](nextjs-nodebackend/README.md)

## วิธีเลือก
- ใช้เส้นทาง .NET เมื่อ backend เป้าหมายคือ ASP.NET Core หรือ .NET
- ใช้เส้นทาง Next.js full stack เมื่อ frontend และ backend อยู่ใน Next.js แอปเดียว
- ใช้เส้นทาง Prisma/Postgres/NextAuth.js/Vercel เมื่อ backend แบบอยู่ในแอปต้องมีฐานข้อมูล, auth, และการ deploy ที่มี opinion ชัดเจน
- ใช้เส้นทาง Python เมื่อ backend เป้าหมายคือ Python service, worker หรือ adapter layer
- ใช้เส้นทาง Node เมื่อ backend เป้าหมายคือ Node API หรือ job processor

## โครงสร้างเริ่มต้น
เลือกโฟลเดอร์แอปให้ตรงกับ path ที่จะใช้:
- `frontend-nextjs/` เมื่อ frontend จับคู่กับ backend แยก
- `web-nextjs/` เมื่อ backend อยู่ใน Next.js แอปเดียว

```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  ├─ web-nextjs/
│  └─ backend-{dotnet|python|node}/
├─ contracts/
│  ├─ api/
│  └─ events/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## ก่อนลงมือทำ
- เลือก backend implementation overlay เพียงตัวเดียว หรือใช้ backend แบบอยู่ในแอปเดียวเมื่อใช้ Next.js full stack
- เขียน contract ใน `backend-common` ก่อนเริ่ม implementation
- รีวิวโค้ดที่ AI สร้างด้วยกฎ boundary ของ overlay ที่เลือก

## ลำดับการอ่าน
1. อ่าน README ของ overlay ที่เกี่ยวข้อง
2. อ่าน README ของ composition ที่ตรงกับ stack
3. อ่าน selection guide
4. ทำตาม implementation order
5. ใช้ curriculum เมื่อสอนระบบให้สมาชิกทีมใหม่
