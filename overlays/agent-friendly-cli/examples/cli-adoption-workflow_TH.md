---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - adoption
  - obsidian
aliases:
  - รูปแบบการนำ CLI ไปใช้
---

# รูปแบบการนำ CLI ไปใช้

ใช้รูปแบบนี้เมื่อ repo มีงานซ้ำที่ตอนนี้ยังแก้ด้วย shell command แบบเฉพาะหน้า

## สถานการณ์

ทีมหนึ่งต้องทำงานเดิมซ้ำ ๆ:

- ตรวจสภาพแวดล้อม
- ไล่รายการ candidate
- อ่านรายละเอียดของรายการหนึ่ง
- export รายงานขนาดใหญ่

งานแบบนี้ควรถูกยกเป็น CLI ที่ใช้ซ้ำได้ แทนการเขียนสคริปต์ชั่วคราว

## แผน

1. อ่าน CLI contract หรือ companion skill ที่มีอยู่
2. เสนอ command surface ก่อนลงมือ implement
3. ทำ default ให้ compact และไม่ interactive
4. แยก discovery ออกจาก exact read
5. เพิ่ม path สำหรับ export ไฟล์ใหญ่
6. ให้ write อยู่หลัง draft หรือ dry-run ก่อน
7. verify จากนอก source directory

## ตัวอย่าง command surface

```bash
mycli doctor
mycli auth status
mycli search --json --limit 20
mycli read <id> --json
mycli export --output artifacts/report.json --json
mycli draft --json
mycli write --dry-run
```

## ตัวอย่าง output

```text
$ mycli doctor
OK  mycli 1.4.0
Config  ~/.config/mycli/config.json
Auth    ready

$ mycli search --json --limit 20
[
  {"id":"item-184","title":"Release 2026-04 audit","status":"open","age":"2h"},
  {"id":"item-191","title":"Release 2026-04 export","status":"queued","age":"5h"}
]

$ mycli read item-184 --json
{"id":"item-184","title":"Release 2026-04 audit","owner":"platform","summary":"Review pending exports and mark the final report path."}

$ mycli export --output artifacts/report.json --json
Exported 24 records to artifacts/report.json
Complete: yes
```

## รูปแบบผลลัพธ์ที่ดี

- `doctor` บอกว่า install และ dependencies พร้อมหรือไม่
- `auth status` บอกว่า credentials พร้อมหรือยัง
- `search` คืนรายการ candidate แบบ compact
- `read <id>` คืนรายละเอียดของ stable identifier หนึ่งตัว
- `export` เขียนไฟล์และบอก path ที่บันทึก
- `draft` หรือ `--dry-run` แสดงสิ่งที่จะเปลี่ยนโดยไม่ apply

## สิ่งที่ต้องระวัง

- มี interactive prompt ใน flow ปกติ
- ยิง JSON ใหญ่มากไปที่ stdout
- discovery command ไม่บอก id ที่เอาไปอ่านต่อได้
- write เกิดขึ้นทั้งที่กำลังอ่านข้อมูล

## prompt สั้นสำหรับครั้งหน้า

ใช้ repository CLI ก่อน เริ่มจาก `doctor` แล้วค่อย discovery, exact read,
export และหยุดที่ `draft` หรือ `--dry-run` เว้นแต่ผู้ใช้สั่ง live write ชัดเจน
