# Real-World Integration

## With Codex CLI
Use AGENTS.md as the root contract.
Start tasks with a clear lifecycle instruction.
Prefer using prompts in `prompts/`.

## With Claude Code
Use the role model in `agent_team/`.
Let LEAD coordinate and ARCHITECT define structure before BUILDER executes.

## With OpenClaw
Use this toolkit as the prompt/rules source.
Map planning models and coding models separately if your runtime supports it.

## With CI/CD
Use verification templates and project-specific scripts.
Do not claim a change is finished when verification has not happened.

## With project submodules
Keep this repo central.
Consume it from project repos.
Put project-specific instructions beside the consuming project, not back into the foundation unless they are widely reusable.
