#!/bin/bash
# 🌌 restore_enhanced_map.sh - Restore the good sector layout with enhancements

echo "🌌 CloudQuest RPG - Restore Enhanced Sector Map"
echo "==============================================="

echo "🗺️ Creating proper sector-based map with enhancements..."

cat > templates/space_adventure_map.html << 'EOF'
{% extends "base.html" %}

{% block title %}Space Adventure Map - CloudQuest RPG{% endblock %}

{% block head %}
<style>
/* Enhanced Space Adventure Map - Proper Sector Layout */
.space-adventure-wrapper {
    background: radial-gradient(ellipse at center, #1a1a2e 0%, #16213e 35%, #0f0f23 100%);
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

/* Animated starfield */
.starfield {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
}

.star {
    position: absolute;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    animation: twinkle 4s ease-in-out infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.2; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.2); }
}

/* Main map content */
.map-content {
    position: relative;
    z-index: 1;
    padding: 40px 20px;
    max-width: 1400px;
    margin: 0 auto;
}

/* Map header */
.map-header {
    text-align: center;
    margin-bottom: 50px;
    padding: 0 20px;
}

.map-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #32b8c6, #f7d51d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 15px;
    text-shadow: 0 0 30px rgba(50, 184, 198, 0.3);
}

.map-subtitle {
    font-size: 1.2rem;
    color: #94a3b8;
    font-weight: 500;
}

/* Sectors grid */
.sectors-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 40px;
    position: relative;
}

/* Individual sector cards */
.sector-card {
    background: rgba(13, 27, 42, 0.95);
    border: 2px solid rgba(50, 184, 198, 0.3);
    border-radius: 24px;
    padding: 30px;
    position: relative;
    backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    box-shadow: 
        0 10px 30px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
    overflow: hidden;
}

.sector-card::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(45deg, 
        rgba(50, 184, 198, 0.1), 
        rgba(138, 43, 226, 0.1), 
        rgba(245, 158, 11, 0.1)
    );
    border-radius: 24px;
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: -1;
}

