/**
 * Enhanced Space Adventure Map - FTL-Style Animated Interactions
 * Inspired by smooth UI animations and sector-based gameplay
 */

class SpaceAdventureMap {
    constructor() {
        this.sectors = [];
        this.connections = [];
        this.animationQueue = [];
        this.audioEnabled = true;
        
        this.init();
    }
    
    init() {
        this.createBackground();
        this.initializeSectors();
        this.createConnections();
        this.setupEventListeners();
        this.startAnimations();
    }
    
    createBackground() {
        // Create dynamic starfield
        const starfield = document.getElementById('starfield');
        if (!starfield) return;
        
        // Generate stars with different sizes and twinkle rates
        for (let i = 0; i < 150; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            const size = Math.random() * 3 + 0.5;
            const brightness = Math.random() * 0.8 + 0.2;
            
            star.style.cssText = `
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                width: ${size}px;
                height: ${size}px;
                opacity: ${brightness};
                animation-delay: ${Math.random() * 3}s;
                animation-duration: ${Math.random() * 2 + 2}s;
            `;
            
            starfield.appendChild(star);
        }
        
        // Create moving nebula clouds
        this.createNebulaEffects();
    }
    
    createNebulaEffects() {
        const container = document.querySelector('.space-adventure-container');
        if (!container) return;
        
        for (let i = 0; i < 3; i++) {
            const nebula = document.createElement('div');
            nebula.style.cssText = `
                position: absolute;
                width: ${Math.random() * 400 + 200}px;
                height: ${Math.random() * 300 + 150}px;
                background: radial-gradient(ellipse, 
                    rgba(50, 184, 198, 0.1) 0%, 
                    rgba(138, 43, 226, 0.05) 50%, 
                    transparent 70%
                );
                border-radius: 50%;
                left: ${Math.random() * 80}%;
                top: ${Math.random() * 80}%;
                animation: nebulaDrift ${Math.random() * 30 + 20}s ease-in-out infinite;
                pointer-events: none;
                z-index: -1;
            `;
            
            container.appendChild(nebula);
        }
        
        // Add CSS for nebula animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes nebulaDrift {
                0%, 100% { 
                    transform: translateX(0) translateY(0) rotate(0deg);
                    opacity: 0.6;
                }
                33% { 
                    transform: translateX(50px) translateY(-30px) rotate(120deg);
                    opacity: 0.8;
                }
                66% { 
                    transform: translateX(-30px) translateY(40px) rotate(240deg);
                    opacity: 0.4;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    initializeSectors() {
        const sectorElements = document.querySelectorAll('.service-sector');
        
        sectorElements.forEach((element, index) => {
            const sector = {
                element: element,
                id: element.dataset.sector,
                unlocked: true, // Will be dynamically set based on progress
                lessons: [],
                connections: []
            };
            
            // Initialize lesson beacons in this sector
            const lessonBeacons = element.querySelectorAll('.lesson-beacon');
            lessonBeacons.forEach(beacon => {
                const lessonData = {
                    element: beacon,
                    id: beacon.href?.split('/').pop(),
                    status: beacon.classList.contains('completed') ? 'completed' :
                           beacon.classList.contains('current') ? 'current' :
                           beacon.classList.contains('available') ? 'available' : 'locked'
                };
                
                sector.lessons.push(lessonData);
                this.enhanceLessonBeacon(lessonData);
            });
            
            this.sectors.push(sector);
            this.enhanceSector(sector, index);
        });
    }
    
    enhanceSector(sector, index) {
        const element = sector.element;
        
        // Add entrance animation with staggered delay
        setTimeout(() => {
            element.classList.add('sector-visible');
        }, index * 150);
        
        // Enhanced hover effects
        element.addEventListener('mouseenter', () => {
            this.onSectorHover(sector);
        });
        
        element.addEventListener('mouseleave', () => {
            this.onSectorLeave(sector);
        });
        
        // Click effects
        element.addEventListener('click', (e) => {
            if (!e.target.closest('.lesson-beacon')) {
                this.onSectorClick(sector);
            }
        });
    }
    
    enhanceLessonBeacon(lesson) {
        const element = lesson.element;
        
        // Add ripple effect on interaction
        element.addEventListener('mouseenter', (e) => {
            if (lesson.status !== 'locked') {
                this.createRippleEffect(element);
                this.playUISound('hover');
            }
        });
        
        element.addEventListener('click', (e) => {
            if (lesson.status !== 'locked') {
                this.createClickEffect(element);
                this.playUISound('click');
            } else {
                e.preventDefault();
                this.createDeniedEffect(element);
                this.playUISound('denied');
            }
        });
        
        // Add special effects based on status
        if (lesson.status === 'current') {
            this.addCurrentLessonEffects(element);
        } else if (lesson.status === 'available') {
            this.addAvailableLessonEffects(element);
        }
    }
    
    createRippleEffect(element) {
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
        
        // Add ripple animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes rippleExpand {
                to {
                    width: ${size * 2}px;
                    height: ${size * 2}px;
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
        
        setTimeout(() => {
            ripple.remove();
            style.remove();
        }, 600);
    }
    
    createClickEffect(element) {
        // Burst effect for successful clicks
        const burst = document.createElement('div');
        burst.style.cssText = `
            position: absolute;
            top: 50%;
            left: 50%;
            width: 4px;
            height: 4px;
            transform: translate(-50%, -50%);
            pointer-events: none;
            z-index: 10;
        `;
        
        element.style.position = 'relative';
        element.appendChild(burst);
        
        // Create multiple particles for burst
        for (let i = 0; i < 8; i++) {
            const particle = document.createElement('div');
            const angle = (i / 8) * Math.PI * 2;
            const distance = 40;
            
            particle.style.cssText = `
                position: absolute;
                width: 3px;
                height: 3px;
                background: #32b8c6;
                border-radius: 50%;
                transform: translate(-50%, -50%);
                animation: burstParticle 0.5s ease-out forwards;
            `;
            
            // Set custom properties for animation
            particle.style.setProperty('--end-x', Math.cos(angle) * distance + 'px');
            particle.style.setProperty('--end-y', Math.sin(angle) * distance + 'px');
            
            burst.appendChild(particle);
        }
        
        // Add burst animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes burstParticle {
                to {
                    transform: translate(calc(-50% + var(--end-x)), calc(-50% + var(--end-y)));
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
        
        setTimeout(() => {
            burst.remove();
            style.remove();
        }, 500);
    }
    
    createDeniedEffect(element) {
        // Shake effect for locked lessons
        element.style.animation = 'shake 0.4s cubic-bezier(0.36, 0.07, 0.19, 0.97)';
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-5px) rotateZ(-2deg); }
                75% { transform: translateX(5px) rotateZ(2deg); }
            }
        `;
        document.head.appendChild(style);
        
        setTimeout(() => {
            element.style.animation = '';
            style.remove();
        }, 400);
    }
    
    addCurrentLessonEffects(element) {
        // Enhanced glow for current lesson
        const glow = document.createElement('div');
        glow.style.cssText = `
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            bottom: -10px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(245, 158, 11, 0.3) 0%, transparent 70%);
            animation: currentGlow 2s ease-in-out infinite;
            pointer-events: none;
            z-index: -1;
        `;
        
        element.style.position = 'relative';
        element.appendChild(glow);
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes currentGlow {
                0%, 100% { 
                    transform: scale(1);
                    opacity: 0.6;
                }
                50% { 
                    transform: scale(1.2);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    addAvailableLessonEffects(element) {
        // Subtle pulse for available lessons
        element.style.animation = 'availablePulse 3s ease-in-out infinite';
    }
    
    createConnections() {
        const connectionsContainer = document.querySelector('.sector-connections');
        if (!connectionsContainer) return;
        
        // Define connection paths between sectors
        const connections = [
            { from: 0, to: 1, style: 'top: 25%; left: 20%; width: 60%; transform: rotate(15deg);' },
            { from: 1, to: 2, style: 'top: 35%; left: 45%; width: 40%; transform: rotate(-10deg);' },
            { from: 2, to: 3, style: 'top: 65%; left: 25%; width: 50%; transform: rotate(20deg);' },
            { from: 3, to: 4, style: 'top: 75%; left: 10%; width: 70%; transform: rotate(-5deg);' },
            { from: 4, to: 5, style: 'top: 85%; left: 35%; width: 45%; transform: rotate(12deg);' }
        ];
        
        connections.forEach((conn, index) => {
            const path = document.createElement('div');
            path.className = 'connection-path';
            path.style.cssText = conn.style;
            path.style.animationDelay = index * 0.5 + 's';
            
            connectionsContainer.appendChild(path);
        });
    }
    
    onSectorHover(sector) {
        // Highlight connected sectors
        this.sectors.forEach(s => {
            if (s !== sector) {
                s.element.style.borderColor = 'rgba(50, 184, 198, 0.2)';
                s.element.style.transform = 'scale(0.98)';
            }
        });
        
        // Show sector info tooltip (optional)
        this.showSectorTooltip(sector);
    }
    
    onSectorLeave(sector) {
        // Reset all sector styles
        this.sectors.forEach(s => {
            s.element.style.borderColor = '';
            s.element.style.transform = '';
        });
        
        this.hideSectorTooltip();
    }
    
    onSectorClick(sector) {
        // Sector selection effects
        sector.element.style.animation = 'sectorSelect 0.3s ease-out';
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes sectorSelect {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        `;
        document.head.appendChild(style);
        
        setTimeout(() => {
            sector.element.style.animation = '';
            style.remove();
        }, 300);
    }
    
