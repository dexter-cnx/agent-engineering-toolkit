# วิธีทำเกม Tetris ใน Unity

## เป้าหมาย

สร้างเกม Tetris ที่เล่นได้ใน Unity โดยมีโครงสร้างโปรเจกต์ที่ชัดเจน, bootstrap scene, การควบคุมด้วย Input System, และ UI แบบเรียบง่าย

## สิ่งที่จะสร้าง

- โครงสร้างโฟลเดอร์ Unity ที่มั่นคง
- bootstrap scene ที่โหลดฉากเกม
- กระดาน Tetris แบบกริด
- การเกิด, เคลื่อนที่, หมุน, และลบแถวของ tetromino
- HUD แสดงคะแนนขนาดเล็ก
- checklist สำหรับตรวจหาความเสียหายที่เห็นได้ชัด

## skills ที่ใช้

- `unity-project-structure`
- `unity-scene-and-bootstrap`
- `unity-prefab-architecture`
- `unity-input-system`
- `unity-state-machine`
- `unity-ugui`
- `unity-testing`

## ลำดับ prompt

ใช้ prompt ของ skill ไปตามลำดับขณะทำงาน:

1. Run the project structure prompt from `overlays/unity/skills/unity-project-structure/prompts/add_project_structure.md`
2. Run the startup prompt from `overlays/unity/skills/unity-scene-and-bootstrap/prompts/add_scene_and_bootstrap.md`
3. Run the input prompt from `overlays/unity/skills/unity-input-system/prompts/add_input_system.md`

ตัวอย่างบล็อกคำสั่ง:

```text
Follow AGENTS.md strictly.
Apply overlays/unity/AGENTS.overlay.md.
Use these skills:
- unity-project-structure
- unity-scene-and-bootstrap
- unity-input-system

Task:
Create a playable Unity Tetris game with a bootstrap scene, grid-based board, tetromino movement, line clearing, and a score HUD.

Deliver:
1. file plan
2. scene plan
3. capability boundaries
4. implementation notes
5. verification checklist
6. follow-up risks
```

## ขั้นตอนที่ 1: สร้างโครงสร้างโปรเจกต์

ให้ทำตาม `unity-project-structure`

ใช้โครงแบบนี้:

```text
Assets/_Project/
  Scenes/
  Scripts/
  Prefabs/
  Art/
  Audio/
  Tests/
```

asmdef ที่แนะนำ:
- `Tetris.Runtime`
- `Tetris.Editor`
- `Tetris.Tests`

ให้ namespaces สอดคล้องกับ assembly เหล่านั้น เช่น `UnityTetris.Runtime` และ `UnityTetris.UI`

## ขั้นตอนที่ 2: สร้างฉาก

สร้าง 2 ฉาก:
- `Bootstrap`
- `Game`

bootstrap scene ควรทำเพียงหน้าที่เดียว: เริ่มเกม scene

### Bootstrap scene hierarchy

```text
Bootstrap
  - TetrisBootstrapper
```

### `TetrisBootstrapper.cs`

```csharp
using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace UnityTetris.Bootstrap
{
    public sealed class TetrisBootstrapper : MonoBehaviour
    {
        [SerializeField] private string gameplaySceneName = "Game";

        private IEnumerator Start()
        {
            yield return null;
            yield return SceneManager.LoadSceneAsync(gameplaySceneName, LoadSceneMode.Single);
        }
    }
}
```

เหตุผลที่ใช้โครงแบบนี้:
- โค้ดเริ่มต้นจะไม่ปนกับวัตถุ gameplay
- การโหลด scene ชัดเจน
- ในอนาคตสามารถเพิ่ม service registration ได้โดยไม่ต้องเขียนเกม scene ใหม่

## ขั้นตอนที่ 3: เพิ่ม tetromino library

tutorial นี้เก็บ shape ไว้ในโค้ดเพื่อให้เวอร์ชันเล่นได้แรกเริ่มทำตามได้ง่าย

### `TetrominoLibrary.cs`

