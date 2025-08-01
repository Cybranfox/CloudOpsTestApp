/* Simple service worker for AWS Orbit PWA prototype.
 *
 * This service worker caches the app shell and API responses to enable
 * offline usage. In production, you would add more sophisticated caching
 * strategies (e.g. stale-while-revalidate) and precache important assets.
 */
const CACHE_NAME = 'aws-orbit-pwa-v1';
const APP_SHELL = [
  '/',
  '/index.html',
  '/static/styles.css',
  '/static/zap.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(APP_SHELL))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener('activate', event => {
  const allowedCaches = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(keys => Promise.all(keys.map(key => {
      if (!allowedCaches.includes(key)) {
        return caches.delete(key);
      }
    })))
  );
});