    showSectorTooltip(sector) {
        // Optional: Show detailed sector information
        // Implementation depends on your tooltip system
    }
    
    hideSectorTooltip() {
        // Hide any active tooltips
    }
    
    playUISound(type) {
        if (!this.audioEnabled || !window.awsOrbitAudio) return;
        
        switch (type) {
            case 'hover':
                window.awsOrbitAudio.playClick?.();
                break;
            case 'click':
                window.awsOrbitAudio.playCorrect?.();
                break;
            case 'denied':
                window.awsOrbitAudio.playWrong?.();
                break;
        }
    }
    
    setupEventListeners() {
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            this.handleKeyNavigation(e);
        });
        
        // Resize handler
        window.addEventListener('resize', () => {
            this.handleResize();
        });
    }
    
    handleKeyNavigation(e) {
        // Implement keyboard navigation for accessibility
        const focusedElement = document.activeElement;
        
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
            // Navigate to next lesson/sector
            this.navigateNext(focusedElement);
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            // Navigate to previous lesson/sector
            this.navigatePrevious(focusedElement);
        }
    }
    
    navigateNext(currentElement) {
        // Find next focusable lesson beacon
        const beacons = Array.from(document.querySelectorAll('.lesson-beacon:not(.locked)'));
        const currentIndex = beacons.indexOf(currentElement);
        const nextBeacon = beacons[currentIndex + 1] || beacons[0];
        
        if (nextBeacon) {
            nextBeacon.focus();
            this.createRippleEffect(nextBeacon);
        }
    }
    
    navigatePrevious(currentElement) {
        // Find previous focusable lesson beacon
        const beacons = Array.from(document.querySelectorAll('.lesson-beacon:not(.locked)'));
        const currentIndex = beacons.indexOf(currentElement);
        const prevBeacon = beacons[currentIndex - 1] || beacons[beacons.length - 1];
        
        if (prevBeacon) {
            prevBeacon.focus();
            this.createRippleEffect(prevBeacon);
        }
    }
    
    handleResize() {
        // Adjust layout for different screen sizes
        const container = document.querySelector('.galaxy-sectors');
        if (!container) return;
        
        const width = window.innerWidth;
        
        if (width <= 768) {
            container.style.gridTemplateColumns = '1fr';
        } else if (width <= 1200) {
            container.style.gridTemplateColumns = 'repeat(2, 1fr)';
        } else {
            container.style.gridTemplateColumns = 'repeat(3, 1fr)';
        }
    }
    
    startAnimations() {
        // Start any continuous animations or effects
        this.animateConnections();
        
        // Set up intersection observer for scroll animations
        this.setupScrollAnimations();
    }
    
    animateConnections() {
        const connections = document.querySelectorAll('.connection-path');
        connections.forEach((conn, index) => {
            // Stagger the connection animations
            conn.style.animationDelay = (index * 0.3) + 's';
        });
    }
    
    setupScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.service-sector').forEach(sector => {
            observer.observe(sector);
        });
    }
    
    // Public methods for external control
    unlockSector(sectorId) {
        const sector = this.sectors.find(s => s.id === sectorId);
        if (sector && !sector.unlocked) {
            sector.unlocked = true;
            sector.element.classList.add('newly-unlocked');
            this.playUISound('correct');
        }
    }
    
    updateLessonStatus(lessonId, status) {
        this.sectors.forEach(sector => {
            const lesson = sector.lessons.find(l => l.id === lessonId);
            if (lesson) {
                lesson.status = status;
                lesson.element.className = `lesson-beacon ${status}`;
                
                if (status === 'completed') {
                    this.createCompletionEffect(lesson.element);
                }
            }
        });
    }
    
    createCompletionEffect(element) {
        // Celebration effect for completed lessons
        const celebration = document.createElement('div');
        celebration.style.cssText = `
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 24px;
            color: #22c55e;
            animation: celebrationPop 1s ease-out forwards;
            pointer-events: none;
            z-index: 20;
        `;
        celebration.textContent = '✨';
        
        element.style.position = 'relative';
        element.appendChild(celebration);
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes celebrationPop {
                0% { 
                    transform: translateX(-50%) translateY(0) scale(0);
                    opacity: 0;
                }
                50% { 
                    transform: translateX(-50%) translateY(-30px) scale(1.5);
                    opacity: 1;
                }
                100% { 
                    transform: translateX(-50%) translateY(-50px) scale(1);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
        
        setTimeout(() => {
            celebration.remove();
            style.remove();
        }, 1000);
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    window.spaceAdventureMap = new SpaceAdventureMap();
    
    // Add smooth scrolling for internal navigation
    document.addEventListener('click', function(e) {
        if (e.target.closest('.lesson-beacon') && !e.target.classList.contains('locked')) {
            // Optional: Add loading transition before navigation
            e.target.style.transform = 'scale(0.95)';
            setTimeout(() => {
                e.target.style.transform = '';
            }, 150);
        }
    });
    
    console.log('🌌 Space Adventure Map Enhanced - Ready for exploration!');
});