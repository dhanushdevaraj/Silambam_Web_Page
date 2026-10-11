# PowerShell Launcher for Silambam Web App
Write-Host "=======================================================" -ForegroundColor Yellow
Write-Host "  KALAI THAI SILAMBAM DHARMAPURI - STARTING WEB APPLICATION   " -ForegroundColor Yellow
Write-Host "=======================================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Server running at: http://127.0.0.1:5000" -ForegroundColor Green
Write-Host "Press Ctrl+C to terminate the server."
Write-Host ""

$pythonExe = "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe"
if (Test-Path $pythonExe) {
    & $pythonExe app.py
} else {
    python app.py
}