.sector-card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: rgba(50, 184, 198, 0.6);
    box-shadow: 
        0 20px 50px rgba(0, 0, 0, 0.4),
        0 0 50px rgba(50, 184, 198, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.sector-card:hover::before {
    opacity: 1;
    animation: borderGlow 2s ease-in-out infinite;
}

@keyframes borderGlow {
    0%, 100% { 
        background-position: 0% 50%;
        filter: hue-rotate(0deg);
    }
    33% { 
        background-position: 50% 0%;
        filter: hue-rotate(120deg);
    }
    66% { 
        background-position: 100% 50%;
        filter: hue-rotate(240deg);
    }
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
    width: 80px;
    height: 80px;
    background: linear-gradient(135deg, #32b8c6, #1a8a96);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 36px;
    position: relative;
    box-shadow: 
        0 10px 20px rgba(50, 184, 198, 0.3),
        inset 0 2px 0 rgba(255, 255, 255, 0.2);
    transition: all 0.3s ease;
}

.sector-icon::before {
    content: '';
    position: absolute;
    top: -4px;
    left: -4px;
    right: -4px;
    bottom: -4px;
    background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    border-radius: 50%;
    opacity: 0;
    transition: all 0.3s ease;
}

.sector-card:hover .sector-icon {
    transform: scale(1.1);
    box-shadow: 
        0 15px 30px rgba(50, 184, 198, 0.4),
        inset 0 2px 0 rgba(255, 255, 255, 0.3);
}

.sector-card:hover .sector-icon::before {
    opacity: 1;
    animation: iconShine 1s ease-out;
}

@keyframes iconShine {
    0% { transform: rotate(0deg) scale(1); opacity: 0; }
    50% { transform: rotate(180deg) scale(1.2); opacity: 1; }
    100% { transform: rotate(360deg) scale(1); opacity: 0; }
}

.sector-info h3 {
    color: #32b8c6;
    font-size: 1.8rem;
    font-weight: 700;
    margin: 0 0 8px 0;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.sector-description {
    color: #94a3b8;
    font-size: 1rem;
    margin: 0;
    line-height: 1.5;
}

/* Lessons grid within sector */
.lessons-container {
    margin-top: 25px;
}

.lessons-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-bottom: 20px;
}

/* Individual lesson nodes */
.lesson-node {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
    text-decoration: none;
    position: relative;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    border: 3px solid transparent;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* Lesson states */
.lesson-node.completed {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-color: rgba(34, 197, 94, 0.3);
    box-shadow: 
        0 4px 12px rgba(34, 197, 94, 0.4),
        0 0 20px rgba(34, 197, 94, 0.2);
}

.lesson-node.completed::after {
    content: '✓';
    position: absolute;
    font-size: 24px;
    font-weight: 900;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    animation: checkPulse 0.5s ease-out;
}

@keyframes checkPulse {
    0% { transform: scale(0) rotate(-180deg); opacity: 0; }
    50% { transform: scale(1.3) rotate(0deg); opacity: 1; }
    100% { transform: scale(1) rotate(0deg); opacity: 1; }
}

.lesson-node.current {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
    border-color: rgba(245, 158, 11, 0.4);
    animation: currentPulse 2s ease-in-out infinite;
    box-shadow: 
        0 4px 12px rgba(245, 158, 11, 0.4),
        0 0 25px rgba(245, 158, 11, 0.3);
}

@keyframes currentPulse {
    0%, 100% { 
        transform: scale(1);
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4), 0 0 25px rgba(245, 158, 11, 0.3);
    }
    50% { 
        transform: scale(1.15);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.6), 0 0 35px rgba(245, 158, 11, 0.5);
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
    opacity: 0.6;
}

.lesson-node:hover:not(.locked) {
    transform: scale(1.2) translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

/* Progress section */
.sector-progress {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 20px;
    padding: 8px;
    position: relative;
    overflow: hidden;
}

.progress-track {
    height: 16px;
    background: rgba(100, 116, 139, 0.3);
    border-radius: 12px;
    position: relative;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #32b8c6, #22c55e);
    border-radius: 12px;
    position: relative;
    transition: width 1.5s cubic-bezier(0.23, 1, 0.320, 1);
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
    animation: shimmer 2.5s infinite;
}

@keyframes shimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

.progress-text {
    text-align: center;
    color: #e2e8f0;
    font-size: 0.95rem;
    font-weight: 600;
    margin-top: 8px;
}

/* Connection paths between sectors */
.sector-connections {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.connection-path {
    position: absolute;
    background: linear-gradient(90deg, 
        transparent 0%,
        rgba(50, 184, 198, 0.2) 25%,
        rgba(50, 184, 198, 0.6) 50%,
        rgba(50, 184, 198, 0.2) 75%,
        transparent 100%
    );
    height: 4px;
    border-radius: 2px;
    animation: dataFlow 4s ease-in-out infinite;
}

@keyframes dataFlow {
    0%, 100% { 
        background-position: -200% 0;
        opacity: 0.3;
    }
    50% { 
        background-position: 200% 0;
        opacity: 0.8;
    }
}

/* Mobile responsiveness */
@media (max-width: 1200px) {
    .sectors-grid {
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 30px;
    }
}

@media (max-width: 768px) {
    .map-content {
        padding: 20px 15px;
    }
    
    .map-title {
        font-size: 2.2rem;
    }
    
    .sectors-grid {
        grid-template-columns: 1fr;
        gap: 25px;
    }
    
    .sector-card {
        padding: 25px;
    }
    
    .lessons-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
    }
    
    .lesson-node {
        width: 60px;
        height: 60px;
        font-size: 16px;
    }
    
    .sector-icon {
        width: 70px;
        height: 70px;
        font-size: 32px;
    }
}

@media (max-width: 480px) {
    .lessons-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
    
    .lesson-node {
        width: 55px;
        height: 55px;
        font-size: 14px;
    }
}

/* Entrance animations */
.sector-card {
    opacity: 0;
    transform: translateY(50px);
    animation: sectorEnter 0.8s ease-out forwards;
}

.sector-card:nth-child(1) { animation-delay: 0.1s; }
.sector-card:nth-child(2) { animation-delay: 0.2s; }
.sector-card:nth-child(3) { animation-delay: 0.3s; }
.sector-card:nth-child(4) { animation-delay: 0.4s; }
.sector-card:nth-child(5) { animation-delay: 0.5s; }
.sector-card:nth-child(6) { animation-delay: 0.6s; }

@keyframes sectorEnter {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
{% endblock %}

{% block content %}
<div class="space-adventure-wrapper">
    <!-- Animated starfield -->
    <div class="starfield" id="starfield"></div>
    
    <div class="map-content">
        <!-- Map header -->
        <div class="map-header">
            <h1 class="map-title">AWS Cloud Orbit</h1>
            <p class="map-subtitle">Master cloud computing through interconnected learning sectors</p>
        </div>
        
        <!-- Connection paths -->
        <div class="sector-connections">
            <div class="connection-path" style="top: 25%; left: 15%; width: 70%; transform: rotate(8deg);"></div>
            <div class="connection-path" style="top: 45%; left: 20%; width: 60%; transform: rotate(-5deg);"></div>
            <div class="connection-path" style="top: 65%; left: 10%; width: 80%; transform: rotate(3deg);"></div>
        </div>
        
        <!-- Sectors grid -->
        <div class="sectors-grid">
            <!-- Compute Sector -->
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">⚡</div>
                    <div class="sector-info">
                        <h3>Compute Sector</h3>
                        <p class="sector-description">Master cloud processing power with EC2, Lambda, and serverless computing</p>
                    </div>
                </div>
                
                <div class="lessons-container">
                    <div class="lessons-grid">
                        <a href="/lesson/1" class="lesson-node {% if progress.current_lesson > 1 %}completed{% elif progress.current_lesson == 1 %}current{% else %}available{% endif %}">1</a>
                        <a href="/lesson/2" class="lesson-node {% if progress.current_lesson > 2 %}completed{% elif progress.current_lesson == 2 %}current{% elif progress.current_lesson >= 1 %}available{% else %}locked{% endif %}">2</a>
                        <a href="/lesson/3" class="lesson-node {% if progress.current_lesson > 3 %}completed{% elif progress.current_lesson == 3 %}current{% elif progress.current_lesson >= 2 %}available{% else %}locked{% endif %}">3</a>
                        <a href="/lesson/4" class="lesson-node {% if progress.current_lesson > 4 %}completed{% elif progress.current_lesson == 4 %}current{% elif progress.current_lesson >= 3 %}available{% else %}locked{% endif %}">4</a>
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
                        <div class="progress-text">{{ compute_completed }}/4 Lessons Complete</div>
                    </div>
                </div>
            </div>

            <!-- Storage Sector -->
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">💾</div>
                    <div class="sector-info">
                        <h3>Storage Sector</h3>
                        <p class="sector-description">Explore data storage solutions with S3, EBS, and backup strategies</p>
                    </div>
                </div>
                
                <div class="lessons-container">
                    <div class="lessons-grid">
                        <a href="/lesson/5" class="lesson-node {% if progress.current_lesson > 5 %}completed{% elif progress.current_lesson == 5 %}current{% elif progress.current_lesson >= 4 %}available{% else %}locked{% endif %}">5</a>
                        <a href="/lesson/6" class="lesson-node {% if progress.current_lesson > 6 %}completed{% elif progress.current_lesson == 6 %}current{% elif progress.current_lesson >= 5 %}available{% else %}locked{% endif %}">6</a>
                        <a href="/lesson/7" class="lesson-node {% if progress.current_lesson > 7 %}completed{% elif progress.current_lesson == 7 %}current{% elif progress.current_lesson >= 6 %}available{% else %}locked{% endif %}">7</a>
                        <a href="/lesson/8" class="lesson-node {% if progress.current_lesson > 8 %}completed{% elif progress.current_lesson == 8 %}current{% elif progress.current_lesson >= 7 %}available{% else %}locked{% endif %}">8</a>
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
                        <div class="progress-text">{{ storage_completed }}/4 Lessons Complete</div>
                    </div>
                </div>
            </div>

            <!-- Security Sector -->
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">🛡️</div>
                    <div class="sector-info">
                        <h3>Security Sector</h3>
                        <p class="sector-description">Learn cloud security, IAM, encryption, and compliance best practices</p>
                    </div>
                </div>
                
                <div class="lessons-container">
                    <div class="lessons-grid">
                        <a href="/lesson/9" class="lesson-node {% if progress.current_lesson > 9 %}completed{% elif progress.current_lesson == 9 %}current{% elif progress.current_lesson >= 8 %}available{% else %}locked{% endif %}">9</a>
                        <a href="/lesson/10" class="lesson-node {% if progress.current_lesson > 10 %}completed{% elif progress.current_lesson == 10 %}current{% elif progress.current_lesson >= 9 %}available{% else %}locked{% endif %}">10</a>
                        <a href="/lesson/11" class="lesson-node {% if progress.current_lesson > 11 %}completed{% elif progress.current_lesson == 11 %}current{% elif progress.current_lesson >= 10 %}available{% else %}locked{% endif %}">11</a>
                        <a href="/lesson/12" class="lesson-node {% if progress.current_lesson > 12 %}completed{% elif progress.current_lesson == 12 %}current{% elif progress.current_lesson >= 11 %}available{% else %}locked{% endif %}">12</a>
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
                        <div class="progress-text">{{ security_completed }}/4 Lessons Complete</div>
                    </div>
                </div>
            </div>

            <!-- Networking Sector -->
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">🌐</div>
                    <div class="sector-info">
                        <h3>Network Sector</h3>
                        <p class="sector-description">Connect systems with VPCs, CDNs, and load balancing strategies</p>
                    </div>
                </div>
                
                <div class="lessons-container">
                    <div class="lessons-grid">
                        <a href="/lesson/13" class="lesson-node {% if progress.current_lesson > 13 %}completed{% elif progress.current_lesson == 13 %}current{% elif progress.current_lesson >= 12 %}available{% else %}locked{% endif %}">13</a>
                        <a href="/lesson/14" class="lesson-node {% if progress.current_lesson > 14 %}completed{% elif progress.current_lesson == 14 %}current{% elif progress.current_lesson >= 13 %}available{% else %}locked{% endif %}">14</a>
                        <a href="/lesson/15" class="lesson-node {% if progress.current_lesson > 15 %}completed{% elif progress.current_lesson == 15 %}current{% elif progress.current_lesson >= 14 %}available{% else %}locked{% endif %}">15</a>
                        <a href="/lesson/16" class="lesson-node {% if progress.current_lesson > 16 %}completed{% elif progress.current_lesson == 16 %}current{% elif progress.current_lesson >= 15 %}available{% else %}locked{% endif %}">16</a>
                    </div>
                    
                    <div class="sector-progress">
                        <div class="progress-track">
                            {% set network_completed = 0 %}
                            {% for lesson in [13,14,15,16] %}
                                {% if lesson in progress.completed_lessons %}
                                    {% set network_completed = network_completed + 1 %}
                                {% endif %}
                            {% endfor %}
                            <div class="progress-fill" style="width: {{ (network_completed / 4 * 100) | round }}%"></div>
                        </div>
                        <div class="progress-text">{{ network_completed }}/4 Lessons Complete</div>
                    </div>
                </div>
            </div>

            <!-- Database Sector -->
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">🗄️</div>
                    <div class="sector-info">
                        <h3>Database Sector</h3>
                        <p class="sector-description">Manage data with RDS, DynamoDB, and database optimization techniques</p>
                    </div>
                </div>
                
                <div class="lessons-container">
                    <div class="lessons-grid">
                        <a href="/lesson/17" class="lesson-node {% if progress.current_lesson > 17 %}completed{% elif progress.current_lesson == 17 %}current{% elif progress.current_lesson >= 16 %}available{% else %}locked{% endif %}">17</a>
                        <a href="/lesson/18" class="lesson-node {% if progress.current_lesson > 18 %}completed{% elif progress.current_lesson == 18 %}current{% elif progress.current_lesson >= 17 %}available{% else %}locked{% endif %}">18</a>
                        <a href="/lesson/19" class="lesson-node {% if progress.current_lesson > 19 %}completed{% elif progress.current_lesson == 19 %}current{% elif progress.current_lesson >= 18 %}available{% else %}locked{% endif %}">19</a>
                        <a href="/lesson/20" class="lesson-node {% if progress.current_lesson > 20 %}completed{% elif progress.current_lesson == 20 %}current{% elif progress.current_lesson >= 19 %}available{% else %}locked{% endif %}">20</a>
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
                        <div class="progress-text">{{ database_completed }}/4 Lessons Complete</div>
                    </div>
                </div>
            </div>

            <!-- DevOps Sector -->
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">🚀</div>
                    <div class="sector-info">
                        <h3>DevOps Sector</h3>
                        <p class="sector-description">Automate deployment, monitoring, and CI/CD pipeline management</p>
                    </div>
                </div>
                
                <div class="lessons-container">
                    <div class="lessons-grid">
                        <a href="/lesson/21" class="lesson-node {% if progress.current_lesson > 21 %}completed{% elif progress.current_lesson == 21 %}current{% elif progress.current_lesson >= 20 %}available{% else %}locked{% endif %}">21</a>
                        <a href="/lesson/22" class="lesson-node {% if progress.current_lesson > 22 %}completed{% elif progress.current_lesson == 22 %}current{% elif progress.current_lesson >= 21 %}available{% else %}locked{% endif %}">22</a>
                        <a href="/lesson/23" class="lesson-node {% if progress.current_lesson > 23 %}completed{% elif progress.current_lesson == 23 %}current{% elif progress.current_lesson >= 22 %}available{% else %}locked{% endif %}">23</a>
                        <a href="/lesson/24" class="lesson-node {% if progress.current_lesson > 24 %}completed{% elif progress.current_lesson == 24 %}current{% elif progress.current_lesson >= 23 %}available{% else %}locked{% endif %}">24</a>
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
                        <div class="progress-text">{{ devops_completed }}/4 Lessons Complete</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Create starfield
    function createStarfield() {
        const starfield = document.getElementById('starfield');
        const starCount = 120;
        
        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            const size = Math.random() * 3 + 1;
            star.style.cssText = `
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                width: ${size}px;
                height: ${size}px;
                animation-delay: ${Math.random() * 4}s;
                animation-duration: ${Math.random() * 3 + 3}s;
            `;
            
            starfield.appendChild(star);
        }
    }
    
    // Enhanced lesson interactions
    const lessonNodes = document.querySelectorAll('.lesson-node');
    lessonNodes.forEach(node => {
        if (!node.classList.contains('locked')) {
            node.addEventListener('click', function(e) {
                createRippleEffect(this);
                
                // Play sound if available
                if (window.awsOrbitAudio && window.awsOrbitAudio.playClick) {
                    window.awsOrbitAudio.playClick();
                }
            });
            
            node.addEventListener('mouseenter', function() {
                // Subtle hover sound
                if (window.awsOrbitAudio && window.awsOrbitAudio.playClick) {
                    setTimeout(() => window.awsOrbitAudio.playClick(), 0);
                }
            });
        } else {
            node.addEventListener('click', function(e) {
                e.preventDefault();
                createDeniedEffect(this);
                
                if (window.awsOrbitAudio && window.awsOrbitAudio.playWrong) {
                    window.awsOrbitAudio.playWrong();
                }
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
            background: rgba(255, 255, 255, 0.6);
            transform: translate(-50%, -50%);
            animation: rippleExpand 0.6s ease-out;
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
        element.style.animation = 'denyShake 0.5s ease-in-out';
        
        setTimeout(() => {
            element.style.animation = '';
        }, 500);
    }
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes rippleExpand {
            to {
                width: 140px;
                height: 140px;
                opacity: 0;
            }
        }
        
        @keyframes denyShake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-8px); }
            75% { transform: translateX(8px); }
        }
    `;
    document.head.appendChild(style);
    
    // Initialize starfield
    createStarfield();
    
    console.log('🌌 Enhanced Space Adventure Map - Ready for exploration!');
});
</script>
{% endblock %}
EOF

echo "✅ Enhanced sector map restored!"

echo ""
echo "🎉 Proper Sector Map Restored & Enhanced!"
echo "========================================"
echo ""
echo "🌌 FEATURES RESTORED:"
echo "• Rich sector cards with proper content"
echo "• Detailed descriptions for each sector"
echo "• Beautiful icons and typography"
echo "• Smooth hover animations and effects"
echo "• Progress tracking with shimmer effects"
echo "• FTL-inspired connection paths"
echo "• Interactive feedback with ripples"
echo "• Professional gradients and shadows"
echo ""
echo "🚀 Test it now:"
echo "python app.py"
echo "Visit: http://localhost:5001"