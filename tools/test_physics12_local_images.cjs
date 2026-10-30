/* Reproduce local-file AI review with a canvas that rejects file-image pixels.
   No AI service or network requests: only generated local companion scripts run. */
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL,fileURLToPath}=require('node:url');
const {JSDOM,VirtualConsole,ResourceLoader}=require(process.env.PHYSICS_JSDOM_PATH||'jsdom');
const root=path.resolve(__dirname,'..'),loaded=[],decoded=[],requests=[],solutionRequests=[],contexts=new WeakMap();
class LocalAssets extends ResourceLoader{
  fetch(url,options){
    assert.ok(url.startsWith('file:')&&url.endsWith('.png.js'),'Only local image companion scripts may load: '+url);
    loaded.push(url);return super.fetch(url,options);
  }
}
const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e));
const dom=new JSDOM(fs.readFileSync(path.join(root,'physics12-practice.html'),'utf8'),{
  url:pathToFileURL(path.join(root,'physics12-practice.html')).href,
  resources:new LocalAssets(),runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:vc,
  beforeParse(w){
    const storage=new Map();
    Object.defineProperty(w,'localStorage',{value:{getItem:k=>storage.get(k)??null,setItem:(k,v)=>storage.set(k,String(v)),removeItem:k=>storage.delete(k)}});
    Object.defineProperty(w.navigator,'onLine',{value:true,configurable:true});
    w.HTMLElement.prototype.scrollIntoView=()=>{};w.HTMLMediaElement.prototype.pause=()=>{};
    w.HTMLCanvasElement.prototype.getContext=function(){
      if(!contexts.has(this))contexts.set(this,new Proxy({ink:false,tainted:false,
        getImageData(){return {data:new Uint8ClampedArray(this.ink?[0,0,0,255]:[255,255,255,255])};},
        fillRect(){this.ink=false;},fill(){this.ink=true;},stroke(){this.ink=true;},
        drawImage(img){if(img.src&&!img.src.startsWith('data:'))this.tainted=true;},
      },{get:(o,k)=>k in o?o[k]:(()=>{})}));
      return contexts.get(this);
    };
    w.HTMLCanvasElement.prototype.toDataURL=function(){
      if(this.getContext('2d').tainted)throw new w.DOMException('Tainted canvases may not be exported.','SecurityError');
      return 'data:image/jpeg;base64,YQ==';
    };
    w.HTMLCanvasElement.prototype.getBoundingClientRect=function(){return {left:0,top:0,width:600,height:400};};
    w.HTMLCanvasElement.prototype.setPointerCapture=function(id){this._pointer=id;};
    w.HTMLCanvasElement.prototype.hasPointerCapture=function(id){return this._pointer===id;};
    w.HTMLCanvasElement.prototype.releasePointerCapture=function(){this._pointer=null;};
    w.Image=class{
      constructor(){this.width=this.naturalWidth=640;this.height=this.naturalHeight=160;}
      set src(value){this._src=value;if(value){decoded.push(value);setTimeout(()=>this.onload?.(),0);}}
      get src(){return this._src;}
    };
    w.fetch=async(url,options)=>{
      const body=JSON.parse(options.body);
      if(body.filename==='physics-worked-solution-references.jpg'){
        solutionRequests.push({url,body});const ref=JSON.parse(body.message.split('\n').pop());
        return {ok:true,json:async()=>({answers:[{id:ref.id,answer:'Mock result',steps:['Identify the quantities.','Apply the relation to obtain the result.'],check:'Checked units.'}]})};
      }
      requests.push({url,body});return {ok:true,json:async()=>({verdict:'correct',confidence:'high',feedback:'Net horizontal force is zero at constant speed.',answer_check:'Every part checked.',steps:[],weak_points:[]})};};
  }
});
const w=dom.window,$=id=>w.document.getElementById(id);
const pause=()=>new Promise(r=>setTimeout(r,25));
async function until(check){for(let i=0;i<160;i++){if(check())return;await pause();}throw Error('Timed out: '+$('ai-status').textContent+' '+$('feedback').textContent);}
function change(id,value){$(id).value=value;$(id).dispatchEvent(new w.Event('change'));}
function pointer(type,x,y){const event=new w.MouseEvent(type,{clientX:x,clientY:y,button:0,bubbles:true,cancelable:true});Object.defineProperties(event,{pointerId:{value:1},isPrimary:{value:true},pointerType:{value:'pen'}});$('drawing-canvas').dispatchEvent(event);}
(async()=>{
  await pause();assert.deepEqual(errors,[]);
  assert.equal(loaded.length,0,'Local scripts load only when AI needs image pixels');
  $('login-name').value='Local regression';$('login-form').dispatchEvent(new w.Event('submit',{cancelable:true}));
  change('practice-chapter','giancoli-ch4');change('mode','chapter');change('chapter-question','giancoli-ch4-q36');
  pointer('pointerdown',20,30);pointer('pointermove',120,70);pointer('pointerup',120,70);
  Object.defineProperty(w.navigator,'onLine',{value:false,configurable:true});
  $('check').click();assert.match($('solution-body').textContent,/Prebuilt AI answer/);
  Object.defineProperty(w.navigator,'onLine',{value:true,configurable:true});
  $('ai-check').click();await until(()=>requests.length===1&&!$('ai-check').disabled);
  assert.match($('ai-status').textContent,/Explanation ready/);
  assert.ok(requests[0].body.image,'Drawing and textbook question can be exported together');
  assert.ok(loaded.some(url=>url.endsWith('ch4-q36-1.png.js')),'The exact screenshot question uses its local image bundle');
  assert.ok(decoded.every(src=>src.startsWith('data:')),'No file image can taint a canvas');
  assert.ok(decoded.length>=2,'Question and handwritten work are both decoded');
  const source='assets/physics12-practice/ch4-q36-1.png';
  const image=await w.PhysicsImageAssets.decode(source);
  assert.deepEqual(Buffer.from(image.src.split(',')[1],'base64'),fs.readFileSync(path.join(root,source)),'Image bytes retain the original question');
  const previousLoads=loaded.length;await w.PhysicsImageAssets.decode(source);assert.equal(loaded.length,previousLoads,'Repeated review reuses cached image bytes');
  // A keyed question must safely export both its question and answer-key image.
  change('practice-chapter','giancoli-ch1');change('chapter-question','giancoli-ch1-q1');
  $('response-input').value='a) 3, b) 4, c) 3, d) 1, e) 2, f) 4, g) 2';$('response-input').dispatchEvent(new w.Event('input'));
  $('check').click();await until(()=>requests.length===2&&$('attempt-count').textContent==='1');
  assert.ok(loaded.some(url=>url.endsWith('answer-ch1-q1-1.png.js')),'Automatic verification includes an origin-clean answer key');
  const controller=new w.AbortController(),canceled=w.PhysicsImageAssets.decode('assets/physics12-practice/ch1-q2-1.png',controller.signal);
  controller.abort();await assert.rejects(canceled,e=>e.name==='AbortError');
  await w.PhysicsImageAssets.decode('assets/physics12-practice/ch1-q2-1.png');
  assert.deepEqual(errors,[]);
  assert.equal(solutionRequests.length,1,'Missing worked steps export reference images independently of student verification');
  assert.ok(solutionRequests[0].body.image);
  assert.ok([...requests,...solutionRequests].every(r=>r.url===w.PhotoReview.endpoint),'Only the mocked AI endpoint is called');
  for(const url of loaded)assert.ok(fs.existsSync(fileURLToPath(url)));
  w.close();console.log('Passed: local-file handwritten AI review, question/key image export, byte fidelity, cache reuse and cancellation.');
})().catch(e=>{console.error(e);w.close();process.exitCode=1;});
