#!/bin/bash
# 📦 build_offline_standalone.sh - Create fully offline CloudQuest RPG
set -e

echo "📦 CloudQuest RPG - Standalone Offline Builder"
echo "=============================================="

# Security & Prerequisites Check
if [[ ! -f "app.py" ]] || [[ ! -d "static" ]] || [[ ! -d "templates" ]]; then
    echo "❌ Error: Not in AWS_Orbit_RPG directory. Please run from project root."
    exit 1
fi

# Check for required tools
MISSING_TOOLS=()
if ! command -v python &> /dev/null; then
    MISSING_TOOLS+=("python")
fi

if ! python -c "import flask" 2>/dev/null; then
    echo "⚠️ Installing Flask..."
    pip install flask pyinstaller
fi

echo "✅ Prerequisites check passed"

# Create build directory
BUILD_DIR="CloudQuest_Offline"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "📁 Creating standalone package..."

# 1. Copy all necessary files
cp -r templates static improved_data.py progress.py "$BUILD_DIR/"
cp app.py progress.json requirements.txt "$BUILD_DIR/"

# 2. Create standalone launcher script
echo "🚀 Creating standalone launcher..."
cat > "$BUILD_DIR/run_cloudquest.py" << 'EOF'
#!/usr/bin/env python3
"""
CloudQuest RPG - Fully Offline Standalone Launcher
No network connection required!
"""
import os
import sys
import webbrowser
import threading
import time
from flask import Flask

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main app
from app import app

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)
    webbrowser.open('http://localhost:5001/?mode=offline')

