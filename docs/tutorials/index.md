---
tags:
  - agent-engineering-toolkit
  - tutorial
  - obsidian
aliases:
  - Tutorial Hub
  - Step by Step Tutorials
---

# ศูนย์รวม Tutorial

โฟลเดอร์นี้รวบรวม tutorial แบบเปิดอ่านใน Obsidian ได้ง่าย โดยมีทั้งภาษาไทยและภาษาอังกฤษ

## เริ่มอ่านตรงนี้

- [เริ่มจากโฟลเดอร์เปล่า](./00-common-start.md)
- [AGENTS.md และ prompt guide](./agents-and-prompts.md)
- [เส้นทางหลัก 10 นาทีแรก](./01-golden-path.md)
- [Mental model ของระบบ Agent](./02-agent-mental-model.md)
- [Workflow ของจริงแบบ Lead → Architecture → Feature](./03-real-workflow.md)
- [วิธีสร้าง feature แบบ production](./04-build-production-feature.md)
- [วิธี reuse toolkit](./05-reuse-toolkit.md)
- [วิธี debug agent run ที่พัง](./06-debugging-agent-runs.md)
- [วิธีใช้ multi-agent execution](./07-multi-agent-execution.md)
- [ตัวอย่างเต็ม: Flutter project](./08-full-example-flutter.md)
- [Start from Blank Folder](./00-common-start_EN.md)
- [AGENTS.md and prompt guide](./agents-and-prompts_EN.md)
- [10-minute golden path](./01-golden-path_EN.md)
- [Agent system mental model](./02-agent-mental-model_EN.md)
- [Real workflow: Lead → Architecture → Feature](./03-real-workflow_EN.md)
- [Build a production feature](./04-build-production-feature_EN.md)
- [Reuse toolkit patterns](./05-reuse-toolkit_EN.md)
- [Debug failed agent runs](./06-debugging-agent-runs_EN.md)
- [Multi-agent execution](./07-multi-agent-execution_EN.md)
- [Full example: Flutter project](./08-full-example-flutter_EN.md)

## Core Execution Path

ชุดนี้คือ tutorial track ใหม่ที่เน้น **ลงมือทำจริง** มากกว่า reference อ่านเล่น

| ลำดับ | Tutorial | เป้าหมาย |
| --- | --- | --- |
| 1 | [เส้นทางหลัก 10 นาทีแรก](./01-golden-path.md) | ให้ user ได้ first success เร็วที่สุด |
| 2 | [Mental model ของระบบ Agent](./02-agent-mental-model.md) | แก้ความสับสนว่า agent, prompt, skill, overlay ต่างกันอย่างไร |
| 3 | [Workflow ของจริงแบบ Lead → Architecture → Feature](./03-real-workflow.md) | ทำให้ลำดับการสั่งงาน predictable |
| 4 | [วิธีสร้าง feature แบบ production](./04-build-production-feature.md) | สาธิตการทำงานเป็นงานจริง 1 ชิ้น |
| 5 | [วิธี reuse toolkit](./05-reuse-toolkit.md) | ชี้ทางเลือก submodule, copy, foundation repo |
| 6 | [วิธี debug agent run ที่พัง](./06-debugging-agent-runs.md) | รับมือ hallucination, scope drift, broken verification |
| 7 | [วิธีใช้ multi-agent execution](./07-multi-agent-execution.md) | ใช้ agent team แบบมี boundary ชัด |
| 8 | [ตัวอย่างเต็ม: Flutter project](./08-full-example-flutter.md) | เชื่อมทุกอย่างเป็น workflow เดียว |

## Agent Team

| Topic | ไทย | English |
| --- | --- | --- |
| วิธีใช้ Team Agents | [วิธีใช้ Team Agents](./team/how-to-use-team-agents.md) | [How to Use Team Agents](./team/how-to-use-team-agents_EN.md) |

## Flutter

