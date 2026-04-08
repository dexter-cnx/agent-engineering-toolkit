---
tags:
  - tutorial
  - production-feature
  - worked-example
aliases:
  - Build Feature
---

# วิธีสร้าง feature แบบ production

tutorial นี้ทำให้เห็นว่างานจริง 1 ชิ้นควรถูกผลักผ่าน toolkit อย่างไร

ตัวอย่าง feature: **account preferences capability**

## objective

ต้องการ feature ที่มี:

- entry flow ที่ชัด
- use case ใน domain
- repository abstraction
- data source / adapter
- state handling ถ้าจำเป็น
- handoff หรือ navigation หลังบันทึกสำเร็จ ถ้ามี
- verification plan ที่ชัด

## boundary ที่ควรได้ก่อนเขียน

- entry-layer code ห้ามคุยกับ data source ตรง
- provider จริงต้องอยู่หลัง abstraction
- persistence เป็น adapter concern
- handoff logic ไม่ควรกระจายมั่ว

## output structure ที่คาดหวัง

```text
entry/
domain/
data/
```

## prompt sequence ที่แนะนำ

### 1. Plan

```text
Plan a production-shaped account preferences feature for the consuming repo.
Need:
- scope
- files to create
- risks
- verification approach
Do not implement yet.
```

### 2. Architecture

```text
Review the architecture boundary for the account preferences feature.

Decide:
- entry/domain/data responsibilities or the equivalent layers in this repo
- repository abstraction
- persistence boundary
- state management responsibilities
- handoff after successful save

Do not implement yet.
```

### 3. Implement

```text
Implement the approved account preferences feature.
Keep boundaries explicit.
Avoid unrelated refactors.
```

### 4. Review

```text
Review the implemented account preferences feature.
Look for:
- boundary leakage
- inconsistent naming
- missing abstractions
- unnecessary complexity
- missing verification
```

### 5. Verify

```text
Produce a verification pass for the account preferences feature.
State clearly:
- what was checked
- what was not checked
- what still needs human or CI verification
```

## checklist หลังจบงาน

- มี input validation หรือยัง
- error state ชัดหรือยัง
- success path ชัดหรือยัง
- loading state ชัดหรือยัง
- testable boundary มีหรือยัง
- secret หรือ provider-specific code ถูกดันไปหลัง adapter หรือยัง

## สัญญาณว่า feature ยังไม่ production-shaped

- entry code เรียก provider SDK โดยตรง
- use case ไปแตะ storage เอง
- state, handoff, side effects ปนกัน
- ไม่มี verification plan
- final summary ไม่บอก limitation

## ควรเขียน tutorial นี้ไปทางไหนต่อ

หลังจากหน้านี้ คุณสามารถแตก worked examples เพิ่มได้ เช่น:

- signup
- settings
- offline sync
- push notification enrollment
- role-based access
