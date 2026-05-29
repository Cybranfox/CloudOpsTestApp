#!/bin/bash
# 🧹 cleanup_project.sh - Remove unnecessary scripts and bloat

echo "🧹 CloudQuest RPG - Project Cleanup"
echo "==================================="

echo "📂 Removing unnecessary build and test scripts..."

# Remove all the temporary build scripts we created
rm -f build_android_apk.sh
rm -f fix_and_build_apk.sh  
rm -f fix_java_compatibility.sh
rm -f setup_mobile_pwa.sh
rm -f simple_apk_build.sh
rm -f start_mobile.sh
rm -f test_pwa.sh
rm -f deploy_ftl_enhancements.sh
rm -f fix_deployment.sh
rm -f fix_jinja_template.sh
rm -f restore_enhanced_map.sh
rm -f create_duolingo_ftl_map.sh
rm -f create_duolingo_inspired_map.sh
rm -f fix_lesson_circles.sh
rm -f diagnose_css_issue.sh
rm -f test_ftl_enhancements.sh
rm -f optimize_mobile.sh

# Remove backup templates if they exist
rm -f templates/space_adventure_map_backup.html
rm -f templates/enhanced_space_adventure_map.html

# Remove temporary CSS files
rm -f static/ftl_style_sectors.css
rm -f static/space_adventure_enhanced.js

# Remove build directories if they exist
rm -rf android_build/

# Remove any .pyc files and __pycache__
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null

# Keep only essential files
echo ""
echo "✅ CLEANED UP FILES:"
echo "• Removed all temporary build scripts"
echo "• Removed backup templates" 
echo "• Removed unused CSS/JS files"
echo "• Removed build directories"
echo "• Cleared Python cache files"

echo ""
echo "📂 KEEPING ESSENTIAL FILES:"
echo "• app.py - Main application"
echo "• progress.py - Progress tracking"
echo "• improved_data.py - Lesson content"
echo "• requirements.txt - Dependencies"
echo "• templates/ - HTML templates"
echo "• static/ - Essential assets only"
echo "• CloudQuest_Offline/ - Portable version"

echo ""
echo "🎯 CURRENT PROJECT STRUCTURE:"
ls -la

echo ""
echo "🧹 CLEANUP COMPLETE!"
echo "==================="
echo ""
echo "💡 PROJECT IS NOW CLEAN AND MINIMAL"
echo "• Removed ~15 unnecessary script files"
echo "• Kept only production-ready files"
echo "• Reduced directory bloat"
echo "• Ready for final testing and deployment"
echo ""
echo "🚀 NEXT STEPS:"
echo "1. Restart Flask: python app.py"
echo "2. Test the clean map: http://localhost:5001"
echo "3. Verify lesson circles work properly"
echo "4. Commit clean state: git add . && git commit -m 'Clean final version'"