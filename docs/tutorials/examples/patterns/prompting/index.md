---
tags:
  - agent-engineering-toolkit
  - tutorial
  - example
  - patterns
  - prompting
  - obsidian
aliases:
  - Prompting Patterns
---

# รูปแบบการตั้ง Prompt

ใช้รูปแบบเหล่านี้เพื่อจัดโครง prompt ก่อนเริ่ม implement

## สถานการณ์ที่พบบ่อย

- การตั้งกรอบงานใหม่
- การ prompt แบบ architecture-first
- การ prompt สำหรับ review และ verification
- การ prompt ตาม design contract

## โครงที่แนะนำ

1. ทวนโจทย์อีกครั้ง
2. ระบุข้อเท็จจริงของ repo
3. ลิสต์สมมติฐาน
4. ระบุข้อจำกัด
5. เลือก stage ถัดไปของ prompt
6. ยังไม่ implement จนกว่าขอบเขตจะชัด

## สิ่งที่ไม่ควรทำ

- ขอให้สร้างโค้ดก่อนที่ contract จะชัด
- ทำให้ review กับ verification กลายเป็นขั้นเดียวกัน
- ปล่อยให้ stack ไม่ระบุ ทั้งที่ stack เป็นสาระสำคัญ
