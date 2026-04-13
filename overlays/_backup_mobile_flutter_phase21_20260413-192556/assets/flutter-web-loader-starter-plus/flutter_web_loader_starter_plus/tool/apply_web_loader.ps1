param(
  [string]$ProjectDir = ".",
  [ValidateSet("minimal", "dark", "enterprise")]
  [string]$Theme = "minimal"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
$TemplateDir = Join-Path $RootDir ("templates\" + $Theme)
$WebDir = Join-Path $ProjectDir "web"

if (-not (Test-Path $TemplateDir)) {
  throw "Unknown theme: $Theme"
}

New-Item -ItemType Directory -Force -Path $WebDir | Out-Null

Copy-Item (Join-Path $TemplateDir "index.html") (Join-Path $WebDir "index.html") -Force
Copy-Item (Join-Path $TemplateDir "style.css") (Join-Path $WebDir "style.css") -Force
Copy-Item (Join-Path $TemplateDir "flutter_bootstrap.js") (Join-Path $WebDir "flutter_bootstrap.js") -Force

Write-Host "Applied Flutter web loader"
Write-Host "Project: $ProjectDir"
Write-Host "Theme: $Theme"
