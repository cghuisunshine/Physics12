#!/usr/bin/env python3
"""Extract Giancoli's numbered problem sets and build a Physics 12 practice studio.

Uses PyMuPDF to retain the original mathematical typography. The inventory records
every source rectangle; PNG assets are shared by the studio and stay local.
Rebuild markup with Python alone, or pass --extract to regenerate the inventory
and images from Physics12.pdf (requires PyMuPDF and Poppler's pdftotext).
"""
import argparse
import base64
from functools import lru_cache
import html
import hashlib
import json
from pathlib import Path
import re
import subprocess
from generate_physics12_answers import valid as valid_prebuilt, fingerprint

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / 'tools'
INVENTORY = ROOT / 'content/physics12/practice-problems.json'
ASSETS = ROOT / 'assets/physics12-practice'
CHAPTERS = json.loads((ROOT / 'content/physics12/chapters.json').read_text())
E = html.escape


def reference_pages(text, pages_text):
    refs = set()
    # Include chained references ("Figs. 4–5 and 4–6") and figures in other chapters.
    for match in re.finditer(r'Fig(?:ure)?s?\.?\s*(\d+)[;–−-](\d+)',text):
        pairs=[match.groups()]
        rest=text[match.end():match.end()+70]
        chain=re.match(r'[a-z]?(?:\s*(?:,|and|or)\s*\d+[;–−-]\d+[a-z]?)*',rest)[0]
        pairs += re.findall(r'(\d+)[;–−-](\d+)',chain)
        for ch,fig in pairs:
            chapter=next((c for c in CHAPTERS if c['number']==int(ch)),None)
            if chapter:
                pattern=r'FIGURE\s+'+ch+r'[;–−-]'+fig+r'\b'
                refs.update(i+1 for i in range(chapter['start']+20,chapter['end']+21) if re.search(pattern,pages_text[i]))
    return sorted(refs)


