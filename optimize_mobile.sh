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
