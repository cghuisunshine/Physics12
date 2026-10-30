#!/usr/bin/env python3
"""Build the standalone tutorial using the chapter-tutorial-html skill renderer."""
from pathlib import Path
import html
import importlib.util
import json
import re
import sys

from physics12_content import CHAPTERS, CONSTANTS
from physics12_derivations import REVIEW_URL, REVIEW_CHAPTERS

ROOT = Path(__file__).resolve().parents[1]
esc = html.escape


def diagram(number):
    drawings = {
        4: ('Forces on a crate sliding right on a level floor. Normal force points up, weight down, pull right, kinetic friction left.',
            '<path d="M60 210H550" stroke="#bac9c2" stroke-width="2"/><rect x="245" y="130" width="110" height="80" rx="6" fill="#e5f0e8" stroke="#076c68" stroke-width="2"/>'
            '<g stroke-width="3" fill="none" marker-end="url(#d4arrow)"><path d="M300 165V55" stroke="#245fa6"/><path d="M300 175V280" stroke="#245fa6"/><path d="M320 170H500" stroke="#076c68"/><path d="M280 170H175" stroke="#c07b28"/></g>'
            '<text x="315" y="64">N</text><text x="315" y="277">mg</text><text x="425" y="152">pull</text><text x="135" y="152">friction</text>',
            'Free-body diagram for the worked crate example. Opposite vertical forces balance; the horizontal resultant accelerates the crate. Arrows are schematic.'),
        5: ('Circular orbit with velocity tangent to the orbit and gravitational acceleration toward the central mass.',
            '<circle cx="280" cy="165" r="115" fill="none" stroke="#bac9c2" stroke-dasharray="5 5" stroke-width="2"/><circle cx="280" cy="165" r="35" fill="#e1ece5" stroke="#076c68" stroke-width="2"/><circle cx="395" cy="165" r="8" fill="#076c68"/>'
            '<path d="M395 154V42" stroke="#245fa6" stroke-width="3" marker-end="url(#d5arrow)"/><path d="M384 165H320" stroke="#c07b28" stroke-width="3" marker-end="url(#d5arrow)"/>'
            '<text x="410" y="75">v (tangent)</text><text x="327" y="190">a (inward)</text><text x="250" y="170">mass M</text><text x="284" y="300">circular orbit</text>',
            'For a circular satellite orbit, gravity changes the direction of velocity. The tangent velocity and inward acceleration are perpendicular.'),
        16: ('Two equal positive charges at equal distances from a midpoint. Their fields at that midpoint point in opposite directions and cancel.',
             '<path d="M80 165H530" stroke="#bac9c2" stroke-width="2"/><circle cx="115" cy="165" r="29" fill="#e5f0e8" stroke="#076c68" stroke-width="2"/><circle cx="485" cy="165" r="29" fill="#e5f0e8" stroke="#076c68" stroke-width="2"/>'
             '<text x="103" y="172" style="font-size:23px;fill:#076c68">+</text><text x="473" y="172" style="font-size:23px;fill:#076c68">+</text><circle cx="300" cy="165" r="4" fill="#142e40"/>'
             '<path d="M300 147H405" stroke="#245fa6" stroke-width="3" marker-end="url(#d16arrow)"/><path d="M300 183H195" stroke="#c07b28" stroke-width="3" marker-end="url(#d16arrow)"/>'
             '<text x="310" y="125">field from left charge</text><text x="155" y="214">field from right charge</text><text x="220" y="270">midpoint: E_net = 0</text>',
             'Superposition at a single point. These are the two field contributions at the midpoint, not lines tracing the field throughout space.'),
        23: ('Ray diagram for a converging lens: object 30 centimetres to the left, focal length 10 centimetres, real inverted image 15 centimetres to the right.',
             '<path d="M20 180H580" stroke="#bac9c2"/><path d="M350 50V270" stroke="#076c68" stroke-width="3"/><path d="M344 62l6-12 6 12M344 258l6 12 6-12" stroke="#076c68" fill="none" stroke-width="2"/>'
             '<path d="M50 180V100m-5 9 5-9 5 9" fill="none" stroke="#142e40" stroke-width="3"/><path d="M500 180V220m-5-9 5 9 5-9" fill="none" stroke="#142e40" stroke-width="3"/>'
             '<path d="M50 100H350L500 220" fill="none" stroke="#245fa6" stroke-width="2"/><path d="M50 100 500 220" fill="none" stroke="#c07b28" stroke-width="2"/><path d="M50 100 350 220H500" fill="none" stroke="#076c68" stroke-width="2"/>'
             '<circle cx="250" cy="180" r="3" fill="#142e40"/><circle cx="450" cy="180" r="3" fill="#142e40"/><text x="235" y="200">F</text><text x="445" y="200">F</text><text x="25" y="85">object</text><text x="470" y="245">image</text><text x="315" y="35">lens</text><text x="104" y="293">d_o = 30 cm</text><text x="386" y="293">d_i = 15 cm</text>',
             'Three ideal rays meet at a real, inverted image. The diagram uses the same object distance, focal length, and image distance as the worked example.'),
    }
    if number not in drawings:
        return ''
    alt, body, caption = drawings[number]
    return (f'<figure class="diagram"><svg viewBox="0 0 600 330" role="img" aria-labelledby="diagram-{number}"><title id="diagram-{number}">{esc(alt)}</title>'
            f'<defs><marker id="d{number}arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="#526675"/></marker></defs>'
            f'{body}</svg><figcaption>{esc(caption)}</figcaption></figure>')


