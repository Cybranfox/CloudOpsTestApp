const CACHE_NAME = 'cloudquest-v1.0';
const STATIC_ASSETS = [
  '/',
  '/?mode=offline',
  '/badges',
  '/static/styles.css',
  '/static/zap_animator.js', 
  '/static/enhanced_zap_animator.js',
  '/static/audio_integration.js',
  '/static/zap.png',
  '/static/mascot/zap_idle.png',
  '/static/mascot/zap_curious.png', 
  '/static/mascot/zap_victory.png',
  '/static/mascot/zap_levelup.png',
  '/static/mascot/zap_defeat.png',
  '/static/mascot/zap_sleeping.png',
  '/static/mascot/zap_shopping.png',
  '/static/mascot/zap_explaining.png'
];

// Install event - cache static assets
self.addEventListener('install', event => {
  console.log('📦 CloudQuest PWA installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('💾 Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate event - cleanup old caches
self.addEventListener('activate', event => {
  console.log('🚀 CloudQuest PWA activated');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('🗑️ Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', event => {
  // Cache-first strategy for static assets
  if (event.request.url.includes('/static/') || 
      event.request.url.includes('/?mode=offline')) {
    event.respondWith(
      caches.match(event.request)
        .then(response => {
          if (response) {
            return response; // Serve from cache
          }
          return fetch(event.request); // Fallback to network
        })
        .catch(() => {
          // If both cache and network fail, return offline page
          if (event.request.destination === 'document') {
            return caches.match('/?mode=offline');
          }
        })
    );
  }
});

// Background sync for progress data
self.addEventListener('sync', event => {
  if (event.tag === 'progress-sync') {
    console.log('🔄 Syncing progress data...');
    // Handle progress sync when connection is restored
  }
});
