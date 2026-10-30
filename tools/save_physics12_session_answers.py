#!/usr/bin/env python3
"""Validate and save in-session AI solutions; never replace textbook answers.

Usage: python3 tools/save_physics12_session_answers.py CHAPTER answers.json
The input maps problem numbers to solution objects or concise answer strings.
"""
import argparse
from datetime import datetime, timezone
import json
from generate_physics12_answers import INVENTORY, OUTPUT, fingerprint, valid, save


def save_session(chapter, entries):
    inventory=json.loads(INVENTORY.read_text())
    questions={q['number']:q for q in inventory['questions'] if q['chapter']==chapter}
    data=json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {'version':1,'source':'Physics12.pdf','answers':{}}
    prepared={}
    for number, value in entries.items():
        q=questions[int(number)]
        if q['answers']:
            raise ValueError(f'{q["id"]} already has a textbook answer')
        source_hash=fingerprint(q)
        if valid(data['answers'].get(q['id']),source_hash):
            raise ValueError(f'{q["id"]} already has a current prebuilt answer')
        entry={'answer':value} if isinstance(value,str) else dict(value)
        entry.update(id=q['id'],sourceHash=source_hash,provenance='prebuilt-ai',
                     generationMethod='in-session',generatedAt=datetime.now(timezone.utc).isoformat())
        for key,default in [('steps',[]),('check',''),('assumptions',[]),('needsReview',False)]:
            entry.setdefault(key,default)
        if not valid(entry,source_hash):
            raise ValueError(f'Invalid answer for {q["id"]}')
        prepared[q['id']]=entry
    data['answers'].update(prepared)
    save(data)
    print(f'Saved {len(prepared)} in-session AI answers for chapter {chapter}; {len(data["answers"])} total prebuilt.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('chapter',type=int)
    parser.add_argument('file',type=argparse.FileType('r'))
    args=parser.parse_args()
    save_session(args.chapter,json.load(args.file))