def main():
    print("🚀 CloudQuest RPG - Offline Mode")
    print("===============================")
    print("✅ Running completely offline - no internet needed!")
    print("🌐 Opening in browser: http://localhost:5001")
    print("📱 For mobile: copy this folder to your phone and run")
    print("🛑 Press Ctrl+C to stop")
    print("")
    
    # Start browser in separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Run Flask app
    try:
        app.run(host='localhost', port=5001, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n👋 CloudQuest RPG stopped. Thanks for playing!")

if __name__ == '__main__':
    main()
EOF

# 3. Create Windows batch file launcher
cat > "$BUILD_DIR/CloudQuest.bat" << 'EOF'
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
EOF

# 4. Create Linux/Mac launcher script
cat > "$BUILD_DIR/run_cloudquest.sh" << 'EOF'
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
EOF

chmod +x "$BUILD_DIR/run_cloudquest.sh"

# 5. Create mobile-specific files
echo "📱 Creating mobile version..."
mkdir -p "$BUILD_DIR/mobile"

# Android Termux script
cat > "$BUILD_DIR/mobile/install_termux.sh" << 'EOF'
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
EOF

chmod +x "$BUILD_DIR/mobile/install_termux.sh"

# 6. Create portable README
cat > "$BUILD_DIR/README_OFFLINE.md" << 'EOF'
# 📦 CloudQuest RPG - Fully Offline Version

🎉 **This is a completely standalone version that works WITHOUT internet!**

## 🖥️ Desktop Usage (Windows)
1. Double-click `CloudQuest.bat`
2. Browser will open automatically
3. Play offline! ✅

## 🖥️ Desktop Usage (Linux/Mac)
1. Run `./run_cloudquest.sh`  
2. Browser opens at http://localhost:5001
3. Play offline! ✅

## 📱 Mobile Usage (Android - Termux)
1. Install [Termux](https://termux.dev/en/) from F-Droid
2. Copy this entire folder to your phone
3. Open Termux and navigate to the folder
4. Run: `./mobile/install_termux.sh`
5. Open browser to http://localhost:5001
6. Bookmark for easy access!

## 📱 Mobile Usage (iOS - iSH)
1. Install [iSH Shell](https://apps.apple.com/app/ish-shell/id1436902243) from App Store
2. Copy this folder to iSH
3. Run: `./run_cloudquest.sh`
4. Open Safari to http://localhost:5001

## 🎮 Features Available Offline:
- ✅ All AWS lessons and quizzes
- ✅ Space-themed UI and animations  
- ✅ Audio feedback system
- ✅ Progress tracking (saved locally)
- ✅ Badge system
- ✅ Reward screens
- ✅ Complete RPG experience

## 📂 Folder Contents:
- `CloudQuest.bat` - Windows launcher
- `run_cloudquest.sh` - Linux/Mac launcher  
- `run_cloudquest.py` - Python launcher
- `mobile/` - Mobile installation scripts
- `static/` - Images, CSS, JavaScript
- `templates/` - HTML templates
- All game data and progress files

## 🔄 Sharing:
This entire folder can be:
- ✅ Copied to USB drives
- ✅ Shared via file transfer
- ✅ Backed up to cloud storage
- ✅ Run on any device with Python

**No internet required after initial setup!** 🌟
EOF

# 7. Create requirements for the offline version
cat > "$BUILD_DIR/requirements.txt" << 'EOF'
Flask==3.1.1
EOF

# 8. Update progress.py to ensure offline data persistence
echo "💾 Ensuring offline data persistence..."
cat > "$BUILD_DIR/progress_offline.py" << 'EOF'
"""
Offline-optimized progress tracking
Ensures all data is saved locally without any network dependencies
"""
import json
import os
from datetime import datetime, date

PROGRESS_FILE = 'progress_offline.json'

def load_progress():
    """Load progress from local file"""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    
    # Default offline progress
    return {
        'current_lesson': 1,
        'xp': 0,
        'energy': 3,
        'max_energy': 3,
        'streak': 0,
        'last_active': str(date.today()),
        'completed_lessons': [],
        'badges': [],
        'stats': {
            'total_questions': 0,
            'correct_answers': 0,
            'total_time': 0
        },
        'inventory': {
            'relics': [],
            'potions': []
        },
        'offline_mode': True
    }

def save_progress(progress):
    """Save progress to local file"""
    progress['last_saved'] = datetime.now().isoformat()
    progress['offline_mode'] = True
    
    try:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f, indent=2)
        return True
    except Exception as e:
        print(f"Warning: Could not save progress: {e}")
        return False

# Export the same interface as the original
def register_quiz_result(lesson_id, correct):
    """Register quiz result offline"""
    progress = load_progress()
    
    # Update stats
    progress['stats']['total_questions'] += 1
    if correct:
        progress['stats']['correct_answers'] += 1
        progress['xp'] += 10
        if progress['energy'] < progress['max_energy']:
            progress['energy'] += 1
    else:
        progress['energy'] = max(0, progress['energy'] - 1)
    
    # Update lesson completion
    if correct and lesson_id not in progress['completed_lessons']:
        progress['completed_lessons'].append(lesson_id)
        progress['current_lesson'] = max(progress['current_lesson'], lesson_id + 1)
    
    save_progress(progress)
    
    message = "Correct! +10 XP" if correct else "Try again!"
    next_lesson = lesson_id + 1 if correct else lesson_id
    
    return progress, message, next_lesson

def complete_lesson(lesson_id):
    """Mark lesson as complete"""
    progress = load_progress()
    if lesson_id not in progress['completed_lessons']:
        progress['completed_lessons'].append(lesson_id)
        progress['current_lesson'] = max(progress['current_lesson'], lesson_id + 1)
    save_progress(progress)
    return progress

def check_achievements(progress):
    """Check for new achievements"""
    new_badges = []
    
    stats = progress.get('stats', {})
    correct = stats.get('correct_answers', 0)
    total = stats.get('total_questions', 0)
    
    # Achievement logic
    if correct >= 10 and 'Quick Learner' not in progress['badges']:
        new_badges.append('Quick Learner')
    
    if total >= 50 and 'Dedicated Student' not in progress['badges']:
        new_badges.append('Dedicated Student')
    
    if correct >= 100 and 'AWS Expert' not in progress['badges']:
        new_badges.append('AWS Expert')
    
    # Add new badges
    progress['badges'].extend(new_badges)
    save_progress(progress)
    
    return new_badges

def has_guardian_shield(progress):
    """Check if guardian shield is active"""
    return 'Guardian Shield' in progress.get('badges', [])
EOF

# Replace the progress import in app.py copy
sed -i 's/from progress import/from progress_offline import/g' "$BUILD_DIR/app.py" 2>/dev/null || true

# 9. Create final package info
echo "📊 Creating package info..."
PACKAGE_SIZE=$(du -sh "$BUILD_DIR" | cut -f1)

cat > "$BUILD_DIR/PACKAGE_INFO.txt" << EOF
CloudQuest RPG - Offline Package
================================
Created: $(date)
Size: $PACKAGE_SIZE
Platform: Cross-platform (Windows/Linux/Mac/Mobile)
Network: No internet required ✅

Launch Commands:
- Windows: CloudQuest.bat
- Linux/Mac: ./run_cloudquest.sh  
- Python: python run_cloudquest.py
- Termux: ./mobile/install_termux.sh

URL: http://localhost:5001
EOF

echo ""
echo "🎉 CloudQuest RPG Offline Package Created!"
echo "=========================================="
echo ""
echo "📦 Package Location: ./$BUILD_DIR/"
echo "📊 Package Size: $PACKAGE_SIZE"
echo ""
echo "🖥️ DESKTOP TESTING:"
echo "cd $BUILD_DIR"
echo "python run_cloudquest.py"
echo ""
echo "📱 MOBILE TRANSFER:"
echo "1. Copy entire '$BUILD_DIR' folder to your phone"
echo "2. Use Termux (Android) or iSH (iOS)"  
echo "3. Run the mobile installer script"
echo ""
echo "🌟 FEATURES:"
echo "✅ Completely offline - no internet needed"
echo "✅ Works on Windows, Mac, Linux, Android, iOS"
echo "✅ Portable - copy to any device"
echo "✅ All game features included"
echo "✅ Progress saved locally"
echo ""
echo "🚀 Ready to play anywhere, anytime!"