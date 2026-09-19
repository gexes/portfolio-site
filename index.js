const menuButton = document.querySelector(".header__main-ham-menu-cont");
const smallMenu = document.querySelector(".header__sm-menu");
const openIcon = document.querySelector(".header__main-ham-menu");
const closeIcon = document.querySelector(".header__main-ham-menu-close");
function setMenu(open) {
  smallMenu.classList.toggle("header__sm-menu--active", open);
  menuButton.setAttribute("aria-expanded", String(open));
  menuButton.setAttribute(
    "aria-label",
    open ? "Close navigation" : "Open navigation",
  );
  openIcon.classList.toggle("d-none", open);
  closeIcon.classList.toggle("d-none", !open);
}
if (menuButton && smallMenu) {
  menuButton.addEventListener("click", () =>
    setMenu(menuButton.getAttribute("aria-expanded") !== "true"),
  );
  smallMenu
    .querySelectorAll("a")
    .forEach((link) => link.addEventListener("click", () => setMenu(false)));
  document.addEventListener("keydown", (event) => {
    if (
      event.key === "Escape" &&
      menuButton.getAttribute("aria-expanded") === "true"
    ) {
      setMenu(false);
      menuButton.focus();
    }
  });
  window
    .matchMedia("(min-width: 37.5em)")
    .addEventListener("change", (event) => {
      if (event.matches) setMenu(false);
    });
}
