---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - operator
  - obsidian
aliases:
  - รูปแบบการใช้ CLI
---

# รูปแบบการใช้ CLI

ใช้รูปแบบนี้เมื่อมี CLI ที่ใช้ซ้ำได้อยู่แล้ว และควรใช้มันก่อนกลับไปใช้ shell

## สถานการณ์

ต้อง inspect งานหนึ่งใน repo โดยยังไม่ mutate อะไร

## ลำดับการทำงาน

1. อ่าน CLI contract และ companion skill
2. รัน `doctor`
3. รัน `auth status` ถ้า flow นั้นต้องใช้ credential
4. รัน `search` หรือ `list`
5. รัน `read <id>` กับ stable identifier หนึ่งตัว
6. รัน `download` หรือ `export` ถ้าต้องการ artifact ขนาดใหญ่
7. หยุดที่ `draft` หรือ `--dry-run` สำหรับ write flow เว้นแต่มีคำสั่งให้ mutate ชัดเจน

## ตัวอย่าง session

```bash
mycli doctor
mycli auth status
mycli search --limit 10 --json
mycli read item-184 --json
mycli export item-184 --output artifacts/item-184.json --json
```

## ตัวอย่าง output

```text
$ mycli doctor
OK  mycli 1.4.0
Config  ~/.config/mycli/config.json
Auth    ready

$ mycli auth status
Authenticated as build-bot
Token expires in 14 days

$ mycli search --limit 10 --json
[
  {"id":"item-184","title":"Release 2026-04 audit","status":"open"},
  {"id":"item-191","title":"Release 2026-04 export","status":"queued"}
]

$ mycli read item-184 --json
{"id":"item-184","title":"Release 2026-04 audit","owner":"platform","updatedAt":"2026-04-14T08:30:00Z"}

$ mycli export item-184 --output artifacts/item-184.json --json
Saved item-184 to artifacts/item-184.json
Bytes written: 4821
```

## พฤติกรรมที่ควรได้

- stdout ต้อง compact
- search ต้องพอให้เลือก id ได้
- read ต้องคืนรายละเอียดของ id นั้นแบบ exact
- export ต้องเขียนไฟล์และบอก path

## ความผิดพลาดที่พบบ่อย

- กระโดดไป write เลย
- discovery command พิมพ์เยอะเกินไป
- ใช้ hidden state แทน command ที่ inspect ได้
- ผสม read กับ write ใน command เดียว

## prompt สั้นสำหรับครั้งหน้า

ใช้ repository CLI เดิมก่อน ทำตามลำดับ doctor, auth status ถ้ามี,
discovery, exact read และ export อย่าทำ live write โดยค่าเริ่มต้น
