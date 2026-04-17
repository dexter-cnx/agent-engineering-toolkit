# คู่มือ Karpathy

## เป้าหมาย

ใช้ Karpathy overlay เพื่อปรับปรุง `SKILL.md` ด้วยการเปลี่ยนแบบ eval-driven,
ปลอด regression และควบคุม token อย่างเป็นระบบ คู่มือนี้เหมาะกับงานคุณภาพและ
promotion ของ skill ไม่ใช่งานพัฒนา feature ทั่วไป

## เมื่อควรใช้

ใช้ Karpathy เมื่อคุณต้องการ:
- baseline ที่วัดได้สำหรับ skill
- mutation ที่ควบคุมได้และเปลี่ยนทีละมิติ
- regression gate ก่อน promotion
- การคุมการเติบโตของ token
- บันทึกผลที่ตรวจสอบย้อนหลังได้ใน `reports/` และ `memory/`

## เมื่อไม่ควรใช้

ไม่ควรใช้ Karpathy สำหรับ:
- งานพัฒนา feature ของ product ที่ไม่เกี่ยวกับคุณภาพของ skill
- งาน delivery ที่ผูกกับ stack ใด stack หนึ่ง
- งานเขียนแบบ exploratory ที่ไม่ต้องการ rubric scoring หรือ promotion gate
- การเปลี่ยนระดับ foundation ที่ไม่เกี่ยวกับ skill

## คำสำคัญ

- `baseline` - `SKILL.md` ปัจจุบันก่อน mutation
- `candidate` - เวอร์ชันที่ถูก mutate เพื่อประเมินผล
- `dry-run` - รัน cycle โดยไม่เขียน skill ที่ promote แล้ว
- `promotion` - การเขียน candidate ที่ชนะกลับไปเป็น `SKILL.md`
- `runtime artifacts` - `reports/latest_report.md`, `reports/history/`, `memory/score_history.json`, และ `memory/candidate_archive.json`
- `static examples` - snapshot ใน `examples/` ที่ใช้เป็นเอกสารอ้างอิง ไม่ใช่ runtime output

## Workflow ที่แนะนำ

1. ยืนยันว่า skill นั้นอยู่ภายใต้ Karpathy overlay
2. อ่าน `overlays/agent-karpathy/README.md` และ `overlays/agent-karpathy/AGENTS.overlay.md`
3. ตรวจ path ของ skill ที่ `overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md`
4. รัน baseline evaluation:

```bash
./scripts/karpathy-eval.sh overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md
```

5. อ่าน `reports/latest_report.md` แล้วดูมิติที่คะแนนต่ำสุด
6. รัน dry-run cycle ก่อน โดยแนะนำให้ใช้ flag ชัดเจน:

```bash
./scripts/karpathy-run-cycle.sh \
  overlays/agent-karpathy/skills/<category>/<skill-name>/SKILL.md \
  --dry-run --n 3 --pretty
```

7. ตรวจ decision trace:
- `baseline_score`
- `candidate_score`
- `score_delta`
- `token_delta`
- `regression_pass`
- `token_policy_pass`
- `final_decision`
- `reason`

8. อนุญาต promotion เฉพาะเมื่อ regression และ token policy ผ่านทั้งคู่
9. ตรวจ runtime artifacts และเก็บ `examples/` ไว้เป็นข้อมูลอ้างอิงแบบ static

## จุดที่ต้องระวัง

- `final_score` ควรไม่น้อยกว่า `0.60` หากต้องการ promotion
- คะแนนที่สูงขึ้นไม่ได้ลบผล regression failure
- คะแนนที่ดีขึ้นไม่ได้แปลว่าควรยอมรับ token เพิ่มมากเสมอไป
- `REJECT` เป็นผลลัพธ์ปกติเมื่อ baseline ดีอยู่แล้ว

## คำแนะนำเชิงปฏิบัติ

- เปลี่ยนทีละเรื่อง
- เลือกชุด skill ที่น้อยที่สุดแต่เพียงพอ
- ทำให้ `Validation checklist` รันได้จริงและชัดเจน
- เลี่ยง filler prose ที่เพิ่ม token โดยไม่เพิ่มคุณค่าการตรวจ
- เก็บ `examples/` ให้เป็น static reference ไม่ใช่ผลลัพธ์สด
- ใช้ `--dry-run` หรือ `--verify-only` เมื่ออยากดูพฤติกรรมก่อน promotion
- ใช้รูปแบบ positional `true` / `false` เฉพาะกรณีที่ต้องรองรับของเดิม

## ข้อผิดพลาดที่พบบ่อย

- ใช้ Karpathy กับงาน implement feature ทั่วไป
- แก้หลายมิติใน mutation เดียวแล้วพยายามเดาว่าอะไรเป็นสาเหตุของผลลัพธ์
- ข้าม regression เพราะคะแนนดีขึ้น
- สับสนระหว่าง snapshot ใน `examples/` กับรายงานจริงใน `reports/`
- มอง `REJECT` เป็นความล้มเหลว ทั้งที่บ่อยครั้งหมายถึง baseline ดีอยู่แล้ว

## CI และ automation

- `karpathy-eval.yml` ใช้ตรวจ skill ที่เปลี่ยนใน push และ pull request
- `karpathy-cycle.yml` ใช้รัน optimization loop ตาม schedule หรือสั่งเอง
- CI ควรใช้ dry-run เป็นค่าเริ่มต้น เว้นแต่ workflow จะอนุญาต promotion อย่างชัดเจน

## ถ้ามีอะไรดูไม่ตรง

- รัน baseline eval ใหม่แล้วเทียบกับ `SKILL.md` ปัจจุบัน
- ตรวจว่า path ของ skill มีอยู่จริงและอยู่ใน overlay ที่ถูกต้อง
- ตรวจว่าระบบเขียน runtime artifacts ไปยังตำแหน่งที่คาดไว้
- ดู `docs/promotion-system.md`, `docs/token-optimizer.md`, และ `docs/guardrails.md` หาก gate ใด gate หนึ่งล้มเหลว

## อ่านต่อ

- `docs/adoption-guide.md`
- `docs/continuous-optimization.md`
- `docs/eval-system.md`
- `docs/promotion-system.md`
- `docs/token-optimizer.md`
- `docs/guardrails.md`
