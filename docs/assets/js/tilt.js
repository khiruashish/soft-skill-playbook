/* Soft Skill Playbook — lightweight 3D tilt for cards (no dependencies). */
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var MAX = 8; // degrees

  function bind(el) {
    if (el.dataset.sspTilt) return;
    el.dataset.sspTilt = "1";
    el.addEventListener("mousemove", function (e) {
      var r = el.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform =
        "perspective(800px) rotateX(" + (-y * MAX).toFixed(2) + "deg) rotateY(" +
        (x * MAX).toFixed(2) + "deg) translateZ(6px)";
    });
    el.addEventListener("mouseleave", function () { el.style.transform = ""; });
  }

  function init() {
    if (reduce) return;
    document.querySelectorAll(".md-typeset .grid.cards > ul > li").forEach(bind);
  }

  // Works with Material's instant navigation and with plain page loads.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
