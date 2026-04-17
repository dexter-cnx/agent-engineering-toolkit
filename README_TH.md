# agent-engineering-toolkit

ชุดเครื่องมือพื้นฐานสำหรับการทำวิศวกรรมซอฟต์แวร์แบบ AI-assisted อย่างเป็นระบบ โดยยังคงความเป็นกลางทางโดเมน

Repository นี้ตั้งใจให้เป็น foundation toolkit ที่นำไปใช้ต่อได้กับ:
- mobile projects
- backend services
- web frontends
- AI และ agent systems
- monorepos
- internal engineering platforms

Repository นี้ตั้งใจให้เป็น foundation toolkit ที่เป็นกลางทาง stack ในชั้นฐาน ส่วนกฎเฉพาะทางของแต่ละ stack จะอยู่ใน overlay

## จุดอ้างอิงหลัก

- แหล่งอ้างอิง lifecycle หลัก: `docs/prompt-pipeline.md`
- แหล่งอ้างอิง role model หลัก: `docs/agent-team-system.md`
- คู่มือใช้งาน: `docs/how-to-use.md`
- บทสอน: `docs/tutorial.md`
- แนวคิด overlay: `docs/overlays.md`

## Overlay catalog

รายละเอียดเชิงลึกอยู่ใน README และ `AGENTS.overlay.md` ของแต่ละ overlay

- `overlays/backend-node/README.md`
- `overlays/mobile-flutter/README.md`
- `overlays/unity/README.md`
- `overlays/python-service/README.md`
- [overlays/agent-karpathy/README.md](overlays/agent-karpathy/README.md) - การปรับปรุง skill แบบ eval-driven, mutation, promotion ที่มี regression guardrail, และ token governance
- `overlays/web-frontend/README.md`

## เมื่อใดควรใช้ Karpathy Layer

ใช้ `agent-karpathy` overlay เมื่อกำลังทำงานกับ quality หรือ promotion workflow ของ AI skill
โดยเฉพาะ ระบบนี้เป็นชั้น eval-driven optimization ของ repository: วัด skill ด้วย rubric,
สร้าง mutation แบบควบคุม, block regression, ใช้ token governance และ promote เฉพาะ candidate
ที่ชนะ baseline แบบชัดเจนเท่านั้น

คำสั่งหลัก:

```bash
./scripts/karpathy-eval.sh <skill>
./scripts/karpathy-run-cycle.sh <skill> true 3
./scripts/karpathy-run-cycle.sh <skill> false 3
```

runtime outputs ไปที่:
- `reports/latest_report.md`
- `reports/history/`
- `memory/score_history.json`
- `memory/candidate_archive.json`

ตัวอย่างแบบ static อยู่ใน `examples/` และไม่ใช่ runtime output

## เริ่มต้นอ่าน

- `README_START_HERE.md`
- `docs/how-to-use.md`
- `docs/how-to-use_TH.md`
- `docs/tutorial.md`
- `docs/tutorial_TH.md`
- `docs/overlays.md`
- ถ้ากำลังทำงานด้านคุณภาพของ AI skill ให้เริ่มที่ [overlays/agent-karpathy/README.md](overlays/agent-karpathy/README.md)
