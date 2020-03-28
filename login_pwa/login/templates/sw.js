self.addEventListener('install', (event) => {
    console.log('service worker installed', event);
});
self.addEventListener('activate', (event) => {
  console.log('service worker activated', event);
});


self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request).then((response) => {
          console.log('fetched from network this time!');
          return caches.open('version1').then((cache) => {
            cache.put(event.request, response.clone());
            return response;
          });
        });
    })
  );
});