```csharp
using UnityEngine;

namespace UnityTetris.Gameplay
{
    public static class TetrominoLibrary
    {
        public static readonly Color[] Colors =
        {
            new Color(0.00f, 0.90f, 0.90f), // I
            new Color(0.95f, 0.95f, 0.20f), // O
            new Color(0.75f, 0.20f, 0.95f), // T
            new Color(0.95f, 0.55f, 0.10f), // L
            new Color(0.10f, 0.35f, 0.95f), // J
            new Color(0.20f, 0.85f, 0.30f), // S
            new Color(0.90f, 0.15f, 0.20f), // Z
        };

        public static readonly Vector2Int[][][] Shapes =
        {
            new[]
            {
                new[] { new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(2, 0) },
                new[] { new Vector2Int(1, -1), new Vector2Int(1, 0), new Vector2Int(1, 1), new Vector2Int(1, 2) },
                new[] { new Vector2Int(-1, 1), new Vector2Int(0, 1), new Vector2Int(1, 1), new Vector2Int(2, 1) },
                new[] { new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(0, 1), new Vector2Int(0, 2) },
            },
            new[]
            {
                new[] { new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
                new[] { new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
                new[] { new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
                new[] { new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
            },
            new[]
            {
                new[] { new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1) },
                new[] { new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1) },
                new[] { new Vector2Int(0, -1), new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0) },
                new[] { new Vector2Int(0, -1), new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(0, 1) },
            },
            new[]
            {
                new[] { new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(1, 1) },
                new[] { new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(0, 1), new Vector2Int(1, -1) },
                new[] { new Vector2Int(-1, -1), new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0) },
                new[] { new Vector2Int(-1, 1), new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(0, 1) },
            },
            new[]
            {
                new[] { new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(-1, 1) },
                new[] { new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
                new[] { new Vector2Int(1, -1), new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(1, 0) },
                new[] { new Vector2Int(-1, -1), new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(0, 1) },
            },
            new[]
            {
                new[] { new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
                new[] { new Vector2Int(1, -1), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1) },
                new[] { new Vector2Int(-1, 0), new Vector2Int(0, 0), new Vector2Int(0, 1), new Vector2Int(1, 1) },
                new[] { new Vector2Int(1, -1), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(0, 1) },
            },
            new[]
            {
                new[] { new Vector2Int(-1, 1), new Vector2Int(0, 1), new Vector2Int(0, 0), new Vector2Int(1, 0) },
                new[] { new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(1, 1) },
                new[] { new Vector2Int(-1, 1), new Vector2Int(0, 1), new Vector2Int(0, 0), new Vector2Int(1, 0) },
                new[] { new Vector2Int(0, -1), new Vector2Int(0, 0), new Vector2Int(1, 0), new Vector2Int(1, 1) },
            },
        };
    }
}
```

## ขั้นตอนที่ 4: เพิ่ม board model

board เป็นเจ้าของ state ของกติกา ส่วน UI และ visuals มีหน้าที่สะท้อน state นั้นเท่านั้น

### `TetrisBoardModel.cs`

```csharp
using System.Collections.Generic;
using UnityEngine;

namespace UnityTetris.Gameplay
{
    public readonly struct ColoredCell
    {
        public readonly Vector2Int Position;
        public readonly Color Color;

        public ColoredCell(Vector2Int position, Color color)
        {
            Position = position;
            Color = color;
        }
    }

    public sealed class TetrisBoardModel
    {
        public const int Width = 10;
        public const int Height = 20;

        private readonly Color?[,] cells = new Color?[Width, Height];

        public bool IsInside(Vector2Int position)
        {
            return position.x >= 0 && position.x < Width &&
                   position.y >= 0 && position.y < Height;
        }

        public bool CanPlace(TetrisPiece piece)
        {
            foreach (var cell in piece.GetCells())
            {
                if (!IsInside(cell) || cells[cell.x, cell.y].HasValue)
                {
                    return false;
                }
            }

            return true;
        }

        public void LockPiece(TetrisPiece piece)
        {
            foreach (var cell in piece.GetCells())
            {
                cells[cell.x, cell.y] = piece.Color;
            }
        }

        public int ClearFullLines()
        {
            int cleared = 0;

            for (int y = 0; y < Height; y++)
            {
                if (!IsRowFull(y))
                {
                    continue;
                }

                ClearRow(y);

                for (int shiftY = y; shiftY < Height - 1; shiftY++)
                {
                    for (int x = 0; x < Width; x++)
                    {
                        cells[x, shiftY] = cells[x, shiftY + 1];
                    }
                }

                for (int x = 0; x < Width; x++)
                {
                    cells[x, Height - 1] = null;
                }

                y--;
                cleared++;
            }

            return cleared;
        }

        public IEnumerable<ColoredCell> EnumerateCells()
        {
            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    if (cells[x, y].HasValue)
                    {
                        yield return new ColoredCell(new Vector2Int(x, y), cells[x, y].Value);
                    }
                }
            }
        }

        public void Clear()
        {
            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    cells[x, y] = null;
                }
            }
        }

        private bool IsRowFull(int y)
        {
            for (int x = 0; x < Width; x++)
            {
                if (!cells[x, y].HasValue)
                {
                    return false;
                }
            }

            return true;
        }

        private void ClearRow(int y)
        {
            for (int x = 0; x < Width; x++)
            {
                cells[x, y] = null;
            }
        }
    }
}
```

