/**
 * Cloud Orbit — Offline Engine
 * Client-side quiz logic + localStorage progress when Flask backend is unavailable.
 * Used in Capacitor APK / PWA offline mode.
 */

const CloudOrbitOffline = {
    // ── Progress (localStorage) ──────────────────────────────────────────
    _progress: null,

    loadProgress() {
        try {
            const raw = localStorage.getItem('cloud_orbit_progress');
            if (raw) {
                this._progress = JSON.parse(raw);
                return this._progress;
            }
        } catch (e) { /* corrupt, reset */ }
        this._progress = {
            xp: 0, streak: 0, energy: 3, max_energy: 3,
            badges: [], completed_lessons: [], weak_spots: [],
            inventory: { relics: [], potions: [], gems: 0, cards: [] },
            stats: { total_questions: 0, correct_answers: 0,
                     battles_won: 0, elites_defeated: 0, bosses_defeated: 0,
                     streak_best: 0, runs_completed: 0 },
            achievements: [], ascension_level: 0, relic_uses: {},
        };
        return this._progress;
    },

    saveProgress() {
        try {
            localStorage.setItem('cloud_orbit_progress', JSON.stringify(this._progress));
        } catch (e) { /* quota exceeded, ignore */ }
    },

    getProgress() {
        return this._progress || this.loadProgress();
    },

    // ── Quiz Engine ─────────────────────────────────────────────────────
    checkAnswer(lessonData, userAnswer) {
        const progress = this.getProgress();
        progress.stats.total_questions = (progress.stats.total_questions || 0) + 1;

        let correct = false;
        if (Array.isArray(lessonData.answer)) {
            correct = JSON.stringify([...userAnswer].sort()) ===
                      JSON.stringify([...lessonData.answer].sort());
        } else {
            correct = userAnswer === lessonData.answer;
        }

        if (correct) {
            progress.stats.correct_answers = (progress.stats.correct_answers || 0) + 1;
            progress.xp = (progress.xp || 0) + 20;
            progress.energy = Math.min(progress.max_energy, (progress.energy || 3) + 1);

            // Track completion
            if (progress.completed_lessons.indexOf(lessonData.id) === -1) {
                progress.completed_lessons.push(lessonData.id);
            }
            // Remove from weak spots
            const ws = progress.weak_spots || [];
            const idx = ws.indexOf(lessonData.id);
            if (idx !== -1) ws.splice(idx, 1);

            // Room type stats
            const rt = lessonData.room_type || 'battle';
            if (rt === 'battle') progress.stats.battles_won = (progress.stats.battles_won || 0) + 1;
            else if (rt === 'elite') progress.stats.elites_defeated = (progress.stats.elites_defeated || 0) + 1;
            else if (rt === 'boss') progress.stats.bosses_defeated = (progress.stats.bosses_defeated || 0) + 1;

            // Gems based on difficulty
            const diff = lessonData.difficulty || 'easy';
            const gemReward = { easy: 1, medium: 2, hard: 3 }[diff] || 1;
            progress.inventory.gems = (progress.inventory.gems || 0) + gemReward;

            // Award badge
            const badge = lessonData.badge;
            if (badge && progress.badges.indexOf(badge) === -1) {
                progress.badges.push(badge);
            }

        } else {
            progress.energy = Math.max(0, (progress.energy || 3) - 1);
            // Track weak spot
            const ws = progress.weak_spots || [];
            if (ws.indexOf(lessonData.id) === -1) ws.push(lessonData.id);
            progress.weak_spots = ws;
        }

        this.saveProgress();
        return {
            correct,
            progress,
            explanation: lessonData.explanation || '',
            badge: correct ? lessonData.badge : null,
            gemReward: correct ? ({ easy: 1, medium: 2, hard: 3 }[lessonData.difficulty || 'easy'] || 1) : 0,
        };
    },

    // ── Get next lesson ─────────────────────────────────────────────────
    getNextLessonId(currentId, allIds) {
        const idx = allIds.indexOf(currentId);
        if (idx !== -1 && idx < allIds.length - 1) return allIds[idx + 1];
        return null;
    },

    // ── Is backend available? ───────────────────────────────────────────
    _backendAvailable: null,

    async checkBackend() {
        if (this._backendAvailable !== null) return this._backendAvailable;
        try {
            const resp = await fetch('/api/progress', { method: 'HEAD' });
            this._backendAvailable = resp.ok;
        } catch {
            this._backendAvailable = false;
        }
        return this._backendAvailable;
    },
};

// Export for module use
if (typeof module !== 'undefined') module.exports = CloudOrbitOffline;
