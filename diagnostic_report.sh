#!/bin/bash
# AWS Cloud Orbit RPG - Diagnostic Information Collector
# Use this script to quickly gather project status for troubleshooting and updates

echo "🔍 AWS Cloud Orbit RPG - Diagnostic Report"
echo "=========================================="
echo "Generated: $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "Directory: $(pwd)"
echo ""

# Git Status & Branch Info
echo "📁 GIT STATUS"
echo "============="
echo "Current Branch: $(git branch --show-current 2>/dev/null || echo 'Not a git repository')"
echo "Commits ahead/behind remote:"
git status -uno 2>/dev/null | grep -E "(ahead|behind|up to date)" || echo "No remote tracking"
echo ""

echo "Uncommitted Changes:"
git status --porcelain 2>/dev/null || echo "No git repository found"
echo ""

# Project Structure
echo "📂 PROJECT STRUCTURE"
echo "===================="
echo "Core Files:"
ls -la | grep -E "\.(py|json|txt|md)$" | awk '{print "  " $9 " (" $5 " bytes, modified " $6 " " $7 " " $8 ")"}'
echo ""

echo "Directories:"
ls -la | grep "^d" | awk '{print "  📁 " $9 "/"}'
echo ""

# Key File Sizes and Dates
echo "🎯 KEY FILES STATUS"
echo "==================="
key_files=("app.py" "progress.py" "improved_data.py" "progress.json" "requirements.txt")
for file in "${key_files[@]}"; do
    if [ -f "$file" ]; then
        size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null)
        modified=$(stat -c%y "$file" 2>/dev/null || stat -f%Sm -t%Y-%m-%d\ %H:%M "$file" 2>/dev/null)
        echo "  ✅ $file ($size bytes, modified: $modified)"
    else
        echo "  ❌ $file (missing)"
    fi
done
echo ""

# Templates Status
echo "🎨 TEMPLATES STATUS"
echo "=================="
if [ -d "templates" ]; then
    echo "Template files found:"
    ls -la templates/ | grep "\.html$" | awk '{print "  📄 " $9 " (" $5 " bytes)"}'
else
    echo "  ❌ templates/ directory not found"
fi
echo ""

# Static Assets Status
echo "🎮 STATIC ASSETS STATUS"
echo "======================="
if [ -d "static" ]; then
    echo "Static directory size: $(du -sh static/ 2>/dev/null | cut -f1)"
    echo "Key assets:"
    assets=("zap.png" "styles.css" "zap_animator.js" "enhanced_zap_animator.js")
    for asset in "${assets[@]}"; do
        if [ -f "static/$asset" ]; then
            size=$(stat -c%s "static/$asset" 2>/dev/null || stat -f%z "static/$asset" 2>/dev/null)
            echo "  ✅ $asset ($size bytes)"
        else
            echo "  ❌ $asset (missing)"
        fi
    done
    
    echo ""
    echo "Mascot animations:"
    if [ -d "static/mascot" ]; then
        ls -la static/mascot/ | grep "\.png$" | awk '{print "  🤖 " $9 " (" $5 " bytes)"}'
    else
        echo "  ❌ static/mascot/ directory not found"
    fi
else
    echo "  ❌ static/ directory not found"
fi
echo ""

# Recent Changes
echo "📊 RECENT CHANGES"
echo "================="
echo "Last 5 commits:"
git log --oneline -5 2>/dev/null || echo "No git history available"
echo ""

echo "Modified files in last 24 hours:"
find . -type f -mtime -1 -not -path "./.git/*" -not -path "./__pycache__/*" 2>/dev/null | head -10 || echo "No recently modified files found"
echo ""

# Python Environment
echo "🐍 PYTHON ENVIRONMENT"
echo "====================="
echo "Python version: $(python --version 2>/dev/null || echo 'Python not found')"
echo "Flask installation:"
python -c "import flask; print(f'Flask {flask.__version__}')" 2>/dev/null || echo "Flask not installed"
echo ""

echo "Dependencies from requirements.txt:"
if [ -f "requirements.txt" ]; then
    cat requirements.txt
else
    echo "No requirements.txt found"
fi
echo ""

# Running Processes
echo "🔄 RUNNING PROCESSES"
echo "===================="
flask_processes=$(ps aux | grep -E "flask|app\.py" | grep -v grep | wc -l)
echo "Flask processes running: $flask_processes"
if [ $flask_processes -gt 0 ]; then
    echo "Flask processes:"
    ps aux | grep -E "flask|app\.py" | grep -v grep | awk '{print "  PID " $2 ": " $11 " " $12 " " $13}'
