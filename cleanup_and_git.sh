#!/bin/bash
# AWS Cloud Orbit RPG - Cleanup and Git Workflow Script
# Run this script to clean up bloat and prepare for production

echo "🧹 AWS Cloud Orbit RPG - Cleanup Script"
echo "========================================"

# Step 1: Remove bloat files
echo "📂 Removing unnecessary files..."

# Development artifacts
rm -f ai_analysis.txt
rm -f ai_dev_assistant.py
rm -f analysis_report.md
rm -f AI_PROGRESS_REPORT.md
rm -f code_quality_report.md

# Old/duplicate files
rm -f data.py
rm -f enhanced_progress.py
rm -f requirements_new.txt
rm -f package.json

# Build scripts (not needed for web app)
rm -f build-apk-simple.sh
rm -f build-apk.sh
rm -f fix-android-build.sh
rm -f fix-java-version.sh

# Old directory structures
rm -rf src/
rm -rf mobile_components/
rm -rf docs/
rm -rf __pycache__/

echo "✅ Cleanup complete!"

# Step 2: Update core files
echo "📝 Updating core files..."

# Update requirements.txt
cp requirements_clean.txt requirements.txt
rm requirements_clean.txt

# Update README.md
cp README_updated.md README.md
rm README_updated.md

echo "✅ Core files updated!"

# Step 3: Git workflow
echo "🔄 Git workflow..."

# Stage all changes
git add .

# Commit the cleanup
git commit -m "🧹 Major cleanup: Remove bloat, update documentation, finalize RPG mechanics

- Remove unnecessary build scripts and dev artifacts
- Clean up duplicate and old files
- Update README with current feature set
- Streamline requirements.txt
- Finalize working RPG learning system with:
  * Energy shield mechanics
  * Guardian's Shield relic system
  * 10 comprehensive AWS lessons
  * Responsive UI with readable answer options
  * Achievement and badge system"

echo "✅ Changes committed!"

# Step 4: Display current status
echo ""
echo "📊 Current repository status:"
echo "============================="
git status --short
echo ""

# Step 5: Show final structure
echo "📁 Final project structure:"
echo "=========================="
find . -type f -name "*.py" -o -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.txt" -o -name "*.md" -o -name "*.json" | grep -v __pycache__ | sort

echo ""
echo "🎯 Ready to push! Use: git push origin main"
echo "🚀 Your AWS Cloud Orbit RPG is clean and production-ready!"