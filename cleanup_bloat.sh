#!/bin/bash
# AWS Cloud Orbit RPG - Smart Cleanup Script
# Removes bloat while preserving your excellent working app

echo "🧹 AWS Cloud Orbit RPG - Smart Cleanup"
echo "======================================"
echo "This will remove unnecessary files while keeping your working app intact."
echo ""

# Show what will be removed
echo "📋 FILES TO REMOVE (AI artifacts and duplicates):"
files_to_remove=(
    "ai_analysis.txt"
    "ai_dev_assistant.py"
    "AI_PROGRESS_REPORT.md"
    "analysis_report.md"
    "code_quality_report.md"
    "build-apk-simple.sh"
    "build-apk.sh"
    "fix-android-build.sh"
    "fix-java-version.sh"
    "package.json"
    "requirements_new.txt"
    "data.py"
    "enhanced_progress.py"
)

for file in "${files_to_remove[@]}"; do
    if [ -f "$file" ]; then
        echo "  ❌ $file ($(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null) bytes)"
    fi
done

# Show directories to remove
echo ""
echo "📁 DIRECTORIES TO REMOVE:"
dirs_to_remove=(
    "__pycache__"
    "docs"
    "mobile_components"
    "src"
)

for dir in "${dirs_to_remove[@]}"; do
    if [ -d "$dir" ]; then
        size=$(du -sh "$dir" 2>/dev/null | cut -f1)
        echo "  ❌ $dir/ ($size)"
    fi
done

echo ""
echo "✅ KEEPING (your working app):"
echo "  ✅ app.py - Main Flask application"
echo "  ✅ progress.py - RPG mechanics"
echo "  ✅ improved_data.py - AWS lesson content"
echo "  ✅ progress.json - Your game progress"
echo "  ✅ requirements.txt - Python dependencies"
echo "  ✅ README.md - Documentation"
echo "  ✅ templates/ - All your working HTML templates"
echo "  ✅ static/ - All assets, images, CSS, JS"

echo ""
read -p "🤔 Proceed with cleanup? This will remove the files listed above. (y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🧹 Starting cleanup..."
    
    # Remove files
    removed_files=0
    for file in "${files_to_remove[@]}"; do
        if [ -f "$file" ]; then
            rm -f "$file"
            echo "  🗑️  Removed $file"
            ((removed_files++))
        fi
    done
    
    # Remove directories
    removed_dirs=0
    for dir in "${dirs_to_remove[@]}"; do
        if [ -d "$dir" ]; then
            rm -rf "$dir"
            echo "  🗑️  Removed $dir/"
            ((removed_dirs++))
        fi
    done
    
    echo ""
    echo "✅ Cleanup complete!"
    echo "   📁 Removed $removed_dirs directories"
    echo "   📄 Removed $removed_files files"
    
    # Show final status
    echo ""
    echo "🎯 FINAL PROJECT STRUCTURE:"
    ls -la | grep -E "(^-.*\.(py|json|txt|md|sh)$|^d)" | awk '{
        if ($1 ~ /^d/) {
            print "  📁 " $9 "/"
        } else {
            print "  📄 " $9 " (" $5 " bytes)"
        }
    }'
    
    echo ""
    echo "💾 Ready to commit clean state:"
    echo "   git add ."
    echo "   git commit -m '🧹 Cleanup: Remove AI artifacts and unused files'"
    echo "   git push origin main"
    
    echo ""
    echo "🚀 Your working AWS Cloud Orbit RPG is now clean and ready!"
    echo "   Run: python app.py"
    echo "   Visit: http://localhost:5001"
    
else
    echo ""
    echo "❌ Cleanup cancelled. No files were modified."
    echo ""
    echo "💡 You can run this script anytime to clean up bloat."
    echo "   Your working app files are always preserved!"
fi

echo ""
echo "==============================================="