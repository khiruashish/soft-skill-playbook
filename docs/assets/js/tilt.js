/* Soft Skill Playbook: site-wide 3D interactions (no dependencies).
   - tilt for cards
   - mouse parallax for the hero and page banners
   - 3D scroll-reveal for page sections */
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia && window.matchMedia("(pointer: fine)").matches;
  var observer = null;

  function tilt(el, max, base) {
    if (el.dataset.sspTilt) return;
    el.dataset.sspTilt = "1";
    el.addEventListener("mousemove", function (e) {
      var r = el.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform = "perspective(900px) rotateX(" + (-y * max).toFixed(2) + "deg) rotateY(" +
        (x * max).toFixed(2) + "deg) " + (base || "translateZ(6px)");
    });
    el.addEventListener("mouseleave", function () { el.style.transform = ""; });
  }

  function reveal() {
    var targets = document.querySelectorAll(
      ".md-typeset > h2, .md-typeset > .admonition, .md-typeset > details, .md-typeset > table, " +
      ".md-typeset > .tabbed-set, .md-typeset > .highlight, .md-typeset > .ssp-say, " +
      ".md-typeset > .ssp-stack, .md-typeset > .grid, .md-typeset > .md-typeset__scrollwrap, " +
      ".md-typeset > .ssp-chat, .md-typeset > .ssp-day"
    );
    if (!("IntersectionObserver" in window)) return;
    if (observer) observer.disconnect();
    observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("ssp-in"); observer.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    targets.forEach(function (el) {
      // anything already on screen shows immediately
      var r = el.getBoundingClientRect();
      el.classList.add("ssp-reveal");
      if (r.top < window.innerHeight) el.classList.add("ssp-in");
      else observer.observe(el);
    });
  }

  /* ---- Course progress: ticked days are remembered in this browser only ---- */
  var KEY = "ssp-course-progress"; // keys are lesson paths, e.g. "everyday/gym"
  function loadDone() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; }
  }
  function saveDone(d) {
    try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) { /* storage blocked: ignore */ }
  }
  function progress() {
    var done = loadDone();
    document.querySelectorAll("input.ssp-done").forEach(function (box) {
      var day = box.getAttribute("data-day");
      box.checked = !!done[day];
      var card = box.closest(".ssp-day");
      if (card) card.classList.toggle("is-done", box.checked);
      if (box.dataset.sspBound) return;
      box.dataset.sspBound = "1";
      box.addEventListener("change", function () {
        var d = loadDone();
        if (box.checked) d[day] = 1; else delete d[day];
        saveDone(d);
        progress();
      });
    });
    var counter = document.querySelector(".ssp-roadmap-progress");
    if (counter) {
      var boxes = document.querySelectorAll("table input.ssp-done");
      var ticked = Array.prototype.filter.call(boxes, function (b) { return b.checked; }).length;
      counter.textContent = "Your progress: " + ticked + " of " + boxes.length + " days done";
    }
  }

  function init() {
    progress();
    if (reduce) return;
    document.documentElement.classList.add("ssp-js");
    reveal();
    if (!fine) return; // no hover effects on touch screens
    document.querySelectorAll(".md-typeset .grid.cards > ul > li").forEach(function (el) { tilt(el, 8); });
    document.querySelectorAll(".ssp-banner, .ssp-hero").forEach(function (el) { tilt(el, 4, ""); });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);   // Material instant navigation
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
