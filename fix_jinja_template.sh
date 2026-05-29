#!/bin/bash
# 🔧 fix_jinja_template.sh - Fix the intersect filter error

echo "🔧 Fixing Jinja2 Template Error"
echo "==============================="

echo "📝 Adding custom intersect filter to app.py..."

# Add the intersect filter function to app.py
if ! grep -q "def intersect_filter" app.py; then
    # Add the custom filter after the Flask app initialization
    sed -i '/app = Flask(__name__)/a\\n# Custom Jinja2 filters\ndef intersect_filter(list1, list2):\n    """Return intersection of two lists"""\n    return [item for item in list1 if item in list2]\n\n# Register the filter\napp.jinja_env.filters['"'"'intersect'"'"'] = intersect_filter' app.py
    echo "✅ Added intersect filter to app.py"
else
    echo "✅ Intersect filter already exists in app.py"
fi

echo "🗺️ Creating fixed space adventure map template..."

# Create a fixed version of the template without the intersect filter
cat > templates/space_adventure_map.html << 'EOF'
{% extends "base.html" %}

{% block title %}Space Adventure Map - CloudQuest RPG{% endblock %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='ftl_style_sectors.css') }}">
<style>
/* Enhanced Space Adventure Map - FTL-Style */
.space-adventure-container {
    background: radial-gradient(ellipse at center, #1a1a2e 0%, #16213e 35%, #0f0f23 100%);
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

.starfield {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
}

.star {
    position: absolute;
    background: white;
    border-radius: 50%;
    animation: twinkle 3s ease-in-out infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.2); }
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
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.3),
        0 0 30px rgba(50, 184, 198, 0.2);
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

.sector-description {
    color: #94a3b8;
    font-size: 0.9rem;
    margin-top: 5px;
    line-height: 1.4;
}

.lesson-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
    gap: 12px;
    margin-top: 20px;
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
    position: relative;
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

.sector-progress {
    margin-top: 20px;
    background: rgba(0, 0, 0, 0.4);
    border-radius: 25px;
    padding: 4px;
    position: relative;
    overflow: hidden;
}

.progress-track {
    height: 12px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    background: rgba(100, 116, 139, 0.3);
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #32b8c6, #22c55e);
    border-radius: 20px;
    transition: width 1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    position: relative;
    overflow: hidden;
}

.progress-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, 
        transparent, 
        rgba(255,255,255,0.3), 
        transparent
    );
    animation: progressShimmer 2s infinite;
}

@keyframes progressShimmer {
    0% { left: -100%; }
    100% { left: 100%; }
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
    
    .sector-title {
        font-size: 1.2rem;
    }
}
</style>
{% endblock %}

