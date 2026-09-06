/* Service worker minimo del portale "Comitato feste 87".
 *
 * Scopo: rendere la pagina installabile (PWA) e apribile anche offline nel suo
 * guscio, SENZA mai mettere in cache le risposte /api (dati + auth: devono
 * sempre passare dalla rete). Alza CACHE_VERSION a ogni modifica al guscio per
 * forzare l'aggiornamento della cache sui client gia' installati. */
const CACHE_VERSION = "v1";
const CACHE_NAME = `cf87-shell-${CACHE_VERSION}`;

const SHELL = [
  "/",
  "/index.html",
  "/manifest.webmanifest",
  "/icon-192.png",
  "/icon-512.png",
  "/icon-maskable-512.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (url.pathname.startsWith("/api/")) return;   // dati e auth: sempre rete, mai cache

  // Navigazioni (apertura app): rete prima, guscio dalla cache se offline.
  if (req.mode === "navigate") {
    event.respondWith(
      fetch(req).catch(() => caches.match("/index.html", { ignoreSearch: true }))
    );
    return;
  }

  // Asset statici del guscio (icone, manifest): cache prima, poi rete + aggiorna.
  event.respondWith(
    caches.match(req).then((hit) => {
      const net = fetch(req).then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => hit);
      return hit || net;
    })
  );
});
