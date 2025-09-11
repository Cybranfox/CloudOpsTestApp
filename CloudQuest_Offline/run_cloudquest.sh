#!/bin/bash
# CloudQuest RPG - Offline Launcher for Linux/Mac

echo "🚀 CloudQuest RPG - Offline Mode"
echo "==============================="
echo "✅ Fully offline - no internet needed!"
echo "🌐 Opening in browser..."
echo "🛑 Press Ctrl+C to stop"
echo ""

cd "$(dirname "$0")"
python3 run_cloudquest.py
