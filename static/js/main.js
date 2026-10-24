// ===== هوش نو — جاوااسکریپت تعاملی =====
document.addEventListener('DOMContentLoaded', () => {
  // ۱) منوی موبایل: بستن منو پس از کلیک روی لینک
  const nav = document.getElementById('mainNav');
  document.querySelectorAll('#mainNav .nav-link').forEach(l =>
    l.addEventListener('click', () => {
      if (nav.classList.contains('show') && window.bootstrap)
        bootstrap.Collapse.getOrCreateInstance(nav).hide();
    }));

  // ۲) اسکرول نرم برای لینک‌های داخلی (#)
  document.querySelectorAll('a[href^="#"]').forEach(a =>
    a.addEventListener('click', e => {
      const t = document.querySelector(a.getAttribute('href'));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
    }));

  // ۳) مودال مشاوره — دکمه شناور با لرزش ملایم
  const fab = document.getElementById('consultBtn');
  if (fab) {
    fab.addEventListener('click', () => {
      const m = document.getElementById('consultModal');
      if (m && window.bootstrap) bootstrap.Modal.getOrCreateInstance(m).show();
    });
    setInterval(() => { fab.animate([{ transform: 'scale(1)' }, { transform: 'scale(1.12)' }, { transform: 'scale(1)' }], { duration: 900 }); }, 6000);
  }

  // ۴) فیلتر زنده دوره‌ها (سن/سطح/دسته/جست‌وجو)
  const grid = document.getElementById('courseGrid');
  if (grid) {
    const items = [...grid.querySelectorAll('.course-item')];
    const fAge = document.getElementById('fAge'), fLevel = document.getElementById('fLevel'),
          fCat = document.getElementById('fCat'), fSearch = document.getElementById('fSearch'),
          fReset = document.getElementById('fReset');
    const apply = () => {
      const age = parseInt(fAge.value || 0), lv = fLevel.value, cat = fCat.value,
            q = (fSearch.value || '').trim().toLowerCase();
      items.forEach(it => {
        const amin = +it.dataset.agemin, amax = +it.dataset.agemax;
        let ok = true;
        if (age && (age < amin || age > amax)) ok = false;
        if (lv && it.dataset.level !== lv) ok = false;
        if (cat && it.dataset.cat !== cat) ok = false;
        if (q && !it.dataset.title.toLowerCase().includes(q)) ok = false;
        it.style.display = ok ? '' : 'none';
      });
    };
    [fAge, fLevel, fCat].forEach(el => el.addEventListener('change', apply));
    fSearch.addEventListener('input', apply);
    fReset.addEventListener('click', () => { [fAge, fLevel, fCat].forEach(e => e.value = ''); fSearch.value = ''; apply(); });
  }

  // ۵) ذرات پاستل شناور در پس‌زمینه
  const canvas = document.getElementById('particles');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    const colors = ['#b9a8ee', '#8fdcc0', '#ff9b8a', '#8fc4f5', '#ffe680'];
    let W, H, parts = [];
    const resize = () => { W = canvas.width = innerWidth; H = canvas.height = innerHeight; };
    resize(); addEventListener('resize', resize);
    const N = Math.min(45, Math.floor(innerWidth / 30));
    for (let i = 0; i < N; i++) parts.push({
      x: Math.random() * W, y: Math.random() * H,
      r: 2 + Math.random() * 5, c: colors[i % colors.length],
      vx: (Math.random() - .5) * .4, vy: -(.2 + Math.random() * .5), a: .25 + Math.random() * .35
    });
    (function loop() {
      ctx.clearRect(0, 0, W, H);
      parts.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if (p.y < -10) { p.y = H + 10; p.x = Math.random() * W; }
        if (p.x < -10) p.x = W + 10; if (p.x > W + 10) p.x = -10;
        ctx.globalAlpha = p.a; ctx.fillStyle = p.c;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
      });
      requestAnimationFrame(loop);
    })();
  }
});


/* ===== چرخش خودکار اخبار هوش مصنوعی (تیکر) ===== */
document.addEventListener('DOMContentLoaded', function(){
  const ticker = document.getElementById('newsTicker');
  if(!ticker) return;
  setInterval(function(){
    const items = ticker.querySelectorAll('.news-item');
    if(items.length < 2) return;
    const first = items[0];
    first.style.animation = 'none';
    ticker.appendChild(first);
    void first.offsetWidth;
    first.style.animation = 'newsIn .5s ease both';
  }, 6000);
});