## ขั้นตอนที่ 5: เพิ่ม runtime piece

### `TetrisPiece.cs`

```csharp
using UnityEngine;

namespace UnityTetris.Gameplay
{
    public sealed class TetrisPiece
    {
        public int ShapeIndex { get; }
        public int RotationIndex { get; private set; }
        public Vector2Int Position { get; private set; }
        public Color Color => TetrominoLibrary.Colors[ShapeIndex];

        public TetrisPiece(int shapeIndex, Vector2Int position)
        {
            ShapeIndex = shapeIndex;
            Position = position;
            RotationIndex = 0;
        }

        public void Move(Vector2Int delta)
        {
            Position += delta;
        }

        public void RotateClockwise()
        {
            RotationIndex = (RotationIndex + 1) % 4;
        }

        public void RotateCounterClockwise()
        {
            RotationIndex = (RotationIndex + 3) % 4;
        }

        public void RewindRotation(int rotationIndex)
        {
            RotationIndex = rotationIndex;
        }

        public Vector2Int[] GetCells()
        {
            var shape = TetrominoLibrary.Shapes[ShapeIndex][RotationIndex];
            var result = new Vector2Int[shape.Length];

            for (int i = 0; i < shape.Length; i++)
            {
                result[i] = Position + shape[i];
            }

            return result;
        }
    }
}
```

## ขั้นตอนที่ 6: เพิ่ม adapter สำหรับ Input System

สร้าง input actions asset ที่มี action map ชื่อ `Gameplay`

Actions:
- `Move` as a `Vector2`
- `RotateCW` as a button
- `RotateCCW` as a button
- `SoftDrop` as a button
- `HardDrop` as a button
- `Pause` as a button

### `TetrisInputAdapter.cs`

```csharp
using System;
using UnityEngine;
using UnityEngine.InputSystem;

namespace UnityTetris.Input
{
    public sealed class TetrisInputAdapter : MonoBehaviour
    {
        [SerializeField] private InputActionReference moveAction;
        [SerializeField] private InputActionReference rotateCwAction;
        [SerializeField] private InputActionReference rotateCcwAction;
        [SerializeField] private InputActionReference softDropAction;
        [SerializeField] private InputActionReference hardDropAction;
        [SerializeField] private InputActionReference pauseAction;

        public event Action<Vector2Int> MoveRequested;
        public event Action RotateClockwiseRequested;
        public event Action RotateCounterClockwiseRequested;
        public event Action<bool> SoftDropChanged;
        public event Action HardDropRequested;
        public event Action PauseRequested;

        private void OnEnable()
        {
            moveAction.action.performed += OnMove;
            rotateCwAction.action.performed += OnRotateCw;
            rotateCcwAction.action.performed += OnRotateCcw;
            softDropAction.action.performed += OnSoftDropStarted;
            softDropAction.action.canceled += OnSoftDropEnded;
            hardDropAction.action.performed += OnHardDrop;
            pauseAction.action.performed += OnPause;

            moveAction.action.Enable();
            rotateCwAction.action.Enable();
            rotateCcwAction.action.Enable();
            softDropAction.action.Enable();
            hardDropAction.action.Enable();
            pauseAction.action.Enable();
        }

        private void OnDisable()
        {
            moveAction.action.performed -= OnMove;
            rotateCwAction.action.performed -= OnRotateCw;
            rotateCcwAction.action.performed -= OnRotateCcw;
            softDropAction.action.performed -= OnSoftDropStarted;
            softDropAction.action.canceled -= OnSoftDropEnded;
            hardDropAction.action.performed -= OnHardDrop;
            pauseAction.action.performed -= OnPause;
        }

        private void OnMove(InputAction.CallbackContext context)
        {
            var value = context.ReadValue<Vector2>();

            if (Mathf.Abs(value.x) < 0.5f)
            {
                return;
            }

            MoveRequested?.Invoke(new Vector2Int((int)Mathf.Sign(value.x), 0));
        }

        private void OnRotateCw(InputAction.CallbackContext context) => RotateClockwiseRequested?.Invoke();
        private void OnRotateCcw(InputAction.CallbackContext context) => RotateCounterClockwiseRequested?.Invoke();
        private void OnSoftDropStarted(InputAction.CallbackContext context) => SoftDropChanged?.Invoke(true);
        private void OnSoftDropEnded(InputAction.CallbackContext context) => SoftDropChanged?.Invoke(false);
        private void OnHardDrop(InputAction.CallbackContext context) => HardDropRequested?.Invoke();
        private void OnPause(InputAction.CallbackContext context) => PauseRequested?.Invoke();
    }
}
```

