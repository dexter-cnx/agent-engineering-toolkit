---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - obsidian
aliases:
  - ตัวอย่าง CLI ที่เป็นมิตรกับเอเจนต์
---

# ตัวอย่าง

ตัวอย่างใช้งานจริงสำหรับ agent-friendly CLI overlay

ใช้หน้านี้เป็นจุดเริ่มต้นของ workflow ที่ต้องอ่านก่อน ใช้ output ให้สั้น
และปลอดภัยโดยค่าเริ่มต้น

## ลำดับการอ่านที่แนะนำ

1. [รูปแบบการนำ CLI ไปใช้](./cli-adoption-workflow_TH.md)
2. [รูปแบบการใช้ CLI](./cli-operator-workflow_TH.md)
3. [เปรียบเทียบ Dry-run กับ Write](./cli-dry-run-vs-write_TH.md)
4. [การ Export Payload ขนาดใหญ่](./cli-export-large-payload_TH.md)
5. [เช็กลิสต์การตรวจ CLI](./cli-verification-checklist_TH.md)
6. [การจัดการความล้มเหลวของ CLI](./cli-failure-handling_TH.md)

## เวอร์ชันภาษา

- ไฟล์ภาษาอังกฤษใช้ชื่อเดิมในโฟลเดอร์นี้
- ไฟล์ภาษาไทยใช้ basename เดียวกันและเติม `_TH.md`
- คู่ของแต่ละ scenario ควรมีโครงสร้างสอดคล้องกัน
- ฮับภาษาอังกฤษอยู่ที่ [README.md](./README.md)

## สิ่งที่ตัวอย่างชุดนี้ครอบคลุม

- การเปลี่ยนงานที่ทำซ้ำให้เป็น CLI ที่ใช้ซ้ำได้
- การทำ discovery ก่อน exact read
- การเก็บ output ใหญ่ลงไฟล์
- การแยก draft หรือ dry-run ออกจาก live write
- การ verify CLI จากนอก source directory
- การรายงาน failure ให้ชัดเจน

## ขอบเขต

ตัวอย่างชุดนี้ตั้งใจให้เป็นกลางต่อ stack
ถ้าต้องการรายละเอียดเฉพาะภาษา framework หรือ product ให้ใช้ overlay ของ
repo ปลายทางแทน
