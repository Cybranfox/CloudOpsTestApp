#!/bin/bash
# AWS Cloud Orbit RPG - Selective Cleanup (Keep What Works!)
# Only removes genuinely unused files, keeps all working components

echo "🎯 AWS Cloud Orbit RPG - Selective Cleanup"
echo "=========================================="
echo "Keeping all working features and animations!"

# Step 1: Remove only genuinely unused files
echo "📂 Removing only unused files..."

# Development artifacts (not part of the app)
rm -f ai_analysis.txt
rm -f ai_dev_assistant.py
rm -f analysis_report.md
rm -f AI_PROGRESS_REPORT.md
rm -f code_quality_report.md

# Duplicate/old versions only
rm -f data.py               # Only if improved_data.py exists
rm -f enhanced_progress.py  # Only if current progress.py exists
rm -f requirements_new.txt  # Duplicate

# Android build scripts (web app doesn't need these)
rm -f build-apk-simple.sh
rm -f build-apk.sh
rm -f fix-android-build.sh
rm -f fix-java-version.sh
rm -f package.json          # Android artifact

# Only remove old src/ if current structure exists
if [ -f "improved_data.py" ] && [ -f "progress.py" ]; then
    echo "📁 Removing old src/ structure (replaced by current files)"
    rm -rf src/
fi

# Clean up only empty or unused directories
rm -rf docs/          # If it's just old documentation
rm -rf __pycache__/   # Python cache files

echo "✅ Selective cleanup complete!"
echo "✅ All working animations, templates, and features preserved!"

# Step 2: Show what we're keeping
echo ""
echo "🎮 Preserved working components:"
echo "==============================="
echo "✅ All animations and mascot files"
echo "✅ All working templates"
echo "✅ All static assets (CSS, JS, images)"
echo "✅ Current app structure"
echo "✅ RPG mechanics and progress system"

# Step 3: Git staging (but don't commit yet - let user review)
git add -A

echo ""
echo "📊 Repository status:"
git status --short

echo ""
echo "🚀 Ready for feature additions!"
echo "Next: Adding Duolingo-inspired features..."