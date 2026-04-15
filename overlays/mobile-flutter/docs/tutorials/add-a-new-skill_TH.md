# เพิ่ม skill ใหม่

## เป้าหมาย

เพิ่ม Flutter skill แบบ atomic ให้ปลอดภัยและไม่ทับ responsibility ที่มีอยู่

## สิ่งที่ต้องมี

- อ่าน [SKILLS_INDEX.md](../../SKILLS_INDEX.md) แล้ว
- รู้ว่า task นี้เป็น skill ใหม่จริง ไม่ใช่ policy/template/example
- เข้าใจว่า skill ต้องมี one responsibility

## พาธใน repository ที่ต้องเปิด

- `overlays/mobile-flutter/AGENT_CONTRIBUTION_RULES.md`
- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `overlays/mobile-flutter/SKILL_SCHEMA.md`
- `overlays/mobile-flutter/docs/tutorials/add-a-new-skill.md`
- `tools/skillgen/README.md`

## ขั้นตอน

1. ตรวจ skill ที่ใกล้ที่สุดใน `SKILLS_INDEX.md`
2. อ่าน `AGENT_CONTRIBUTION_RULES.md` และ maintainer checklist
3. ใช้ generator สร้าง skill folder ใหม่
4. เติมทุก required section ใน `SKILL.md`
5. เพิ่ม example และ template reference อย่างน้อยอย่างละหนึ่ง
6. sync `SKILLS_INDEX.md`
7. รัน validation, overlap detection และ docs sync
8. อัปเดต workflow หรือ tutorial เฉพาะเมื่อ orchestration เปลี่ยนจริง

## ควรใช้ skill อะไร

- `flutter-clean-architecture-audit` สำหรับตรวจว่า skill ใหม่นี้ควรแยกจริงหรือไม่
- `flutter-feature-folder-scaffold` ถ้างานใหม่เกี่ยวกับ folder scaffold
- `flutter-go-router-route-map` ถ้างานใหม่เกี่ยวกับ route tree
- `flutter-firebase-auth-adapter` ถ้างานใหม่เกี่ยวกับ Firebase auth boundary

## อินพุตที่คาดหวัง

- ชื่อ skill
- category
- purpose
- inputs
- outputs
- related skills

## เอาต์พุตที่คาดหวัง

- skill folder ใหม่
- `SKILL.md` ที่ครบ schema
- example และ checklist placeholders
- index และ validation ที่อัปเดตแล้ว

## ความผิดพลาดที่พบบ่อย

- สร้าง skill ใหม่ทั้งที่ update skill เดิมได้
- ลืม link example/template
- ใช้ชื่อที่ไม่ตรงกับ folder
- ไม่รัน index sync หลังสร้างเสร็จ

## วิธีแก้ปัญหา

- ถ้า skill ใหม่ดูคล้ายของเดิม ให้ split boundary ให้แคบก่อน
- ถ้า generator สร้าง file ไม่ครบ ให้เติม placeholder ตาม schema แล้ว rerun
- ถ้า validation fail ให้แก้ field ที่ขาดก่อน

## Prompt สำหรับ Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Read overlays/mobile-flutter/AGENT_CONTRIBUTION_RULES.md first.
Use `tools/skillgen/README.md` and `tools/skillgen/bin/skillgen` to scaffold the skill.

Task:
Create a new atomic skill called <skill name>.

Deliver:
1. why the new skill is needed
2. exact files to create
3. category and naming
4. example/template links
5. validation checklist
```

## English

ดู `add-a-new-skill.md`
