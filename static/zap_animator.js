/**
 * Enhanced ZapAnimator for Cloud Orbit - Slay the Spire Edition
 * 
 * Inspired by Duolingo's character animation system with Rive-like state management
 * Optimized for mobile with touch-friendly interactions and contextual animations
 * Supports Slay the Spire room types and battle feedback
 */

export default class EnhancedZapAnimator {
    constructor(mascotElement, speechBubbleElement, canvasElement = null) {
        this.mascot = mascotElement;
        this.speech = speechBubbleElement;
        this.canvas = canvasElement;
        this.currentState = 'idle';
        this.animationTimer = null;
        this.idleTimer = null;
        this.lipSyncActive = false;

        // Enhanced state system inspired by Duolingo
        this.states = {
            // Basic states
            idle: {
                cssClass: 'zap-idle',
                duration: 4000,
                messages: [
                    'Ready for your next challenge!',
                    'What AWS service shall we explore?',
                    'Your knowledge grows stronger!',
                    'The cloud awaits your mastery!'
                ],
                variations: ['idle-default', 'idle-blink', 'idle-look-around', 'idle-nod']
            },

            // Battle states (Slay the Spire inspired)
            battle_ready: {
                cssClass: 'zap-battle-ready',
                duration: 2000,
                messages: [
                    'Battle stations! Time to test your knowledge!',
                    'Ready to face this challenge!',
                    'Let\'s conquer this together!'
                ]
            },

            victory: {
                cssClass: 'zap-victory',
                duration: 3000,
                messages: [
                    'Excellent! You\'ve mastered that concept!',
                    'Victory! Your AWS skills are growing!',
                    'Outstanding work! Ready for the next challenge?',
                    'Perfect! You\'re becoming a cloud expert!'
                ]
            },

            defeat: {
                cssClass: 'zap-defeat',
                duration: 2500,
                messages: [
                    'Don\'t worry! Learning comes from trying!',
                    'Almost there! You\'ll get it next time!',
                    'Every expert was once a beginner!',
                    'Keep going! You\'re closer than you think!'
                ]
            },

            // Elite battle states
            elite_victory: {
                cssClass: 'zap-elite-victory',
                duration: 4000,
                messages: [
                    '🏆 Elite defeated! You\'re truly skilled!',
                    '👑 Masterful! That was no easy challenge!',
                    '⚡ Incredible! You\'ve proven your expertise!'
                ]
            },

            // Boss battle states  
            boss_encounter: {
                cssClass: 'zap-boss-encounter',
                duration: 3000,
                messages: [
                    '🐉 Boss battle! This is the ultimate test!',
                    '💀 Face your greatest challenge!',
                    '👹 The final trial awaits!'
                ]
            },

            boss_victory: {
                cssClass: 'zap-boss-victory',
                duration: 5000,
                messages: [
                    '🎉 BOSS DEFEATED! You are a true AWS champion!',
                    '👑 LEGENDARY! You\'ve conquered the ultimate test!',
                    '🚀 MASTER ACHIEVED! Your skills are unmatched!'
                ]
            },

            // Learning states
            explaining: {
                cssClass: 'zap-explaining',
                duration: 0, // Variable duration based on content
                messages: [
                    'Let me explain this concept...',
                    'Here\'s how this works...',
                    'This is an important detail...'
                ]
            },

            hint: {
                cssClass: 'zap-hint',
                duration: 3000,
                messages: [
                    '💡 Here\'s a helpful hint...',
                    '🔍 Think about the documentation...',
                    '⚡ Remember the best practices!',
                    '🎯 Focus on the key concepts!'
                ]
            },

            // Progression states
            level_up: {
                cssClass: 'zap-level-up',
                duration: 4000,
                messages: [
                    '🚀 Level up! New abilities unlocked!',
                    '⭐ Zap evolved! Your knowledge expands!',
                    '🎊 Congratulations! You\'ve advanced!'
                ]
            },

            streak_celebration: {
                cssClass: 'zap-streak',
                duration: 3500,
                messages: [
                    '🔥 Streak unlocked! You\'re on fire!',
                    '⚡ Amazing streak! Keep it going!',
                    '🌟 Stellar streak! Unstoppable!'
                ]
            },

            // Loot and rewards
            loot_found: {
                cssClass: 'zap-loot-found',
                duration: 3000,
                messages: [
                    '🎁 Treasure found! Check your inventory!',
                    '💎 Rare loot discovered!',
                    '🏆 Valuable knowledge acquired!'
                ]
            },

            // Rest and recovery states
            resting: {
                cssClass: 'zap-resting',
                duration: 2000,
                messages: [
                    '😴 Taking a well-deserved rest...',
                    '🛡️ Shields recharged! Ready to continue!',
                    '💤 Rest up! The journey continues!'
                ]
            },

            // Shopping states
            shopping: {
                cssClass: 'zap-shopping',
                duration: 2500,
                messages: [
                    '🛒 Welcome to the knowledge shop!',
                    '💰 Wise investments await!',
                    '🏪 Choose your upgrades carefully!'
                ]
            },

            // Event states
            curious: {
                cssClass: 'zap-curious',
                duration: 2000,
                messages: [
                    '🤔 Interesting choice ahead...',
                    '❓ What path will you choose?',
                    '🎲 Fortune favors the bold!'
                ]
            },

            // Error states
            confused: {
                cssClass: 'zap-confused',
                duration: 2000,
                messages: [
                    '🤔 Hmm, something\'s not quite right...',
                    '❓ Let me think about this...',
                    '🔄 Let\'s try that again!'
                ]
            }
        };

        // Start idle animation cycle
        this.startIdleCycle();
    }