## ขั้นตอนที่ 7: เพิ่ม gameplay controller

controller เป็นเจ้าของ flow ของเกม และคุยกับ board model, input adapter, view, และ HUD

### `TetrisGameController.cs`

```csharp
using UnityEngine;
using UnityTetris.Input;
using UnityTetris.UI;

namespace UnityTetris.Gameplay
{
    public sealed class TetrisGameController : MonoBehaviour
    {
        [SerializeField] private TetrisInputAdapter input;
        [SerializeField] private TetrisBoardView boardView;
        [SerializeField] private TetrisHud hud;
        [SerializeField] private float fallInterval = 0.8f;
        [SerializeField] private float softDropInterval = 0.05f;

        private readonly TetrisBoardModel board = new TetrisBoardModel();
        private TetrisPiece currentPiece;
        private float fallTimer;
        private bool softDropHeld;
        private bool gameOver;
        private int score;
        private int linesCleared;
        private int activeShapeIndex;

        private void OnEnable()
        {
            input.MoveRequested += OnMoveRequested;
            input.RotateClockwiseRequested += OnRotateClockwiseRequested;
            input.RotateCounterClockwiseRequested += OnRotateCounterClockwiseRequested;
            input.SoftDropChanged += OnSoftDropChanged;
            input.HardDropRequested += OnHardDropRequested;
            input.PauseRequested += OnPauseRequested;
        }

        private void OnDisable()
        {
            input.MoveRequested -= OnMoveRequested;
            input.RotateClockwiseRequested -= OnRotateClockwiseRequested;
            input.RotateCounterClockwiseRequested -= OnRotateCounterClockwiseRequested;
            input.SoftDropChanged -= OnSoftDropChanged;
            input.HardDropRequested -= OnHardDropRequested;
            input.PauseRequested -= OnPauseRequested;
        }

        private void Start()
        {
            board.Clear();
            score = 0;
            linesCleared = 0;
            gameOver = false;
            hud.SetState("Playing");
            SpawnPiece();
            RefreshView();
            RefreshHud();
        }

        private void Update()
        {
            if (gameOver || currentPiece == null)
            {
                return;
            }

            fallTimer += Time.deltaTime;
            var interval = softDropHeld ? softDropInterval : fallInterval;

            if (fallTimer < interval)
            {
                return;
            }

            fallTimer = 0f;

            if (!TryMove(Vector2Int.down))
            {
                LockCurrentPiece();
            }
        }

        private void OnMoveRequested(Vector2Int delta)
        {
            if (!gameOver)
            {
                TryMove(delta);
            }
        }

        private void OnRotateClockwiseRequested()
        {
            if (!gameOver)
            {
                TryRotate(+1);
            }
        }

        private void OnRotateCounterClockwiseRequested()
        {
            if (!gameOver)
            {
                TryRotate(-1);
            }
        }

        private void OnSoftDropChanged(bool held)
        {
            softDropHeld = held;
        }

        private void OnHardDropRequested()
        {
            if (gameOver)
            {
                return;
            }

            while (TryMove(Vector2Int.down))
            {
            }

            LockCurrentPiece();
        }

        private void OnPauseRequested()
        {
            // Hook pause/menu logic here if you add it later.
        }

        private void SpawnPiece()
        {
            activeShapeIndex = Random.Range(0, TetrominoLibrary.ShapeCount);
            currentPiece = new TetrisPiece(activeShapeIndex, new Vector2Int(TetrisBoardModel.Width / 2, TetrisBoardModel.Height - 2));

            if (!board.CanPlace(currentPiece))
            {
                gameOver = true;
                hud.SetState("Game Over");
                return;
            }

            hud.SetState("Playing");
            RefreshView();
        }

        private bool TryMove(Vector2Int delta)
        {
            var oldPosition = currentPiece.Position;
            currentPiece.Move(delta);

            if (board.CanPlace(currentPiece))
            {
                RefreshView();
                return true;
            }

            currentPiece = new TetrisPiece(activeShapeIndex, oldPosition) { };
            currentPiece.RewindRotation(currentPiece.RotationIndex);
            currentPiece.Move(Vector2Int.zero);
            currentPiece = RestorePiece(oldPosition, currentPiece.RotationIndex);
            return false;
        }

        private bool TryRotate(int direction)
        {
            var oldRotation = currentPiece.RotationIndex;

            if (direction > 0)
            {
                currentPiece.RotateClockwise();
            }
            else
            {
                currentPiece.RotateCounterClockwise();
            }

            if (board.CanPlace(currentPiece))
            {
                RefreshView();
                return true;
            }

            currentPiece.RewindRotation(oldRotation);
            return false;
        }

        private void LockCurrentPiece()
        {
            board.LockPiece(currentPiece);
            var cleared = board.ClearFullLines();
            linesCleared += cleared;
            score += cleared * 100;

            currentPiece = null;
            RefreshView();
            RefreshHud();

            SpawnPiece();
        }

        private void RefreshView()
        {
            boardView.Redraw(board, currentPiece);
        }

        private void RefreshHud()
        {
            hud.SetScore(score, linesCleared);
        }

        private TetrisPiece RestorePiece(Vector2Int position, int rotationIndex)
        {
            var piece = new TetrisPiece(activeShapeIndex, position);

            while (piece.RotationIndex != rotationIndex)
            {
                piece.RotateClockwise();
            }

            return piece;
        }
    }
}
```

