const CACHE_NAME = 'cloud-orbit-v2.0';
const STATIC_ASSETS = [
    '/',
    '/daily',
    '/weekly',
    '/progress',
    '/badges',
    '/practice',
    '/onboarding',
    '/privacy',
    '/terms',
    '/static/styles.css',
    '/static/zap_animator.js',
    '/static/audio_integration.js',
    '/static/space_adventure_enhanced.js',
    '/static/zap.png',
    '/static/mascot/zap_idle.png',
    '/static/mascot/zap_curious.png',
    '/static/mascot/zap_victory.png',
    '/static/mascot/zap_levelup.png',
    '/static/mascot/zap_defeat.png',
    '/static/mascot/zap_sleeping.png',
    '/static/mascot/zap_shopping.png',
    '/static/mascot/zap_explaining.png',
    '/static/manifest.json',
];

// Install — cache all static assets for offline use
self.addEventListener('install', event => {
    console.log('Cloud Orbit PWA installing...');
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(STATIC_ASSETS))
            .then(() => self.skipWaiting())
    );
});

// Activate — purge old caches
self.addEventListener('activate', event => {
    console.log('Cloud Orbit PWA activated');
    event.waitUntil(
        caches.keys().then(names => Promise.all(
            names.filter(n => n !== CACHE_NAME).map(n => caches.delete(n))
        )).then(() => self.clients.claim())
    );
});

// Fetch — cache-first for static, network-first for API
self.addEventListener('fetch', event => {
    const url = event.request.url;

    // API calls — network first (always get fresh data)
    if (url.includes('/api/')) {
        event.respondWith(
            fetch(event.request)
                .catch(() => caches.match(event.request))
        );
        return;
    }

    // Static + pages — cache first (offline-ready)
    event.respondWith(
        caches.match(event.request)
            .then(cached => cached || fetch(event.request).then(resp => {
                // Cache new pages dynamically
                if (resp.ok && resp.type === 'basic') {
                    const clone = resp.clone();
                    caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
                }
                return resp;
            }))
            .catch(() => {
                // Offline fallback for navigation
                if (event.request.destination === 'document') {
                    return caches.match('/');
                }
            })
    );
});