def slider(ident, label, minimum, maximum, value, step, unit):
    return (f'<label for="{ident}">{label}<span><output id="{ident}-value" for="{ident}">{value}</output> {unit}</span>'
            f'<input id="{ident}" type="range" min="{minimum}" max="{maximum}" value="{value}" step="{step}"></label>')


def lab(number):
    if number == 3:
        return ('<section class="lab" aria-labelledby="projectile-title"><span class="lab-tag">Interactive model 01</span><h3 id="projectile-title">Explore a projectile</h3><p>Change launch speed and angle. Predict the range before you move a slider.</p><div class="lab-controls">'
                + slider('projectile-speed', 'Launch speed', 5, 40, 20, 1, 'm/s')
                + slider('projectile-angle', 'Launch angle', 10, 80, 30, 1, '°')
                + '</div><svg viewBox="0 0 600 290" role="img" aria-labelledby="projectile-chart-title projectile-desc"><title id="projectile-chart-title">Projectile trajectory, horizontal distance versus height</title><desc id="projectile-desc"></desc><path class="axis" d="M45 30V240H575M45 135H575"/><text x="20" y="244">0</text><text x="7" y="139">50</text><text x="2" y="34">100</text><text x="45" y="265">0</text><text x="295" y="265">100</text><text x="548" y="265">200 m</text><text x="50" y="20">height / m</text><path id="projectile-path" class="curve" d="M45 240"/></svg><p id="projectile-result" class="lab-result" role="status"></p><p class="assumption">Model: no air resistance, g = 9.81 m/s², and equal launch and landing height. The axes stay fixed so different launches can be compared. Try complementary angles, then 45°.</p></section>')
    if number == 19:
        return ('<section class="lab" aria-labelledby="circuit-title"><span class="lab-tag">Interactive model 02</span><h3 id="circuit-title">Series or parallel?</h3><p>Compare the same two resistors across an ideal battery. Watch which quantity is shared.</p><div class="lab-controls">'
                '<label for="circuit-mode">Connection<select id="circuit-mode"><option value="series">Series</option><option value="parallel" selected>Parallel</option></select></label>'
                + slider('circuit-voltage', 'Battery voltage', 1, 24, 12, 1, 'V')
                + slider('circuit-r1', 'Resistance R₁', 1, 20, 6, 1, 'Ω')
                + slider('circuit-r2', 'Resistance R₂', 1, 20, 3, 1, 'Ω')
                + '</div><svg viewBox="0 0 600 260" role="img" aria-labelledby="circuit-chart-title circuit-desc"><title id="circuit-chart-title">Ideal battery and two-resistor circuit</title><desc id="circuit-desc"></desc><g id="circuit-drawing"></g></svg><p id="circuit-result" class="lab-result" role="status"></p><p class="assumption">Model: ideal DC voltage source and ohmic resistors. Wire and battery internal resistance are zero. Power values describe this model; the controls do not specify real component ratings.</p></section>')
    if number == 24:
        return ('<section class="lab" aria-labelledby="interference-title"><span class="lab-tag">Interactive model 03</span><h3 id="interference-title">Move the interference fringes</h3><p>Change wavelength and slit spacing. The graph shows intensity relative to its maximum.</p><div class="lab-controls">'
                + slider('interference-wavelength', 'Wavelength', 400, 700, 600, 10, 'nm')
                + slider('interference-separation', 'Slit separation', 0.1, 0.6, 0.2, 0.01, 'mm')
                + '</div><svg viewBox="0 0 600 270" role="img" aria-labelledby="interference-chart-title interference-desc"><title id="interference-chart-title">Double-slit relative intensity versus screen position</title><desc id="interference-desc"></desc><path class="axis" d="M45 35V220H575"/><text x="15" y="42">1</text><text x="15" y="224">0</text><text x="43" y="245">−20</text><text x="305" y="245">0</text><text x="540" y="245">+20 mm</text><text x="47" y="20">relative intensity</text><path class="curve" id="interference-path" d="M45 220"/></svg><p id="interference-result" class="lab-result" role="status"></p><p class="assumption">Model: equal coherent sources, ideal narrow slits, screen distance L = 2.00 m, and small angles. I/I_max = cos²(πdy/λL). The finite-width single-slit envelope is omitted to isolate fringe spacing.</p></section>')
    if number == 30:
        return ('<section class="lab" aria-labelledby="decay-title"><span class="lab-tag">Interactive model 04</span><h3 id="decay-title">Follow the parent nuclei</h3><p>Compare how changing half-life changes the expected surviving fraction at a fixed time.</p><div class="lab-controls">'
                + slider('decay-halflife', 'Half-life', 1, 10, 6, 0.5, 'h')
                + slider('decay-time', 'Elapsed time', 0, 24, 18, 0.5, 'h')
                + '</div><svg viewBox="0 0 600 285" role="img" aria-labelledby="decay-chart-title decay-desc"><title id="decay-chart-title">Expected parent nuclei remaining versus time</title><desc id="decay-desc"></desc><path class="axis" d="M45 35V235H575M45 135H575"/><text x="5" y="40">100%</text><text x="12" y="139">50%</text><text x="22" y="239">0</text><text x="45" y="260">0</text><text x="299" y="260">12</text><text x="550" y="260">24 h</text><path id="decay-path" class="curve" d="M45 35"/><path id="decay-marker" class="accent" d="M45 235V35"/><circle id="decay-dot" r="5" fill="#c07b28" cx="45" cy="35"/></svg><p id="decay-result" class="lab-result" role="status"></p><p class="assumption">Model: one radioactive parent species with a constant decay probability per nucleus, no replenishment, and no tracking of daughter decays. The curve is a statistical expectation; individual decay times are random.</p></section>')
    return ''


