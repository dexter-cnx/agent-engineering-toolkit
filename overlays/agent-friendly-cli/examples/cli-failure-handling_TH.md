---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - failures
  - obsidian
aliases:
  - การจัดการความล้มเหลวของ CLI
---

# การจัดการความล้มเหลวของ CLI

ใช้รูปแบบนี้เมื่อ CLI ต้อง fail ให้ชัดเจนและช่วยแก้ปัญหาได้

## สถานการณ์

CLI ขาด setup, credential หรือ valid identifier

## กรณีที่ fail

### ขาด setup

พฤติกรรมที่ควรได้:

- `doctor` บอกว่าขาดอะไร
- ข้อความบอกวิธีแก้
- exit code ต้องไม่เป็นศูนย์

### ขาด auth

พฤติกรรมที่ควรได้:

- `auth status` บอกว่า credential หรือ session หาย
- command ไม่ควรพยายามไปต่อแบบเงียบ ๆ
- output ต้อง compact

### identifier ไม่ถูกต้อง

พฤติกรรมที่ควรได้:

- `read <id>` บอกว่าไม่พบ ID
- command แนะนำให้ใช้ `search` หรือ `list` ก่อน

### ไม่มีผลลัพธ์

พฤติกรรมที่ควรได้:

- `search` บอกชัดเจนว่าไม่มีผลลัพธ์
- output ยังควรมี context พอให้ปรับ query ต่อ

## ตัวอย่างข้อความ

```text
Missing configuration: set MYCLI_TOKEN or run mycli auth login.
No results found for "release-2026-04". Try a wider search or use mycli list.
Unknown item id: item-184. Run mycli search --limit 20 to discover valid IDs.
```

## ตัวอย่าง response

```text
$ mycli doctor
Error: missing configuration
Set MYCLI_TOKEN or run `mycli auth login`.
Exit code: 2

$ mycli auth status
Error: authentication required
No valid session found.
Exit code: 3

$ mycli read item-999
Error: unknown item id item-999
Try `mycli search --limit 20` to find valid IDs.
Exit code: 4
```

## anti-pattern

- raw stack trace สำหรับ user error ปกติ
- fail แบบเงียบและยัง exit 0
- ข้อความกำกวมเช่น "error occurred"
- fallback ที่ซ่อนปัญหาจริง

## prompt สั้นสำหรับครั้งหน้า

ทำให้ failure ชัด, ใช้การได้, และ compact ชี้ไปยังคำสั่งถัดไปที่ปลอดภัย
