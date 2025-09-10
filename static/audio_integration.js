// AWS Cloud Orbit - Audio System Integration
// Add this to your existing JavaScript or as a separate file

// Initialize the audio system when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AWS Orbit Audio System
    window.awsOrbitAudio = new AWSCloudOrbitAudio();
    
    // Add click sounds to existing buttons
    document.addEventListener('click', function(e) {
        if (e.target.matches('button, .btn, a[href], .option-label, input[type="radio"], input[type="checkbox"], .lesson-card')) {
            if (window.awsOrbitAudio) {
                window.awsOrbitAudio.playClick();
            }
        }
    });
    
    console.log('🎵 AWS Cloud Orbit Audio System ready!');
});

// Audio System Class
class AWSCloudOrbitAudio {
    constructor() {
        this.audioContext = null;
        this.enabled = true;
        this.volume = 0.7;
        this.sounds = {};
        
        this.initialize();
    }

    async initialize() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            // Handle browser autoplay restrictions
            if (this.audioContext.state === 'suspended') {
                document.addEventListener('click', () => {
                    this.audioContext.resume();
                }, { once: true });
            }
            
            this.generateSounds();
            console.log('🔊 AWS Cloud Orbit Audio System initialized');
        } catch (error) {
            console.warn('Audio not supported:', error);
            this.enabled = false;
        }
    }

    generateSounds() {
        if (!this.enabled || !this.audioContext) return;

        this.sounds = {
            correct: this.createCorrectChime(),
            wrong: this.createWrongSound(),
            shieldLoss: this.createShieldLossSound(),
            shieldGain: this.createShieldGainSound(),
            levelUp: this.createLevelUpFanfare(),
            badgeEarned: this.createBadgeSound(),
            streakBonus: this.createStreakSound(),
            rewardScreen: this.createRewardFanfare(),
            click: this.createClickSound(),
            whoosh: this.createWhooshSound(),
            notification: this.createNotificationSound()
        };
    }

    // Duolingo-style correct answer chime
    createCorrectChime() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const frequencies = [523.25, 659.25, 783.99, 1046.50]; // C5-E5-G5-C6
            
            frequencies.forEach((freq, index) => {
                const oscillator = this.audioContext.createOscillator();
                const gainNode = this.audioContext.createGain();
                
                oscillator.frequency.setValueAtTime(freq, now);
                oscillator.type = 'sine';
                
                const startTime = now + (index * 0.1);
                gainNode.gain.setValueAtTime(0, startTime);
                gainNode.gain.linearRampToValueAtTime(this.volume * 0.3, startTime + 0.02);
                gainNode.gain.exponentialRampToValueAtTime(0.001, startTime + 0.5);
                
                oscillator.connect(gainNode);
                gainNode.connect(this.audioContext.destination);
                
                oscillator.start(startTime);
                oscillator.stop(startTime + 0.5);
            });
        };
    }

    createWrongSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(350, now);
            oscillator.frequency.exponentialRampToValueAtTime(200, now + 0.4);
            oscillator.type = 'sine';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.15, now + 0.02);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.4);
        };
    }

    createShieldLossSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(800, now);
            oscillator.frequency.exponentialRampToValueAtTime(150, now + 0.3);
            oscillator.type = 'sawtooth';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.2, now + 0.01);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.3);
        };
    }

    createShieldGainSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(300, now);
            oscillator.frequency.exponentialRampToValueAtTime(800, now + 0.3);
            oscillator.type = 'sine';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.2, now + 0.02);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.3);
        };
    }

    createLevelUpFanfare() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const melody = [
                { freq: 523.25, time: 0 },    // C5
                { freq: 659.25, time: 0.15 }, // E5
                { freq: 783.99, time: 0.3 },  // G5
                { freq: 1046.5, time: 0.45 }, // C6
                { freq: 1318.5, time: 0.6 }   // E6
            ];
            
            melody.forEach(note => {
                const oscillator = this.audioContext.createOscillator();
                const gainNode = this.audioContext.createGain();
                
                oscillator.frequency.setValueAtTime(note.freq, now);
                oscillator.type = 'triangle';
                
                const startTime = now + note.time;
                gainNode.gain.setValueAtTime(0, startTime);
                gainNode.gain.linearRampToValueAtTime(this.volume * 0.4, startTime + 0.02);
                gainNode.gain.exponentialRampToValueAtTime(0.001, startTime + 0.4);
                
                oscillator.connect(gainNode);
                gainNode.connect(this.audioContext.destination);
                
                oscillator.start(startTime);
                oscillator.stop(startTime + 0.4);
            });
        };
    }

    createBadgeSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const frequencies = [1000, 1200, 1500, 2000];
            
            frequencies.forEach((freq, index) => {
                const oscillator = this.audioContext.createOscillator();
                const gainNode = this.audioContext.createGain();
                
                oscillator.frequency.setValueAtTime(freq, now);
                oscillator.type = 'sine';
                
                const startTime = now + (index * 0.08);
                gainNode.gain.setValueAtTime(0, startTime);
                gainNode.gain.linearRampToValueAtTime(this.volume * 0.25, startTime + 0.01);
                gainNode.gain.exponentialRampToValueAtTime(0.001, startTime + 0.3);
                
                oscillator.connect(gainNode);
                gainNode.connect(this.audioContext.destination);
                
                oscillator.start(startTime);
                oscillator.stop(startTime + 0.3);
            });
        };
    }

    createStreakSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(600, now);
            oscillator.frequency.exponentialRampToValueAtTime(1200, now + 0.4);
            oscillator.type = 'square';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.3, now + 0.02);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.4);
        };
    }

    createRewardFanfare() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const fanfare = [
                { freq: 261.63, time: 0 },    // C4
                { freq: 329.63, time: 0.1 },  // E4
                { freq: 392.00, time: 0.2 },  // G4
                { freq: 523.25, time: 0.3 },  // C5
                { freq: 659.25, time: 0.4 },  // E5
                { freq: 783.99, time: 0.5 },  // G5
                { freq: 1046.5, time: 0.6 }   // C6
            ];
            
            fanfare.forEach(note => {
                const oscillator = this.audioContext.createOscillator();
                const gainNode = this.audioContext.createGain();
                
                oscillator.frequency.setValueAtTime(note.freq, now);
                oscillator.type = 'triangle';
                
                const startTime = now + note.time;
                gainNode.gain.setValueAtTime(0, startTime);
                gainNode.gain.linearRampToValueAtTime(this.volume * 0.35, startTime + 0.02);
                gainNode.gain.exponentialRampToValueAtTime(0.001, startTime + 0.8);
                
                oscillator.connect(gainNode);
                gainNode.connect(this.audioContext.destination);
                
                oscillator.start(startTime);
                oscillator.stop(startTime + 0.8);
            });
        };
    }

    createClickSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(800, now);
            oscillator.type = 'sine';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.1, now + 0.01);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.08);
        };
    }

    createWhooshSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(150, now);
            oscillator.frequency.exponentialRampToValueAtTime(600, now + 0.2);
            oscillator.type = 'sawtooth';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.12, now + 0.05);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.2);
        };
    }

    createNotificationSound() {
        return () => {
            if (!this.enabled) return;
            
            const now = this.audioContext.currentTime;
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.frequency.setValueAtTime(880, now);
            oscillator.frequency.setValueAtTime(1760, now + 0.1);
            oscillator.type = 'sine';
            
            gainNode.gain.setValueAtTime(0, now);
            gainNode.gain.linearRampToValueAtTime(this.volume * 0.2, now + 0.02);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.start(now);
            oscillator.stop(now + 0.3);
        };
    }

    // Public methods
    playCorrect() { this.sounds.correct?.(); }
    playWrong() { this.sounds.wrong?.(); }
    playShieldLoss() { this.sounds.shieldLoss?.(); }
    playShieldGain() { this.sounds.shieldGain?.(); }
    playLevelUp() { this.sounds.levelUp?.(); }
    playBadgeEarned() { this.sounds.badgeEarned?.(); }
    playStreakBonus() { this.sounds.streakBonus?.(); }
    playRewardScreen() { this.sounds.rewardScreen?.(); }
    playClick() { this.sounds.click?.(); }
    playWhoosh() { this.sounds.whoosh?.(); }
    playNotification() { this.sounds.notification?.(); }

    setVolume(volume) {
        this.volume = Math.max(0, Math.min(1, volume));
    }

    setEnabled(enabled) {
        this.enabled = enabled;
    }

    toggle() {
        this.enabled = !this.enabled;
        return this.enabled;
    }
}