/* Decision Wizard service worker. It keeps a copy of the wizard so the installed app opens offline.
   Online, the newest version always loads: the network is tried first, and the copy is used only when the network fails. */
"use strict";
var CACHE = "decision-wizard-app";
var CORE = ["./", "./index.html"];
var EXTRA = ["./manifest.webmanifest", "./icons/icon-192.png", "./icons/icon-512.png", "./icons/icon-maskable-512.png"];

self.addEventListener("install", function(ev){
  ev.waitUntil(caches.open(CACHE).then(function(c){
    return c.addAll(CORE).then(function(){
      return Promise.all(EXTRA.map(function(u){ return c.add(u).catch(function(){}); }));
    });
  }).then(function(){ return self.skipWaiting(); }));
});
self.addEventListener("activate", function(ev){
  ev.waitUntil(self.clients.claim());
});
function keep(req, res){
  if(res && res.ok){ var copy = res.clone(); caches.open(CACHE).then(function(c){ c.put(req, copy); }); }
  return res;
}
self.addEventListener("fetch", function(ev){
  var req = ev.request;
  if(req.method !== "GET") return;
  var url = new URL(req.url);
  if(url.origin === self.location.origin){
    ev.respondWith(fetch(req).then(function(res){ return keep(req, res); }).catch(function(){
      return caches.match(req, { ignoreSearch: true }).then(function(hit){ return hit || (req.mode === "navigate" ? caches.match("./index.html") : Response.error()); });
    }));
    return;
  }
  if(url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com"){
    ev.respondWith(caches.match(req).then(function(hit){ return hit || fetch(req).then(function(res){ return keep(req, res); }); }));
  }
});
