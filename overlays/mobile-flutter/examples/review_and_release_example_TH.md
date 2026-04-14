# ตัวอย่าง Review และ release

## สถานการณ์

ฟีเจอร์พร้อมเข้าสู่ review และตรวจ release readiness

ตัวอย่างการเปลี่ยนแปลง:

- code review pass
- release audit
- ตรวจความเสี่ยงเฉพาะ platform

## Skill ที่แนะนำ

- `flutter-code-reviewer`
- `flutter-release-reviewer`
- `guide-app-release-checklist`
- `policy-commit-pr-checks`

## ไฟล์อ้างอิง

- `overlays/mobile-flutter/skills/flutter-code-reviewer/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-release-reviewer/SKILL.md`
- `overlays/mobile-flutter/prompts/code_review.md`
- `overlays/mobile-flutter/prompts/release_audit.md`
- `overlays/mobile-flutter/templates/pull_request_checklist.md`
- `overlays/mobile-flutter/CHECKLIST.md`

## ตัวอย่าง invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-code-reviewer
- flutter-release-reviewer
- guide-app-release-checklist

Reference files:
- overlays/mobile-flutter/skills/flutter-code-reviewer/SKILL.md
- overlays/mobile-flutter/prompts/code_review.md
- overlays/mobile-flutter/prompts/release_audit.md

Task:
Review the feature for correctness, architecture fit, and release readiness.

Deliver:
1. review findings
2. release risks
3. verification gaps
4. go/no-go recommendation
```

## สิ่งที่ควรได้

- blocking issues แยกจาก non-blocking notes
- architecture fit ถูกตรวจอย่างชัดเจน
- release risks ถูกระบุแบบไม่ทำให้เบา
- verification gaps ที่ยังเหลืออยู่เห็นชัด

## Review notes

- อย่าเอา review กับ implementation concern มาปนกัน
- ชี้ platform-specific risks ให้ชัด
- recommendation ต้องยึด evidence ไม่ใช่ความรู้สึก

## Verification notes

- ตรวจว่าผล review แยกตาม severity
- ตรวจว่า release risks ชัด
- ตรวจว่า checklist ตรงกับเส้นทาง release ที่รีวิว
