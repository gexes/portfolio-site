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

const previews = document.querySelectorAll(".image-preview");
if (previews.length) {
  const viewer = document.createElement("dialog");
  viewer.className = "media-viewer";
  viewer.setAttribute("aria-label", "Enlarged image");
  viewer.innerHTML = '<button class="media-viewer__close" type="button">Close image</button><div class="media-viewer__picture"></div>';
  document.body.append(viewer);
  const picture = viewer.querySelector(".media-viewer__picture");
  picture.addEventListener("click", () => viewer.classList.toggle("is-zoomed"));
  viewer.addEventListener("click", event => {
    if (!picture.contains(event.target)) viewer.close();
  });
  for (const preview of previews) {
    preview.addEventListener("click", () => {
      const original = preview.querySelector("img");
      const image = new Image();
      image.alt = original.alt;
      image.src = preview.dataset.fullSrc || original.currentSrc || original.src;
      picture.style.setProperty("--ratio", original.naturalWidth / original.naturalHeight || 1);
      picture.replaceChildren(image);
      for (const marker of preview.querySelectorAll("span")) {
        picture.append(marker.cloneNode(true));
      }
      picture.classList.toggle("track-study", preview.classList.contains("track-study"));
      viewer.classList.remove("is-zoomed");
      viewer.showModal();
    });
  }
}
