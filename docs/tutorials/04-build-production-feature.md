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

ตัวอย่าง feature: **login feature สำหรับ Flutter app**

## objective

ต้องการ feature ที่มี:

- หน้า login
- use case ใน domain
- repository abstraction
- data source / adapter
- state handling
- navigation หลัง login
- verification plan ที่ชัด

## boundary ที่ควรได้ก่อนเขียน

- UI ห้ามคุยกับ data source ตรง
- auth provider จริงต้องอยู่หลัง abstraction
- token storage เป็น adapter concern
- navigation logic ไม่ควรกระจายมั่ว

## output structure ที่คาดหวัง

```text
presentation/
domain/
data/
```

## prompt sequence ที่แนะนำ

### 1. Plan

```text
Plan a production-shaped login feature for a Flutter app.
Need:
- scope
- files to create
- risks
- verification approach
Do not implement yet.
```

### 2. Architecture

```text
Review the architecture boundary for the login feature.

Decide:
- presentation/domain/data responsibilities
- auth repository abstraction
- session persistence boundary
- state management responsibilities
- route handoff after successful login

Do not implement yet.
```

### 3. Implement

```text
Implement the approved login feature.
Keep boundaries explicit.
Avoid unrelated refactors.
```

### 4. Review

```text
Review the implemented login feature.
Look for:
- boundary leakage
- inconsistent naming
- missing abstractions
- unnecessary complexity
- missing verification
```

### 5. Verify

```text
Produce a verification pass for the login feature.
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

- widget เรียก auth SDK โดยตรง
- use case ไปแตะ storage เอง
- state, routing, side effects ปนกัน
- ไม่มี verification plan
- final summary ไม่บอก limitation

## ควรเขียน tutorial นี้ไปทางไหนต่อ

หลังจากหน้านี้ คุณสามารถแตก worked examples เพิ่มได้ เช่น:

- signup
- settings
- offline sync
- push notification enrollment
- role-based access
