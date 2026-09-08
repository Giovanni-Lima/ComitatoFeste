/* Service worker minimo del portale "Comitato feste 87".
 *
 * Scopo: rendere la pagina installabile (PWA) e apribile anche offline nel suo
 * guscio, SENZA mai mettere in cache le risposte /api (dati + auth: devono
 * sempre passare dalla rete). Alza CACHE_VERSION a ogni modifica al guscio per
 * forzare l'aggiornamento della cache sui client gia' installati. */
const CACHE_VERSION = "v7";
const CACHE_NAME = `cf87-shell-${CACHE_VERSION}`;

const SHELL = [
  "/",
  "/index.html",
  "/manifest.webmanifest",
  "/icon-192.png",
  "/icon-512.png",
  "/icon-maskable-512.png",
  "/fonts/ThaleahFat.woff2",
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

/* --- Web Push -----------------------------------------------------------
 * L'API (PushSender) invia un payload JSON { title, body, url, tag }.
 * Stesso `tag` per giorno ⇒ una nuova notifica dello stesso giorno
 * rimpiazza la precedente invece di impilarsi. */
self.addEventListener("push", (event) => {
  let d = {};
  try { d = event.data ? event.data.json() : {}; } catch (_) { d = {}; }
  const title = d.title || "Comitato feste 87";
  event.waitUntil(
    self.registration.showNotification(title, {
      body: d.body || "",
      icon: "/icon-192.png",
      badge: "/icon-192.png",
      tag: d.tag || "digest",
      renotify: true,
      data: { url: d.url || "/" },
    })
  );
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const target = (event.notification.data && event.notification.data.url) || "/";
  event.waitUntil((async () => {
    const wins = await self.clients.matchAll({ type: "window", includeUncontrolled: true });
    for (const c of wins) {
      if (c.url.startsWith(self.location.origin)) {
        await c.focus();
        if ("navigate" in c) { try { await c.navigate(target); } catch (_) {} }
        return;
      }
    }
    await self.clients.openWindow(target);
  })());
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
