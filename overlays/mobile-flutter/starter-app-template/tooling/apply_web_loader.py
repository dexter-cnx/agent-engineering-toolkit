from pathlib import Path
import sys

INDEX_HTML = """<!DOCTYPE html>
<html>
<head>
  <base href="$FLUTTER_BASE_HREF">
  <meta charset="UTF-8">
  <meta content="IE=Edge" http-equiv="X-UA-Compatible">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flutter App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="boot-loader" class="boot-shell">
    <div class="boot-card">
      <div class="boot-title">Loading app…</div>
      <div class="progress-container">
        <div class="progress-bar"></div>
      </div>
      <div class="boot-caption">Preparing Flutter runtime and assets</div>
    </div>
  </div>
  <script src="flutter_bootstrap.js" async></script>
</body>
</html>
"""

STYLE_CSS = """html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

body {
  font-family: Arial, sans-serif;
  background: #f7f7f7;
}

.boot-shell {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.boot-card {
  width: min(420px, 100%);
  background: white;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.10);
}

.boot-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 16px;
}

.boot-caption {
  margin-top: 12px;
  color: #666;
  font-size: 14px;
}

.progress-container {
  width: 100%;
  height: 10px;
  border-radius: 999px;
  overflow: hidden;
  background: #ececec;
}

.progress-bar {
  height: 100%;
  width: 35%;
  border-radius: 999px;
  animation: indeterminate 1.2s infinite ease-in-out;
  background: linear-gradient(90deg, #7aa2ff, #4f7cff);
}

@keyframes indeterminate {
  0%   { transform: translateX(-120%); width: 30%; }
  50%  { transform: translateX(60%); width: 45%; }
  100% { transform: translateX(260%); width: 30%; }
}
"""

BOOTSTRAP_JS = """window.addEventListener('flutter-first-frame', function () {
  const loader = document.getElementById('boot-loader');
  if (loader) {
    loader.style.transition = 'opacity 220ms ease';
    loader.style.opacity = '0';
    setTimeout(() => loader.remove(), 240);
  }
});
"""

def main():
    project_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    web_dir = project_root / "web"
    web_dir.mkdir(parents=True, exist_ok=True)

    (web_dir / "index.html").write_text(INDEX_HTML, encoding="utf-8")
    (web_dir / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (web_dir / "flutter_bootstrap.js").write_text(BOOTSTRAP_JS, encoding="utf-8")

    print(f"Applied web loader baseline to: {web_dir}")

if __name__ == "__main__":
    main()
