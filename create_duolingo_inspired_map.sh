#!/bin/bash
# 🎮 create_duolingo_inspired_map.sh - True Duolingo-style map with sci-fi lofi theme

echo "🎮 CloudQuest RPG - Duolingo-Inspired Sci-Fi Map"
echo "==============================================="

echo "🗺️ Creating authentic Duolingo-style map with sci-fi theme..."

cat > templates/space_adventure_map.html << 'EOF'
{% extends "base.html" %}

{% block title %}Space Adventure Map - CloudQuest RPG{% endblock %}

{% block head %}
<style>
/* Duolingo-Inspired Sci-Fi Learning Map */
.duolingo-map-container {
    background: linear-gradient(180deg, 
        #0d1421 0%, 
        #1a1b3e 25%, 
        #2d1b69 50%, 
        #1a1b3e 75%, 
        #0d1421 100%
    );
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
    overflow-y: auto;
}

/* Animated background elements */
.space-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
}

.floating-particle {
    position: absolute;
    background: rgba(100, 200, 255, 0.3);
    border-radius: 50%;
    animation: float 8s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
    50% { transform: translateY(-20px) rotate(180deg); opacity: 0.8; }
}

/* Main learning path */
.learning-path {
    position: relative;
    z-index: 1;
    max-width: 500px;
    margin: 0 auto;
    padding: 60px 20px 100px 20px;
}

/* Map header */
.map-header {
    text-align: center;
    margin-bottom: 50px;
    padding: 20px;
    background: rgba(13, 20, 33, 0.8);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(100, 200, 255, 0.2);
}

.map-title {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #64c8ff, #a855f7, #06d6a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 10px;
    text-shadow: 0 0 20px rgba(100, 200, 255, 0.3);
}

.map-subtitle {
    color: #94a3b8;
    font-size: 1rem;
    font-weight: 500;
}

/* Duolingo-style connecting path */
.main-path {
    position: absolute;
    left: 50%;
    top: 200px;
    bottom: 0;
    width: 6px;
    background: linear-gradient(to bottom,
        #64c8ff 0%,
        #a855f7 25%,
        #06d6a0 50%,
        #f59e0b 75%,
        #ef4444 100%
    );
    border-radius: 3px;
    transform: translateX(-50%);
    opacity: 0.6;
    box-shadow: 0 0 10px rgba(100, 200, 255, 0.3);
}

/* Lesson units (like Duolingo sections) */
.lesson-unit {
    position: relative;
    margin: 0 auto 80px auto;
    z-index: 2;
}

/* Unit header */
.unit-header {
    text-align: center;
    margin-bottom: 30px;
}

.unit-title {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(13, 20, 33, 0.9);
    color: #64c8ff;
    font-size: 1.2rem;
    font-weight: 700;
    padding: 12px 20px;
    border-radius: 25px;
    border: 2px solid rgba(100, 200, 255, 0.3);
    backdrop-filter: blur(10px);
    box-shadow: 
        0 4px 12px rgba(0, 0, 0, 0.3),
        0 0 20px rgba(100, 200, 255, 0.1);
    transition: all 0.3s ease;
}

.unit-title:hover {
    border-color: rgba(100, 200, 255, 0.6);
    box-shadow: 
        0 6px 16px rgba(0, 0, 0, 0.4),
        0 0 30px rgba(100, 200, 255, 0.2);
    transform: translateY(-2px);
}

.unit-icon {
    font-size: 1.5rem;
    filter: drop-shadow(0 0 8px rgba(100, 200, 255, 0.5));
}

/* Lessons arranged in Duolingo's organic pattern */
.lessons-path {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;
}

.lesson-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    position: relative;
}

.lesson-row.offset-left {
    transform: translateX(-40px);
}

.lesson-row.offset-right {
    transform: translateX(40px);
}

