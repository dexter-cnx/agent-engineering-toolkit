# การวิเคราะห์สิ่งที่นำกลับมาใช้จาก Backend Node

## เหตุผลที่มีเอกสารนี้
`overlays/backend-node` คือ backend overlay ที่มีอยู่เดิมใน repository ส่วน `backend-common` ควรนำกลับมาใช้เฉพาะสิ่งที่เป็นแนวคิดร่วมกัน และไม่ควรคัดลอกรายละเอียดเฉพาะ Node เข้าไปในชั้น backend แบบทั่วไป

## แนวคิดที่นำกลับมาใช้ได้จาก backend-node
- route handler ที่บาง
- service เป็นขอบเขตของ orchestration
- repository เป็นขอบเขตของ persistence
- adapter สำหรับ integration ภายนอก
- project memory สำหรับ conventions ที่ควรจำถาวร

## รูปแบบ skill ที่นำกลับมาใช้ได้
- guidance แบบสั้นและมีงานเดียว
- กฎ boundary ที่ชัดเจน
- verification notes
- เอกสารอิงตัวอย่างขนาดเล็ก

## อะไรที่เป็น Node-specific
- type ของ request/response จาก Express หรือ Fastify
- package และคำสั่งของ Node
- กลไก middleware ของ Node
- convention ด้านไฟล์ โมดูล และ runtime ที่เฉพาะ Node

## backend-common ควรสอดคล้องอย่างไร
- อธิบาย shape ของ backend ในภาษาที่เป็นกลางต่อ runtime
- ใช้คำศัพท์ contract/validation/auth ให้ร่วมกัน
- เก็บรายละเอียด implementation ไว้ใน backend-dotnet หรือ backend-node

## backend-dotnet ควรสอดคล้องอย่างไร
- ใช้ภาษาขอบเขตแบบเดียวกัน
- เก็บรายละเอียด wiring เฉพาะ .NET ไว้ในเอกสารของ .NET
- ใช้ vocabulary ร่วมโดยไม่ดึงสมมติฐานของ Node เข้ามา

## โอกาสในการทำให้สอดคล้องกันในอนาคต
- template สำหรับ API contract ที่ใช้ร่วมกัน
- vocabulary ร่วมสำหรับ auth และ permission
- review checklist ร่วมสำหรับ backend boundaries

