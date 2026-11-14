/* Progressive enhancement: all content remains readable without JavaScript. */
document.documentElement.classList.add('js');
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
if (menuButton && navigation) {
  menuButton.hidden = false;
  const closeMenu = () => {
    navigation.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
  };
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  });
  navigation.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      closeMenu(); menuButton.focus();
    }
  });
  window.matchMedia('(min-width: 901px)').addEventListener('change', closeMenu);
}

const form = document.querySelector('#publication-filters');
if (form) {
  form.hidden = false;
  const search = document.querySelector('#paper-search');
  const year = document.querySelector('#paper-year');
  const topic = document.querySelector('#paper-topic');
  const rows = [...document.querySelectorAll('[data-publication]')];
  const groups = [...document.querySelectorAll('[data-year-group]')];
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-results');
  const normalize = text => text.normalize('NFKC').toLowerCase().replace(/[\u2062\u200b]/g, '');
  const searchable = new Map(rows.map(row => [row, normalize(row.dataset.search)]));
  const update = () => {
    const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    let visible = 0;
    rows.forEach(row => {
      const matches = terms.every(term => searchable.get(row).includes(term))
        && (year.value === 'all' || row.dataset.year === year.value)
        && (topic.value === 'all' || row.dataset.topics.split('|').includes(topic.value));
      row.hidden = !matches;
      if (matches) visible++;
    });
    groups.forEach(group => { group.hidden = !group.querySelector('[data-publication]:not([hidden])'); });
    count.textContent = `${visible} of ${rows.length} publications & accepted papers`;
    empty.hidden = visible !== 0;
  };
  form.addEventListener('input', update);
  form.addEventListener('change', update);
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('reset', () => { setTimeout(update, 0); });
  document.querySelector('#clear-filters').addEventListener('click', () => { form.reset(); search.focus(); });
  document.querySelectorAll('.year-nav a').forEach(anchor => {
    anchor.addEventListener('click', () => { form.reset(); });
  });
  update();
}

// Keep preview visits out of production analytics.
if (location.hostname === 'tmm-group.github.io') {
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', 'G-L6D9WK8K81');
  const analytics = document.createElement('script');
  analytics.async = true;
  analytics.src = 'https://www.googletagmanager.com/gtag/js?id=G-L6D9WK8K81';
  document.head.append(analytics);
}