fi
echo ""

# Network Status
echo "🌐 NETWORK STATUS"
echo "================="
echo "Checking if Flask app is running on port 5001:"
if command -v curl >/dev/null 2>&1; then
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:5001 2>/dev/null | grep -q "200\|302\|404"; then
        echo "  ✅ App appears to be running on localhost:5001"
    else
        echo "  ❌ No response from localhost:5001"
    fi
else
    if command -v nc >/dev/null 2>&1; then
        if nc -z localhost 5001 2>/dev/null; then
            echo "  ✅ Port 5001 is open"
        else
            echo "  ❌ Port 5001 is not open"
        fi
    else
        echo "  ❓ Cannot check port status (curl and nc not available)"
    fi
fi
echo ""

# System Info
echo "💻 SYSTEM INFO"
echo "=============="
echo "Operating System: $(uname -s 2>/dev/null || echo 'Unknown')"
echo "Architecture: $(uname -m 2>/dev/null || echo 'Unknown')"
echo "Available disk space:"
df -h . 2>/dev/null | tail -1 | awk '{print "  " $4 " available (" $5 " used)"}' || echo "  Could not determine disk space"
echo "Current directory size: $(du -sh . 2>/dev/null | cut -f1 || echo 'Unknown')"
echo ""

# Quick Health Check
echo "🏥 QUICK HEALTH CHECK"
echo "====================="
health_score=0
total_checks=8

# Check 1: Core files exist
if [ -f "app.py" ] && [ -f "progress.py" ] && [ -f "improved_data.py" ]; then
    echo "  ✅ Core Python files present"
    ((health_score++))
else
    echo "  ❌ Missing core Python files"
fi

# Check 2: Templates exist
if [ -d "templates" ] && [ -f "templates/index.html" ] && [ -f "templates/quiz.html" ]; then
    echo "  ✅ Essential templates present"
    ((health_score++))
else
    echo "  ❌ Missing essential templates"
fi

# Check 3: Static assets exist
if [ -d "static" ] && [ -f "static/zap.png" ] && [ -f "static/styles.css" ]; then
    echo "  ✅ Core static assets present"
    ((health_score++))
else
    echo "  ❌ Missing core static assets"
fi

# Check 4: Progress file exists and is valid JSON
if [ -f "progress.json" ] && python -c "import json; json.load(open('progress.json'))" 2>/dev/null; then
    echo "  ✅ Progress file valid"
    ((health_score++))
else
    echo "  ❌ Progress file missing or invalid"
fi

# Check 5: Python can import main modules
if python -c "import improved_data, progress" 2>/dev/null; then
    echo "  ✅ Python modules importable"
    ((health_score++))
else
    echo "  ❌ Python modules have import errors"
fi

# Check 6: Flask is installed
if python -c "import flask" 2>/dev/null; then
    echo "  ✅ Flask is installed"
    ((health_score++))
else
    echo "  ❌ Flask not installed"
fi

# Check 7: Git repository is healthy
if git status >/dev/null 2>&1; then
    echo "  ✅ Git repository healthy"
    ((health_score++))
else
    echo "  ❌ Git repository issues"
fi

# Check 8: No critical file size issues
large_files=$(find . -type f -size +10M -not -path "./.git/*" 2>/dev/null | wc -l)
if [ "$large_files" -lt 5 ]; then
    echo "  ✅ No excessive large files"
    ((health_score++))
else
    echo "  ⚠️  Many large files detected ($large_files files > 10MB)"
fi

echo ""
echo "📈 HEALTH SCORE: $health_score/$total_checks"
if [ $health_score -ge 7 ]; then
    echo "🟢 Project Status: EXCELLENT"
elif [ $health_score -ge 5 ]; then
    echo "🟡 Project Status: GOOD"
elif [ $health_score -ge 3 ]; then
    echo "🟠 Project Status: NEEDS ATTENTION"
else
    echo "🔴 Project Status: CRITICAL ISSUES"
fi

echo ""
echo "🚀 RECOMMENDED ACTIONS"
echo "======================"
if [ $health_score -lt 8 ]; then
    echo "  📋 Review missing components above"
    echo "  🔧 Run: python app.py (to test the application)"
    echo "  📦 Run: pip install -r requirements.txt (if Flask import failed)"
fi

if git status --porcelain 2>/dev/null | grep -q .; then
    echo "  💾 Commit pending changes: git add . && git commit -m 'Update'"
fi

echo "  📊 Share this report for troubleshooting support"
echo "  🎮 Visit http://localhost:5001 when app is running"

echo ""
echo "================== END DIAGNOSTIC REPORT =================="