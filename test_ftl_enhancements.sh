#!/bin/bash
echo "🧪 Testing FTL-Style CloudQuest Enhancements"
echo "==========================================="

echo "🔍 Checking files..."
if [[ -f "static/ftl_style_sectors.css" ]]; then
    echo "✅ FTL CSS deployed"
else
    echo "❌ FTL CSS missing"
fi

if [[ -f "static/space_adventure_enhanced.js" ]]; then
    echo "✅ Enhanced JavaScript deployed"
else
    echo "❌ Enhanced JavaScript missing"
fi

if [[ -f "templates/space_adventure_map.html" ]]; then
    echo "✅ Enhanced space map template deployed"
else
    echo "❌ Enhanced space map template missing"
fi

echo ""
echo "🚀 Starting CloudQuest with FTL enhancements..."
python app.py &
APP_PID=$!

sleep 3

echo "🌐 Testing server..."
if curl -s http://localhost:5001 > /dev/null; then
    echo "✅ Server running successfully!"
    echo ""
    echo "🎮 READY TO TEST:"
    echo "==============================="
    echo "🌐 Visit: http://localhost:5001"
    echo ""
    echo "🔍 Look for:"
    echo "• Sector-based layout (3x2 grid)"
    echo "• Smooth hover animations"
    echo "• Animated connection paths"
    echo "• Ripple effects on lesson clicks"
    echo "• Dynamic starfield background"
    echo "• Progress bars with shimmer"
    echo "• Responsive design"
    echo ""
    echo "📱 Mobile test:"
    echo "• Resize browser window"
    echo "• Should adapt to single column"
    echo ""
    echo "⌨️  Keyboard navigation:"
    echo "• Tab through lessons"
    echo "• Arrow keys for navigation"
    echo ""
    echo "Press Enter to stop test server..."
    read
    kill $APP_PID
else
    echo "❌ Server failed to start"
    kill $APP_PID 2>/dev/null
fi
