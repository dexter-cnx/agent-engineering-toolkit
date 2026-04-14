---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - safety
  - obsidian
aliases:
  - เปรียบเทียบ Dry-run กับ Write
---

# เปรียบเทียบ Dry-run กับ Write

ใช้รูปแบบนี้เมื่อ CLI สามารถเปลี่ยน state ได้

## สถานการณ์

คำสั่งหนึ่งสามารถเปลี่ยน state ของ repo, remote state หรือ artifact ที่สร้างขึ้น
ดังนั้น command นั้นควรมี path สำหรับ preview ที่ชัดเจนและแยกจาก live write

## Flow ที่ปลอดภัย

1. ตรวจ state ปัจจุบัน
2. สร้าง draft หรือ dry-run preview
3. รีวิว preview output
4. apply live write เฉพาะตอนที่ผู้ใช้สั่งชัดเจน

## ตัวอย่างคำสั่ง

```bash
mycli draft --json
mycli write --dry-run --json
mycli write --json
```

## ตัวอย่าง output

```text
$ mycli draft --json
{
  "action":"archive",
  "target":"item-184",
  "changes":["set status=archived","move to archive index"]
}

$ mycli write --dry-run --json
Dry run only. No changes applied.
Would archive item-184 and update 2 related records.

$ mycli write --json
Applied: archived item-184
Updated 2 related records
```

## พฤติกรรมที่ดี

- `draft` หรือ `--dry-run` แสดงสิ่งที่จะเปลี่ยนโดยไม่ apply
- preview output ต้อง compact และ machine-readable
- live write ต้องเป็นคนละ command หรือคนละ mode ที่แยกชัด
- error message ต้องบอกก่อนว่าขาดอะไรจึงทำ mutation ไม่ได้

## พฤติกรรมที่ไม่ดี

- read command ที่แอบ mutate state
- write command ที่ไม่มี preview path
- mutation ถูกกระตุ้นโดยค่า default เพราะลืม flag
- dump diff ใหญ่ ๆ ลง stdout แทนการเขียนไฟล์

## prompt สั้นสำหรับครั้งหน้า

ใช้ `draft` หรือ `--dry-run` ก่อน ตรวจ result แล้วค่อย run live write เมื่อ
ผู้ใช้ขอให้ mutate ชัดเจน
