
// Hamburger toggle
const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");
const overlay = document.getElementById("nav-overlay");

if (menuToggle) {
  menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("show");
    overlay.classList.toggle("show");
  });
}

if (overlay) {
  overlay.addEventListener("click", () => {
    navLinks.classList.remove("show");
    overlay.classList.remove("show");
  });
}

// Auto-expand textarea
document.addEventListener("input", function (e) {
  if (e.target.tagName.toLowerCase() === "textarea") {
    e.target.style.height = "auto"; // reset
    e.target.style.height = e.target.scrollHeight + "px"; // expand
  }
});