### ข้อแก้ไขเล็กน้อยสำหรับ `TryMove`

snippet ด้านบนช่วยให้เห็น control flow ชัดเจน แต่ในโปรเจกต์จริงควรทำ rollback ของการเคลื่อนที่ให้เรียบง่าย:

```csharp
private bool TryMove(Vector2Int delta)
{
    var oldPosition = currentPiece.Position;
    currentPiece.Move(delta);

    if (board.CanPlace(currentPiece))
    {
        RefreshView();
        return true;
    }

    currentPiece = new TetrisPiece(activeShapeIndex, oldPosition);
    while (currentPiece.RotationIndex != oldRotationIndex)
    {
        currentPiece.RotateClockwise();
    }

    return false;
}
```

ถ้าต้องการโค้ดที่อ่านง่ายกว่า ให้เก็บ position และ rotation แยกกันก่อนทดสอบการเคลื่อนที่ วิธีนี้ทำให้ rollback เข้าใจง่ายกว่าการสร้าง piece ใหม่แบบ inline

## ขั้นตอนที่ 8: เพิ่ม board view

view นี้ redraw board ทุกครั้งที่ model เปลี่ยน ซึ่งเป็นวิธีที่เรียบง่ายและเพียงพอสำหรับเกม Tetris ขนาดเล็ก

### `TetrisBoardView.cs`

```csharp
using System.Collections.Generic;
using UnityEngine;

namespace UnityTetris.Gameplay
{
    public sealed class TetrisBoardView : MonoBehaviour
    {
        [SerializeField] private Transform cellRoot;
        [SerializeField] private SpriteRenderer cellPrefab;
        [SerializeField] private float cellSize = 1f;

        private readonly List<GameObject> spawned = new List<GameObject>();

        public void Redraw(TetrisBoardModel board, TetrisPiece activePiece)
        {
            for (int i = 0; i < spawned.Count; i++)
            {
                if (spawned[i] != null)
                {
                    Destroy(spawned[i]);
                }
            }

            spawned.Clear();

            foreach (var cell in board.EnumerateCells())
            {
                SpawnCell(cell.Position, cell.Color);
            }

            if (activePiece != null)
            {
                foreach (var cell in activePiece.GetCells())
                {
                    SpawnCell(cell, activePiece.Color);
                }
            }
        }

        private void SpawnCell(Vector2Int position, Color color)
        {
            var view = Instantiate(cellPrefab, cellRoot);
            view.transform.localPosition = new Vector3(position.x * cellSize, position.y * cellSize, 0f);
            view.color = color;
            spawned.Add(view.gameObject);
        }
    }
}
```

## ขั้นตอนที่ 9: เพิ่ม HUD

### `TetrisHud.cs`

