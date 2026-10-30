const assert=require('node:assert/strict'),fs=require('node:fs');
const {JSDOM}=require(process.env.PHYSICS_JSDOM_PATH||'jsdom');
const format=require('./physics12-solution-format.js'),worked=require('./physics12-worked-solution.js');
require('./physics12-answer-key.js');
const steps=[
  '1. The charges are +Q and −Q, their separation is ℓ, and the uniform electric field has magnitude E and is perpendicular to the rod. Each charge is ℓ/2 from the central pin.',
  '2\\. Apply the electric-force law F⃗ = qE⃗. Both forces have magnitude QE.',
  '3. Each torque has magnitude τ₁ = rF sin 90° = (ℓ/2)(QE).',
  '4. Add: τnet = QEℓ/2 + QEℓ/2 = QEℓ.'
];
const dom=new JSDOM(worked.render({answer:'τnet = QEℓ',steps,check:'Units: N·m.',assumptions:[]}));
const d=dom.window.document;
assert.equal(d.querySelectorAll('ol.worked-steps > li').length,4);
for(const li of d.querySelectorAll('li'))assert.ok(!/^\d+[.\\]/.test(li.textContent),'No doubled numbering');
assert.ok(d.querySelector('mover'),'Vector arrows are attached to their variables');
assert.ok(d.querySelector('msub'),'Subscripts have mathematical layout');
assert.ok(d.querySelector('.katex'));
assert.equal(format.text('The charges are +Q and −Q.'),'The charges are +Q and −Q.','Prose must not become an equation');
assert.equal(format.cleanStep('1. 2\\. Apply the force law.'),'Apply the force law.');
assert.equal(format.cleanStep('1.5 m is the length.'),'1.5 m is the length.','Decimal values are not list markers');
const latex=JSDOM.fragment(format.text(String.raw`Use $\vec F = q\vec E$, then $$\tau_{\mathrm{net}} = \frac{QE\ell}{2}+\frac{QE\ell}{2}.$$ Check \(v^2\) and \[\sqrt{x}\].`));
assert.equal(latex.querySelectorAll('.solution-math').length,4);
assert.equal(latex.querySelectorAll('.solution-math-block').length,2);
assert.ok(JSDOM.fragment(format.text('6.8 × 10⁻³')).querySelector('msup'));
assert.ok(latex.querySelector('mfrac'));assert.ok(latex.querySelector('msqrt'));assert.ok(latex.querySelector('msup'));
const untrusted=JSDOM.fragment(format.text(String.raw`<img src=x onerror=alert(1)> $\href{javascript:alert(1)}{bad}$ $\includegraphics{https://evil.test/a.png}$`));
assert.equal(untrusted.querySelector('img,a,script'),null,'Untrusted text and math cannot inject HTML or network resources');
const bad=JSDOM.fragment(format.text(String.raw`Before $\badcommand{$ after`));
assert.match(bad.textContent,/Before/);assert.match(bad.textContent,/after/);
const original=d.createElement('div');original.innerHTML='<img src="textbook.png"><ol class="worked-steps"><li>1. F⃗ = qE⃗</li></ol>';
format.enhance(original);assert.equal(original.querySelector('img').getAttribute('src'),'textbook.png');
assert.ok(original.querySelector('mover'));assert.ok(!/^1\./.test(original.querySelector('li').textContent));
const once=original.innerHTML;format.enhance(original);assert.equal(original.innerHTML,once,'Repeated enhancement does not nest rendered equations');
const page=fs.readFileSync(require('node:path').join(__dirname,'../physics12-practice.html'),'utf8');
assert.ok(page.includes('katex.renderToString'));assert.ok(page.includes('assets/physics12-math/fonts/KaTeX_Main-Regular.woff2'));
assert.ok(fs.existsSync(require('node:path').join(__dirname,'../assets/physics12-math/fonts/KaTeX_Main-Regular.woff2')));
dom.window.close();console.log('Passed: supplied torque example, single step numbering, vectors, scripts, fractions, delimiters, safe fallback, offline assets and repeat rendering.');