    /**
     * Play an animation state with enhanced mobile optimization
     * @param {string} stateName - State to play
     * @param {Object} options - Additional options (message, duration, callback)
     */
    play(stateName, options = {}) {
        const state = this.states[stateName];
        if (!state) {
            console.warn(`Animation state '${stateName}' not found`);
            return;
        }

        // Clear existing timers
        this.clearTimers();

        // Remove all existing state classes
        this.clearAllStates();

        // Set new state
        this.currentState = stateName;
        this.mascot.classList.add(state.cssClass);

        // Show message
        const message = options.message || this.getRandomMessage(state);
        this.showMessage(message, options.messageType);

        // Handle lip sync for explanation states
        if (stateName === 'explaining' && options.audioData) {
            this.startLipSync(options.audioData);
        }

        // Set animation duration
        const duration = options.duration || state.duration;
        if (duration > 0) {
            this.animationTimer = setTimeout(() => {
                this.returnToIdle();
                if (options.callback) options.callback();
            }, duration);
        }

        // Trigger haptic feedback on mobile
        this.triggerHapticFeedback(stateName);
    }

    /**
     * Enhanced idle system with multiple variations
     */
    startIdleCycle() {
        this.idleTimer = setInterval(() => {
            if (this.currentState === 'idle') {
                const variation = this.getRandomIdleVariation();
                this.playIdleVariation(variation);
            }
        }, 8000); // Change idle animation every 8 seconds
    }

    getRandomIdleVariation() {
        const variations = this.states.idle.variations;
        return variations[Math.floor(Math.random() * variations.length)];
    }

    playIdleVariation(variation) {
        this.mascot.classList.remove('zap-idle');
        this.mascot.classList.add(`zap-${variation}`);

        setTimeout(() => {
            this.mascot.classList.remove(`zap-${variation}`);
            this.mascot.classList.add('zap-idle');
        }, 2000);
    }

    /**
     * Room-specific animations based on Slay the Spire mechanics
     */
    playRoomEntry(roomType) {
        const roomAnimations = {
            'battle': 'battle_ready',
            'elite': 'battle_ready',
            'boss': 'boss_encounter',
            'shop': 'shopping',
            'event': 'curious',
            'rest': 'resting'
        };

        const animation = roomAnimations[roomType] || 'battle_ready';
        this.play(animation);
    }

    playBattleResult(correct, roomType = 'battle') {
        if (correct) {
            const victoryAnimations = {
                'battle': 'victory',
                'elite': 'elite_victory',
                'boss': 'boss_victory'
            };
            this.play(victoryAnimations[roomType] || 'victory');
        } else {
            this.play('defeat');
        }
    }

    /**
     * Duolingo-inspired lip sync system (simplified)
     */
    startLipSync(audioData) {
        if (!audioData || this.lipSyncActive) return;

        this.lipSyncActive = true;
        const phonemes = this.parsePhonemes(audioData);

        phonemes.forEach((phoneme, index) => {
            setTimeout(() => {
                this.updateMouthShape(phoneme.shape);
            }, phoneme.timing);
        });

        // Clear lip sync after audio ends
        setTimeout(() => {
            this.lipSyncActive = false;
            this.updateMouthShape('closed');
        }, audioData.duration);
    }

