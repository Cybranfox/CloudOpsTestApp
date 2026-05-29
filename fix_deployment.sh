#!/bin/bash
# 🔧 fix_deployment.sh - Fix file paths and complete FTL deployment

echo "🔧 CloudQuest RPG - Fix FTL Enhancement Deployment"
echo "=================================================="

# Check we're in the right directory
if [[ ! -f "app.py" ]]; then
    echo "❌ Error: Run from AWS_Orbit_RPG directory"
    exit 1
fi

echo "📁 Using correct filenames..."

# Copy files with correct names
if [[ -f "templates/enhanced_space_adventure_map.html" ]]; then
    echo "🗺️ Deploying enhanced space adventure map..."
    cp templates/enhanced_space_adventure_map.html templates/space_adventure_map.html
    echo "✅ Enhanced map template deployed"
else
    echo "❌ Enhanced map template not found"
fi

# Check if the CSS and JS files exist in static
if [[ -f "static/ftl_style_sectors.css" ]]; then
    echo "✅ FTL CSS already in place"
else
    echo "❌ FTL CSS missing from static/"
fi

if [[ -f "static/space_adventure_enhanced.js" ]]; then
    echo "✅ Enhanced JavaScript already in place"
else
    echo "❌ Enhanced JavaScript missing from static/"
fi

echo "🔧 Updating app.py home route..."
# Update the home route to use the space adventure map
if grep -q "return render_template('index.html'" app.py; then
    sed -i "s/return render_template('index.html'/return render_template('space_adventure_map.html'/" app.py
    echo "✅ Updated app.py home route"
else
    echo "ℹ️ App.py route already updated or different format"
fi

echo "📝 Checking base.html for script inclusion..."
if ! grep -q "space_adventure_enhanced.js" templates/base.html; then
    # Add before closing body tag
    sed -i '/<\/body>/i\    <script src="{{ url_for('"'"'static'"'"', filename='"'"'space_adventure_enhanced.js'"'"') }}"></script>' templates/base.html
    echo "✅ Added enhanced script to base.html"
else
    echo "✅ Enhanced script already in base.html"
fi

echo "🎮 Testing deployment..."
echo ""
echo "🔍 File verification:"
echo "====================="

files_ok=0
total_files=3

if [[ -f "templates/space_adventure_map.html" ]]; then
    echo "✅ Enhanced space map template"
    ((files_ok++))
else
    echo "❌ Enhanced space map template missing"
fi

if [[ -f "static/ftl_style_sectors.css" ]]; then
    echo "✅ FTL style CSS"
    ((files_ok++))
else
    echo "❌ FTL style CSS missing"
fi

if [[ -f "static/space_adventure_enhanced.js" ]]; then
    echo "✅ Enhanced JavaScript"
    ((files_ok++))
else
    echo "❌ Enhanced JavaScript missing"
fi

echo ""
echo "📊 Deployment Status: $files_ok/$total_files files ready"

if [[ $files_ok -eq $total_files ]]; then
    echo "🎉 FTL Enhancement deployment complete!"
    echo ""
    echo "🚀 Quick Test:"
    echo "python app.py"
    echo "Visit: http://localhost:5001"
    echo ""
    echo "🔍 What to look for:"
    echo "• Sector-based map layout (instead of linear)"
    echo "• Smooth hover animations on sectors" 
    echo "• Animated starfield background"
    echo "• Progress bars with shimmer effects"
    echo "• Ripple effects on lesson clicks"
else
    echo "⚠️ Some files are missing. Let me create them..."
    
    # Create missing CSS if needed
    if [[ ! -f "static/ftl_style_sectors.css" ]]; then
        echo "🎨 Creating FTL style CSS..."
        cat > static/ftl_style_sectors.css << 'EOF'
