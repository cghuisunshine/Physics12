/* Integration checks for the offline tutorial and physical model outputs. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM, VirtualConsole} = require(process.env.PHYSICS_JSDOM_PATH || 'jsdom');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'physics12-tutorial.html'), 'utf8');
const chapters = JSON.parse(fs.readFileSync(path.join(root, 'content/physics12/chapters.json'), 'utf8'));
const key = 'physics12-giancoli-tutorial-v1';
function open({url='https://example.test/physics12-tutorial.html', saved, blocked=false}={}) {
  const errors=[], vc=new VirtualConsole(); vc.on('jsdomError', e=>errors.push(e.message));
  const dom=new JSDOM(html,{url,runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:vc,beforeParse(w){
    w.HTMLElement.prototype.scrollIntoView=()=>{};
    w.print=()=>{};
    w.HTMLDialogElement.prototype.showModal=function(){this.setAttribute('open','');};
    w.HTMLDialogElement.prototype.close=function(){this.removeAttribute('open');this.dispatchEvent(new w.Event('close'));};
    if(blocked) Object.defineProperty(w,'localStorage',{get(){throw Error('Storage unavailable');}});
    else if(saved)w.localStorage.setItem(key,saved);
  }});
  return {dom,w:dom.window,d:dom.window.document,errors};
}
const p=open(),{w,d,errors}=p,$=id=>d.getElementById(id);
const shown=()=>[...d.querySelectorAll('.chapter')].filter(e=>!e.hidden);
const input=(id,value,type='input')=>{$(id).value=String(value);$(id).dispatchEvent(new w.Event(type,{bubbles:true}));};
const choose=mode=>d.querySelector(`.modes [data-mode="${mode}"]`).click();
try {
  assert.deepEqual(errors,[]);
  assert.equal(shown().length,33);
  assert.equal(d.querySelectorAll('.worked').length,33);
  assert.equal(d.querySelectorAll('.solution[open]').length,0);
  assert.equal(d.querySelectorAll('.quiz').length,33);
  assert.equal(d.querySelectorAll('.lab').length,4);
  assert.equal(d.querySelectorAll('.diagram').length,4);
  assert.equal(d.querySelectorAll('.derivations').length,33);
  assert.equal(d.querySelectorAll('.derivation').length,62);
  assert.equal(d.querySelectorAll('.derivation[open]').length,33);
  assert.equal(d.querySelectorAll('.teaching-visual').length,161);
  assert.equal(d.querySelectorAll('.visual-answer').length,161);
  assert.equal(d.querySelectorAll('.visual-answer[open]').length,0);
  for(const section of d.querySelectorAll('.concept,.derivation')){
    const figure=section.querySelector('.teaching-visual');assert.ok(figure,section.id);
    assert.ok(figure.querySelector('svg[role=img] title').textContent);
    assert.ok(figure.querySelector('svg desc').textContent);
  }
  const reviewChapters=new Set([...d.querySelectorAll('.derivation-sources a')].map(a=>Number(a.hash.split('-').pop())));
  assert.deepEqual([...reviewChapters].sort((a,b)=>a-b),Array.from({length:44},(_,i)=>i+1));
  assert.equal(d.querySelectorAll('script[src],link[rel=stylesheet],iframe').length,0);
  assert.equal(d.querySelectorAll('img[src^="http"]').length,0);
  const ids=[...d.querySelectorAll('[id]')].map(e=>e.id);
  assert.equal(new Set(ids).size,ids.length);
  for(const a of d.querySelectorAll('a[href^="#"]'))assert.ok(d.querySelector(a.getAttribute('href')),a.getAttribute('href'));
  // Diagram enlargement must remain labelled and avoid duplicating SVG IDs.
  const picture=$('visual-concept-3-1'), opener=picture.querySelector('.visual-enlarge');
  opener.click();assert.ok($('visual-dialog').open);
  assert.equal($('visual-dialog-title').textContent,picture.querySelector('.visual-heading strong').textContent);
  assert.equal($('visual-dialog-image').querySelectorAll('[id]').length,0);
  $('visual-zoom-in').click();assert.equal($('visual-zoom-level').textContent,'125%');
  $('visual-zoom-out').click();assert.equal($('visual-zoom-level').textContent,'100%');
  assert.ok($('visual-zoom-out').disabled);
  $('visual-dialog-close').click();assert.ok(!$('visual-dialog').open);assert.equal(d.activeElement,opener);
  assert.equal($('visual-dialog-image').children.length,0);
  for(const c of chapters){
    const card=$(`chapter-${c.number}`);assert.ok(card);
    for(const [title,text] of c.concepts){assert.ok(card.textContent.includes(title));assert.ok(card.textContent.includes(text.replace(/\u20d7/g,'')));}
    assert.match(card.querySelector('a[href^="Physics12.pdf"]').href,new RegExp(`#page=${c.start+21}$`));
    const quiz=card.querySelector('.quiz'),options=[...quiz.querySelectorAll('[data-choice]')];
    options[(c.quiz.correct+1)%3].click();assert.match(quiz.querySelector('.feedback').textContent,/Not quite/);
    options[c.quiz.correct].click();assert.match(quiz.querySelector('.feedback').textContent,/^Correct\./);
    assert.equal(quiz.querySelector('.feedback').hidden,false);assert.equal(quiz.querySelectorAll('.correct').length,1);
    const solution=card.querySelector('.solution');solution.querySelector('summary').click();assert.ok(solution.open);solution.querySelector('summary').click();assert.ok(!solution.open);
  }
  input('subject','Light & Optics','change');assert.deepEqual(shown().map(e=>Number(e.dataset.number)),[23,24,25]);
  input('search','Malus');assert.deepEqual(shown().map(e=>Number(e.dataset.number)),[24]);
  choose('slides');assert.equal(shown().length,1);assert.ok($('previous').disabled&&$('next').disabled);
  input('search','nothing-matches-this');assert.equal(shown().length,0);assert.ok(!$('empty').hidden);
  $('clear').click();assert.equal(shown().length,1);assert.equal(shown()[0].id,'chapter-1');
  $('next').click();assert.equal(shown()[0].id,'chapter-2');
  choose('study');assert.equal(shown().length,33);
  // A term appearing only in a collapsed extension must reveal its explanation.
  const gasExtension=$('derivation-15-1'), entropyExtension=$('derivation-15-2');
  gasExtension.open=false;entropyExtension.open=false;$('chapter-15').querySelector('.lesson').open=false;
  input('search','Carnot');assert.deepEqual(shown().map(c=>c.id),['chapter-15']);
  assert.ok(entropyExtension.open);assert.ok($('chapter-15').querySelector('.lesson').open);
  assert.ok(!gasExtension.open);
  // Printing opens even unselected explanations in matching chapters only,
  // and then restores both lesson and nested explanation states.
  const otherExtension=$('derivation-17-2');otherExtension.open=false;
  const prediction=gasExtension.querySelector('.visual-answer'),otherPrediction=otherExtension.querySelector('.visual-answer');
  prediction.open=false;otherPrediction.open=false;
  w.dispatchEvent(new w.Event('beforeprint'));
  assert.ok(gasExtension.open&&entropyExtension.open);assert.ok(!otherExtension.open);
  assert.ok(prediction.open);assert.ok(!otherPrediction.open);
  w.dispatchEvent(new w.Event('afterprint'));
  assert.ok(!gasExtension.open&&entropyExtension.open);assert.ok(!otherExtension.open);
  assert.ok(!prediction.open&&!otherPrediction.open);
  input('search','');
  input('search','half-life');assert.ok(shown().some(e=>e.id==='chapter-30'));
  d.querySelector('[data-nav-chapter="3"]').click();assert.equal($('search').value,'');assert.equal(w.location.hash,'#chapter-3');
  $('collapse').click();assert.equal(d.querySelectorAll('.lesson[open]').length,0);
  $('expand').click();assert.equal(d.querySelectorAll('.lesson[open]').length,33);
  choose('simple');assert.equal(shown().length,33);assert.equal(d.body.dataset.mode,'simple');
  choose('slides');assert.equal(shown().length,1);
  $('collapse').click();const initiallyOpen=d.querySelectorAll('.lesson[open]').length;
  w.dispatchEvent(new w.Event('beforeprint'));assert.equal(d.querySelectorAll('.lesson[open]').length,33);
  w.dispatchEvent(new w.Event('afterprint'));assert.equal(d.querySelectorAll('.lesson[open]').length,initiallyOpen);
  const completed=$('chapter-3').querySelector('[data-complete]');completed.click();assert.equal($('progress').value,1);
  const saved=w.localStorage.getItem(key);assert.ok(JSON.parse(saved).studied.includes(3));
  const restored=open({saved});assert.equal(restored.d.querySelector('#progress').value,1);assert.deepEqual(restored.errors,[]);restored.dom.window.close();
  const corrupted=open({saved:'broken JSON'});assert.equal(corrupted.d.querySelectorAll('.chapter:not([hidden])').length,33);assert.deepEqual(corrupted.errors,[]);corrupted.dom.window.close();
  const blocked=open({blocked:true});assert.deepEqual(blocked.errors,[]);assert.equal(blocked.d.querySelectorAll('.chapter:not([hidden])').length,33);blocked.dom.window.close();
  const deep=open({url:'https://example.test/physics12-tutorial.html?mode=slides#chapter-30'});assert.equal(deep.d.querySelector('.chapter:not([hidden])').id,'chapter-30');deep.dom.window.close();
  // Independently known values and limiting cases, beyond merely checking a path exists.
  assert.match($('projectile-result').textContent,/Range 35\.31 m/);
  input('projectile-angle',60);assert.match($('projectile-result').textContent,/Range 35\.31 m/,'Complementary ideal launch angles have equal range');
  input('projectile-angle',45);assert.match($('projectile-result').textContent,/Range 40\.77 m/);
  assert.match($('circuit-result').textContent,/R_eq = 2\.00 Ω/);assert.match($('circuit-result').textContent,/current = 6\.00 A/);
  input('circuit-mode','series');assert.match($('circuit-result').textContent,/R_eq = 9\.00 Ω/);assert.match($('circuit-result').textContent,/V₁ = 8\.00 V · V₂ = 4\.00 V/);
  input('circuit-r1',3);assert.match($('circuit-result').textContent,/I₁ = 2\.00 A · I₂ = 2\.00 A/);
  assert.match($('interference-result').textContent,/6\.00 mm/);
  input('interference-separation',0.4);assert.match($('interference-result').textContent,/3\.00 mm/);
  assert.match($('decay-result').textContent,/12\.500%/);
  input('decay-time',0);assert.match($('decay-result').textContent,/100\.000%/);
  input('decay-time',6);assert.match($('decay-result').textContent,/50\.000%/);
  for(const id of ['projectile-path','interference-path','decay-path'])assert.ok(!/NaN|Infinity/.test($(id).getAttribute('d')));
  assert.deepEqual(errors,[]);
  console.log('Passed: all 33 chapters; 161 accessible teaching pictures across 99 concepts and 62 equation explanations; diagram enlargement/zoom/focus; prediction answers and filtered print restoration; 44 review chapter links; quizzes and solutions; filters and reading modes; navigation; local progress; four physical models.');
} finally {w.close();}
