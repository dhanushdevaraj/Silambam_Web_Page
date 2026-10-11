@echo off
title Silambam Academy Web Server
echo =======================================================
echo   KALAI THAI SILAMBAM DHARMAPURI - STARTING WEB APPLICATION
echo =======================================================
echo.
echo Starting Flask web server at: http://127.0.0.1:5000
echo Press Ctrl+C in this terminal window to stop the server.
echo.

set PYTHON_CMD=python
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python app.py
) else (
    "%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe" app.py
)
pause
