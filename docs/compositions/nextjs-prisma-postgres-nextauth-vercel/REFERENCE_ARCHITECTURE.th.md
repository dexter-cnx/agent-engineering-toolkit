# สถาปัตยกรรมอ้างอิง

## การแบ่งสแต็กที่แนะนำ
- Frontend: `web-frontend-common` + `web-frontend-nextjs`
- แนวคิด backend: `backend-common`
- การ implement แบบ app-local: Next.js Server Actions, route handlers, NextAuth.js, Prisma, Postgres และ config ของ Vercel

## โครงสร้าง repo โดยประมาณ
```text
repo/
├─ apps/
│  └─ web-nextjs/
│     ├─ app/
│     │  ├─ api/
│     │  └─ (routes)/
│     ├─ auth/
│     ├─ components/
│     ├─ db/
│     ├─ features/
│     ├─ prisma/
│     ├─ server/
│     │  ├─ actions/
│     │  ├─ services/
│     │  ├─ adapters/
│     │  └─ repositories/
│     └─ tests/
├─ contracts/
├─ docs/
└─ project_memory/
```

## การไหลของ contract
1. กำหนด UI need ใน `web-frontend-common`
2. ตัดสินใจ boundary ของ Next.js ใน `web-frontend-nextjs`
3. กำหนด resource, auth และ permission shape ใน `backend-common`
4. implement Server Action, Prisma adapter และ auth checks ภายในแอป Next.js

## ตัวอย่าง end-to-end
- auth flow: frontend sign-in state -> backend-common session shape -> NextAuth.js config -> protected route behavior
- CRUD flow: frontend form -> backend-common contract -> server action validation -> Prisma write/read
- membership flow: frontend gated UI -> backend-common role rule -> server-side session check -> conditional persistence
- deployment flow: env vars -> Prisma connection -> build checks -> Vercel runtime

## สิ่งที่ reuse จาก web-frontend-nextjs
- ตำแหน่งของ App Router
- server/client boundaries
- route protection
- data fetching discipline

## สิ่งที่ควรอยู่ใน app-local เท่านั้น
- provider และ callback config ของ NextAuth.js
- Prisma client setup และ repository adapters
- server actions และ route handlers
- database migrations และ seed tooling
- handling ของ Vercel runtime และ environment variables

## หมายเหตุเรื่อง persistence
- keep Prisma calls behind a small adapter or repository boundary
- ไม่ให้ client components เห็น database models โดยตรง
- treat schema และ migration changes เป็นส่วนหนึ่งของ implementation order
- ทำให้ env var requirements ชัดเจน เพื่อไม่ให้ deployment พึ่ง state แอบแฝง