{% block content %}
<div class="space-adventure-container">
    <div class="starfield" id="starfield"></div>

    <div class="galaxy-sectors">
        <!-- Compute Sector -->
        <div class="service-sector" data-sector="compute">
            <div class="sector-header">
                <div class="sector-icon">⚡</div>
                <div>
                    <h3 class="sector-title">Compute Sector</h3>
                    <p class="sector-description">Processing power across the galaxy</p>
                </div>
            </div>
            
            <div class="lesson-grid">
                <a href="/lesson/1" class="lesson-beacon {% if progress.current_lesson > 1 %}completed{% elif progress.current_lesson == 1 %}current{% else %}available{% endif %}">
                    1
                </a>
                <a href="/lesson/2" class="lesson-beacon {% if progress.current_lesson > 2 %}completed{% elif progress.current_lesson == 2 %}current{% elif progress.current_lesson >= 1 %}available{% else %}locked{% endif %}">
                    2
                </a>
                <a href="/lesson/3" class="lesson-beacon {% if progress.current_lesson > 3 %}completed{% elif progress.current_lesson == 3 %}current{% elif progress.current_lesson >= 2 %}available{% else %}locked{% endif %}">
                    3
                </a>
                <a href="/lesson/4" class="lesson-beacon {% if progress.current_lesson > 4 %}completed{% elif progress.current_lesson == 4 %}current{% elif progress.current_lesson >= 3 %}available{% else %}locked{% endif %}">
                    4
                </a>
            </div>
            
            <div class="sector-progress">
                <div class="progress-track">
                    {% set compute_completed = 0 %}
                    {% for lesson in [1,2,3,4] %}
                        {% if lesson in progress.completed_lessons %}
                            {% set compute_completed = compute_completed + 1 %}
                        {% endif %}
                    {% endfor %}
                    <div class="progress-fill" style="width: {{ (compute_completed / 4 * 100) | round }}%"></div>
                </div>
            </div>
        </div>

        <!-- Storage Sector -->
        <div class="service-sector" data-sector="storage">
            <div class="sector-header">
                <div class="sector-icon">💾</div>
                <div>
                    <h3 class="sector-title">Storage Sector</h3>
                    <p class="sector-description">Data repositories and archives</p>
                </div>
            </div>
            
            <div class="lesson-grid">
                <a href="/lesson/5" class="lesson-beacon {% if progress.current_lesson > 5 %}completed{% elif progress.current_lesson == 5 %}current{% elif progress.current_lesson >= 4 %}available{% else %}locked{% endif %}">
                    5
                </a>
                <a href="/lesson/6" class="lesson-beacon {% if progress.current_lesson > 6 %}completed{% elif progress.current_lesson == 6 %}current{% elif progress.current_lesson >= 5 %}available{% else %}locked{% endif %}">
                    6
                </a>
                <a href="/lesson/7" class="lesson-beacon {% if progress.current_lesson > 7 %}completed{% elif progress.current_lesson == 7 %}current{% elif progress.current_lesson >= 6 %}available{% else %}locked{% endif %}">
                    7
                </a>
                <a href="/lesson/8" class="lesson-beacon {% if progress.current_lesson > 8 %}completed{% elif progress.current_lesson == 8 %}current{% elif progress.current_lesson >= 7 %}available{% else %}locked{% endif %}">
                    8
                </a>
            </div>
            
            <div class="sector-progress">
                <div class="progress-track">
                    {% set storage_completed = 0 %}
                    {% for lesson in [5,6,7,8] %}
                        {% if lesson in progress.completed_lessons %}
                            {% set storage_completed = storage_completed + 1 %}
                        {% endif %}
                    {% endfor %}
                    <div class="progress-fill" style="width: {{ (storage_completed / 4 * 100) | round }}%"></div>
                </div>
            </div>
        </div>

        <!-- Security Sector -->
        <div class="service-sector" data-sector="security">
            <div class="sector-header">
                <div class="sector-icon">🛡️</div>
                <div>
                    <h3 class="sector-title">Security Sector</h3>
                    <p class="sector-description">Defensive systems and protocols</p>
                </div>
            </div>
            
            <div class="lesson-grid">
                <a href="/lesson/9" class="lesson-beacon {% if progress.current_lesson > 9 %}completed{% elif progress.current_lesson == 9 %}current{% elif progress.current_lesson >= 8 %}available{% else %}locked{% endif %}">
                    9
                </a>
                <a href="/lesson/10" class="lesson-beacon {% if progress.current_lesson > 10 %}completed{% elif progress.current_lesson == 10 %}current{% elif progress.current_lesson >= 9 %}available{% else %}locked{% endif %}">
                    10
                </a>
                <a href="/lesson/11" class="lesson-beacon {% if progress.current_lesson > 11 %}completed{% elif progress.current_lesson == 11 %}current{% elif progress.current_lesson >= 10 %}available{% else %}locked{% endif %}">
                    11
                </a>
                <a href="/lesson/12" class="lesson-beacon {% if progress.current_lesson > 12 %}completed{% elif progress.current_lesson == 12 %}current{% elif progress.current_lesson >= 11 %}available{% else %}locked{% endif %}">
                    12
                </a>
            </div>
            
            <div class="sector-progress">
                <div class="progress-track">
                    {% set security_completed = 0 %}
                    {% for lesson in [9,10,11,12] %}
                        {% if lesson in progress.completed_lessons %}
                            {% set security_completed = security_completed + 1 %}
                        {% endif %}
                    {% endfor %}
                    <div class="progress-fill" style="width: {{ (security_completed / 4 * 100) | round }}%"></div>
                </div>
            </div>
        </div>

        <!-- Networking Sector -->
        <div class="service-sector" data-sector="networking">
            <div class="sector-header">
                <div class="sector-icon">🌐</div>
                <div>
                    <h3 class="sector-title">Network Sector</h3>
                    <p class="sector-description">Communication and connectivity</p>
                </div>
            </div>
            
            <div class="lesson-grid">
                <a href="/lesson/13" class="lesson-beacon {% if progress.current_lesson > 13 %}completed{% elif progress.current_lesson == 13 %}current{% elif progress.current_lesson >= 12 %}available{% else %}locked{% endif %}">
                    13
                </a>
                <a href="/lesson/14" class="lesson-beacon {% if progress.current_lesson > 14 %}completed{% elif progress.current_lesson == 14 %}current{% elif progress.current_lesson >= 13 %}available{% else %}locked{% endif %}">
                    14
                </a>
                <a href="/lesson/15" class="lesson-beacon {% if progress.current_lesson > 15 %}completed{% elif progress.current_lesson == 15 %}current{% elif progress.current_lesson >= 14 %}available{% else %}locked{% endif %}">
                    15
                </a>
                <a href="/lesson/16" class="lesson-beacon {% if progress.current_lesson > 16 %}completed{% elif progress.current_lesson == 16 %}current{% elif progress.current_lesson >= 15 %}available{% else %}locked{% endif %}">
                    16
                </a>
            </div>
            
            <div class="sector-progress">
                <div class="progress-track">
                    {% set networking_completed = 0 %}
                    {% for lesson in [13,14,15,16] %}
                        {% if lesson in progress.completed_lessons %}
                            {% set networking_completed = networking_completed + 1 %}
                        {% endif %}
                    {% endfor %}
                    <div class="progress-fill" style="width: {{ (networking_completed / 4 * 100) | round }}%"></div>
                </div>
            </div>
        </div>

        <!-- Database Sector -->
        <div class="service-sector" data-sector="database">
            <div class="sector-header">
                <div class="sector-icon">🗄️</div>
                <div>
                    <h3 class="sector-title">Database Sector</h3>
                    <p class="sector-description">Information management systems</p>
                </div>
            </div>
            
            <div class="lesson-grid">
                <a href="/lesson/17" class="lesson-beacon {% if progress.current_lesson > 17 %}completed{% elif progress.current_lesson == 17 %}current{% elif progress.current_lesson >= 16 %}available{% else %}locked{% endif %}">
                    17
                </a>
                <a href="/lesson/18" class="lesson-beacon {% if progress.current_lesson > 18 %}completed{% elif progress.current_lesson == 18 %}current{% elif progress.current_lesson >= 17 %}available{% else %}locked{% endif %}">
                    18
                </a>
                <a href="/lesson/19" class="lesson-beacon {% if progress.current_lesson > 19 %}completed{% elif progress.current_lesson == 19 %}current{% elif progress.current_lesson >= 18 %}available{% else %}locked{% endif %}">
                    19
                </a>
                <a href="/lesson/20" class="lesson-beacon {% if progress.current_lesson > 20 %}completed{% elif progress.current_lesson == 20 %}current{% elif progress.current_lesson >= 19 %}available{% else %}locked{% endif %}">
                    20
                </a>
            </div>
            
            <div class="sector-progress">
                <div class="progress-track">
                    {% set database_completed = 0 %}
                    {% for lesson in [17,18,19,20] %}
                        {% if lesson in progress.completed_lessons %}
                            {% set database_completed = database_completed + 1 %}
                        {% endif %}
                    {% endfor %}
                    <div class="progress-fill" style="width: {{ (database_completed / 4 * 100) | round }}%"></div>
                </div>
            </div>
        </div>

        <!-- DevOps Sector -->
        <div class="service-sector" data-sector="devops">
            <div class="sector-header">
                <div class="sector-icon">🚀</div>
                <div>
                    <h3 class="sector-title">DevOps Sector</h3>
                    <p class="sector-description">Automation and deployment</p>
                </div>
            </div>
            
            <div class="lesson-grid">
                <a href="/lesson/21" class="lesson-beacon {% if progress.current_lesson > 21 %}completed{% elif progress.current_lesson == 21 %}current{% elif progress.current_lesson >= 20 %}available{% else %}locked{% endif %}">
                    21
                </a>
                <a href="/lesson/22" class="lesson-beacon {% if progress.current_lesson > 22 %}completed{% elif progress.current_lesson == 22 %}current{% elif progress.current_lesson >= 21 %}available{% else %}locked{% endif %}">
                    22
                </a>
                <a href="/lesson/23" class="lesson-beacon {% if progress.current_lesson > 23 %}completed{% elif progress.current_lesson == 23 %}current{% elif progress.current_lesson >= 22 %}available{% else %}locked{% endif %}">
                    23
                </a>
                <a href="/lesson/24" class="lesson-beacon {% if progress.current_lesson > 24 %}completed{% elif progress.current_lesson == 24 %}current{% elif progress.current_lesson >= 23 %}available{% else %}locked{% endif %}">
                    24
                </a>
            </div>
            
            <div class="sector-progress">
                <div class="progress-track">
                    {% set devops_completed = 0 %}
                    {% for lesson in [21,22,23,24] %}
                        {% if lesson in progress.completed_lessons %}
                            {% set devops_completed = devops_completed + 1 %}
                        {% endif %}
                    {% endfor %}
                    <div class="progress-fill" style="width: {{ (devops_completed / 4 * 100) | round }}%"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Generate animated starfield
    function createStarfield() {
        const starfield = document.getElementById('starfield');
        const starCount = 100;
        
        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.width = star.style.height = Math.random() * 3 + 1 + 'px';
            star.style.animationDelay = Math.random() * 3 + 's';
            star.style.animationDuration = (Math.random() * 3 + 2) + 's';
            
            starfield.appendChild(star);
        }
    }
    
    // Enhanced lesson beacon interactions
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
    
    // Initialize starfield
    createStarfield();
    
    console.log('🌌 Space Adventure Map Enhanced - Ready for exploration!');
});
</script>
{% endblock %}
EOF

echo "✅ Fixed space adventure map template created"

echo ""
echo "🎉 Jinja2 Template Error Fixed!"
echo "==============================="
echo ""
echo "✅ Custom intersect filter added to app.py"
echo "✅ Fixed space adventure map template created"  
echo "✅ Removed problematic intersect filter usage"
echo ""
echo "🚀 Ready to test:"
echo "python app.py"
echo "Visit: http://localhost:5001"