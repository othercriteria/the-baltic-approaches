/* The plate's hover panel (book-site.md §6.1): mouseover/focus on a
   node or edge shows its atlas record — reference affordance, not
   decoration. Vanilla JS, no requests; the entries ride inline in
   #atlas-data. */
(function () {
  "use strict";
  var dataEl = document.getElementById("atlas-data");
  var panel = document.getElementById("atlas-panel");
  if (!dataEl || !panel) return;
  var entries = JSON.parse(dataEl.textContent);
  var idle = panel.innerHTML;
  var current = null;

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function fmtCap(n) {
    return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }

  function show(key) {
    var e = entries[key];
    if (!e) return;
    var kind = key.charAt(0) === "e" ? "edge" : "node";
    var h = "<h3>" + esc(e.name) + "</h3>";
    var bits = [];
    if (kind === "edge") {
      var cls = e.mode === "road" ? e["class"] : e.mode;
      if (e.tracks) cls += ", " + e.tracks + " track";
      bits.push(esc(cls));
      if (e.route) bits.push(esc(e.route));
      if (e.km) bits.push(e.km + " km");
      h += '<p class="fields">' + bits.join(" · ");
      if (e.cap_t_d) {
        h +=
          " · " + fmtCap(e.cap_t_d) + " t/day" +
          '<span class="tier" title="capacity source grade">' +
          esc(e.provenance) + "</span>";
      }
      h += "</p>";
    } else {
      if (e.region) bits.push(esc(e.region));
      if (bits.length) h += '<p class="fields">' + bits.join(" · ") + "</p>";
    }
    if (e.notes) h += '<p class="notes">' + esc(e.notes) + "</p>";
    panel.innerHTML = h;
  }

  function clear() {
    if (current) current.classList.remove("hl");
    current = null;
    panel.innerHTML = idle;
  }

  var hits = document.querySelectorAll("[data-a]");
  Array.prototype.forEach.call(hits, function (el) {
    var key = el.getAttribute("data-a");
    function on() {
      if (current) current.classList.remove("hl");
      current = el;
      el.classList.add("hl");
      show(key);
    }
    el.addEventListener("mouseenter", on);
    el.addEventListener("focus", on);
    el.addEventListener("click", function (ev) {
      on();
      ev.stopPropagation();
    });
  });
  document.addEventListener("click", function (ev) {
    if (!ev.target.closest || !ev.target.closest("[data-a]")) clear();
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") clear();
  });
})();
