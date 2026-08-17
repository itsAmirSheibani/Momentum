/**
 * Momentum — app.js
 * Plain vanilla JS for simple UI behaviors only.
 * No API calls, no auth, no persistence — Django will wire up the real
 * behavior later (see README "Wiring this up in Django").
 */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     Mobile sidebar drawer
  ------------------------------------------------------------------ */
  var appEl = document.querySelector(".momentum-app");
  var openBtn = document.getElementById("sidebarOpen");
  var closeBtn = document.getElementById("sidebarClose");
  var scrim = document.getElementById("sidebarScrim");

  function openSidebar() {
    appEl.classList.add("sidebar-open");
    openBtn.setAttribute("aria-expanded", "true");
  }

  function closeSidebar() {
    appEl.classList.remove("sidebar-open");
    openBtn.setAttribute("aria-expanded", "false");
  }

  if (openBtn) openBtn.addEventListener("click", openSidebar);
  if (closeBtn) closeBtn.addEventListener("click", closeSidebar);
  if (scrim) scrim.addEventListener("click", closeSidebar);

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeSidebar();
  });

  /* ------------------------------------------------------------------
     Task checkbox toggle
  ------------------------------------------------------------------ */
  var taskList = document.getElementById("taskList");

  if (taskList) {
    taskList.addEventListener("click", function (event) {
      var check = event.target.closest(".momentum-task-card__check");
      if (!check) return;

      var card = check.closest(".momentum-task-card");
      var isNowComplete = !card.classList.contains("is-completed");

      card.classList.toggle("is-completed", isNowComplete);
      check.setAttribute("aria-checked", String(isNowComplete));
      check.setAttribute(
        "aria-label",
        isNowComplete ? "Mark task incomplete" : "Mark task complete"
      );

      // Django note: this is where a fetch()/form POST would toggle
      // Task.is_completed on the backend and re-render or update counts.
    });
  }

  /* ------------------------------------------------------------------
     Task filter (client-side text match, purely presentational)
  ------------------------------------------------------------------ */
  var taskFilter = document.getElementById("taskFilter");

  if (taskFilter && taskList) {
    taskFilter.addEventListener("input", function () {
      var query = taskFilter.value.trim().toLowerCase();
      var cards = taskList.querySelectorAll(".momentum-task-card");

      cards.forEach(function (card) {
        var title = card.querySelector(".momentum-task-card__title");
        var text = title ? title.textContent.toLowerCase() : "";
        card.style.display = text.indexOf(query) !== -1 ? "" : "none";
      });
    });
  }

  /* ------------------------------------------------------------------
     Mood selection
  ------------------------------------------------------------------ */
  var moodOptions = document.querySelectorAll(".momentum-mood__option");

  moodOptions.forEach(function (option) {
    option.addEventListener("click", function () {
      moodOptions.forEach(function (other) {
        other.classList.remove("is-selected");
        other.setAttribute("aria-pressed", "false");
      });
      option.classList.add("is-selected");
      option.setAttribute("aria-pressed", "true");

      // Django note: POST { mood: option.dataset.mood } to save today's mood.
    });
  });

  /* ------------------------------------------------------------------
     Energy range display
  ------------------------------------------------------------------ */
  var energyRange = document.getElementById("energyRange");
  var energyValue = document.getElementById("energyValue");

  if (energyRange && energyValue) {
    energyRange.addEventListener("input", function () {
      energyValue.textContent = energyRange.value;
    });
  }

  /* ------------------------------------------------------------------
     Reflection note — "Add note" button
  ------------------------------------------------------------------ */
  var saveNoteBtn = document.getElementById("saveNoteBtn");
  var reflectionText = document.getElementById("reflectionText");

  if (saveNoteBtn && reflectionText) {
    saveNoteBtn.addEventListener("click", function () {
      var original = saveNoteBtn.textContent;
      saveNoteBtn.textContent = "Saved";
      setTimeout(function () {
        saveNoteBtn.textContent = original;
      }, 1200);

      // Django note: POST reflectionText.value to save/update today's Note.
    });
  }

  /* ------------------------------------------------------------------
     Add Task button (placeholder — opens nothing yet)
  ------------------------------------------------------------------ */
  var addTaskBtn = document.getElementById("addTaskBtn");

  if (addTaskBtn) {
    addTaskBtn.addEventListener("click", function () {
      // Django note: replace with a modal, drawer, or redirect to the
      // "create task" view/form once this is wired into Django.
      console.log("Add Task clicked — hook this up to a create-task form.");
    });
  }

  /* ------------------------------------------------------------------
     Today's date (only used for the static preview; Django should
     render {{ today|date:"l, F j" }} server-side instead)
  ------------------------------------------------------------------ */
  var todayDateEl = document.getElementById("todayDate");

  if (todayDateEl) {
    var today = new Date();
    var options = { weekday: "long", month: "long", day: "numeric" };
    todayDateEl.textContent = today.toLocaleDateString("en-US", options);
  }
})();
