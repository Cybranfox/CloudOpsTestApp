/**
 * Cloud Orbit — Capacitor Local Notifications
 * Streak reminders + daily challenge nudge (Duolingo model).
 *
 * Wired when Capacitor is available (Android/iOS).
 * Falls back silently in browser / PWA mode.
 */

const Notifications = {
    async requestPermission() {
        if (typeof Capacitor === 'undefined') return false;
        try {
            const { LocalNotifications } = await import(
                '@capacitor/local-notifications'
            );
            const result = await LocalNotifications.requestPermissions();
            return result.display === 'granted';
        } catch {
            return false;
        }
    },

    async scheduleStreakReminder(hour = 18, minute = 0) {
        if (typeof Capacitor === 'undefined') return;
        try {
            const { LocalNotifications } = await import(
                '@capacitor/local-notifications'
            );
            await LocalNotifications.schedule({
                notifications: [{
                    id: 1,
                    title: 'Cloud Orbit',
                    body: 'Keep your streak alive! Complete today\'s daily challenge.',
                    schedule: {
                        on: { hour, minute },
                        every: 'day',
                    },
                }],
            });
        } catch {
            // Silent fail — notifications are a nice-to-have
        }
    },

    async scheduleInactiveReminder(days = 3) {
        if (typeof Capacitor === 'undefined') return;
        try {
            const { LocalNotifications } = await import(
                '@capacitor/local-notifications'
            );
            // Fire if app hasn't been opened in N days
            const since = new Date();
            since.setDate(since.getDate() - days);
            await LocalNotifications.schedule({
                notifications: [{
                    id: 2,
                    title: 'Zap misses you!',
                    body: 'Your cloud skills are getting rusty. Come back for a quick battle!',
                    schedule: { at: since },
                }],
            });
        } catch {
            // Silent fail
        }
    },

    async cancelAll() {
        if (typeof Capacitor === 'undefined') return;
        try {
            const { LocalNotifications } = await import(
                '@capacitor/local-notifications'
            );
            await LocalNotifications.cancel({ notifications: [{ id: 1 }, { id: 2 }] });
        } catch {
            // Silent fail
        }
    },
};

// Auto-request on first interaction
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => Notifications.requestPermission(), 3000);
});

export default Notifications;
