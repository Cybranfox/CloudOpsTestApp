#!/bin/bash
# 🌌 deploy_ftl_enhancements.sh - Add FTL-style sector map and animations

echo "🚀 CloudQuest RPG - FTL-Style Enhancement Deployment"
echo "====================================================="

# Check we're in the right directory
if [[ ! -f "app.py" ]]; then
    echo "❌ Error: Run from AWS_Orbit_RPG directory"
    exit 1
fi

echo "📁 Backing up existing files..."
if [[ -f "templates/space_adventure_map.html" ]]; then
    cp templates/space_adventure_map.html templates/space_adventure_map_backup.html
fi

echo "🎨 Deploying enhanced CSS..."
cp ftl_style_sectors.css static/

echo "🗺️ Deploying enhanced space adventure map..."
cp enhanced_space_adventure_map.html templates/space_adventure_map.html

echo "✨ Deploying enhanced JavaScript..."
cp space_adventure_enhanced.js static/

echo "🔧 Updating app.py route..."
# Update the home route to use the new template
sed -i "s/return render_template('index.html'/return render_template('space_adventure_map.html'/" app.py

echo "📝 Updating base.html to include new scripts..."
# Check if already included
if ! grep -q "space_adventure_enhanced.js" templates/base.html; then
    # Add before closing body tag
    sed -i '/<\/body>/i\    <script src="{{ url_for('"'"'static'"'"', filename='"'"'space_adventure_enhanced.js'"'"') }}"></script>' templates/base.html
fi

echo "🎮 Creating test script..."
cat > test_ftl_enhancements.sh << 'EOF'
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
EOF

chmod +x test_ftl_enhancements.sh

echo "🎯 Creating mobile optimization script..."
cat > optimize_mobile.sh << 'EOF'
#!/bin/bash
echo "📱 Mobile Optimization for CloudQuest FTL"
echo "========================================"

# Optimize images for mobile
if command -v convert &> /dev/null; then
    echo "🖼️ Optimizing mascot images for mobile..."
    for img in static/mascot/*.png; do
        if [[ -f "$img" ]]; then
            filename=$(basename "$img" .png)
            convert "$img" -resize 256x256 -quality 85 "static/mascot/${filename}_mobile.png"
        fi
    done
    echo "✅ Mobile-optimized images created"
else
    echo "⚠️ ImageMagick not found - skipping image optimization"
fi

# Create mobile-specific CSS optimizations
cat >> static/ftl_style_sectors.css << 'CSS'

/* Additional mobile optimizations */
@media (max-width: 480px) {
    .galaxy-sectors {
        gap: 20px;
        padding: 10px;
    }
    
    .service-sector {
        padding: 15px;
        min-height: 160px;
    }
    
    .sector-title {
        font-size: 1.1rem;
    }
    
    .lesson-beacon {
        width: 45px;
        height: 45px;
        font-size: 12px;
    }
    
    .connection-path {
        height: 2px;
    }
}

/* High DPI display optimizations */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
    .lesson-beacon {
        border: 0.5px solid rgba(255, 255, 255, 0.1);
    }
    
    .sector-icon {
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
}
CSS

echo "✅ Mobile optimizations added"
echo ""
echo "📱 Test on mobile:"
echo "• Use browser dev tools"
echo "• Set to mobile viewport"
echo "• Check touch interactions"
echo "• Verify single-column layout"
EOF

chmod +x optimize_mobile.sh

echo "📋 Creating README for new features..."
cat > FTL_ENHANCEMENTS.md << 'EOF'
# 🌌 CloudQuest RPG - FTL-Style Enhancements

## ✨ New Features

### 🗺️ Sector-Based Map
- **6 AWS service sectors** (Compute, Storage, Security, Network, Database, DevOps)
- **FTL-inspired layout** with interconnected sectors
- **Animated connection paths** showing data flow between sectors

### 🎮 Enhanced UI Animations
- **Smooth hover effects** with scale and glow
- **Ripple interactions** on lesson clicks
- **Sector unlock animations** with rotation and scaling
- **Progress bar shimmer effects**
- **Dynamic starfield background**

### 📱 Mobile Optimizations
- **Responsive grid** (3→2→1 columns)
- **Touch-friendly buttons** (larger tap targets)
- **Optimized animations** for mobile performance
- **Reduced particle count** on smaller screens

### ⌨️ Accessibility
- **Keyboard navigation** with arrow keys
- **Focus indicators** for all interactive elements
- **Screen reader friendly** with proper ARIA labels
- **High contrast mode** support

### 🎵 Audio Integration
- **UI sound effects** for interactions
- **Hover, click, and error sounds**
- **Audio toggle** in settings

## 🚀 Files Added/Modified

- `static/ftl_style_sectors.css` - FTL-style sector CSS
- `static/space_adventure_enhanced.js` - Enhanced interactions
- `templates/space_adventure_map.html` - New sector-based template
- `templates/base.html` - Updated to include new scripts

## 🧪 Testing

Run the test script:
```bash
./test_ftl_enhancements.sh
```

For mobile optimization:
```bash
./optimize_mobile.sh
```

## 🎮 New User Experience

1. **Sector Overview** - See all AWS domains at a glance
2. **Visual Progress** - Animated progress bars per sector
3. **Smooth Navigation** - Fluid transitions between lessons
4. **Interactive Feedback** - Immediate visual/audio feedback
5. **Mobile-First** - Optimized for phone and tablet use

## 🔧 Customization

### Colors
Edit CSS variables in `ftl_style_sectors.css`:
- `--primary-glow`: Main accent color
- `--sector-bg`: Sector background opacity
- `--connection-color`: Path connection colors

### Animations
Modify timing in `space_adventure_enhanced.js`:
- `animationDuration`: Speed of effects
- `particleCount`: Number of background particles
- `rippleIntensity`: Interaction feedback strength

### Layout
Adjust grid in CSS:
- `.galaxy-sectors`: Change column count
- `gap`: Spacing between sectors
- `.service-sector`: Individual sector styling

## 📊 Performance

- **Optimized animations** using `transform` and `opacity`
- **Efficient particle system** with requestAnimationFrame
- **Lazy loading** for non-critical effects
- **Mobile-specific** reduced animation complexity

Enjoy exploring the enhanced CloudQuest galaxy! 🌌⚡🎮
EOF

echo ""
echo "🎉 FTL-Style Enhancements Deployment Complete!"
echo "=============================================="
echo ""
echo "📂 Files deployed:"
echo "• static/ftl_style_sectors.css"
echo "• static/space_adventure_enhanced.js" 
echo "• templates/space_adventure_map.html"
echo "• templates/base.html (updated)"
echo ""
echo "🧪 Test your enhancements:"
echo "./test_ftl_enhancements.sh"
echo ""
echo "📱 Optimize for mobile:"
echo "./optimize_mobile.sh"
echo ""
echo "🚀 Quick start:"
echo "python app.py"
echo "Visit: http://localhost:5001"
echo ""
echo "🌟 NEW FEATURES:"
echo "• FTL-style sector-based map"
echo "• Smooth animated UI interactions"  
echo "• Dynamic starfield background"
echo "• Responsive mobile design"
echo "• Enhanced audio feedback"
echo "• Keyboard navigation support"
echo ""
echo "Ready to explore the enhanced CloudQuest galaxy! 🌌⚡"