def outline():
    lines = ['# Physics 12 Tutorial', '@page_title: Physics 12 Tutorial | Giancoli Study Companion',
             '@subtitle: A guided study of all 33 chapters in Physics12.pdf.']
    for c in CHAPTERS:
        lines += [f'\n## {c["number"]} {c["title"]}', f'> {c["goal"]}']
        for name, text in c['concepts']:
            lines += [f'\n### {name}', text]
        lines += ['\n### Essential equations']
        for expression, note in c['formulas']:
            lines += [f'- `{expression}` — {note}']
        lines += ['\n### Equation explanations & derivations',
                  'Original explanations mapped to the topic scope of the university review. '
                  'A derivative is an instantaneous rate; an integral adds small contributions. '
                  'Definitions and physical laws are stated as starting points.']
        for item in c['derivations']['items']:
            lines += [f'\n#### {item["title"]}', f'**Concept:** {item["concept"]}',
                      f'**Assumptions:** {item["assumptions"]}']
            lines += [f'{i}. {step}' for i, step in enumerate(item['steps'], 1)]
            lines += [f'**Result:** `{item["result"]}`', f'**Check:** {item["check"]}']
        lines += ['**Scope reference:** ' + ', '.join(
            f'[{n}. {REVIEW_CHAPTERS[n]}]({REVIEW_URL}#chapter-{n})'
            for n in c['derivations']['review_chapters'])]
        lines += ['\n### Worked example', c['example'], '\n### Solution']
        lines += [f'{i}. {text}' for i, text in enumerate(c['steps'], 1)]
        lines += [f'**Answer:** {c["answer"]}', '\n### Common trap', c['pitfall'],
                  '\n### Self-check', c['quiz']['question']]
        lines += [f'- {text}' for text in c['quiz']['options']]
        lines += [f'**Answer:** {c["quiz"]["options"][c["quiz"]["correct"]]}. {c["quiz"]["explanation"]}']
    return '\n'.join(lines) + '\n'


