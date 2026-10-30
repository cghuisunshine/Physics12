/* Worked-solution integration: immutable keys, safe rendering, caching and request lifecycle. */
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM,VirtualConsole}=require(process.env.PHYSICS_JSDOM_PATH||'jsdom');
require('./physics12-answer-key.js');
const worked=require('./physics12-worked-solution.js');
const problem={id:'test',solutionHash:'current'};
const entry={id:'test',answer:'4 m',steps:['Choose the displacement relation.','Substitute the distances: 2 m + 2 m = 4 m.'],check:'Units are meters.'};
assert.ok(worked.normalize(entry,problem));
assert.equal(worked.normalize({...entry,id:'other'},problem),null);
assert.equal(worked.normalize({...entry,steps:['Only a final answer']},problem),null);
assert.throws(()=>worked.parse({answers:[{...entry,steps:[]}]},problem));
assert.equal(worked.restore(problem,{getItem:()=>JSON.stringify({...entry,sourceHash:'old'})}),null);
assert.equal(worked.save(problem,entry,{setItem(){throw Error('full');}}),false);
const html=fs.readFileSync(path.join(__dirname,'../physics12-practice.html'),'utf8');
const tick=()=>new Promise(resolve=>setTimeout(resolve,40));
function page(storage={}){
  const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e));
  const dom=new JSDOM(html,{url:'https://physics.test/',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:vc,beforeParse(w){
    Object.defineProperty(w.navigator,'onLine',{value:false,configurable:true});
    w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({getImageData:()=>({data:new Uint8ClampedArray([255,255,255,255])})},{get:(o,k)=>o[k]||(()=>{})});
    w.HTMLCanvasElement.prototype.toDataURL=()=> 'data:image/png;base64,YQ==';
    w.HTMLMediaElement.prototype.pause=()=>{};w.HTMLElement.prototype.scrollIntoView=()=>{};
    w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};w.HTMLDialogElement.prototype.close=function(){this.open=false;};
    w.fetch=async()=>{throw Error('Unexpected offline request');};
    for(const [k,v] of Object.entries(storage))w.localStorage.setItem(k,v);
  }});
  return {dom,w:dom.window,$:id=>dom.window.document.getElementById(id),errors};
}
function change(p,id,value){p.$(id).value=value;p.$(id).dispatchEvent(new p.w.Event('change'));}
function login(p){p.$('login-name').value='Private Student';p.$('login-form').dispatchEvent(new p.w.Event('submit',{cancelable:true}));change(p,'practice-chapter','giancoli-ch1');change(p,'mode','chapter');}
function online(p,value){Object.defineProperty(p.w.navigator,'onLine',{value,configurable:true});}
function select(p,id){change(p,'chapter-question',id);}
function storage(p){return Object.fromEntries(Array.from({length:p.w.localStorage.length},(_,i)=>{const k=p.w.localStorage.key(i);return [k,p.w.localStorage.getItem(k)];}));}
(async()=>{
  const p=page();await tick();login(p);select(p,'giancoli-ch1-q1');
  const bank=JSON.parse(p.$('question-bank').textContent),q=bank.find(x=>x.id==='giancoli-ch1-q1');
  assert.equal(q.answerSource,'textbook');assert.ok(q.solutionHash);
  assert.ok(bank.every(q=>q.solutionHash?.length===64),'Every source, including textbook keys, has a cache fingerprint');
  p.$('check').click();await tick();
  assert.equal(p.$('solution').hidden,false);assert.equal(p.$('worked-solution').hidden,false);
  assert.match(p.$('solution-body').innerHTML,/answer-ch1-q1/);
  assert.match(p.$('worked-solution-status').textContent,/Connect to the internet/);
  assert.equal(p.$('worked-solution-retry').hidden,false);
  const original=p.$('solution-body').innerHTML;online(p,true);
  const decoded=[];p.w.PhysicsImageAssets.decode=async src=>{decoded.push(src);return {width:600,height:200};};
  let requests=0;
  const answer={id:q.id,answer:'Final result',steps:['Read each value and count its significant figures.','Keep internal zeros and significant trailing zeros; the result is <img src=x onerror=alert(1)> .'],check:'The result matches the key.',assumptions:[],needsReview:true};
  p.w.fetch=async(url,options)=>{
    requests++;const body=JSON.parse(options.body);
    assert.ok(body.message.includes('STEP-BY-STEP'));assert.ok(body.message.includes(JSON.stringify(q.questionText)));assert.ok(body.image);
    assert.ok(!JSON.stringify(body).includes('Private Student'));assert.ok(!body.message.includes('STUDENT WORK'));
    return {ok:true,json:async()=>({response:JSON.stringify({answers:[answer]})})};
  };
  p.$('worked-solution-retry').click();p.$('worked-solution-retry').click();await tick();
  assert.equal(requests,1);assert.ok(decoded.some(src=>src.includes('answer-ch1-q1')),'Textbook key images accompany the original question');
  assert.equal(p.$('worked-solution-body').querySelectorAll('ol li').length,2);
  assert.equal(p.$('worked-solution-body').querySelector('img'),null,'AI output is escaped');
  assert.match(p.$('worked-solution-body').textContent,/AI-generated worked solution/);
  assert.match(p.$('worked-solution-body').textContent,/flagged for review/);
  assert.equal(p.$('solution-body').innerHTML,original,'The original answer key is preserved');
  assert.equal(p.$('attempt-count').textContent,'0','Generating steps never scores student work');
  const again=page(storage(p));await tick();login(again);select(again,q.id);again.$('check').click();await tick();
  assert.equal(again.$('worked-solution-body').querySelectorAll('ol li').length,2);
  assert.match(again.$('worked-solution-status').textContent,/available offline/);
  // Existing worked solutions need neither a second panel nor a request.
  const prebuilt=bank.find(q=>q.hasWorkedSteps&&q.chapter==='giancoli-ch1');
  assert.ok(prebuilt);select(p,prebuilt.id);p.$('check').click();await tick();
  assert.equal(requests,1);assert.equal(p.$('worked-solution').hidden,true);
  assert.ok(p.$('solution-body').querySelector('ol.worked-steps'));
  // Failure and cancellation keep the key visible, and late responses cannot leak to another problem.
  const other=bank.find(q=>!q.hasWorkedSteps&&q.chapter==='giancoli-ch1'&&q.id!=='giancoli-ch1-q1');
  select(p,other.id);p.w.fetch=async()=>({ok:false,status:503});p.$('check').click();await tick();
  assert.match(p.$('worked-solution-status').textContent,/HTTP 503/);assert.equal(p.$('solution').hidden,false);
  p.w.fetch=async()=>({ok:true,json:async()=>({answers:[{...answer,id:other.id,steps:[]}]})});
  p.$('worked-solution-retry').click();await tick();assert.match(p.$('worked-solution-status').textContent,/did not return a step-by-step/);
  let finish,signal;p.w.fetch=(url,opts)=>{signal=opts.signal;return new Promise(resolve=>{finish=resolve;});};
  p.$('worked-solution-retry').click();await tick();assert.ok(finish);
  p.$('rate-practice').click();assert.equal(p.$('attempt-count').textContent,'1','Solution requests do not block self-rating');
  p.$('worked-solution-cancel').click();assert.equal(signal.aborted,true);
  finish({ok:true,json:async()=>({answers:[{...answer,id:other.id}]})});await tick();
  assert.match(p.$('worked-solution-status').textContent,/canceled/);assert.equal(p.$('worked-solution-body').textContent,'');
  p.$('worked-solution-retry').click();await tick();const late=finish;
  select(p,q.id);assert.equal(signal.aborted,true);late({ok:true,json:async()=>({answers:[{...answer,id:other.id}]})});await tick();
  assert.equal(p.$('worked-solution').hidden,true);assert.equal(p.$('worked-solution-body').textContent,'');
  assert.equal(p.w.localStorage.getItem('physics12WorkedSolution.v1:'+other.id),null);
  assert.deepEqual(p.errors,[]);assert.deepEqual(again.errors,[]);
  p.w.close();again.w.close();
  console.log('Passed: paired solutions, reference-only generation, safe rendering, offline cache, stale keys, failures, cancellation, navigation and independent self-rating.');
})().catch(e=>{console.error(e);process.exit(1);});