    parsePhonemes(audioData) {
        // Simplified phoneme parsing
        // In a real implementation, this would use speech recognition
        return audioData.phonemes || [];
    }

    updateMouthShape(shape) {
        // Remove existing mouth shapes
        const mouthShapes = ['mouth-closed', 'mouth-open', 'mouth-wide', 'mouth-small'];
        mouthShapes.forEach(shape => this.mascot.classList.remove(shape));

        // Add new mouth shape
        this.mascot.classList.add(`mouth-${shape}`);
    }

    /**
     * Mobile optimization features
     */
    triggerHapticFeedback(stateName) {
        if (!navigator.vibrate) return;

        const hapticPatterns = {
            'victory': [100],
            'elite_victory': [100, 50, 100],
            'boss_victory': [200, 100, 200, 100, 200],
            'defeat': [50],
            'level_up': [100, 50, 100, 50, 100],
            'loot_found': [150]
        };

        const pattern = hapticPatterns[stateName];
        if (pattern) {
            navigator.vibrate(pattern);
        }
    }

    /**
     * Adaptive message system based on user progress
     */
    getRandomMessage(state) {
        let messages = state.messages;

        // Could customize messages based on user progress, time of day, etc.
        return messages[Math.floor(Math.random() * messages.length)];
    }

    showMessage(message, type = 'default') {
        if (!this.speech) return;

        this.speech.textContent = message;
        this.speech.classList.remove('speech-success', 'speech-error', 'speech-info');

        if (type === 'success') this.speech.classList.add('speech-success');
        else if (type === 'error') this.speech.classList.add('speech-error');
        else if (type === 'info') this.speech.classList.add('speech-info');

        this.speech.classList.add('visible');

        // Auto-hide message after reading time
        const readingTime = Math.max(2000, message.length * 50);
        setTimeout(() => {
            this.speech.classList.remove('visible');
        }, readingTime);
    }

    /**
     * Utility methods
     */
    clearTimers() {
        if (this.animationTimer) {
            clearTimeout(this.animationTimer);
            this.animationTimer = null;
        }
    }

    clearAllStates() {
        Object.values(this.states).forEach(state => {
            this.mascot.classList.remove(state.cssClass);
        });
    }

    returnToIdle() {
        this.clearAllStates();
        this.currentState = 'idle';
        this.mascot.classList.add('zap-idle');
    }

    /**
     * Advanced animation chaining
     */
    playSequence(sequence) {
        if (!sequence.length) return;

        const playNext = (index) => {
            if (index >= sequence.length) return;

            const step = sequence[index];
            this.play(step.state, {
                ...step.options,
                callback: () => {
                    if (step.options?.callback) step.options.callback();
                    setTimeout(() => playNext(index + 1), step.delay || 0);
                }
            });
        };

        playNext(0);
    }

    /**
     * Cleanup
     */
    destroy() {
        this.clearTimers();
        if (this.idleTimer) {
            clearInterval(this.idleTimer);
        }
        this.clearAllStates();
    }
}

// Export utility functions for integration
export const ZapAnimationUtils = {
    /**
     * Create animation sequence for lesson completion
     */
    createCompletionSequence(correct, roomType, hasLoot = false) {
        const sequence = [];

        if (correct) {
            sequence.push({
                state: roomType === 'boss' ? 'boss_victory' : 
                       roomType === 'elite' ? 'elite_victory' : 'victory',
                options: { messageType: 'success' },
                delay: 500
            });

            if (hasLoot) {
                sequence.push({
                    state: 'loot_found',
                    options: { messageType: 'info' },
                    delay: 1000
                });
            }
        } else {
            sequence.push({
                state: 'defeat',
                options: { messageType: 'error' },
                delay: 500
            });
        }

        return sequence;
    },

    /**
     * Get appropriate animation for room type
     */
    getRoomAnimation(roomType) {
        const animations = {
            'battle': 'battle_ready',
            'elite': 'battle_ready', 
            'boss': 'boss_encounter',
            'shop': 'shopping',
            'event': 'curious',
            'rest': 'resting'
        };

        return animations[roomType] || 'battle_ready';
    }
};
