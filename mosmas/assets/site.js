"use strict";

const menu = document.querySelector(".menu");
const header = document.querySelector(".site-header");
const desktop = window.matchMedia("(min-width: 1141px)");

function setMenu(open, focusButton = false) {
  header.classList.toggle("menu-open", open);
  menu.setAttribute("aria-expanded", String(open));
  if (focusButton) menu.focus();
}

function updateMenu() {
  menu.hidden = desktop.matches;
  setMenu(false);
}

document.documentElement.classList.add("js");
menu.addEventListener("click", () => {
  setMenu(menu.getAttribute("aria-expanded") !== "true");
});
header.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && header.classList.contains("menu-open")) {
    setMenu(false, true);
  }
});
desktop.addEventListener("change", updateMenu);
updateMenu();

const isChinese = document.documentElement.lang === "zh-CN";
const normalize = (text) => text.normalize("NFKC").toLocaleLowerCase()
  .replace(/\s+/g, " ").trim();

for (const block of document.querySelectorAll("[data-filter]")) {
  const filter = block.querySelector(".filters");
  const search = block.querySelector("[data-search]");
  const year = block.querySelector("select[data-year]");
  const summary = block.querySelector("[data-summary]");
  const empty = block.querySelector("[data-empty]");
  const groups = [...block.querySelectorAll("[data-group]")];
  const items = [...block.querySelectorAll("[data-item]")].map((element) => ({
    element,
    text: normalize(element.textContent + " " + (element.dataset.alias || "")),
  }));

  function update() {
    const terms = normalize(search.value).split(" ").filter(Boolean);
    const selected = year?.value;
    let count = 0;
    for (const { element, text } of items) {
      const matches = (!selected || selected === element.dataset.year)
        && terms.every((term) => text.includes(term));
      element.hidden = !matches;
      if (matches) count += 1;
    }
    for (const group of groups) {
      group.hidden = !group.querySelector("[data-item]:not([hidden])");
    }
    summary.textContent = isChinese ? "显示 " + count + " 条" : count + " shown";
    empty.hidden = count !== 0;
  }

  filter.hidden = false;
  search.addEventListener("input", update);
  year?.addEventListener("change", update);
  window.addEventListener("pageshow", update);
  update();
}
