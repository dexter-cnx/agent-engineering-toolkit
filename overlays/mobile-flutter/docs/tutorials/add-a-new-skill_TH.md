# เพิ่ม skill ใหม่

## เป้าหมาย

อธิบายวิธีเพิ่ม Flutter skill แบบ atomic ด้วย path และขั้นตอนที่สั้นที่สุด

## สิ่งที่ต้องมี

- ตรวจ `SKILLS_INDEX.md` ก่อนว่ามี responsibility นี้แล้วหรือยัง
- แน่ใจว่างานนี้ไม่ใช่ policy, template, workflow หรือ tutorial
- อ่าน `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md` และ `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md`

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md`
- `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md`
- `overlays/mobile-flutter/AGENT_CONTRIBUTION_RULES.md`
- `overlays/mobile-flutter/SKILL_SCHEMA.md`
- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `tools/skillgen/README.md`
- `tools/skillgen/bin/skillgen`

## ขั้นตอน

1. ยืนยันว่า responsibility นี้ยังไม่มีใน `SKILLS_INDEX.md`
2. อ่าน `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md` เพื่อเช็กเกณฑ์การเพิ่ม skill
3. ใช้ `tools/skillgen/bin/skillgen new` เพื่อ scaffold skill
4. เติม `SKILL.md` ให้ครบทุก required field พร้อม input, output และ reference จริง
5. sync `SKILLS_INDEX.md` และรัน validator

## ใช้อะไรบ้าง

- `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md` สำหรับ rules ฝั่ง contributor
- `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md` สำหรับเกณฑ์รับงาน
- `tools/skillgen/bin/skillgen` สำหรับ scaffold และ validate

## เอาต์พุตที่คาดหวัง

- skill folder ใหม่ใน category ที่ถูกต้อง
- `SKILL.md` ที่ครบ schema
- example และ template reference อย่างน้อยอย่างละหนึ่ง
- index และ validation ที่อัปเดตแล้ว

## ความผิดพลาดที่พบบ่อย

- สร้าง skill ใหม่ทั้งที่ skill เดิมย่อ boundary ได้
- ทิ้ง placeholder text ไว้ใน `SKILL.md`
- ใช้ workflow/policy/tutorial แทน skill จริง

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Read overlays/mobile-flutter/CONTRIBUTING_SKILLS.md and overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md first.
Use tools/skillgen/bin/skillgen to scaffold the skill.

Task:
Create a new atomic skill called <skill name>.

Deliver:
1. why the new skill is needed
2. exact files to create
3. category and naming
4. example/template links
5. validation checklist
```

## วิธีแก้ปัญหา

- ถ้า skill ดูคล้ายของเดิม ให้ split boundary ก่อนสร้าง
- ถ้า generator สร้างไม่ครบ ให้เติม schema field ที่ขาดแล้วรันใหม่
- ถ้า validation fail ให้แก้ path และ reference ก่อน