/* Individual lesson circles (Duolingo style) */
.lesson-circle {
    width: 85px;
    height: 85px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 18px;
    text-decoration: none;
    position: relative;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    border: 4px solid transparent;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
    z-index: 3;
}

/* Lesson states with sci-fi colors */
.lesson-circle.completed {
    background: linear-gradient(135deg, #06d6a0, #059669);
    color: white;
    border-color: rgba(6, 214, 160, 0.4);
    box-shadow: 
        0 6px 16px rgba(6, 214, 160, 0.3),
        0 0 25px rgba(6, 214, 160, 0.2),
        inset 0 2px 0 rgba(255, 255, 255, 0.2);
}

.lesson-circle.completed::after {
    content: '✓';
    position: absolute;
    font-size: 28px;
    font-weight: 900;
    color: white;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    animation: completedGlow 2s ease-in-out infinite;
}

@keyframes completedGlow {
    0%, 100% { text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3); }
    50% { text-shadow: 0 0 15px rgba(255, 255, 255, 0.8); }
}

.lesson-circle.current {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
    border-color: rgba(245, 158, 11, 0.5);
    animation: currentPulse 2s ease-in-out infinite;
    box-shadow: 
        0 6px 16px rgba(245, 158, 11, 0.4),
        0 0 30px rgba(245, 158, 11, 0.3),
        inset 0 2px 0 rgba(255, 255, 255, 0.2);
}

@keyframes currentPulse {
    0%, 100% { 
        transform: scale(1);
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.4), 0 0 30px rgba(245, 158, 11, 0.3);
    }
    50% { 
        transform: scale(1.1);
        box-shadow: 0 8px 20px rgba(245, 158, 11, 0.6), 0 0 40px rgba(245, 158, 11, 0.5);
    }
}

