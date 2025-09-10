#!/bin/bash
# Quick Status Check for AWS Cloud Orbit RPG
# Use this for rapid troubleshooting and updates

echo "⚡ AWS Cloud Orbit RPG - Quick Status"
echo "====================================="
echo "📅 $(date '+%Y-%m-%d %H:%M:%S')"
echo "📁 $(pwd)"
echo ""

# Core Status
echo "🎯 CORE STATUS:"
[ -f "app.py" ] && echo "  ✅ app.py" || echo "  ❌ app.py missing"
[ -f "progress.py" ] && echo "  ✅ progress.py" || echo "  ❌ progress.py missing"
[ -f "improved_data.py" ] && echo "  ✅ improved_data.py" || echo "  ❌ improved_data.py missing"
[ -f "progress.json" ] && echo "  ✅ progress.json" || echo "  ❌ progress.json missing"
[ -d "templates" ] && echo "  ✅ templates/" || echo "  ❌ templates/ missing"
[ -d "static" ] && echo "  ✅ static/" || echo "  ❌ static/ missing"

echo ""
echo "📊 GIT STATUS:"
echo "  Branch: $(git branch --show-current 2>/dev/null || echo 'no git')"
uncommitted=$(git status --porcelain 2>/dev/null | wc -l)
echo "  Uncommitted changes: $uncommitted files"

echo ""
echo "🐍 PYTHON STATUS:"
python -c "import flask; print('  ✅ Flask', flask.__version__)" 2>/dev/null || echo "  ❌ Flask not available"
python -c "import improved_data, progress; print('  ✅ Modules importable')" 2>/dev/null || echo "  ❌ Module import errors"

echo ""
echo "🌐 APP STATUS:"
if pgrep -f "app.py\|flask" >/dev/null; then
    echo "  ✅ Flask app appears to be running"
    echo "  🌍 Visit: http://localhost:5001"
else
    echo "  ❌ Flask app not running"
    echo "  🚀 Start with: python app.py"
fi

echo ""
echo "📈 RECENT ACTIVITY:"
echo "  Last modified files:"
find . -type f -mtime -1 -not -path "./.git/*" -not -path "./__pycache__/*" 2>/dev/null | head -5 | sed 's/^/    /' || echo "    No recent changes"

if git log --oneline -1 2>/dev/null >/dev/null; then
    echo "  Last commit: $(git log --oneline -1 2>/dev/null)"
fi

echo ""
echo "💡 QUICK ACTIONS:"
echo "  📊 Full report: ./diagnostic_report.sh"
echo "  🚀 Run app: python app.py"
echo "  💾 Commit: git add . && git commit -m 'Update'"
echo "  📤 Push: git push origin main"
echo "==============================================="