| Topic | ไทย | English |
| --- | --- | --- |
| Flutter app พื้นฐาน | [วิธีทำ Flutter app แบบพื้นฐาน](./flutter/how-to-make-basic-flutter-app.md) | [How to Make Basic Flutter App](./flutter/how-to-make-basic-flutter-app_EN.md) |
| Flutter app แบบ offline-first | [วิธีทำ Flutter app แบบ offline-first](./flutter/how-to-make-offline-first-flutter-app.md) | [How to Make Offline-First Flutter App](./flutter/how-to-make-offline-first-flutter-app_EN.md) |
| Flutter app แบบ online | [วิธีทำ Flutter app แบบ online](./flutter/how-to-make-online-flutter-app.md) | [How to Make Online Flutter App](./flutter/how-to-make-online-flutter-app_EN.md) |
| Prompt: add Firebase services to Flutter | [วิธี prompt เพื่อเพิ่ม Firebase services ให้ Flutter](./flutter/how-to-prompt-for-add-firebase-services-to-flutter.md) | [How to Prompt AI to Add Firebase Services to Flutter](./flutter/how-to-prompt-for-add-firebase-services-to-flutter_EN.md) |
| Prompt: add Supabase to Flutter | [วิธี prompt เพื่อเพิ่ม Supabase ให้ Flutter](./flutter/how-to-prompt-for-add-supabase-to-flutter.md) | [How to Prompt AI to Add Supabase to Flutter](./flutter/how-to-prompt-for-add-supabase-to-flutter_EN.md) |
| Flutter app แบบ clean architecture + Riverpod | [วิธีทำ Flutter app แบบ clean architecture + Riverpod](./flutter/how-to-make-flutter-app-with-clean-architecture-and-riverpod.md) | [How to Make a Flutter App with Clean Architecture + Riverpod](./flutter/how-to-make-flutter-app-with-clean-architecture-and-riverpod_EN.md) |
| Flutter app แบบ clean architecture + BLoC | [วิธีทำ Flutter app แบบ clean architecture + BLoC](./flutter/how-to-make-flutter-app-with-clean-architecture-and-bloc.md) | [How to Make a Flutter App with Clean Architecture + BLoC](./flutter/how-to-make-flutter-app-with-clean-architecture-and-bloc_EN.md) |
| Flutter app แบบ clean architecture + GetX | [วิธีทำ Flutter app แบบ clean architecture + GetX](./flutter/how-to-make-flutter-app-with-clean-architecture-and-getx.md) | [How to Make a Flutter App with Clean Architecture + GetX](./flutter/how-to-make-flutter-app-with-clean-architecture-and-getx_EN.md) |
| Localization: Flutter CSV + easy_localization | [วิธีทำ localization หลายภาษาใน Flutter ด้วย CSV ไฟล์เดียว](./flutter/how-to-localize-multi-languages-with-one-csv-file-in-flutter.md) | [How to Localize Multiple Languages in Flutter with One CSV File](./flutter/how-to-localize-multi-languages-with-one-csv-file-in-flutter_EN.md) |
| DESIGN.md in Flutter | [วิธี integrate DESIGN.md กับ Flutter](./flutter/how-to-integrate-design-md-to-existing-project-and-new-project-in-flutter.md) | [How to Integrate DESIGN.md into Flutter Projects](./flutter/how-to-integrate-design-md-to-existing-project-and-new-project-in-flutter_EN.md) |

## Web Frontend

| Topic | ไทย | English |
| --- | --- | --- |
| web-frontend | [วิธีทำ web-frontend](./web/how-to-make-web-frontend.md) | [How to Make Web Frontend](./web/how-to-make-web-frontend_EN.md) |
| Localization: Web CSV | [วิธีทำ localization หลายภาษาใน web-frontend ด้วย CSV ไฟล์เดียว](./web/how-to-localize-multi-languages-with-one-csv-file-in-web-frontend.md) | [How to Localize Multi Languages with One CSV File in Web Frontend](./web/how-to-localize-multi-languages-with-one-csv-file-in-web-frontend_EN.md) |
| DESIGN.md in Web Frontend | [วิธี integrate DESIGN.md กับ web-frontend](./web/how-to-integrate-design-md-to-existing-project-and-new-project-in-web-frontend.md) | [How to Integrate DESIGN.md into Web Frontend Projects](./web/how-to-integrate-design-md-to-existing-project-and-new-project-in-web-frontend_EN.md) |

## Services

| Topic | ไทย | English |
| --- | --- | --- |
| backend-node | [วิธีทำ backend-node](./services/how-to-make-backend-node.md) | [How to Make Backend Node](./services/how-to-make-backend-node_EN.md) |
| python service | [วิธีทำ python service](./services/how-to-make-python-service.md) | [How to Make Python Service](./services/how-to-make-python-service_EN.md) |

## วิธีอ่านโน้ตชุดนี้

ทุก tutorial ใช้รูปแบบเดียวกัน:

1. เริ่มจากเป้าหมายให้ชัด
2. อ่าน boundary และ canonical docs ก่อนลงมือ
3. ใช้ prompt pipeline ตามลำดับ
4. verify ก่อน finalize
5. อัปเดต project memory เฉพาะ decision ที่ควรจำจริง
6. แยก foundation, overlay, และ project-specific concerns ออกจากกันเสมอ

## Canonical references

- [README.md](../../README.md)
- [README_TH.md](../../README_TH.md)
- [docs/how-to-use.md](../how-to-use.md)
- [docs/tutorial.md](../tutorial.md)
- [docs/prompt-pipeline.md](../prompt-pipeline.md)
- [docs/agent-team-system.md](../agent-team-system.md)
- [docs/overlays.md](../overlays.md)