def derivations(chapter):
    n = chapter['number']
    items = []
    for i, item in enumerate(chapter['derivations']['items'], 1):
        opened = ' open' if i == 1 else ''
        items.append(
            f'<details class="derivation" id="derivation-{n}-{i}"{opened}>'
            f'<summary>{esc(item["title"])}</summary><div class="derivation-body">'
            f'<p><strong>Concept.</strong> {esc(item["concept"])}</p>'
            f'<p class="derivation-assumptions"><strong>Assumptions & starting points.</strong> {esc(item["assumptions"])}</p>'
            '<ol>' + ''.join(f'<li>{esc(step)}</li>' for step in item['steps']) + '</ol>'
            f'<div class="equation derivation-result"><small>Result</small><code>{esc(item["result"])}</code></div>'
            f'<p class="derivation-check"><strong>Check & interpretation.</strong> {esc(item["check"])}</p>'
            '</div></details>')
    references = ' · '.join(
        f'<a href="{REVIEW_URL}#chapter-{r}" target="_blank" rel="noopener">{r}. {esc(REVIEW_CHAPTERS[r])}</a>'
        for r in chapter['derivations']['review_chapters'])
    return (f'<section class="derivations" aria-labelledby="derivations-{n}">'
            f'<h3 id="derivations-{n}">Equation explanations & derivations</h3>'
            '<p class="derivation-intro">Follow the idea → assumptions → steps → result → check. '
            'Open a title to study another explanation. A derivative is an instantaneous rate; '
            'an integral adds small contributions. Physical laws and quantum principles are starting points.</p>'
            + ''.join(items)
            + f'<p class="derivation-sources">University review topic links: {references}. '
            'These explanations are written for this tutorial.</p></section>')


def enrich_sections(rendered):
    """Keep the skill-rendered concept prose, adding accessible study controls."""
    raw = re.findall(r'    <section>\n(.*?)    </section>', rendered, re.S)
    assert len(raw) == len(CHAPTERS) == 33
    cards = []
    for c, base in zip(CHAPTERS, raw):
        n = c['number']
        # The generator supplies escaped paragraph content for every concept.
        concepts = base.split('<h3>Essential equations</h3>')[0]
        concepts = re.sub(r'^\s*<h2>.*?</h2>', '', concepts, count=1, flags=re.S)
        concepts = concepts.replace('<h3>Notes</h3>', '')
        formulas = '<div class="equations">' + ''.join(
            f'<div class="equation"><code>{esc(f)}</code><small>{esc(note)}</small></div>' for f, note in c['formulas']) + '</div>'
        example = (f'<section class="worked" aria-labelledby="example-{n}"><h3 id="example-{n}">Worked example</h3><p>{esc(c["example"])}</p>'
                   '<details class="solution"><summary>Show worked solution</summary><div class="solution-body"><ol>'
                   + ''.join(f'<li>{esc(step)}</li>' for step in c['steps']) + '</ol>'
                   f'<p class="result">{esc(c["answer"])}</p></div></details></section>')
        quiz = (f'<section class="quiz" data-chapter="{n}" aria-labelledby="check-{n}"><h3 id="check-{n}">Check your understanding</h3><p>{esc(c["quiz"]["question"])}</p>'
                '<div class="quiz-options" role="group" aria-label="Answer choices">'
                + ''.join(f'<button type="button" data-choice="{i}" aria-pressed="false">{chr(65+i)}. {esc(option)}</button>' for i, option in enumerate(c['quiz']['options']))
                + '</div><p class="feedback" role="status" hidden></p></section>')
        body = (concepts + diagram(n) + '<h3>Essential equations</h3>' + formulas + derivations(c) + lab(n) + example
                + f'<aside class="pitfall"><strong>Common trap</strong><p>{esc(c["pitfall"])}</p></aside>' + quiz)
        card = (f'<section class="chapter" id="chapter-{n}" data-number="{n}" data-subject="{esc(c["group"])}" data-match="true">'
                f'<header class="chapter-head"><span class="chapter-no" aria-hidden="true">{n:02d}</span><div><div class="chapter-meta"><span>{esc(c["group"])}</span>'
                f'<a href="Physics12.pdf#page={c["start"]+21}" target="_blank" rel="noopener">Book pp. {c["start"]}–{c["end"]} ↗</a></div>'
                f'<h2>{n}. {esc(c["title"])}</h2><p class="goal">{esc(c["goal"])}</p></div></header>'
                f'<details class="lesson" open><summary>Lesson, derivations, example & self-check</summary><div class="lesson-body">{body}</div></details>'
                f'<div class="chapter-foot"><label><input type="checkbox" data-complete="{n}"> Mark chapter studied</label>'
                f'<a href="Physics12.pdf#page={c["start"]+21}" target="_blank" rel="noopener">Read chapter {n} in the book ↗</a></div></section>')
        cards.append(card)
    return '\n'.join(cards)


