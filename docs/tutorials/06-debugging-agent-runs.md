---
tags:
  - tutorial
  - debugging
  - verification
aliases:
  - Failed Agent Runs
---

# วิธี debug agent run ที่พัง

ต่อให้ tutorial ดีแค่ไหน ก็ยังมีวันที่ agent พาออกทะเล

หน้านี้มีไว้สอนวิธีวินิจฉัยแบบเป็นระบบ

## อาการพบบ่อย

### 1. scope drift
ขอ login แต่ AI ไปแก้ routing, theme, folder structure ทั้ง repo

### 2. hallucinated files
AI อ้างไฟล์หรือ script ที่ไม่มีจริง

### 3. verification ปลอม
บอกว่าผ่านทั้งหมด ทั้งที่ไม่ได้รันอะไรจริง

### 4. architecture leakage
UI ไปคุยกับ network/storage โดยตรง

### 5. review stage อ่อนเกินไป
สรุปว่า “looks good” โดยไม่เจาะปัญหา

## วิธี debug แบบทีละชั้น

### ชั้นที่ 1: เช็ก AGENTS.md
คำถาม:

- repo identity ชัดไหม
- boundary ชัดไหม
- workflow บังคับให้ verify ไหม
- stack-specific rules พอหรือยัง

ถ้า AGENTS.md กว้างหรือกำกวมเกินไป agent จะ drift ง่าย

### ชั้นที่ 2: เช็ก prompt ว่าข้าม stage ไหม
ถ้าคุณขอให้มัน plan + design + implement + review + verify ใน prompt เดียว
ความแม่นจะตกทันที

### ชั้นที่ 3: เช็กว่ามี architecture stage หรือยัง
ถ้างานแตะ boundary แต่ไม่มี architecture stage มักหลุดชั้น

### ชั้นที่ 4: เช็ก output ของ verify
verify ที่ดีต้องพูด 3 อย่าง:

- ตรวจอะไรแล้ว
- ยังไม่ได้ตรวจอะไร
- ต้องให้คนหรือ CI ตรวจอะไรต่อ

### ชั้นที่ 5: เช็ก memory pollution
ถ้า project memory เก็บเรื่องชั่วคราวเยอะเกินไป
agent จะเริ่มอ้างของเก่าแบบไม่จำเป็น

## prompt แก้สถานการณ์

### กรณี drift

```text
Stop expanding scope.

Re-state the approved task in one paragraph.
List out-of-scope items explicitly.
Continue only with the approved files and boundaries.
```

### กรณี verify ไม่น่าเชื่อถือ

```text
Redo the verification pass.
Only claim checks that were actually performed.
Separate:
- verified
- not verified
- requires human or CI verification
```

### กรณี boundary หลุด

```text
Review the implementation for architecture leakage.
Identify every place where presentation, domain, and data boundaries were crossed.
Propose the smallest corrective refactor.
```

## rule สำคัญ

เวลางานพัง อย่าเริ่มใหม่ทั้งก้อนเสมอไป
หลายครั้งที่ควรย้อนแค่ 1 stage เช่น:

- ย้อนจาก implement ไป architecture
- ย้อนจาก finalize ไป verify
- ย้อนจาก review ไป implement

## สัญญาณว่า tutorial track นี้ช่วยได้
ถ้าคุณ debug ได้จาก stage และ boundary แปลว่าระบบเริ่ม mature แล้ว