/* Enhanced Space Adventure Map - FTL-Style Sectors */
.space-adventure-container {
    background: radial-gradient(ellipse at center, #1a1a2e 0%, #16213e 35%, #0f0f23 100%);
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

.galaxy-sectors {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 60px;
    padding: 40px;
    position: relative;
    z-index: 1;
}

.service-sector {
    position: relative;
    background: rgba(13, 27, 42, 0.85);
    border: 2px solid rgba(50, 184, 198, 0.3);
    border-radius: 20px;
    padding: 25px;
    min-height: 250px;
    backdrop-filter: blur(15px);
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    cursor: pointer;
    overflow: hidden;
}

.service-sector:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: rgba(50, 184, 198, 0.8);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 30px rgba(50, 184, 198, 0.2);
}

.sector-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
}

.sector-icon {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    background: linear-gradient(135deg, #32b8c6, #1a8a96);
    transition: all 0.3s ease;
}

.sector-title {
    color: #32b8c6;
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 0 0 15px rgba(50, 184, 198, 0.4);
}

.lesson-beacon {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 16px;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    margin: 8px;
}

.lesson-beacon.completed {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    box-shadow: 0 0 20px rgba(34, 197, 94, 0.5);
}

.lesson-beacon.current {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
    animation: currentPulse 2s ease-in-out infinite;
    box-shadow: 0 0 25px rgba(245, 158, 11, 0.6);
}

.lesson-beacon.available {
    background: linear-gradient(135deg, #32b8c6, #0891b2);
    color: white;
    box-shadow: 0 0 20px rgba(50, 184, 198, 0.4);
}

.lesson-beacon.locked {
    background: linear-gradient(135deg, #64748b, #475569);
    color: #94a3b8;
    cursor: not-allowed;
    opacity: 0.6;
}

.lesson-beacon:hover:not(.locked) {
    transform: scale(1.15) translateY(-5px);
    box-shadow: 0 10px 30px rgba(50, 184, 198, 0.4);
}

@keyframes currentPulse {
    0%, 100% { 
        transform: scale(1);
        box-shadow: 0 0 25px rgba(245, 158, 11, 0.6);
    }
    50% { 
        transform: scale(1.1);
        box-shadow: 0 0 35px rgba(245, 158, 11, 0.8);
    }
}

@media (max-width: 1200px) {
    .galaxy-sectors {
        grid-template-columns: repeat(2, 1fr);
        gap: 40px;
    }
}

@media (max-width: 768px) {
    .galaxy-sectors {
        grid-template-columns: 1fr;
        gap: 30px;
        padding: 20px;
    }
    
    .service-sector {
        min-height: 200px;
        padding: 20px;
    }
    
    .lesson-beacon {
        width: 60px;
        height: 60px;
        font-size: 14px;
    }
}
EOF
        echo "✅ FTL CSS created"
    fi
    
    # Create minimal JavaScript if needed
    if [[ ! -f "static/space_adventure_enhanced.js" ]]; then
        echo "✨ Creating enhanced JavaScript..."
        cat > static/space_adventure_enhanced.js << 'EOF'
// Enhanced Space Adventure Map - Basic Interactions
document.addEventListener('DOMContentLoaded', function() {
    console.log('🌌 Space Adventure Map Enhanced - Loading...');
    
    // Add ripple effects to lesson beacons
    const lessonBeacons = document.querySelectorAll('.lesson-beacon');
    
    lessonBeacons.forEach(beacon => {
        if (!beacon.classList.contains('locked')) {
            beacon.addEventListener('click', function(e) {
                createRippleEffect(this);
            });
        }
    });
    
    function createRippleEffect(element) {
        const ripple = document.createElement('div');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        
        ripple.style.cssText = `
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(50, 184, 198, 0.4);
            transform: translate(-50%, -50%);
            animation: rippleExpand 0.6s ease-out;
            pointer-events: none;
            z-index: 10;
        `;
        
        element.style.position = 'relative';
        element.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    }
    
    // Add CSS for ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes rippleExpand {
            to {
                width: 150px;
                height: 150px;
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    console.log('✅ Space Adventure Map Enhanced - Ready!');
});
EOF
        echo "✅ Enhanced JavaScript created"
    fi
    
    echo ""
    echo "🎉 Missing files created! Deployment now complete!"
fi

echo ""
echo "🚀 Ready to test your enhanced CloudQuest!"
echo "========================================="
echo "Run: python app.py"
echo "Visit: http://localhost:5001"