def main():
    generators = [Path.home() / f'{root}/skills/chapter-tutorial-html/scripts/generate_chapter_html.py' for root in ('.agents', '.codex')]
    generator = next((p for p in generators if p.exists()), None)
    if not generator:
        raise SystemExit('Install the chapter-tutorial-html skill to rebuild this page.')
    spec = importlib.util.spec_from_file_location('chapter_tutorial_generator', generator)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    md = outline()
    meta, sections = module.parse_outline(md)
    template = (ROOT / 'tools/physics12-template.html').read_text()
    # Render concept prose with the installed skill, then add source-aware UI.
    base = module.render_html(meta, sections, '{{SECTIONS}}')
    page = template.replace('{{SECTIONS}}', enrich_sections(base)).replace('{{PAGE_TITLE}}', esc(meta['page_title']))
    groups = list(dict.fromkeys(c['group'] for c in CHAPTERS))
    navigation, roadmap = [], []
    for group in groups:
        members = [c for c in CHAPTERS if c['group'] == group]
        roadmap.append(f'<a href="#chapter-{members[0]["number"]}">{esc(group)}</a>')
        navigation.append(f'<p class="nav-heading" data-nav-group="{esc(group)}">{esc(group)}</p>')
        navigation += [f'<a href="#chapter-{c["number"]}" data-nav-chapter="{c["number"]}"><span class="nav-number">{c["number"]:02d}</span><span>{esc(c["title"])}</span></a>' for c in members]
    constants = ('<table><caption>Frequently used constants (rounded)</caption><thead><tr><th scope="col">Symbol</th><th scope="col">Value</th><th scope="col">Meaning</th></tr></thead><tbody>'
                 + ''.join(f'<tr><th scope="row">{esc(a)}</th><td>{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in CONSTANTS) + '</tbody></table>')
    formulas = ''.join(f'<div><h4><a href="#chapter-{c["number"]}">{c["number"]}. {esc(c["title"])}</a></h4>' + ''.join(f'<p><code>{esc(f)}</code><br><small>{esc(note)}</small></p>' for f, note in c['formulas']) + '</div>' for c in CHAPTERS)
    payload = {str(c['number']): c['quiz'] for c in CHAPTERS}
    script = 'const PHYSICS12_QUIZZES = ' + json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c') + ';\n' + (ROOT / 'tools/physics12-tutorial.js').read_text()
    count = sum(len(c['derivations']['items']) for c in CHAPTERS)
    for key, value in {'DERIVATION_COUNT': str(count), 'NAVIGATION': ''.join(navigation), 'ROADMAP': ''.join(roadmap), 'SUBJECTS': ''.join(f'<option>{esc(g)}</option>' for g in groups), 'CONSTANTS': constants, 'FORMULAS': formulas, 'SCRIPT': script}.items():
        page = page.replace(f'%%{key}%%', value)
    # Avoid unsupported combining-arrow glyphs in system fonts. Preserve script
    # strings as plain text and use a CSS vector arrow for rendered lesson text.
    markup, scripts = page.split('<script>', 1)
    markup = re.sub(r'([A-Za-z])\u20d7', r'<span class="vector">\1</span>', markup)
    page = markup + '<script>' + scripts
    assert not re.search(r'%%[A-Z]+%%|{{[A-Z_]+}}', page)
    (ROOT / 'physics12-tutorial.html').write_text(page)
    (ROOT / 'content/physics12/tutorial-outline.md').write_text(md)
    (ROOT / 'content/physics12/chapters.json').write_text(json.dumps(CHAPTERS, ensure_ascii=False, indent=2) + '\n')
    print(f'Built physics12-tutorial.html: {len(CHAPTERS)} chapters, {count} equation explanations, 33 examples, 33 checks, 4 labs; {len(page.encode()):,} bytes.')


if __name__ == '__main__':
    main()
