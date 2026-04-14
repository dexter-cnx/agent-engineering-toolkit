# Unity Tetris Worked Example

## Scenario

Build a simple Tetris clone in Unity with:
- a bootstrap scene
- a playfield grid
- falling tetrominoes
- line clearing
- score tracking
- a minimal UI

## Recommended skill set

- `unity-project-structure`
- `unity-scene-and-bootstrap`
- `unity-prefab-architecture`
- `unity-input-system`
- `unity-state-machine`
- `unity-ugui`
- `unity-testing`

## Example invocation

```text
Follow AGENTS.md strictly.
Apply overlays/unity/AGENTS.overlay.md.
Use these skills:
- unity-project-structure
- unity-scene-and-bootstrap
- unity-prefab-architecture
- unity-input-system
- unity-state-machine
- unity-ugui
- unity-testing

Task:
Create a small Unity Tetris tutorial project with a bootstrap scene, playfield, tetromino spawning, line clearing, score UI, and a validation checklist.

Deliver:
1. file plan
2. scene and prefab plan
3. capability boundaries
4. implementation notes
5. verification checklist
6. follow-up risks
```

## Review notes

- bootstrap logic should not be mixed into gameplay pieces
- tetromino movement and rotation should stay separate from UI
- line clearing should operate on grid state, not on scene hierarchy assumptions
- score display should read state instead of owning game rules
