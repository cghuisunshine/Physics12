/* Offline integration checks for the Physics 12 studio; requires jsdom >=26. */
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {JSDOM,VirtualConsole}=require(process.env.PHYSICS_JSDOM_PATH||'jsdom');
const root=path.resolve(__dirname,'..');
const html=fs.readFileSync(path.join(root,'physics12-practice.html'),'utf8');
const inventory=JSON.parse(fs.readFileSync(path.join(root,'content/physics12/practice-problems.json'),'utf8'));
const prebuilt=JSON.parse(fs.readFileSync(path.join(root,'content/physics12/prebuilt-answers.json'),'utf8')).answers;
let calls=0;
function page(storage={}){
  const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e));
  const dom=new JSDOM(html,{url:'https://physics.test/physics12-practice.html',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:vc,beforeParse(w){
    Object.defineProperty(w.navigator,'onLine',{value:false,configurable:true});
    w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({getImageData:()=>({data:new Uint8ClampedArray([255,255,255,255])})},{get:(object,key)=>object[key]||(()=>{})});
    w.HTMLCanvasElement.prototype.toDataURL=()=> 'data:image/png;base64,YQ==';
    w.HTMLMediaElement.prototype.pause=()=>{};
    w.HTMLElement.prototype.scrollIntoView=()=>{};
    w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};
    w.HTMLDialogElement.prototype.close=function(){this.open=false;};
    w.fetch=async()=>{calls++;throw Error('Unexpected network request');};
    w.confirm=()=>true;
    for(const [k,v] of Object.entries(storage))w.localStorage.setItem(k,v);
  }});
  return {dom,w:dom.window,d:dom.window.document,$:id=>dom.window.document.getElementById(id),errors};
}
function change(p,id,value){p.$(id).value=value;p.$(id).dispatchEvent(new p.w.Event('change'));}
function login(p,name){p.$('login-name').value=name;p.$('login-form').dispatchEvent(new p.w.Event('submit',{cancelable:true}));}
function saved(p){return Object.fromEntries(Array.from({length:p.w.localStorage.length},(_,i)=>{const k=p.w.localStorage.key(i);return [k,p.w.localStorage.getItem(k)];}));}
function response(p,text){p.$('response-input').value=text;p.$('response-input').dispatchEvent(new p.w.Event('input'));}
const wait=()=>new Promise(r=>setTimeout(r,30));
const key=require('./physics12-answer-key.js');
const keyProblem={id:'key-test',answerHash:'current-source',hasAnswer:false};
assert.equal(key.normalize({id:'wrong',answer:'1 m'},keyProblem),null,'Reject another question’s key');
assert.equal(key.normalize({id:'key-test',answer:' '},keyProblem),null,'Reject empty answers');
assert.throws(()=>key.parse({response:'Not JSON'},keyProblem));
assert.throws(()=>key.parse({answers:[{id:'key-test',answer:'1 m'},{id:'key-test',answer:'2 m'}]},keyProblem));
assert.equal(key.restore(keyProblem,{getItem:()=>JSON.stringify({id:'key-test',answer:'1 m',sourceHash:'old-source'})}),false,'Reject stale cached answers');
assert.equal(key.save(keyProblem,key.normalize({id:'key-test',answer:'1 m'},keyProblem),{setItem(){throw Error('Quota exceeded');}}),false);
assert.equal(keyProblem.hasAnswer,true,'Storage failure must not hide a generated answer');
(async()=>{
  const p=page({'physics11PracticeStudent':'Grade 11 student','physics11Practice.v1:ada':'DO NOT CHANGE'});
  await wait();assert.deepEqual(p.errors,[]);
  assert.equal(p.$('login-overlay').hidden,false,'Physics 11 sign-in does not carry into Physics 12');
  const bank=JSON.parse(p.$('question-bank').textContent);
  assert.equal(bank.length,inventory.question_count);
  assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
  assert.equal(new Set(bank.map(q=>q.chapterNumber)).size,33);
  assert.equal(bank.filter(q=>q.hasAnswer).length,inventory.answer_count+Object.keys(prebuilt).length,'Textbook and saved AI keys are embedded for offline use');
  assert.equal(bank.filter(q=>q.answerSource==='textbook').length,inventory.answer_count);
  assert.equal(bank.filter(q=>q.answerSource==='prebuilt-ai').length,Object.keys(prebuilt).length);
  for(const q of bank){
    if(!q.hasAnswer){assert.equal(q.answerSource,'pending-ai');assert.equal(q.solution,'');assert.equal(q.answerHash.length,64);assert.ok(q.questionText);continue;}
    assert.ok(q.solution.includes(`data-answer-source="${q.answerSource}"`),'Visible answer provenance: '+q.id);
    assert.ok(!/does not supply an answer|No supplied textbook answer/.test(q.solution),'No missing-answer placeholders: '+q.id);
    if(q.answerSource==='prebuilt-ai'){
      assert.ok(q.solution.includes('Prebuilt AI answer')&&q.solution.includes('prebuilt-answer'));
      assert.ok(q.answer.length>2);
    }
  }
  const generated=p.w.AdaptivePractice.problem({id:'gen-12345678-1234-1234-1234-123456789abc',anchorId:'giancoli-ch1-q2',skill:'units',level:1,title:'Unit conversion',question:'Convert 2 km to metres.',answer:'2000 m',steps:['Multiply 2 by 1000 m/km.'],check:'2 × 1000 m = 2000 m'},bank);
  assert.equal(generated.hasAnswer,true,'Generated worked answers can be checked even when the source problem has no supplied key');
  assert.ok(!html.includes('physics11'),'All persistence and sync namespaces are isolated');
  assert.ok(!html.includes('Grade 11'));
  assert.equal(p.$('practice-chapter').options.length,34);
  assert.equal(p.d.querySelectorAll('script[src]').length,0);
  for(const q of inventory.questions){
    for(const image of [...q.images,...q.context,...q.answers]){
      assert.ok(fs.existsSync(path.join(root,image.src)),image.src);
      assert.ok(fs.existsSync(path.join(root,image.src+'.js')),'Local canvas companion: '+image.src);
      assert.ok(image.rect[3]>image.rect[1]+2,'Nonempty image '+q.id);
      assert.ok(image.page>=22&&image.page<=1046);
    }
  }
  for(let ch=1;ch<=33;ch++){
    const numbers=bank.filter(q=>q.chapterNumber===ch).map(q=>q.number);
    assert.deepEqual(numbers,Array.from({length:numbers.length},(_,i)=>i+1));
    assert.ok(numbers.length>=50,'Full chapter sets');
  }
  assert.equal(bank.filter(q=>q.chapterNumber===1).length,61);
  assert.ok(inventory.questions.find(q=>q.id==='giancoli-ch27-q17').text.includes('electrons from a metal'),'Question below the usual footer boundary is preserved');
  assert.ok(inventory.questions.find(q=>q.id==='giancoli-ch4-q60').context.length,'Floating referenced figure is included');
  login(p,'Ada');change(p,'practice-chapter','giancoli-ch1');change(p,'mode','chapter');
  assert.match(p.d.title,/Physics 12/);
  assert.equal(p.$('chapter-grid').children.length,61);
  assert.equal(p.$('chapter-question').options.length,62);
  assert.ok([...p.$('topic-list').querySelectorAll('input[data-topic]')].some(i=>i.value.endsWith('general')));
  change(p,'chapter-question','giancoli-ch1-q1');
  assert.equal(p.$('solution').hidden,true);
  assert.match(p.$('statement').innerHTML,/ch1-q1-1.png/);
  assert.ok(p.$('source').href.endsWith('Physics12.pdf#page=39'));
  response(p,'a) 3, b) 4, c) 3, d) 1, e) 2, f) 4, g) 2');
  p.$('check').click();await wait();
  assert.equal(p.$('solution').hidden,false);
  assert.match(p.$('solution-body').innerHTML,/answer-ch1-q1/);
  p.$('rate-correct').click();
  assert.equal(p.$('attempt-count').textContent,'1');
  change(p,'chapter-question','giancoli-ch1-q2');
  response(p,'My working');
  p.$('check').click();await wait();
  assert.match(p.$('solution-body').textContent,/Prebuilt AI answer/);
  assert.match(p.$('feedback').textContent,/Offline/);
  const formattedAnswer=p.$('solution-body').querySelector('.prebuilt-answer');
  assert.ok(formattedAnswer.querySelectorAll('.katex').length>=6,'The saved scientific-notation answer is typeset immediately offline');
  for(const value of ['1.156','2.18','6.8','3.2865','2.19','4.44'])assert.ok(formattedAnswer.textContent.includes(value),'Every subpart of the saved key remains visible: '+value);
  p.$('rate-practice').click();
  assert.equal(p.$('review-count').textContent,'1');
  change(p,'mode','review');
  assert.match(p.$('question-title').textContent,/problem 2/);
  const storage=saved(p);
  assert.equal(storage['physics11Practice.v1:ada'],'DO NOT CHANGE');
  assert.ok(storage['physics12Practice.v1:ada']);
  const again=page(storage);await wait();
  assert.equal(again.$('student-name-label').textContent,'Ada');
  assert.equal(again.$('attempt-count').textContent,'2');
  assert.equal(again.$('mode').value,'review');
  assert.equal(again.$('review-count').textContent,'1');
  change(again,'practice-chapter','giancoli-ch33');change(again,'mode','chapter');
  assert.ok(again.$('chapter-grid').children.length>=50);
  assert.deepEqual(p.errors,[]);assert.deepEqual(again.errors,[]);
  assert.equal(calls,0,'Saved answer keys are available offline without generation requests');
  for(const name of ['physics12-monitor.html','content.html','physics12-tutorial.html'])assert.ok(fs.existsSync(path.join(root,name)));
  p.dom.window.close();again.dom.window.close();
  const missing=bank.find(q=>!q.hasAnswer);
  if(missing){
    const fresh=page();await wait();login(fresh,'Answer key test');
    change(fresh,'practice-chapter',missing.chapter);change(fresh,'mode','chapter');change(fresh,'chapter-question',missing.id);
    fresh.$('check').click();await wait();
    assert.equal(fresh.$('solution').hidden,true,'Offline generation does not display a placeholder as an answer');
    assert.match(fresh.$('feedback').textContent,/Connect to the internet/);
    assert.equal(fresh.$('check').disabled,false);
    Object.defineProperty(fresh.w.navigator,'onLine',{value:true,configurable:true});
    fresh.w.PhysicsImageAssets.decode=async()=>({width:600,height:200});
    let requests=0;
    const answer={id:missing.id,answer:'Test answer <img src=x onerror=alert(1)>',steps:['First step'],check:'Checked',assumptions:[],needsReview:true};
    fresh.w.fetch=async(url,options)=>{requests++;const body=JSON.parse(options.body);assert.ok(body.image);assert.ok(!body.message.includes('PRIVATE STUDENT WORK'));assert.ok(body.message.includes(JSON.stringify(missing.questionText)));Object.defineProperty(fresh.w.navigator,'onLine',{value:false,configurable:true});return {ok:true,json:async()=>({response:JSON.stringify({answers:[answer]})})};};
    // Student work is deliberately present, but key generation sends only references.
    response(fresh,'PRIVATE STUDENT WORK');
    fresh.$('check').click();fresh.$('check').click();await wait();
    // Stop automatic grading: answer generation itself must not record an attempt.
    assert.match(fresh.$('solution-body').textContent,/AI-generated answer/);
    assert.match(fresh.$('solution-body').textContent,/flagged for review/);
    assert.equal(fresh.$('solution-body').querySelector('img'),null,'Service text is escaped');
    assert.equal(requests,1,'Duplicate clicks do not generate twice');
    assert.equal(fresh.$('attempt-count').textContent,'0');
    const offline=page(saved(fresh));await wait();login(offline,'Answer key test');
    change(offline,'practice-chapter',missing.chapter);change(offline,'mode','chapter');change(offline,'chapter-question',missing.id);
    offline.$('check').click();await wait();assert.match(offline.$('solution-body').textContent,/Test answer/);
    assert.deepEqual(fresh.errors,[]);assert.deepEqual(offline.errors,[]);
    const other=bank.find(q=>!q.hasAnswer&&q.id!==missing.id);
    if(other){
      change(fresh,'practice-chapter',other.chapter);change(fresh,'mode','chapter');change(fresh,'chapter-question',other.id);
      Object.defineProperty(fresh.w.navigator,'onLine',{value:true,configurable:true});
      fresh.w.fetch=async()=>{throw new fresh.w.TypeError('Network unavailable');};
      fresh.$('check').click();await wait();
      assert.match(fresh.$('feedback').textContent,/Could not reach the answer service/);
      assert.equal(fresh.$('check').disabled,false);assert.equal(fresh.$('solution').hidden,true);
      assert.equal(fresh.$('attempt-count').textContent,'0','Failed generation cannot score a submission');
      fresh.w.fetch=async()=>({ok:true,json:async()=>({answers:[{id:'wrong',answer:'Invalid answer'}]})});
      fresh.$('check').click();await wait();assert.match(fresh.$('feedback').textContent,/incomplete answer/);
      let finish;
      fresh.w.fetch=()=>new Promise(resolve=>{finish=resolve;});
      fresh.$('check').click();await wait();assert.ok(finish);
      fresh.$('ai-cancel').click();
      assert.equal(fresh.$('check').disabled,false);assert.match(fresh.$('feedback').textContent,/canceled/);
      finish({ok:true,json:async()=>({answers:[{id:other.id,answer:'A canceled answer'}]})});await wait();
      assert.equal(fresh.$('solution').hidden,true);
      assert.equal(fresh.w.localStorage.getItem('physics12AnswerKey.v1:'+other.id),null,'Late canceled answers cannot populate the cache');
      fresh.w.fetch=()=>new Promise(resolve=>{finish=resolve;});
      fresh.$('check').click();await wait();
      change(fresh,'chapter-question',missing.id);
      finish({ok:true,json:async()=>({answers:[{id:other.id,answer:'Late answer from previous question'}]})});await wait();
      assert.equal(fresh.$('solution').hidden,true,'Navigating while generating cannot reveal the wrong answer');
      assert.equal(fresh.w.localStorage.getItem('physics12AnswerKey.v1:'+other.id),null);
      fresh.$('check').click();await wait();assert.match(fresh.$('solution-body').textContent,/Test answer/);
      assert.deepEqual(fresh.errors,[]);
    }
    fresh.dom.window.close();offline.dom.window.close();
  }
  console.log(`Physics 12 practice passed: ${bank.length} problems in 33 chapters; source assets, answers, filters, progress, review and storage isolation.`);
})().catch(e=>{console.error(e);process.exit(1);});