def extract():
    import pymupdf as pdf
    source = ROOT / 'Physics12.pdf'
    doc = pdf.open(source)
    ASSETS.mkdir(parents=True, exist_ok=True)
    cache = ROOT / 'tmp/physics12-practice/book.txt'
    cache.parent.mkdir(parents=True, exist_ok=True)
    if not cache.exists():
        subprocess.run(['pdftotext', '-layout', str(source), str(cache)], check=True)
    pages_text = cache.read_text().split('\f')

    @lru_cache(maxsize=24)
    def lines(pg):
        return [dict(text=''.join(s['text'] for s in line['spans']).strip(),
                     box=line['bbox'], spans=line['spans'])
                for b in doc[pg-1].get_text('dict')['blocks'] for line in b.get('lines', [])]

    def raster(pg, rect, name, scale=2.5):
        path = ASSETS / (name + '.png')
        if not path.exists() or rect[3] > 731:
            doc[pg-1].get_pixmap(matrix=pdf.Matrix(scale, scale), clip=pdf.Rect(rect), alpha=False).save(path)
        return {'src': str(path.relative_to(ROOT)), 'page': pg,
                'rect': [round(v, 2) for v in rect], 'width': round(rect[2]-rect[0])}

    def image_run(cells, first, last, y, end_y, prefix):
        result = []
        for j in range(first, last+1):
            cell = cells[j]
            top = y-2 if j == first else cell['top']
            bottom = end_y-2 if j == last else cell['bottom']
            if bottom-top < 3:
                continue
            rect = [cell['x0'], max(cell['top'], top), cell['x1'], min(cell['bottom'], bottom)]
            if rect[3] <= rect[1] or (j != first and not doc[cell['page']-1].get_text(clip=pdf.Rect(rect)).strip()):
                continue
            result.append(raster(cell['page'], rect, f'{prefix}-{len(result)+1}'))
        return result

    questions = []
    for chapter in CHAPTERS:
        n = chapter['number']
        start = max(i+1 for i in range(chapter['start']+20, chapter['end']+21)
                    if re.search(r'^ *Problems *$', pages_text[i], re.M))
        cells, events = [], []
        stopped = False
        for pg in range(start, chapter['end']+22):
            ls = lines(pg)
            headings = sorted((l for l in ls if l['text'] in ['Problems', 'General Problems', 'Search and Learn']
                               and any(s['size'] > 15 for s in l['spans'])), key=lambda l: l['box'][1])
            stop_y = next((l['box'][1]-3 for l in headings if l['text'] == 'Search and Learn'), 755)
            boundaries = [31] + [l['box'][3]+3 for l in headings if l['text'] != 'Search and Learn'] + [stop_y]
            boundaries = sorted(set(v for v in boundaries if v <= stop_y))
            if pg == start:
                boundaries = [v for v in boundaries if v >= next(l['box'][3]+3 for l in headings if l['text']=='Problems')]
            for top, bottom in zip(boundaries, boundaries[1:]):
                for col, (x0, x1) in enumerate([(30, 285), (289, 548)]):
                    ci = len(cells)
                    body_bottom = max([731] + [l['box'][3]+2 for l in ls if x0 <= l['box'][0] < x1
                                              and l['box'][1] < 752 and any('TimesTen' in s['font'] for s in l['spans'])])
                    cells.append(dict(page=pg, top=top, bottom=min(bottom,body_bottom), x0=x0, x1=x1))
                    if col == 0 and any(l['text']=='General Problems' and abs(l['box'][3]+3-top)<1 for l in headings):
                        events.append(dict(cell=ci,y=top-.1,section='general',title='General problems'))
                    for line in sorted(ls, key=lambda l:l['box'][1]):
                        x, y, _, _ = line['box']
                        if not (top <= y < bottom and x0 <= x < x1):
                            continue
                        text = line['text']
                        section = re.match(r'^\*?'+str(n)+r'[;–−-](\d+)\s+(.+)', text)
                        if section and 'Univers-Bold' in line['spans'][0]['font']:
                            events.append(dict(cell=ci, y=y, section=section[1], title=text.replace(';', '–')))
                        match = re.match(r'^\*?(\d{1,3})\.\s*', text)
                        if match and 'TimesTen-Bold' in line['spans'][0]['font'] and x < x0+22:
                            level = re.search(r'\((I{1,3})\)', text)
                            events.append(dict(cell=ci, y=y, number=int(match[1]), level=len(level[1]) if level else 2))
            if stop_y < 755:
                stopped = True
                break
        if not stopped:
            raise ValueError(f'No Search and Learn boundary for chapter {n}')
        events.sort(key=lambda e:(e['cell'],e['y']))
        qs = [e for e in events if 'number' in e]
        numbers = [e['number'] for e in qs]
        if numbers != list(range(1, max(numbers)+1)):
            raise ValueError(f'Nonconsecutive extraction in chapter {n}: {numbers}')
        topic, topic_title = 'Problems', 'Section problems'
        for event in events:
            if 'section' in event:
                topic, topic_title = f'{n}.{event["section"]}', event['title']
                continue
            index = qs.index(event)
            following = qs[index+1] if index+1<len(qs) else dict(cell=len(cells)-1, y=cells[-1]['bottom']+2)
            end_cell = following['cell']
            parts = image_run(cells,event['cell'],end_cell,event['y'],following['y'],f'ch{n}-q{event["number"]}')
            if not parts:
                raise ValueError(f'Empty crop for chapter {n}, problem {event["number"]}: {event}, next {following}')
            source_pages = sorted(set(part['page'] for part in parts))
            text = '\n'.join(doc[p['page']-1].get_text(clip=pdf.Rect(p['rect'])) for p in parts)
            # The floating figure may be outside the question's column/crop.
            # Preserve its complete original page as clearly labelled context.
            refs = reference_pages(text,pages_text)
            context = [raster(pg,[20,25,558,733],f'page-{pg}',2) for pg in sorted(refs)]
            questions.append(dict(id=f'giancoli-ch{n}-q{event["number"]}', chapter=n, number=event['number'],
                                  topic=topic, topicTitle=topic_title, level=event['level'],
                                  page=source_pages[0], images=parts, context=context, text=text))
        print(f'Chapter {n}: {len(qs)} consecutive problems', flush=True)

    # The answer appendix has three columns and chapter headings in reading order.
    cells, events = [], []
    for pg in range(1031,1047):
        ls = lines(pg)
        for col in range(3):
            x0, x1 = 32+174*col, 32+174*(col+1)
            ci = len(cells)
            cells.append(dict(page=pg,top=31,bottom=733,x0=x0,x1=x1))
            for line in ls:
                x,y,_,_ = line['box']
                if not (x0 <= x < x1 and 31 < y < 731):
                    continue
                if re.fullmatch(r'Chapter \d+',line['text']):
                    events.append(dict(cell=ci,y=y,chapter=int(line['text'].split()[1])))
                m = re.match(r'^(\d{1,3})\.\s*',line['text'])
                if m and x<x0+22 and 'TimesTen-Bold' in line['spans'][0]['font']:
                    events.append(dict(cell=ci,y=y,number=int(m[1])))
    events.sort(key=lambda e:(e['cell'],e['y']))
    current = None
    answers = {}
    for i,event in enumerate(events):
        if 'chapter' in event:
            current=event['chapter']
            continue
        if current is None:
            continue
        next_event = events[i+1] if i+1<len(events) else dict(cell=len(cells)-1,y=733)
        key = (current,event['number'])
        if key in answers or event['number']%2 != 1:
            raise ValueError(f'Ambiguous answer label: {key}')
        answers[key] = image_run(cells,event['cell'],next_event['cell'],event['y'],next_event['y'],f'answer-ch{current}-q{event["number"]}')
    for q in questions:
        q['answers'] = answers.get((q['chapter'],q['number']),[])
    inventory = dict(source='Physics12.pdf', printedPageOffset=21, question_count=len(questions),
                     answer_count=sum(bool(q['answers']) for q in questions), questions=questions)
    INVENTORY.write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    print(f'Extracted {len(questions)} problems; {inventory["answer_count"]} supplied answers.',flush=True)


