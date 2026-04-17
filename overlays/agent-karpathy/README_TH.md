# agent-karpathy overlay (ภาษาไทย)

**ระบบปรับปรุง skill AI แบบ production-governed และ eval-driven พร้อม hard gates**

---

## overlay นี้ทำอะไร

`agent-karpathy` overlay เปลี่ยน agent-engineering-toolkit ให้กลายเป็น
**ระบบปรับปรุง skill แบบ eval-driven**  โดยมีโครงสร้างพื้นฐานสำหรับ:

- วัดคุณภาพของ skill ใดๆ โดยใช้ rubric แบบมีน้ำหนัก
- สร้าง mutation candidates แบบควบคุม (เปลี่ยนแค่มิติเดียวต่อครั้ง)
- บังคับ regression guardrails ก่อนที่จะ promote การเปลี่ยนแปลงใดๆ
- ใช้ token efficiency policy เพื่อป้องกัน token bloat
- สร้างรายงาน JSON + Markdown สำหรับทุก optimization run
- รัน improvement loop แบบ manual หรือ CI schedule

---

## เริ่มต้นที่นี่

| เอกสาร | วัตถุประสงค์ |
|--------|------------|
| `AGENTS.overlay.md` | กฎการทำงาน, การ routing ของ skill, กฎการส่งมอบ |
| `skills/` | ห้า skill ครอบคลุม core workflow |
| `docs/adoption-guide.md` | วิธีเพิ่ม skill ใหม่และรัน cycle แรก |
| `docs/karpathy-architecture.md` | สถาปัตยกรรมระบบและ data flow |
| `examples/flutter_deeplink_full_cycle.md` | ตัวอย่างการทำงานแบบ static |
| `docs/continuous-optimization.md` | โหมดรันแบบ CI และแบบ manual |
| `docs/promotion-system.md` | กติกา promotion gate และ decision |

---

## Stack เริ่มต้น

- **ภาษา**: Python 3.11+
- **Schemas**: JSON Schema draft-07
- **เอกสาร**: Markdown (GitHub-flavored)
- **CI**: GitHub Actions
- **การจัดเก็บ**: JSON flat files (`memory/`) + Markdown reports (`reports/`)

ไม่ต้องการ dependencies ภายนอก Python standard library ในการรันระบบหลัก

output runtime ที่เป็น source of truth คือ `reports/latest_report.md`, `reports/history/<run_id>.md`,
`memory/score_history.json`, และ `memory/candidate_archive.json` ส่วน demo แบบ static อยู่ใน
`examples/` และไม่ใช่ output ของการรันจริง

## วิธีรัน

```bash
# Eval only
./scripts/karpathy-eval.sh <skill>

# Full cycle แบบไม่เขียนไฟล์
./scripts/karpathy-run-cycle.sh <skill> true 3

# Full cycle แบบเปิด promotion
./scripts/karpathy-run-cycle.sh <skill> false 3
```

## Audit & Production Guarantees

runtime artifacts คือ `reports/latest_report.md`, `reports/history/<run_id>.md`,
`memory/score_history.json`, และ `memory/candidate_archive.json`; `examples/` เป็น static
example เท่านั้น
promotion decision ทุกครั้งต้องมี `baseline_score`, `candidate_score`, `score_delta`,
`token_delta`, `regression_pass`, `token_policy_pass`, `final_decision`, และ `reason`
promotion จะถูกบล็อกถ้า regression ไม่ผ่าน, token policy ไม่ผ่าน, score threshold ไม่ผ่าน,
หรือ artifact / decision field ที่จำเป็นหายไป; CI ต้อง fail closed

- Deterministic: report generation, token counting, binary และ regression checks, path ของ artifact
- Heuristic: rubric scoring และ candidate mutation selection
- Interpretation: `PROMOTE` คือ candidate ที่ชนะภายใต้ rubric และ gate ปัจจุบัน;
  `REJECT` คือไม่ผ่านเงื่อนไขดังกล่าว

---

## หมวดหมู่ skill ที่ใช้งาน

| หมวดหมู่ | Skills | ใช้สำหรับ |
|---------|--------|----------|
| `evaluation/` | karpathy-evaluation | ให้คะแนน skill ด้วย weighted rubric |
| `mutation/` | karpathy-mutation | สร้าง single-dimension candidates |
| `regression/` | karpathy-regression | บังคับ guardrail ก่อน promotion |
| `optimization/` | karpathy-optimizer | Token policy + การเลือก winner |
| `karpathy-guidelines/` | karpathy-guidelines | ใช้เกณฑ์การประเมินแบบ manual |

---

## กฎการใช้งาน

1. รัน `eval_runner` บน baseline ก่อนเริ่ม mutation cycle เสมอ
2. รัน `regression_runner` ก่อนเรียก `promotion_runner` เสมอ
3. ใช้ `scripts/karpathy-run-cycle.sh` สำหรับการรัน end-to-end — ครอบคลุมทั้ง cycle และเขียน runtime artifacts มาตรฐาน
4. ใช้ `--dry-run` ใน CI เว้นแต่ workflow จะเป็น promotion workflow โดยเฉพาะ

---

## โมเดลคะแนน

คะแนนสุดท้ายคำนวณจาก:

```
final_score =
  0.30 × correctness           (ความถูกต้อง)
  0.15 × scope_discipline      (ขอบเขตชัดเจน)
  0.15 × simplicity            (ความเรียบง่าย)
  0.15 × verifiability         (ตรวจสอบได้)
  0.10 × architecture_alignment (สอดคล้องสถาปัตยกรรม)
  0.10 × token_efficiency      (ประสิทธิภาพ token)
  0.05 × docs_hygiene          (ความสะอาดของเอกสาร)
```

---

## Token Policy

ปฏิเสธ candidate ถ้า:
- ใช้ token เพิ่มขึ้น **มากกว่า 35%** แต่คะแนนดีขึ้น **น้อยกว่า 5%**

ให้ความสำคัญ:
- คะแนนเท่ากันแต่ใช้ token น้อยกว่า
- คะแนนต่ำกว่าเล็กน้อยแต่ถูกกว่ามาก

---

## เอกสารที่เกี่ยวข้อง

- `docs/eval-system.md` — รายละเอียดโมเดลการให้คะแนน
- `docs/mutation-system.md` — ประเภท mutation และข้อจำกัด one-dimension
- `docs/promotion-system.md` — ลอจิก promotion gate
- `docs/token-optimizer.md` — สูตร token policy
- `docs/guardrails.md` — Regression checks และเงื่อนไข hard-fail
- `docs/continuous-optimization.md` — การตั้งเวลาและอัตโนมัติ
