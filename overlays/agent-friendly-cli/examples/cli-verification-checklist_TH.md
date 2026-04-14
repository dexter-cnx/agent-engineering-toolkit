---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - verification
  - obsidian
aliases:
  - เช็กลิสต์การตรวจ CLI
---

# เช็กลิสต์การตรวจ CLI

ใช้เช็กลิสต์นี้เพื่อพิสูจน์ว่า CLI ใช้ซ้ำโดย agent ได้จริง

## สิ่งที่ต้องตรวจ

1. command เรียกได้จากนอก source folder
2. help output อ่านแล้วเข้าใจ
3. มี `doctor` และใช้งานได้จริง
4. มี `auth status` เมื่อ workflow นั้นต้องใช้ auth
5. discovery flow ใช้งานได้
6. exact read flow ใช้งานได้
7. large output export เขียนลงไฟล์ได้
8. live write ไม่ถูกกระตุ้นโดยไม่ตั้งใจ

## ตัวอย่างหลักฐาน

```bash
cd /tmp
mycli --help
mycli doctor --json
mycli search --limit 5 --json
mycli read item-184 --json
mycli export --output /tmp/artifact.json --json
```

## ตัวอย่างผลลัพธ์

```text
$ cd /tmp
$ mycli --help
Usage: mycli <command> [options]

$ mycli doctor --json
{"status":"ok","config":"~/.config/mycli/config.json","auth":"ready"}

$ mycli export --output /tmp/artifact.json --json
Exported 5 records to /tmp/artifact.json
Complete: yes
```

## สิ่งที่ควรดูว่าโอเค

- แต่ละ command มีหน้าที่ชัดและแคบ
- failure บอกวิธีแก้
- search output ช่วยเลือก stable ID ได้
- export output บอก path
- ไม่มี command ไหนที่ surprise ด้วย live mutation

## สิ่งที่ยังต้องระวัง

- command ที่ใช้ได้เฉพาะตอนอยู่ใน repo
- help text ยาวเกินกว่าจะสแกนเร็ว ๆ
- discovery command ที่ไม่มี limit
- identifier ที่ไม่เสถียรหรือกำกวม

## prompt สั้นสำหรับครั้งหน้า

verify CLI จากนอก source directory ให้ครบ help, doctor, discovery, exact read,
export และยืนยันว่า live writes ไม่ได้เกิดขึ้นเอง
