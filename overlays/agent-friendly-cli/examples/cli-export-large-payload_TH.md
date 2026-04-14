---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - export
  - obsidian
aliases:
  - การ Export Payload ขนาดใหญ่
---

# การ Export Payload ขนาดใหญ่

ใช้รูปแบบนี้เมื่อผลลัพธ์ใหญ่เกินกว่าจะเก็บไว้ใน chat หรือ stdout

## สถานการณ์

คำสั่ง discovery หรือ validation สร้าง logs, traces หรือ reports ที่มีประโยชน์
แต่ไม่ควรพิมพ์ออกมา inline

## Pattern

1. default output ต้อง compact
2. มี flag `--output <path>`
3. เขียนผลลัพธ์เต็มลงไฟล์
4. คืนกลับมาแค่ summary สั้น ๆ และ path ที่บันทึก

## ตัวอย่างคำสั่ง

```bash
mycli search --limit 20 --json
mycli export --output artifacts/report.json --json
mycli export logs --output artifacts/logs.txt
```

## ตัวอย่าง output

```text
$ mycli export --output artifacts/report.json --json
Exported 24 records to artifacts/report.json
Bytes written: 18432
Complete: yes

$ mycli export logs --output artifacts/logs.txt
Saved logs to artifacts/logs.txt
Lines written: 1240
```

## ผลลัพธ์ที่ดี

- command บอกว่ากำลัง export อะไร
- command บอกว่าเขียนไปที่ไหน
- command บอกว่าข้อมูลครบหรือไม่
- path ที่คืนต้องเสถียรและเอาไปใช้ต่อได้ง่าย

## ผลลัพธ์ที่ไม่ดี

- dump หลายพันบรรทัดลง stdout
- เขียนไฟล์แต่ไม่บอก path
- ใช้ temp file แบบที่ operator เปิดดูไม่ได้
- export command ไปทำ write อื่นที่ไม่เกี่ยวด้วย

## prompt สั้นสำหรับครั้งหน้า

ใช้ export path สำหรับ payload ใหญ่ ๆ เก็บ stdout ให้เล็ก แล้วเขียน artifact
เต็มลงไฟล์
