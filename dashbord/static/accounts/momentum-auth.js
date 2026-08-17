document.addEventListener("DOMContentLoaded", () => {
  const passwordToggles = document.querySelectorAll("[data-password-toggle]");

  passwordToggles.forEach((toggle) => {
    toggle.addEventListener("click", () => {
      const targetId = toggle.getAttribute("data-password-toggle");
      const input = document.getElementById(targetId);
      if (!input) return;

      const isPassword = input.type === "password";
      input.type = isPassword ? "text" : "password";
      toggle.setAttribute("aria-label", isPassword ? "Hide password" : "Show password");
      toggle.textContent = isPassword ? "Hide" : "Show";
    });
  });
});
