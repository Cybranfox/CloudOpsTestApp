@echo off
title CloudQuest RPG - Offline
echo 🚀 Starting CloudQuest RPG...
echo ===============================
echo ✅ Fully offline - no internet needed!
echo 🌐 Opening in browser...
echo 🛑 Close this window to stop
echo.

cd /d "%~dp0"
python run_cloudquest.py
pause
