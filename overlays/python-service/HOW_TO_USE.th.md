# วิธีใช้งานโอเวอร์เลย์นี้

## มันคืออะไร
โอเวอร์เลย์นี้ให้แนวทางที่ใช้ได้จริงสำหรับ Python service, FastAPI app, worker, adapter layer และระบบ automation

## เมื่อใช้
ใช้เมื่อคุณต้องการ:
- transport handler ที่บาง
- orchestration ใน service layer
- boundary ของ repository และ adapter
- พฤติกรรม background job ที่ปลอดภัย
- โครงสร้างโปรเจกต์ที่ดูแลง่าย

## ใช้ร่วมกับโอเวอร์เลย์อื่นอย่างไร
- ใช้ร่วมกับ `overlays/backend-common/` สำหรับแนวคิด backend แบบกลาง runtime
- ใช้ร่วมกับ `docs/compositions/nextjs-python-service/` เมื่อ backend เป็นส่วนหนึ่งของ full-stack Next.js

## ขั้นตอนเริ่มต้นแบบเร็ว
1. อ่าน `README.md`
2. อ่าน `AGENTS.overlay.md`
3. เปิด `TUTORIAL.md`
4. ดูตัวอย่างใน `examples/`
5. ทำตามกฎ boundary ใน `AGENTS.overlay.md`

## งานที่พบบ่อย
| งาน | อ่านก่อน |
| --- | --- |
| เริ่ม Python service ใหม่ | `README.md` และ `AGENTS.overlay.md` |
| เพิ่ม endpoint ใหม่ | `AGENTS.overlay.md` และ `examples/python_service_feature.md` |
| รีวิวสถาปัตยกรรม | `AGENTS.overlay.md` และ `README.md` |
| ตรวจ composition backend | `docs/compositions/nextjs-python-service/README.md` |

## กฎสำคัญ
- ทำ route handler ให้บาง
- วาง provider calls ไว้หลัง adapter
- อย่าใส่ business rules ใน transport layer
- ให้ test อยู่ใกล้พฤติกรรมที่ต้องป้องกัน