```csharp
using TMPro;
using UnityEngine;

namespace UnityTetris.UI
{
    public sealed class TetrisHud : MonoBehaviour
    {
        [SerializeField] private TMP_Text scoreText;
        [SerializeField] private TMP_Text linesText;
        [SerializeField] private TMP_Text stateText;

        public void SetScore(int score, int lines)
        {
            scoreText.text = $"Score: {score}";
            linesText.text = $"Lines: {lines}";
        }

        public void SetState(string value)
        {
            stateText.text = value;
        }
    }
}
```

ถ้ายังไม่อยากใช้ TextMeshPro ให้ใช้ `UnityEngine.UI.Text` ไปก่อนก็ได้ แต่โดยทั่วไป TextMeshPro จะเหมาะกับโปรเจกต์ Unity มากกว่า

## ขั้นตอนที่ 10: เชื่อมฉาก

ใน `Game` scene:
- วาง camera
- วาง `TetrisGameController`
- วาง `TetrisBoardView`
- วาง `TetrisHud`
- วาง `TetrisInputAdapter`

Create a simple square sprite prefab for the cells and assign it to `TetrisBoardView`.

โครงสร้าง hierarchy ที่แนะนำ:

```text
Game
  - Main Camera
  - BoardRoot
  - GameController
  - InputAdapter
  - Hud
```

## ขั้นตอนที่ 11: ตั้งค่า Input System actions

Create `TetrisInputActions.inputactions`.

action map: `Gameplay`

Actions:
- `Move` - Value / Vector2
- `RotateCW` - Button
- `RotateCCW` - Button
- `SoftDrop` - Button
- `HardDrop` - Button
- `Pause` - Button

binding ที่แนะนำ:
- Move: left/right arrows, A/D, gamepad left stick horizontal
- RotateCW: X, Up Arrow, gamepad east button
- RotateCCW: Z, gamepad west button
- SoftDrop: Down Arrow, S, gamepad south button
- HardDrop: Space, gamepad north button
- Pause: Escape, Start

เชื่อม `InputActionReference` แต่ละตัวเข้ากับ `TetrisInputAdapter`

## ขั้นตอนที่ 12: เพิ่ม tests

เพิ่ม Edit Mode tests สำหรับ:
- `CanPlace`
- `ClearFullLines`
- rotation collision checks

เพิ่ม Play Mode checks สำหรับ:
- bootstrap scene loads the game scene
- a piece spawns
- hard drop and line clear work

## ตัวอย่าง test แบบย่อ

```csharp
using NUnit.Framework;
using UnityEngine;
using UnityTetris.Gameplay;

public sealed class TetrisBoardTests
{
    [Test]
    public void ClearFullLines_RemovesFilledRow()
    {
        var board = new TetrisBoardModel();
        var piece = new TetrisPiece(1, new Vector2Int(5, 0));

        for (int x = 0; x < TetrisBoardModel.Width; x++)
        {
            var rowPiece = new TetrisPiece(1, new Vector2Int(x, 0));
            board.LockPiece(rowPiece);
        }

        var cleared = board.ClearFullLines();

        Assert.AreEqual(1, cleared);
    }
}
```

## checklist สำหรับตรวจสอบ

- bootstrap scene โหลด gameplay scene ได้
- input actions ส่งถึง controller ผ่าน adapter ที่บาง
- board model เป็นเจ้าของ logic เรื่อง collision และ line-clear
- HUD แสดง state เท่านั้น
- hard drop สามารถล็อก piece และลบแถวได้
- tests ครอบคลุมส่วนที่พังง่ายที่สุด

## ทำไมโครงแบบนี้ถึงใช้ได้ผล

- `unity-project-structure` ช่วยไม่ให้ repository กลายเป็นกอง scene แบบกระจัดกระจาย
- `unity-scene-and-bootstrap` ช่วยแยก flow ตอนเริ่มต้นออกจาก gameplay
- `unity-input-system` ช่วยแยกการต่อสาย control ออกจากกติกาของเกม
- `unity-state-machine` ทำให้ flow ของเกมเข้าใจง่าย
- `unity-ugui` ทำให้ HUD บางและไม่แบก logic มากเกินไป
- `unity-testing` ให้ safety net ก่อนเริ่มเก็บรายละเอียด

## สิ่งที่ควรเพิ่มต่อ

เมื่อ core loop ใช้งานได้แล้ว ค่อยเพิ่ม:
- hold piece
- ghost piece
- pause menu
- sound effects
- object pooling
- art แบบ addressable