def refresh_context():
    import pymupdf as pdf
    doc=pdf.open(ROOT/'Physics12.pdf')
    pages_text=(ROOT/'tmp/physics12-practice/book.txt').read_text().split('\f')
    inventory=json.loads(INVENTORY.read_text())
    for q in inventory['questions']:
        q['context']=[]
        for pg in reference_pages(q['text'],pages_text):
            path=ASSETS/f'page-{pg}.png'
            if not path.exists():
                doc[pg-1].get_pixmap(matrix=pdf.Matrix(2,2),clip=pdf.Rect(20,25,558,733),alpha=False).save(path)
            q['context'].append(dict(src=str(path.relative_to(ROOT)),page=pg,rect=[20,25,558,733],width=538))
    INVENTORY.write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')


def img(part, alt):
    return f'<img src="{E(part["src"])}" alt="{E(alt)}" style="width:{part["width"]*2}px;max-width:100%;height:auto" loading="lazy">'


def script(name):
    text=(TOOLS/name).read_text()
    if '</script' in text.lower():
        raise ValueError(f'Unsafe inline script terminator in {name}')
    return '<script>\n'+text+'\n</script>\n'


def build(require_prebuilt=True):
    inventory = json.loads(INVENTORY.read_text())
    prebuilt_path=ROOT/'content/physics12/prebuilt-answers.json'
    prebuilt=json.loads(prebuilt_path.read_text())['answers'] if prebuilt_path.exists() else {}
    missing=[q['id'] for q in inventory['questions'] if not q['answers']
             and not valid_prebuilt(prebuilt.get(q['id']),fingerprint(q))]
    if missing and require_prebuilt:
        raise ValueError(f'{len(missing)} problems need prebuilt answers. The existing practice page was kept. '
                         'Run tools/generate_physics12_answers.py --build to complete the offline key; '
                         f'first missing: {missing[0]}. Use --allow-missing only for a development preview.')
    # Script loading is supported for local files; fetch(file://...) is not.
    # Keep the large image data out of the page and load only the requested PNGs
    # as data URLs for origin-clean canvas export during AI review.
    sources={part['src'] for q in inventory['questions'] for part in q['images']+q['context']+q['answers']}
    for src in sorted(sources):
        image_path=ROOT/src
        companion=Path(str(image_path)+'.js')
        if not companion.exists() or companion.stat().st_mtime<image_path.stat().st_mtime:
            data='data:image/png;base64,'+base64.b64encode(image_path.read_bytes()).decode('ascii')
            companion.write_text('window.PhysicsImageAssets.register('+json.dumps(src)+','+json.dumps(data)+');\n')
    by_ch = {c['number']:c for c in CHAPTERS}
    bank = []
    for q in inventory['questions']:
        c = by_ch[q['chapter']]
        label = f'Chapter {q["chapter"]}, problem {q["number"]}'
        statement = ''.join(img(p,label+(' (continued)' if i else '')+' — '+q['text'][:900]) for i,p in enumerate(q['images']))
        if q['context']:
            statement += '<details class="source-context"><summary>Referenced diagrams · original textbook pages</summary><p class="small">Find the figure number named in the question. Full pages preserve floating figures and their labels.</p>'
            statement += ''.join(img(p,f'Referenced diagram context, PDF page {p["page"]}') for p in q['context'])+'</details>'
        if q['answers']:
            answer_source='textbook'
            answer='See textbook answer key'
            solution=('<div class="answer-provenance" data-answer-source="textbook"><span class="badge">Textbook answer</span></div>'
                      '<p class="small">The book’s final-answer key; full worked solutions are not supplied.</p>'
                      + ''.join(img(p,f'Textbook answer to {label}') for p in q['answers']))
        elif q['id'] not in missing:
            a=prebuilt[q['id']]
            answer_source='prebuilt-ai'
            answer=a['answer']
            solution=('<div class="answer-provenance" data-answer-source="prebuilt-ai"><span class="badge" style="background:#fff0c9;color:#70521d">Prebuilt AI answer</span></div>'
                      '<p class="small">Generated in advance · separate from the textbook answer key.</p>'
                      f'<p class="prebuilt-answer" style="white-space:pre-wrap"><strong>{E(a["answer"])}</strong></p>')
            if a['steps']:
                solution+='<h3>Step-by-step solution</h3><ol class="worked-steps">'+''.join(f'<li style="white-space:pre-wrap">{E(step)}</li>' for step in a['steps'])+'</ol>'
            if a['check']:
                solution+=f'<p style="white-space:pre-wrap"><strong>Check:</strong> {E(a["check"])}</p>'
            if a.get('assumptions'):
                solution+='<h3>Assumptions'+(' / review note' if a.get('needsReview') else '')+'</h3><ul>'+''.join(f'<li>{E(s)}</li>' for s in a['assumptions'])+'</ul>'
            if a.get('needsReview'):
                solution+='<p class="small">AI answer flagged for review.</p>'
        else:
            answer_source='pending-ai'
            answer=solution=''
        bank.append(dict(id=q['id'],sourceId=f'{q["chapter"]}.{q["number"]}',kind='textbook',
                         chapter=f'giancoli-ch{q["chapter"]}',chapterNumber=q['chapter'],chapterTitle=c['title'],
                         number=q['number'],topic=f'Ch {q["chapter"]} · {q["topic"]}',topicTitle=q['topicTitle'],
                         level=q['level'],questionType='Textbook problem',title=f'{label} · {c["title"]}',
                         html=statement,solution=solution,answer=answer,answerSource=answer_source,
                         hasAnswer=bool(solution),questionText=q['text'],
                         hasWorkedSteps=bool(not q['answers'] and prebuilt.get(q['id'],{}).get('steps')),
                         solutionHash=hashlib.sha256((fingerprint(q)+solution).encode()).hexdigest(),
                         answerHash=fingerprint(q) if not q['answers'] else None,
                         url=f'Physics12.pdf#page={q["page"]}'))
    template = (TOOLS/'physics12-practice-template.html').read_text()
    template = template.replace('/* SOLUTION_MATH_CSS */',(TOOLS/'vendor/katex/katex.min.css').read_text())
    template = template.replace('Model answer and worked solution','Answer key')
    template = template.replace('Work through a question, learn from the result, and build from there.',
                                'Practise the original Giancoli problems, one chapter at a time. <a href="physics12-tutorial.html">Study the lessons ↗</a>')
    template = template.replace('<!-- PHYSICS12_FOOTNOTE -->',
                      f'<p class="footnote">{len(bank):,} original numbered problems from all 33 chapters of Physics12.pdf, including general problems. Search and Learn sets are excluded. {inventory["answer_count"]:,} textbook answers and {len(bank)-inventory["answer_count"]-len(missing):,} labelled Prebuilt AI answers are available offline. '+(f'Show answer generates and saves an AI answer for the remaining {len(missing):,} problems; the first generation needs internet. ' if missing else 'Every problem has a saved answer. ')+ 'AI answers are separate from the textbook key. Difficulty I–III follows the book; unranked problems use Intermediate. Keep assets/physics12-practice/ beside this page for offline questions and diagrams, and Physics12.pdf for source links. Drawing, progress, and review work offline. Optional AI assistance and sync require internet.</p>')
    data = json.dumps(bank,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    scripts = '<script id="question-bank" type="application/json">'+data+'</script>\n'
    scripts += ''.join(script(name) for name in ['physics12-activity.js','physics12-adaptive.js','physics12-practice-core.js','physics12-photo-review.js','vendor/katex/katex.min.js','physics12-solution-format.js','physics12-answer-key.js','physics12-worked-solution.js','physics12-drawing-pad.js','physics12-students.js','physics12-live-share.js','physics12-image-assets.js','physics12-practice.js'])
    (ROOT/'physics12-practice.html').write_text(template.replace('<!-- PRACTICE_SCRIPTS -->',scripts))
    head = re.search(r'<head>(.*?)</head>',template,re.S)[1].replace('Practice Studio','Student Activity')
    dialog = re.search(r'<dialog[^>]*>(.*?)</dialog>',template,re.S)[1]
    dialog = re.sub(r'<button id="activity-close".*?</button>','',dialog)
    dialog = re.sub(r'<p><a id="activity-page-link".*?</p>','',dialog)
    monitor = '<!doctype html><html lang="en"><head>'+head+'</head><body><header><a class="brand" href="physics12-practice.html">Physics 12 <span>/ Practice Studio</span></a><a href="content.html">Browse chapters ↗</a></header><main style="max-width:850px">'+dialog
    monitor += '<section class="panel storage"><h3>Optional sync</h3><label for="monitor-key">Firebase API key</label><input id="monitor-key" type="password" autocomplete="off"><button id="monitor-connect" class="secondary" type="button">Connect to synced history</button><p class="small">Reads Physics 12 history only.</p></section></main>'
    monitor += script('physics12-activity.js')+script('physics12-monitor.js')+'</body></html>'
    (ROOT/'physics12-monitor.html').write_text(monitor)
    print(f'Built physics12-practice.html: {len(bank):,} problems; {inventory["answer_count"]:,} textbook answers, {len(bank)-inventory["answer_count"]-len(missing):,} prebuilt AI answers, {len(missing):,} generated on first use.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract',action='store_true')
    parser.add_argument('--refresh-context',action='store_true')
    completeness=parser.add_mutually_exclusive_group()
    completeness.add_argument('--require-prebuilt',action='store_true',help='Require a complete offline key (the default)')
    completeness.add_argument('--allow-missing',action='store_true',help='Development preview only: allow first-use online generation for missing keys')
    args=parser.parse_args()
    if args.extract:
        extract()
    elif args.refresh_context:
        refresh_context()
    build(require_prebuilt=not args.allow_missing)
