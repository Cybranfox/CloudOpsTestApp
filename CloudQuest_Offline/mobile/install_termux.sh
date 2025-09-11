#!/data/data/com.termux/files/usr/bin/bash
# Termux installation script for CloudQuest RPG

echo "📱 CloudQuest RPG - Termux Installation"
echo "======================================"

# Install required packages
echo "📦 Installing Python and Flask..."
pkg install python -y
pip install flask

echo "🚀 Starting CloudQuest RPG..."
cd "$(dirname "$0")/../"
python run_cloudquest.py

echo "🌐 Open your browser and go to: http://localhost:5001"
echo "📱 Bookmark it for easy access!"
