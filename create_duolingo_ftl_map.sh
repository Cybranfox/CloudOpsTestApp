#!/bin/bash
# 🎮 create_duolingo_ftl_map.sh - Create proper Duolingo-style map with FTL inspiration

echo "🎮 CloudQuest RPG - Duolingo-Style FTL Map"
echo "========================================="

echo "🗺️ Creating Duolingo-inspired space adventure map..."

cat > templates/space_adventure_map.html << 'EOF'
{% extends "base.html" %}

{% block title %}Space Adventure Map - CloudQuest RPG{% endblock %}

{% block head %}
<style>
/* Duolingo-Inspired Space Adventure Map with FTL Connections */
.space-map-container {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
    min-height: 100vh;
    padding: 20px;
    position: relative;
    overflow-x: auto;
    overflow-y: auto;
}

/* Animated background stars */
.stars-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.star {
    position: absolute;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    animation: twinkle 3s ease-in-out infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.1); }
}

/* Main learning path container */
.learning-path {
    max-width: 800px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    padding: 40px 20px;
}

/* Path connection line (like Duolingo) */
.path-line {
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    width: 8px;
    height: 100%;
    background: linear-gradient(to bottom,
        rgba(50, 184, 198, 0.6) 0%,
        rgba(138, 43, 226, 0.4) 50%,
        rgba(245, 158, 11, 0.6) 100%
    );
    border-radius: 4px;
    box-shadow: 0 0 20px rgba(50, 184, 198, 0.3);
    animation: pathGlow 4s ease-in-out infinite;
}

@keyframes pathGlow {
    0%, 100% { 
        box-shadow: 0 0 20px rgba(50, 184, 198, 0.3);
        background-position: 0% 0%;
    }
    50% { 
        box-shadow: 0 0 30px rgba(50, 184, 198, 0.6);
        background-position: 0% 100%;
    }
}

