param(
  [Parameter(Mandatory = $true)]
  [string]$AppName,
  [ValidateSet("minimal", "dark", "enterprise")]
  [string]$Theme = "minimal"
)

flutter create $AppName
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
powershell -ExecutionPolicy Bypass -File (Join-Path $ScriptDir "apply_web_loader.ps1") -ProjectDir $AppName -Theme $Theme

Write-Host "Done. Next:"
Write-Host "  cd $AppName"
Write-Host "  flutter run -d chrome"
