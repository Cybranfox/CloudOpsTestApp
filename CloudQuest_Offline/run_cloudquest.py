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