.lesson-circle.available {
    background: linear-gradient(135deg, #64c8ff, #3b82f6);
    color: white;
    border-color: rgba(100, 200, 255, 0.4);
    box-shadow: 
        0 6px 16px rgba(100, 200, 255, 0.3),
        0 0 20px rgba(100, 200, 255, 0.2),
        inset 0 2px 0 rgba(255, 255, 255, 0.2);
}

.lesson-circle.locked {
    background: linear-gradient(135deg, #4b5563, #374151);
    color: #9ca3af;
    border-color: rgba(75, 85, 99, 0.3);
    cursor: not-allowed;
    opacity: 0.6;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.lesson-circle:hover:not(.locked) {
    transform: scale(1.15) translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
}

/* Connection lines between lessons */
.lesson-connection {
    position: absolute;
    height: 4px;
    background: linear-gradient(90deg, 
        rgba(100, 200, 255, 0.3), 
        rgba(100, 200, 255, 0.6), 
        rgba(100, 200, 255, 0.3)
    );
    border-radius: 2px;
    z-index: 1;
    animation: connectionFlow 3s ease-in-out infinite;
}

@keyframes connectionFlow {
    0%, 100% { 
        background-position: -100% 0;
        opacity: 0.4;
    }
    50% { 
        background-position: 100% 0;
        opacity: 0.8;
    }
}

/* Unit progress indicator */
.unit-progress {
    text-align: center;
    margin-top: 25px;
    padding: 15px;
    background: rgba(13, 20, 33, 0.7);
    border-radius: 15px;
    border: 1px solid rgba(100, 200, 255, 0.2);
    backdrop-filter: blur(5px);
}

.progress-bar {
    height: 8px;
    background: rgba(75, 85, 99, 0.5);
    border-radius: 4px;
    overflow: hidden;
    margin: 10px 0;
    position: relative;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #64c8ff, #06d6a0);
    border-radius: 4px;
    transition: width 1s ease-out;
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
        rgba(255, 255, 255, 0.4), 
        transparent
    );
    animation: progressShine 2s infinite;
}

@keyframes progressShine {
    0% { left: -100%; }
    100% { left: 100%; }
}

.progress-text {
    color: #94a3b8;
    font-size: 0.9rem;
    font-weight: 600;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .learning-path {
        max-width: 100%;
        padding: 40px 15px 80px 15px;
    }
    
    .map-title {
        font-size: 2rem;
    }
    
    .lesson-circle {
        width: 75px;
        height: 75px;
        font-size: 16px;
    }
    
    .lesson-row {
        gap: 15px;
    }
    
    .lesson-row.offset-left {
        transform: translateX(-25px);
    }
    
    .lesson-row.offset-right {
        transform: translateX(25px);
    }
}

@media (max-width: 480px) {
    .lesson-circle {
        width: 65px;
        height: 65px;
        font-size: 14px;
    }
    
    .lesson-row {
        gap: 12px;
    }
    
    .lesson-row.offset-left {
        transform: translateX(-15px);
    }
    
    .lesson-row.offset-right {
        transform: translateX(15px);
    }
}

/* Entrance animations */
.lesson-unit {
    opacity: 0;
    transform: translateY(30px);
    animation: unitEnter 0.6s ease-out forwards;
}

.lesson-unit:nth-child(2) { animation-delay: 0.1s; }
.lesson-unit:nth-child(3) { animation-delay: 0.2s; }
.lesson-unit:nth-child(4) { animation-delay: 0.3s; }
.lesson-unit:nth-child(5) { animation-delay: 0.4s; }
.lesson-unit:nth-child(6) { animation-delay: 0.5s; }
.lesson-unit:nth-child(7) { animation-delay: 0.6s; }

@keyframes unitEnter {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
{% endblock %}

{% block content %}
<div class="duolingo-map-container">
    <!-- Animated background -->
    <div class="space-background" id="spaceBackground"></div>
    
    <div class="learning-path">
        <!-- Map header -->
        <div class="map-header">
            <h1 class="map-title">AWS Cloud Orbit</h1>
            <p class="map-subtitle">Master cloud computing through interconnected learning paths</p>
        </div>
        
        <!-- Main connecting path -->
        <div class="main-path"></div>
        
        <!-- Unit 1: Compute Sector -->
        <div class="lesson-unit">
            <div class="unit-header">
                <div class="unit-title">
                    <span class="unit-icon">⚡</span>
                    <span>Compute Sector</span>
                </div>
            </div>
            
            <div class="lessons-path">
                <div class="lesson-row">
                    <a href="/lesson/1" class="lesson-circle {% if progress.current_lesson > 1 %}completed{% elif progress.current_lesson == 1 %}current{% else %}available{% endif %}">1</a>
                    <div class="lesson-connection" style="width: 30px; top: 50%; left: 85px;"></div>
                </div>
                
                <div class="lesson-row offset-right">
                    <a href="/lesson/2" class="lesson-circle {% if progress.current_lesson > 2 %}completed{% elif progress.current_lesson == 2 %}current{% elif progress.current_lesson >= 1 %}available{% else %}locked{% endif %}">2</a>
                </div>
                
                <div class="lesson-row offset-left">
                    <a href="/lesson/3" class="lesson-circle {% if progress.current_lesson > 3 %}completed{% elif progress.current_lesson == 3 %}current{% elif progress.current_lesson >= 2 %}available{% else %}locked{% endif %}">3</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/4" class="lesson-circle {% if progress.current_lesson > 4 %}completed{% elif progress.current_lesson == 4 %}current{% elif progress.current_lesson >= 3 %}available{% else %}locked{% endif %}">4</a>
                </div>
            </div>
            
            <div class="unit-progress">
                {% set compute_completed = 0 %}
                {% for lesson in [1,2,3,4] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set compute_completed = compute_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ (compute_completed / 4 * 100) | round }}%"></div>
                </div>
                <div class="progress-text">{{ compute_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Unit 2: Storage Sector -->
        <div class="lesson-unit">
            <div class="unit-header">
                <div class="unit-title">
                    <span class="unit-icon">💾</span>
                    <span>Storage Sector</span>
                </div>
            </div>
            
            <div class="lessons-path">
                <div class="lesson-row">
                    <a href="/lesson/5" class="lesson-circle {% if progress.current_lesson > 5 %}completed{% elif progress.current_lesson == 5 %}current{% elif progress.current_lesson >= 4 %}available{% else %}locked{% endif %}">5</a>
                </div>
                
                <div class="lesson-row offset-left">
                    <a href="/lesson/6" class="lesson-circle {% if progress.current_lesson > 6 %}completed{% elif progress.current_lesson == 6 %}current{% elif progress.current_lesson >= 5 %}available{% else %}locked{% endif %}">6</a>
                </div>
                
                <div class="lesson-row offset-right">
                    <a href="/lesson/7" class="lesson-circle {% if progress.current_lesson > 7 %}completed{% elif progress.current_lesson == 7 %}current{% elif progress.current_lesson >= 6 %}available{% else %}locked{% endif %}">7</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/8" class="lesson-circle {% if progress.current_lesson > 8 %}completed{% elif progress.current_lesson == 8 %}current{% elif progress.current_lesson >= 7 %}available{% else %}locked{% endif %}">8</a>
                </div>
            </div>
            
            <div class="unit-progress">
                {% set storage_completed = 0 %}
                {% for lesson in [5,6,7,8] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set storage_completed = storage_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ (storage_completed / 4 * 100) | round }}%"></div>
                </div>
                <div class="progress-text">{{ storage_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Unit 3: Security Sector -->
        <div class="lesson-unit">
            <div class="unit-header">
                <div class="unit-title">
                    <span class="unit-icon">🛡️</span>
                    <span>Security Sector</span>
                </div>
            </div>
            
            <div class="lessons-path">
                <div class="lesson-row offset-right">
                    <a href="/lesson/9" class="lesson-circle {% if progress.current_lesson > 9 %}completed{% elif progress.current_lesson == 9 %}current{% elif progress.current_lesson >= 8 %}available{% else %}locked{% endif %}">9</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/10" class="lesson-circle {% if progress.current_lesson > 10 %}completed{% elif progress.current_lesson == 10 %}current{% elif progress.current_lesson >= 9 %}available{% else %}locked{% endif %}">10</a>
                </div>
                
                <div class="lesson-row offset-left">
                    <a href="/lesson/11" class="lesson-circle {% if progress.current_lesson > 11 %}completed{% elif progress.current_lesson == 11 %}current{% elif progress.current_lesson >= 10 %}available{% else %}locked{% endif %}">11</a>
                </div>
                
                <div class="lesson-row offset-right">
                    <a href="/lesson/12" class="lesson-circle {% if progress.current_lesson > 12 %}completed{% elif progress.current_lesson == 12 %}current{% elif progress.current_lesson >= 11 %}available{% else %}locked{% endif %}">12</a>
                </div>
            </div>
            
            <div class="unit-progress">
                {% set security_completed = 0 %}
                {% for lesson in [9,10,11,12] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set security_completed = security_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ (security_completed / 4 * 100) | round }}%"></div>
                </div>
                <div class="progress-text">{{ security_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Unit 4: Network Sector -->
        <div class="lesson-unit">
            <div class="unit-header">
                <div class="unit-title">
                    <span class="unit-icon">🌐</span>
                    <span>Network Sector</span>
                </div>
            </div>
            
            <div class="lessons-path">
                <div class="lesson-row">
                    <a href="/lesson/13" class="lesson-circle {% if progress.current_lesson > 13 %}completed{% elif progress.current_lesson == 13 %}current{% elif progress.current_lesson >= 12 %}available{% else %}locked{% endif %}">13</a>
                </div>
                
                <div class="lesson-row offset-right">
                    <a href="/lesson/14" class="lesson-circle {% if progress.current_lesson > 14 %}completed{% elif progress.current_lesson == 14 %}current{% elif progress.current_lesson >= 13 %}available{% else %}locked{% endif %}">14</a>
                </div>
                
                <div class="lesson-row offset-left">
                    <a href="/lesson/15" class="lesson-circle {% if progress.current_lesson > 15 %}completed{% elif progress.current_lesson == 15 %}current{% elif progress.current_lesson >= 14 %}available{% else %}locked{% endif %}">15</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/16" class="lesson-circle {% if progress.current_lesson > 16 %}completed{% elif progress.current_lesson == 16 %}current{% elif progress.current_lesson >= 15 %}available{% else %}locked{% endif %}">16</a>
                </div>
            </div>
            
            <div class="unit-progress">
                {% set network_completed = 0 %}
                {% for lesson in [13,14,15,16] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set network_completed = network_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ (network_completed / 4 * 100) | round }}%"></div>
                </div>
                <div class="progress-text">{{ network_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Unit 5: Database Sector -->
        <div class="lesson-unit">
            <div class="unit-header">
                <div class="unit-title">
                    <span class="unit-icon">🗄️</span>
                    <span>Database Sector</span>
                </div>
            </div>
            
            <div class="lessons-path">
                <div class="lesson-row offset-left">
                    <a href="/lesson/17" class="lesson-circle {% if progress.current_lesson > 17 %}completed{% elif progress.current_lesson == 17 %}current{% elif progress.current_lesson >= 16 %}available{% else %}locked{% endif %}">17</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/18" class="lesson-circle {% if progress.current_lesson > 18 %}completed{% elif progress.current_lesson == 18 %}current{% elif progress.current_lesson >= 17 %}available{% else %}locked{% endif %}">18</a>
                </div>
                
                <div class="lesson-row offset-right">
                    <a href="/lesson/19" class="lesson-circle {% if progress.current_lesson > 19 %}completed{% elif progress.current_lesson == 19 %}current{% elif progress.current_lesson >= 18 %}available{% else %}locked{% endif %}">19</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/20" class="lesson-circle {% if progress.current_lesson > 20 %}completed{% elif progress.current_lesson == 20 %}current{% elif progress.current_lesson >= 19 %}available{% else %}locked{% endif %}">20</a>
                </div>
            </div>
            
            <div class="unit-progress">
                {% set database_completed = 0 %}
                {% for lesson in [17,18,19,20] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set database_completed = database_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ (database_completed / 4 * 100) | round }}%"></div>
                </div>
                <div class="progress-text">{{ database_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Unit 6: DevOps Sector -->
        <div class="lesson-unit">
            <div class="unit-header">
                <div class="unit-title">
                    <span class="unit-icon">🚀</span>
                    <span>DevOps Sector</span>
                </div>
            </div>
            
            <div class="lessons-path">
                <div class="lesson-row">
                    <a href="/lesson/21" class="lesson-circle {% if progress.current_lesson > 21 %}completed{% elif progress.current_lesson == 21 %}current{% elif progress.current_lesson >= 20 %}available{% else %}locked{% endif %}">21</a>
                </div>
                
                <div class="lesson-row offset-left">
                    <a href="/lesson/22" class="lesson-circle {% if progress.current_lesson > 22 %}completed{% elif progress.current_lesson == 22 %}current{% elif progress.current_lesson >= 21 %}available{% else %}locked{% endif %}">22</a>
                </div>
                
                <div class="lesson-row offset-right">
                    <a href="/lesson/23" class="lesson-circle {% if progress.current_lesson > 23 %}completed{% elif progress.current_lesson == 23 %}current{% elif progress.current_lesson >= 22 %}available{% else %}locked{% endif %}">23</a>
                </div>
                
                <div class="lesson-row">
                    <a href="/lesson/24" class="lesson-circle {% if progress.current_lesson > 24 %}completed{% elif progress.current_lesson == 24 %}current{% elif progress.current_lesson >= 23 %}available{% else %}locked{% endif %}">24</a>
                </div>
            </div>
            
            <div class="unit-progress">
                {% set devops_completed = 0 %}
                {% for lesson in [21,22,23,24] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set devops_completed = devops_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ (devops_completed / 4 * 100) | round }}%"></div>
                </div>
                <div class="progress-text">{{ devops_completed }}/4 Complete</div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Create floating background particles
    function createSpaceBackground() {
        const background = document.getElementById('spaceBackground');
        const particleCount = 20;
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'floating-particle';
            
            const size = Math.random() * 4 + 2;
            particle.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation-delay: ${Math.random() * 8}s;
                animation-duration: ${Math.random() * 6 + 6}s;
            `;
            
            background.appendChild(particle);
        }
    }
    
    // Enhanced lesson interactions
    const lessonCircles = document.querySelectorAll('.lesson-circle');
    lessonCircles.forEach(circle => {
        if (!circle.classList.contains('locked')) {
            circle.addEventListener('click', function(e) {
                createClickEffect(this);
                
                // Play sound if available
                if (window.awsOrbitAudio && window.awsOrbitAudio.playClick) {
                    window.awsOrbitAudio.playClick();
                }
            });
            
            circle.addEventListener('mouseenter', function() {
                // Subtle hover feedback
                this.style.filter = 'brightness(1.1)';
                
                if (window.awsOrbitAudio && window.awsOrbitAudio.playClick) {
                    setTimeout(() => window.awsOrbitAudio.playClick(), 0);
                }
            });
            
            circle.addEventListener('mouseleave', function() {
                this.style.filter = '';
            });
        } else {
            circle.addEventListener('click', function(e) {
                e.preventDefault();
                createDeniedEffect(this);
                
                if (window.awsOrbitAudio && window.awsOrbitAudio.playWrong) {
                    window.awsOrbitAudio.playWrong();
                }
            });
        }
    });
    
    function createClickEffect(element) {
        const ripple = document.createElement('div');
        ripple.style.cssText = `
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: translate(-50%, -50%);
            animation: clickRipple 0.6s ease-out;
            pointer-events: none;
            z-index: 10;
        `;
        
        element.style.position = 'relative';
        element.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    }
    
    function createDeniedEffect(element) {
        element.style.animation = 'none';
        element.offsetHeight; // Force reflow
        element.style.animation = 'denyShake 0.4s ease-in-out';
        
        setTimeout(() => {
            element.style.animation = '';
        }, 400);
    }
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes clickRipple {
            to {
                width: 150px;
                height: 150px;
                opacity: 0;
            }
        }
        
        @keyframes denyShake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-6px); }
            75% { transform: translateX(6px); }
        }
    `;
    document.head.appendChild(style);
    
    // Initialize background
    createSpaceBackground();
    
    console.log('🎮 Duolingo-Style Sci-Fi Map - Ready for exploration!');
});
</script>
{% endblock %}
EOF

echo "✅ Duolingo-style sci-fi map created!"

echo ""
echo "🎮 Authentic Duolingo-Style Map Complete!"
echo "========================================"
echo ""
echo "🌌 DUOLINGO-INSPIRED FEATURES:"
echo "• Vertical learning path with central connection line"
echo "• Circular lesson nodes in organic zigzag pattern"
echo "• Unit headers with icons (like Duolingo sections)"
echo "• Progress bars for each unit"
echo "• Offset lesson rows (left/right) for natural flow"
echo "• Mobile-optimized responsive design"
echo ""
echo "🔮 SCI-FI LOFI THEME:"
echo "• Space gradient backgrounds (deep blues/purples)"
echo "• Floating particle animations"
echo "• Neon glow effects and borders"
echo "• Cyberpunk color scheme (cyan, purple, green)"
echo "• Backdrop blur glass morphism"
echo "• Smooth entrance animations"
echo ""
echo "🚀 Test it now:"
echo "python app.py"
echo "Visit: http://localhost:5001"