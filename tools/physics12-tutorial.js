(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const chapters = [...document.querySelectorAll('.chapter')];
  const links = [...document.querySelectorAll('[data-nav-chapter]')];
  const search = $('search'), subject = $('subject');
  const storageKey = 'physics12-giancoli-tutorial-v1';
  const normalize = text => text.toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '');
  const searchText = new Map(chapters.map(c => [c, normalize(c.textContent)]));
  let mode = 'study', slide = 0, studied = new Set(), beforePrint = null;
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || '{}');
    if (Array.isArray(saved.studied)) studied = new Set(saved.studied.filter(n => Number.isInteger(n) && n >= 1 && n <= 33));
    if (['study', 'slides', 'simple'].includes(saved.mode)) mode = saved.mode;
  } catch {}
  const queryMode = new URLSearchParams(location.search).get('mode');
  if (['study', 'slides', 'simple'].includes(queryMode)) mode = queryMode;
  function save() {
    try { localStorage.setItem(storageKey, JSON.stringify({mode, studied: [...studied]})); } catch {}
  }
  function matches() {
    const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    return chapters.filter(c => (!subject.value || c.dataset.subject === subject.value) && terms.every(term => searchText.get(c).includes(term)));
  }
  function currentChapter() {
    const visible = matches();
    if (mode === 'slides') return visible[slide];
    const edge = document.querySelector('.toolbar').getBoundingClientRect().bottom + 20;
    return visible.find(c => c.getBoundingClientRect().bottom > edge) || visible[0];
  }
  function activeLink(card) {
    for (const link of links) {
      const active = !!card && link.dataset.navChapter === card.dataset.number;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', mode === 'slides' ? 'step' : 'location');
      else link.removeAttribute('aria-current');
    }
  }
  function render() {
    document.body.dataset.mode = mode;
    const visible = matches();
    slide = Math.max(0, Math.min(slide, visible.length - 1));
    const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    for (const card of chapters) {
      const match = visible.includes(card);
      card.dataset.match = String(match);
      card.hidden = !match || (mode === 'slides' && card !== visible[slide]);
      if (match && terms.length) {
        card.querySelector('.lesson').open = true;
        for (const detail of card.querySelectorAll('.derivation')) {
          if (terms.every(term => normalize(detail.textContent).includes(term))) detail.open = true;
        }
      }
    }
    for (const link of links) link.hidden = !visible.some(c => c.dataset.number === link.dataset.navChapter);
    for (const heading of document.querySelectorAll('[data-nav-group]')) heading.hidden = !visible.some(c => c.dataset.subject === heading.dataset.navGroup);
    document.querySelectorAll('.modes button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
    $('filter-status').textContent = `${visible.length} of 33 chapters match`;
    $('empty').hidden = visible.length !== 0;
    $('slide-nav').hidden = mode !== 'slides' || !visible.length;
    $('slide-position').textContent = `Chapter ${visible.length ? slide + 1 : 0} of ${visible.length} matching chapters`;
    $('previous').disabled = slide === 0;
    $('next').disabled = slide >= visible.length - 1;
    $('nav-toggle').hidden = mode === 'simple';
    activeLink(currentChapter());
  }
  function progress() {
    for (const input of document.querySelectorAll('[data-complete]')) input.checked = studied.has(Number(input.dataset.complete));
    for (const link of links) link.classList.toggle('done', studied.has(Number(link.dataset.navChapter)));
    $('progress').value = studied.size;
    $('progress-text').textContent = `${studied.size} of 33 chapters studied`;
  }
  function goTo(card, scroll = true) {
    if (!card) return;
    if (!matches().includes(card)) { search.value = ''; subject.value = ''; }
    slide = matches().indexOf(card);
    card.querySelector('.lesson').open = true;
    render();
    activeLink(card);
    document.body.dataset.nav = 'closed';
    $('nav-toggle').setAttribute('aria-expanded', 'false');
    if (scroll) card.scrollIntoView({block: 'start', behavior: 'instant'});
  }
  function handleHash() {
    const match = /^#chapter-(\d+)$/.exec(location.hash);
    if (match) goTo($(`chapter-${Number(match[1])}`));
  }
  search.addEventListener('input', () => {slide = 0; render();});
  subject.addEventListener('change', () => {slide = 0; render();});
  $('clear').addEventListener('click', () => {search.value = ''; subject.value = ''; slide = 0; render(); search.focus();});
  document.querySelectorAll('.modes button').forEach(button => button.addEventListener('click', () => {
    const card = currentChapter();
    mode = button.dataset.mode;
    slide = Math.max(0, matches().indexOf(card));
    if (mode === 'simple') chapters.forEach(c => c.querySelector('.lesson').open = true);
    render(); save();
    if (card) card.scrollIntoView({block: 'start', behavior: 'instant'});
  }));
  function move(delta) {
    slide += delta; render();
    const card = matches()[slide];
    if (card) {
      card.querySelector('.lesson').open = true;
      card.scrollIntoView({block: 'start', behavior: 'instant'});
    }
  }
  $('previous').addEventListener('click', () => move(-1));
  $('next').addEventListener('click', () => move(1));
  document.addEventListener('keydown', event => {
    if (mode !== 'slides' || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || event.target.closest('input,select,textarea,button,summary,[contenteditable]')) return;
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {event.preventDefault(); move(event.key === 'ArrowRight' ? 1 : -1);}
  });
  $('nav-toggle').addEventListener('click', () => {
    const open = document.body.dataset.nav !== 'open';
    document.body.dataset.nav = open ? 'open' : 'closed';
    $('nav-toggle').setAttribute('aria-expanded', String(open));
    if (open) $('toc').scrollIntoView({block: 'start', behavior: 'instant'});
  });
  for (const [id, open] of [['expand', true], ['collapse', false]]) $(id).addEventListener('click', () => matches().forEach(c => {c.querySelector('.lesson').open = open;}));
  for (const input of document.querySelectorAll('[data-complete]')) input.addEventListener('change', () => {
    const n = Number(input.dataset.complete);
    if (input.checked) studied.add(n); else studied.delete(n);
    progress(); save();
  });
  for (const quiz of document.querySelectorAll('.quiz')) {
    const data = PHYSICS12_QUIZZES[quiz.dataset.chapter];
    for (const button of quiz.querySelectorAll('[data-choice]')) button.addEventListener('click', () => {
      const chosen = Number(button.dataset.choice), correct = chosen === data.correct;
      for (const option of quiz.querySelectorAll('[data-choice]')) {
        option.setAttribute('aria-pressed', String(option === button));
        option.classList.toggle('correct', Number(option.dataset.choice) === data.correct);
      }
      const feedback = quiz.querySelector('.feedback');
      feedback.hidden = false;
      feedback.classList.toggle('retry', !correct);
      feedback.textContent = (correct ? 'Correct. ' : `Not quite. The answer is ${String.fromCharCode(65 + data.correct)}. `) + data.explanation;
    });
  }
  window.addEventListener('hashchange', handleHash);
  // A repeated click on the same hash must still reopen a collapsed lesson.
  document.querySelectorAll('a[href^="#chapter-"]').forEach(a => a.addEventListener('click', event => {
    event.preventDefault();
    const hash = a.getAttribute('href');
    if (location.hash !== hash) history.pushState(null, '', hash);
    goTo(document.querySelector(hash));
  }));
  let scrollScheduled = false;
  window.addEventListener('scroll', () => {
    if (scrollScheduled || mode === 'slides') return;
    scrollScheduled = true;
    requestAnimationFrame(() => {scrollScheduled = false; activeLink(currentChapter());});
  }, {passive: true});
  window.addEventListener('beforeprint', () => {
    beforePrint = [...document.querySelectorAll('.lesson,.derivation')].map(detail => [detail, detail.open]);
    for (const c of chapters) if (c.dataset.match === 'true') {
      for (const detail of c.querySelectorAll('.lesson,.derivation')) detail.open = true;
    }
  });
  window.addEventListener('afterprint', () => {
    if (beforePrint) beforePrint.forEach(([detail, open]) => {detail.open = open;});
    beforePrint = null;
  });
  $('print').addEventListener('click', () => window.print());

  function bindLab(ids, update) {
    ids.forEach(id => $(id).addEventListener('input', update));
    update();
  }
  const value = id => Number($(id).value);
  const fmt = (n, digits = 2) => n.toFixed(digits);
  function label(id, digits = 0) {$(id + '-value').textContent = fmt(value(id), digits);}
  function path(points) {return points.map(([x, y], i) => (i ? 'L' : 'M') + fmt(x) + ' ' + fmt(y)).join(' ');}
  bindLab(['projectile-speed', 'projectile-angle'], () => {
    label('projectile-speed'); label('projectile-angle');
    const speed = value('projectile-speed'), theta = value('projectile-angle') * Math.PI / 180;
    const vx = speed * Math.cos(theta), vy = speed * Math.sin(theta), time = 2 * vy / 9.81;
    const range = vx * time, height = vy * vy / (2 * 9.81);
    const points = Array.from({length: 101}, (_, i) => {
      const t = time * i / 100;
      return [45 + 530 * vx * t / 200, 240 - 210 * Math.max(0, vy * t - 0.5 * 9.81 * t * t) / 100];
    });
    $('projectile-path').setAttribute('d', path(points));
    const text = `Flight time ${fmt(time)} s · Range ${fmt(range)} m · Maximum height ${fmt(height)} m`;
    $('projectile-result').textContent = text; $('projectile-desc').textContent = text;
  });
  bindLab(['circuit-mode', 'circuit-voltage', 'circuit-r1', 'circuit-r2'], () => {
    ['circuit-voltage', 'circuit-r1', 'circuit-r2'].forEach(id => label(id));
    const v = value('circuit-voltage'), r1 = value('circuit-r1'), r2 = value('circuit-r2');
    const series = $('circuit-mode').value === 'series', req = series ? r1 + r2 : r1 * r2 / (r1 + r2);
    const current = v / req, i1 = series ? current : v / r1, i2 = series ? current : v / r2;
    const battery = '<path d="M70 45V107M70 137V215M45 107H95M55 137H85" stroke="#245fa6" stroke-width="3" fill="none"/><text x="32" y="97">+</text><text x="28" y="157">−</text>';
    const circuit = series
      ? '<path d="M70 45H240M320 45H500V215H320M240 215H70" stroke="#076c68" stroke-width="2" fill="none"/><rect x="240" y="32" width="80" height="26" fill="#edf6f3" stroke="#076c68" stroke-width="2"/><rect x="240" y="202" width="80" height="26" fill="#edf6f3" stroke="#076c68" stroke-width="2"/><text x="260" y="25">R₁</text><text x="260" y="194">R₂</text>'
      : '<path d="M70 45H500V215H70M280 45V100M280 152V215M500 45V100M500 152V215" stroke="#076c68" stroke-width="2" fill="none"/><rect x="267" y="100" width="26" height="52" fill="#edf6f3" stroke="#076c68" stroke-width="2"/><rect x="487" y="100" width="26" height="52" fill="#edf6f3" stroke="#076c68" stroke-width="2"/><text x="303" y="131">R₁</text><text x="524" y="131">R₂</text>';
    // Only fixed SVG markup enters innerHTML; slider values appear via textContent.
    $('circuit-drawing').innerHTML = battery + circuit;
    const text = `R_eq = ${fmt(req)} Ω · Battery current = ${fmt(current)} A · I₁ = ${fmt(i1)} A · I₂ = ${fmt(i2)} A · V₁ = ${fmt(i1*r1)} V · V₂ = ${fmt(i2*r2)} V · Total power = ${fmt(v*current)} W`;
    $('circuit-result').textContent = text; $('circuit-desc').textContent = (series ? 'Series connection. ' : 'Parallel connection. ') + text;
  });
  bindLab(['interference-wavelength', 'interference-separation'], () => {
    label('interference-wavelength'); label('interference-separation', 2);
    const wavelength = value('interference-wavelength') * 1e-9, separation = value('interference-separation') * 1e-3;
    const length = 2, spacing = wavelength * length / separation;
    const points = Array.from({length: 801}, (_, i) => {
      const y = -0.020 + 0.040 * i / 800;
      const intensity = Math.cos(Math.PI * separation * y / (wavelength * length)) ** 2;
      return [45 + 530 * i / 800, 220 - 185 * intensity];
    });
    $('interference-path').setAttribute('d', path(points));
    const text = `Adjacent bright-fringe spacing ≈ ${fmt(spacing * 1000)} mm · L = 2.00 m · Central maximum at y = 0`;
    $('interference-result').textContent = text; $('interference-desc').textContent = text;
  });
  bindLab(['decay-halflife', 'decay-time'], () => {
    label('decay-halflife', 1); label('decay-time', 1);
    const half = value('decay-halflife'), time = value('decay-time'), fraction = 2 ** (-time / half);
    const points = Array.from({length: 241}, (_, i) => [45 + 530 * i / 240, 235 - 200 * 2 ** (-(i / 10) / half)]);
    $('decay-path').setAttribute('d', path(points));
    const x = 45 + 530 * time / 24, y = 235 - 200 * fraction;
    $('decay-marker').setAttribute('d', `M${fmt(x)} 235V${fmt(y)}`);
    $('decay-dot').setAttribute('cx', fmt(x)); $('decay-dot').setAttribute('cy', fmt(y));
    const text = `${fmt(time/half)} half-lives elapsed · Expected parent fraction = ${fmt(100*fraction, 3)}% · Decayed fraction = ${fmt(100*(1-fraction), 3)}%`;
    $('decay-result').textContent = text; $('decay-desc').textContent = text;
  });
  progress(); render();
  if (location.hash) handleHash();
})();
