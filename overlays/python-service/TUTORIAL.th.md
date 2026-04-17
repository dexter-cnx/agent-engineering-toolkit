# บทเรียนการใช้งาน

## สถานการณ์
สร้าง endpoint สำหรับ user preferences ใน Python service โดยไม่ให้ transport, business logic และ provider calls ไหลมารวมกันในชั้นเดียว

## ขั้นตอนทีละขั้น
1. เริ่มจากโครงสร้างใน `README.md`
2. อ่าน `AGENTS.overlay.md` เพื่อยืนยันกฎ boundary
3. ใช้ `examples/python_service_feature.md` เพื่อดูรูปแบบ layering ที่คาดหวัง
4. ให้ transport อยู่เฉพาะใน router
5. ให้งาน orchestration อยู่ใน service
6. ให้ persistence อยู่ใน repository
7. ให้อินทิเกรชันภายนอกอยู่ใน adapter
8. เพิ่ม test เพื่อยืนยันว่า endpoint ยังบางอยู่

## ผลลัพธ์ที่ดีควรเป็นแบบนี้
- route บาง
- service รับผิดชอบ use case
- repository ไม่ครอบ business rule
- adapter แยก side effect
- test สะท้อนพฤติกรรมจริง

