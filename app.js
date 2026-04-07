/* ─────────────────────────────────────────────
   SHARED APP JS — theme, language, nav, reveals
───────────────────────────────────────────── */

// ── Dark/Light theme toggle ──────────────────
(function() {
  const html = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  let currentTheme = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  html.setAttribute('data-theme', currentTheme);
  function updateIcon() {
    if (!toggle) return;
    toggle.innerHTML = currentTheme === 'dark'
      ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
      : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    toggle.setAttribute('aria-label', currentTheme === 'dark' ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro');
  }
  updateIcon();
  if (toggle) {
    toggle.addEventListener('click', () => {
      currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', currentTheme);
      updateIcon();
    });
  }
})();

// ── Language toggle (ES/EN) ──────────────────
const browserLang = navigator.language && navigator.language.toLowerCase().startsWith('es') ? 'es' : 'en';
let currentLang = localStorage.getItem('lang') || browserLang;
function setLang(lang) {
  currentLang = lang;
  document.querySelectorAll('[data-es], [data-en]').forEach(el => {
    const val = el.getAttribute('data-' + lang);
    if (val !== null) el.innerHTML = val;
  });
  // Update html lang attribute
  document.documentElement.lang = lang;
  // Update title
  const titleEl = document.querySelector('title');
  if (titleEl) {
    const v = titleEl.getAttribute('data-' + lang);
    if (v) titleEl.textContent = v;
  }
  // Persist choice across pages
  localStorage.setItem('lang', lang);
  // Update lang button states
  document.querySelectorAll('.lang-toggle button').forEach(btn => {
    btn.classList.remove('active');
  });
  const active = document.getElementById('lang-' + lang);
  if (active) active.classList.add('active');
}
// Apply language on load (runs before paint to avoid flash)
(function initLang() {
  setLang(currentLang);
})();
window.setLang = setLang;

// ── Mobile menu ──────────────────────────────
const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('nav-links');
if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', open);
    menuToggle.innerHTML = open
      ? '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
      : '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
    document.body.style.overflow = open ? 'hidden' : '';
  });
  // Close on link click
  navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      navLinks.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });
}

// ── Sticky header shadow ─────────────────────
const header = document.getElementById('site-header');
if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 12);
  }, { passive: true });
}

// ── Scroll reveal ────────────────────────────
const revealEls = document.querySelectorAll('.reveal');
if (revealEls.length > 0) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  revealEls.forEach(el => observer.observe(el));
}

// ── Active nav link ───────────────────────────
const currentPath = location.pathname;
document.querySelectorAll('.nav-links a').forEach(a => {
  const href = a.getAttribute('href');
  // Match current path against nav link href
  // Handle both absolute paths and paths ending with /
  const isActive = currentPath === href || 
                   (href !== '/' && currentPath.endsWith(href)) ||
                   (href === '/index.html' && (currentPath === '/' || currentPath.endsWith('/index.html')));
  a.classList.toggle('active', isActive);
});