/* Sector units (like Duolingo units) */
.sector-unit {
    background: rgba(13, 27, 42, 0.95);
    border: 3px solid rgba(50, 184, 198, 0.4);
    border-radius: 24px;
    margin: 60px 0;
    padding: 30px;
    position: relative;
    backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    box-shadow: 
        0 10px 30px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.sector-unit:hover {
    transform: translateY(-5px) scale(1.02);
    border-color: rgba(50, 184, 198, 0.8);
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.4),
        0 0 40px rgba(50, 184, 198, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

/* Sector header */
.sector-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 25px;
    position: relative;
}

.sector-icon {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #32b8c6, #1a8a96);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    position: relative;
    box-shadow: 
        0 8px 16px rgba(50, 184, 198, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    transition: all 0.3s ease;
}

.sector-icon::before {
    content: '';
    position: absolute;
    top: -3px;
    left: -3px;
    right: -3px;
    bottom: -3px;
    background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    border-radius: 50%;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.sector-unit:hover .sector-icon::before {
    opacity: 1;
    animation: iconShine 0.8s ease-out;
}

@keyframes iconShine {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.sector-info h3 {
    color: #32b8c6;
    font-size: 1.8rem;
    font-weight: 800;
    margin: 0 0 8px 0;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.sector-description {
    color: #94a3b8;
    font-size: 1rem;
    margin: 0;
    font-weight: 500;
}

/* Lesson grid (Duolingo-style circular lessons) */
.lessons-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 25px;
    position: relative;
}

/* Individual lesson nodes */
.lesson-node {
    width: 80px;
    height: 80px;
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
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* Lesson states with Duolingo-inspired colors */
.lesson-node.completed {
    background: linear-gradient(135deg, #58cc02, #4caf50);
    color: white;
    border-color: rgba(88, 204, 2, 0.3);
    box-shadow: 
        0 4px 12px rgba(88, 204, 2, 0.4),
        0 0 20px rgba(88, 204, 2, 0.2);
}

.lesson-node.completed::after {
    content: '✓';
    position: absolute;
    font-size: 24px;
    font-weight: 900;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.lesson-node.current {
    background: linear-gradient(135deg, #ff9600, #ff7b00);
    color: white;
    border-color: rgba(255, 150, 0, 0.4);
    animation: currentLessonPulse 2s ease-in-out infinite;
    box-shadow: 
        0 4px 12px rgba(255, 150, 0, 0.4),
        0 0 25px rgba(255, 150, 0, 0.3);
}

@keyframes currentLessonPulse {
    0%, 100% { 
        transform: scale(1);
        box-shadow: 0 4px 12px rgba(255, 150, 0, 0.4), 0 0 25px rgba(255, 150, 0, 0.3);
    }
    50% { 
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(255, 150, 0, 0.6), 0 0 35px rgba(255, 150, 0, 0.5);
    }
}

.lesson-node.available {
    background: linear-gradient(135deg, #1cb0f6, #0ea5e9);
    color: white;
    border-color: rgba(28, 176, 246, 0.3);
    box-shadow: 
        0 4px 12px rgba(28, 176, 246, 0.3),
        0 0 20px rgba(28, 176, 246, 0.2);
}

.lesson-node.locked {
    background: linear-gradient(135deg, #4b5563, #374151);
    color: #9ca3af;
    border-color: rgba(75, 85, 99, 0.3);
    cursor: not-allowed;
    opacity: 0.7;
}

.lesson-node:hover:not(.locked) {
    transform: scale(1.15) translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

/* Progress indicator for each sector */
.sector-progress {
    margin-top: 20px;
    background: rgba(0, 0, 0, 0.3);
    border-radius: 20px;
    padding: 6px;
    position: relative;
    overflow: hidden;
}

.progress-bar {
    height: 12px;
    background: linear-gradient(90deg, #32b8c6, #58cc02);
    border-radius: 14px;
    position: relative;
    transition: width 1.2s cubic-bezier(0.23, 1, 0.320, 1);
    overflow: hidden;
}

.progress-bar::after {
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
    animation: progressShimmer 2.5s infinite;
}

@keyframes progressShimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

.progress-text {
    text-align: center;
    color: #e2e8f0;
    font-size: 0.9rem;
    font-weight: 600;
    margin-top: 8px;
}

/* Connecting paths between lessons */
.lesson-connections {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
}

.connection-line {
    position: absolute;
    background: rgba(50, 184, 198, 0.4);
    border-radius: 2px;
    animation: connectionFlow 3s ease-in-out infinite;
}

@keyframes connectionFlow {
    0%, 100% { 
        opacity: 0.3;
        background: rgba(50, 184, 198, 0.3);
    }
    50% { 
        opacity: 0.8;
        background: rgba(50, 184, 198, 0.6);
    }
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .learning-path {
        padding: 20px 10px;
    }
    
    .sector-unit {
        margin: 40px 0;
        padding: 20px;
    }
    
    .lessons-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }
    
    .lesson-node {
        width: 70px;
        height: 70px;
        font-size: 16px;
    }
    
    .sector-icon {
        width: 56px;
        height: 56px;
        font-size: 28px;
    }
    
    .sector-info h3 {
        font-size: 1.5rem;
    }
}

@media (max-width: 480px) {
    .lessons-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
    }
    
    .lesson-node {
        width: 60px;
        height: 60px;
        font-size: 14px;
    }
}

/* Smooth entrance animations */
.sector-unit {
    opacity: 0;
    transform: translateY(30px);
    animation: sectorEnter 0.6s ease-out forwards;
}

.sector-unit:nth-child(1) { animation-delay: 0.1s; }
.sector-unit:nth-child(2) { animation-delay: 0.2s; }
.sector-unit:nth-child(3) { animation-delay: 0.3s; }
.sector-unit:nth-child(4) { animation-delay: 0.4s; }
.sector-unit:nth-child(5) { animation-delay: 0.5s; }
.sector-unit:nth-child(6) { animation-delay: 0.6s; }

@keyframes sectorEnter {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
{% endblock %}

{% block content %}
<div class="space-map-container">
    <!-- Animated starfield background -->
    <div class="stars-bg" id="starsBackground"></div>
    
    <div class="learning-path">
        <!-- Main connecting path line -->
        <div class="path-line"></div>
        
        <!-- Compute Sector -->
        <div class="sector-unit">
            <div class="sector-header">
                <div class="sector-icon">⚡</div>
                <div class="sector-info">
                    <h3>Compute Sector</h3>
                    <p class="sector-description">Master cloud processing and serverless computing</p>
                </div>
            </div>
            
            <div class="lessons-grid">
                <div class="lesson-connections">
                    <div class="connection-line" style="top: 40px; left: 90px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 150px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 210px; width: 40px; height: 3px;"></div>
                </div>
                
                <a href="/lesson/1" class="lesson-node {% if progress.current_lesson > 1 %}completed{% elif progress.current_lesson == 1 %}current{% else %}available{% endif %}">
                    1
                </a>
                <a href="/lesson/2" class="lesson-node {% if progress.current_lesson > 2 %}completed{% elif progress.current_lesson == 2 %}current{% elif progress.current_lesson >= 1 %}available{% else %}locked{% endif %}">
                    2
                </a>
                <a href="/lesson/3" class="lesson-node {% if progress.current_lesson > 3 %}completed{% elif progress.current_lesson == 3 %}current{% elif progress.current_lesson >= 2 %}available{% else %}locked{% endif %}">
                    3
                </a>
                <a href="/lesson/4" class="lesson-node {% if progress.current_lesson > 4 %}completed{% elif progress.current_lesson == 4 %}current{% elif progress.current_lesson >= 3 %}available{% else %}locked{% endif %}">
                    4
                </a>
            </div>
            
            <div class="sector-progress">
                {% set compute_completed = 0 %}
                {% for lesson in [1,2,3,4] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set compute_completed = compute_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar" style="width: {{ (compute_completed / 4 * 100) | round }}%"></div>
                <div class="progress-text">{{ compute_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Storage Sector -->
        <div class="sector-unit">
            <div class="sector-header">
                <div class="sector-icon">💾</div>
                <div class="sector-info">
                    <h3>Storage Sector</h3>
                    <p class="sector-description">Explore data storage and backup solutions</p>
                </div>
            </div>
            
            <div class="lessons-grid">
                <div class="lesson-connections">
                    <div class="connection-line" style="top: 40px; left: 90px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 150px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 210px; width: 40px; height: 3px;"></div>
                </div>
                
                <a href="/lesson/5" class="lesson-node {% if progress.current_lesson > 5 %}completed{% elif progress.current_lesson == 5 %}current{% elif progress.current_lesson >= 4 %}available{% else %}locked{% endif %}">
                    5
                </a>
                <a href="/lesson/6" class="lesson-node {% if progress.current_lesson > 6 %}completed{% elif progress.current_lesson == 6 %}current{% elif progress.current_lesson >= 5 %}available{% else %}locked{% endif %}">
                    6
                </a>
                <a href="/lesson/7" class="lesson-node {% if progress.current_lesson > 7 %}completed{% elif progress.current_lesson == 7 %}current{% elif progress.current_lesson >= 6 %}available{% else %}locked{% endif %}">
                    7
                </a>
                <a href="/lesson/8" class="lesson-node {% if progress.current_lesson > 8 %}completed{% elif progress.current_lesson == 8 %}current{% elif progress.current_lesson >= 7 %}available{% else %}locked{% endif %}">
                    8
                </a>
            </div>
            
            <div class="sector-progress">
                {% set storage_completed = 0 %}
                {% for lesson in [5,6,7,8] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set storage_completed = storage_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar" style="width: {{ (storage_completed / 4 * 100) | round }}%"></div>
                <div class="progress-text">{{ storage_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Security Sector -->
        <div class="sector-unit">
            <div class="sector-header">
                <div class="sector-icon">🛡️</div>
                <div class="sector-info">
                    <h3>Security Sector</h3>
                    <p class="sector-description">Learn cloud security and compliance</p>
                </div>
            </div>
            
            <div class="lessons-grid">
                <div class="lesson-connections">
                    <div class="connection-line" style="top: 40px; left: 90px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 150px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 210px; width: 40px; height: 3px;"></div>
                </div>
                
                <a href="/lesson/9" class="lesson-node {% if progress.current_lesson > 9 %}completed{% elif progress.current_lesson == 9 %}current{% elif progress.current_lesson >= 8 %}available{% else %}locked{% endif %}">
                    9
                </a>
                <a href="/lesson/10" class="lesson-node {% if progress.current_lesson > 10 %}completed{% elif progress.current_lesson == 10 %}current{% elif progress.current_lesson >= 9 %}available{% else %}locked{% endif %}">
                    10
                </a>
                <a href="/lesson/11" class="lesson-node {% if progress.current_lesson > 11 %}completed{% elif progress.current_lesson == 11 %}current{% elif progress.current_lesson >= 10 %}available{% else %}locked{% endif %}">
                    11
                </a>
                <a href="/lesson/12" class="lesson-node {% if progress.current_lesson > 12 %}completed{% elif progress.current_lesson == 12 %}current{% elif progress.current_lesson >= 11 %}available{% else %}locked{% endif %}">
                    12
                </a>
            </div>
            
            <div class="sector-progress">
                {% set security_completed = 0 %}
                {% for lesson in [9,10,11,12] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set security_completed = security_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar" style="width: {{ (security_completed / 4 * 100) | round }}%"></div>
                <div class="progress-text">{{ security_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Network Sector -->
        <div class="sector-unit">
            <div class="sector-header">
                <div class="sector-icon">🌐</div>
                <div class="sector-info">
                    <h3>Network Sector</h3>
                    <p class="sector-description">Connect systems with VPCs and CDNs</p>
                </div>
            </div>
            
            <div class="lessons-grid">
                <div class="lesson-connections">
                    <div class="connection-line" style="top: 40px; left: 90px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 150px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 210px; width: 40px; height: 3px;"></div>
                </div>
                
                <a href="/lesson/13" class="lesson-node {% if progress.current_lesson > 13 %}completed{% elif progress.current_lesson == 13 %}current{% elif progress.current_lesson >= 12 %}available{% else %}locked{% endif %}">
                    13
                </a>
                <a href="/lesson/14" class="lesson-node {% if progress.current_lesson > 14 %}completed{% elif progress.current_lesson == 14 %}current{% elif progress.current_lesson >= 13 %}available{% else %}locked{% endif %}">
                    14
                </a>
                <a href="/lesson/15" class="lesson-node {% if progress.current_lesson > 15 %}completed{% elif progress.current_lesson == 15 %}current{% elif progress.current_lesson >= 14 %}available{% else %}locked{% endif %}">
                    15
                </a>
                <a href="/lesson/16" class="lesson-node {% if progress.current_lesson > 16 %}completed{% elif progress.current_lesson == 16 %}current{% elif progress.current_lesson >= 15 %}available{% else %}locked{% endif %}">
                    16
                </a>
            </div>
            
            <div class="sector-progress">
                {% set network_completed = 0 %}
                {% for lesson in [13,14,15,16] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set network_completed = network_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar" style="width: {{ (network_completed / 4 * 100) | round }}%"></div>
                <div class="progress-text">{{ network_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- Database Sector -->
        <div class="sector-unit">
            <div class="sector-header">
                <div class="sector-icon">🗄️</div>
                <div class="sector-info">
                    <h3>Database Sector</h3>
                    <p class="sector-description">Manage data with RDS and DynamoDB</p>
                </div>
            </div>
            
            <div class="lessons-grid">
                <div class="lesson-connections">
                    <div class="connection-line" style="top: 40px; left: 90px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 150px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 210px; width: 40px; height: 3px;"></div>
                </div>
                
                <a href="/lesson/17" class="lesson-node {% if progress.current_lesson > 17 %}completed{% elif progress.current_lesson == 17 %}current{% elif progress.current_lesson >= 16 %}available{% else %}locked{% endif %}">
                    17
                </a>
                <a href="/lesson/18" class="lesson-node {% if progress.current_lesson > 18 %}completed{% elif progress.current_lesson == 18 %}current{% elif progress.current_lesson >= 17 %}available{% else %}locked{% endif %}">
                    18
                </a>
                <a href="/lesson/19" class="lesson-node {% if progress.current_lesson > 19 %}completed{% elif progress.current_lesson == 19 %}current{% elif progress.current_lesson >= 18 %}available{% else %}locked{% endif %}">
                    19
                </a>
                <a href="/lesson/20" class="lesson-node {% if progress.current_lesson > 20 %}completed{% elif progress.current_lesson == 20 %}current{% elif progress.current_lesson >= 19 %}available{% else %}locked{% endif %}">
                    20
                </a>
            </div>
            
            <div class="sector-progress">
                {% set database_completed = 0 %}
                {% for lesson in [17,18,19,20] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set database_completed = database_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar" style="width: {{ (database_completed / 4 * 100) | round }}%"></div>
                <div class="progress-text">{{ database_completed }}/4 Complete</div>
            </div>
        </div>

        <!-- DevOps Sector -->
        <div class="sector-unit">
            <div class="sector-header">
                <div class="sector-icon">🚀</div>
                <div class="sector-info">
                    <h3>DevOps Sector</h3>
                    <p class="sector-description">Automate deployment and monitoring</p>
                </div>
            </div>
            
            <div class="lessons-grid">
                <div class="lesson-connections">
                    <div class="connection-line" style="top: 40px; left: 90px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 150px; width: 40px; height: 3px;"></div>
                    <div class="connection-line" style="top: 40px; left: 210px; width: 40px; height: 3px;"></div>
                </div>
                
                <a href="/lesson/21" class="lesson-node {% if progress.current_lesson > 21 %}completed{% elif progress.current_lesson == 21 %}current{% elif progress.current_lesson >= 20 %}available{% else %}locked{% endif %}">
                    21
                </a>
                <a href="/lesson/22" class="lesson-node {% if progress.current_lesson > 22 %}completed{% elif progress.current_lesson == 22 %}current{% elif progress.current_lesson >= 21 %}available{% else %}locked{% endif %}">
                    22
                </a>
                <a href="/lesson/23" class="lesson-node {% if progress.current_lesson > 23 %}completed{% elif progress.current_lesson == 23 %}current{% elif progress.current_lesson >= 22 %}available{% else %}locked{% endif %}">
                    23
                </a>
                <a href="/lesson/24" class="lesson-node {% if progress.current_lesson > 24 %}completed{% elif progress.current_lesson == 24 %}current{% elif progress.current_lesson >= 23 %}available{% else %}locked{% endif %}">
                    24
                </a>
            </div>
            
            <div class="sector-progress">
                {% set devops_completed = 0 %}
                {% for lesson in [21,22,23,24] %}
                    {% if lesson in progress.completed_lessons %}
                        {% set devops_completed = devops_completed + 1 %}
                    {% endif %}
                {% endfor %}
                <div class="progress-bar" style="width: {{ (devops_completed / 4 * 100) | round }}%"></div>
                <div class="progress-text">{{ devops_completed }}/4 Complete</div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Create starfield background
    function createStarfield() {
        const starsContainer = document.getElementById('starsBackground');
        const starCount = 80;
        
        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            const size = Math.random() * 2 + 1;
            star.style.cssText = `
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                width: ${size}px;
                height: ${size}px;
                animation-delay: ${Math.random() * 3}s;
                animation-duration: ${Math.random() * 2 + 2}s;
            `;
            
            starsContainer.appendChild(star);
        }
    }
    
    // Enhanced lesson interactions
    const lessonNodes = document.querySelectorAll('.lesson-node');
    lessonNodes.forEach(node => {
        if (!node.classList.contains('locked')) {
            node.addEventListener('click', function(e) {
                createClickEffect(this);
                
                // Play sound if available
                if (window.awsOrbitAudio && window.awsOrbitAudio.playClick) {
                    window.awsOrbitAudio.playClick();
                }
            });
            
            node.addEventListener('mouseenter', function() {
                if (window.awsOrbitAudio && window.awsOrbitAudio.playClick) {
                    // Quieter hover sound
                    setTimeout(() => window.awsOrbitAudio.playClick(), 0);
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
            background: rgba(255, 255, 255, 0.5);
            transform: translate(-50%, -50%);
            animation: lessonRipple 0.6s ease-out;
            pointer-events: none;
            z-index: 10;
        `;
        
        element.style.position = 'relative';
        element.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    }
    
    // Add ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes lessonRipple {
            to {
                width: 120px;
                height: 120px;
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Initialize
    createStarfield();
    
    console.log('🎮 Duolingo-Style Space Adventure Map - Ready!');
});
</script>
{% endblock %}
EOF

echo "✅ Duolingo-style space adventure map created!"

echo ""
echo "🎉 Enhanced Duolingo-Style Map Complete!"
echo "========================================"
echo ""
echo "🎮 NEW FEATURES:"
echo "• Duolingo-style vertical learning path"
echo "• FTL-inspired connection lines between lessons"
echo "• Polished sector units with proper spacing"
echo "• Smooth entrance animations"
echo "• Professional gradients and shadows"
echo "• Mobile-responsive design"
echo "• Interactive feedback with ripple effects"
echo ""
echo "🚀 Test it now:"
echo "python app.py"
echo "Visit: http://localhost:5001"