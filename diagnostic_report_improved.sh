#!/bin/bash
# 🔍 diagnostic_report_improved.sh - Enhanced Diagnostic Report with Log

echo "🔍 AWS Cloud Orbit RPG - Enhanced Diagnostic Report"
echo "================================================="

echo "Generated: $(date)"
echo "Directory: $(pwd)"
echo ""

echo "📁 GIT STATUS"
echo "============"
git status

echo ""
echo "📂 PROJECT FILES AND FOLDERS"
echo "============================"
# List all files and folders with details
find . -maxdepth 2 | sed 's/^/  /'

echo ""
echo "🐍 PYTHON ENVIRONMENT"
echo "====================="
python --version 2>&1
pip freeze | grep -E 'Flask|jinja2' || echo "No relevant Python packages installed"

echo ""
echo "💻 SYSTEM INFO"
echo "=============="
uname -a

# Save full log to file
LOGFILE="diagnostic_full_$(date +%Y%m%d_%H%M%S).log"
echo "Logging complete report to $LOGFILE"
{
    echo "Generated: $(date)"
    echo
    echo "Git Status:"; git status
    echo
    echo "Project Files:"; find .
    echo
    echo "Python Version:"; python --version 2>&1
    echo "Installed Packages:"; pip freeze
    echo
    echo "System Info:"; uname -a
} > "$LOGFILE"

echo ""
echo "🚀 Enhanced diagnostic complete!"
echo "   Log file created: $LOGFILE"

# Instructions for user
echo "Please attach $LOGFILE for detailed analysis."
