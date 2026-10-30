"""Offline-key regression checks; all writes occur in isolated temporary folders."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import generate_physics12_answers as generator
import save_physics12_session_answers as session
import build_physics12_practice as builder


class OfflineKeyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.inventory = self.root / 'inventory.json'
        self.output = self.root / 'content/physics12/prebuilt-answers.json'
        self.output.parent.mkdir(parents=True)
        self.question = dict(id='q1', chapter=1, number=1, text='Find 2 + 2.',
                             images=[], context=[], answers=[])
        self.inventory.write_text(json.dumps({'questions': [self.question]}))
        for target, name, value in [
            (session, 'INVENTORY', self.inventory), (session, 'OUTPUT', self.output),
            (generator, 'OUTPUT', self.output), (builder, 'ROOT', self.root),
            (builder, 'INVENTORY', self.inventory),
        ]:
            p = patch.object(target, name, value)
            p.start()
            self.addCleanup(p.stop)

    def test_saved_answer_has_current_source_and_ai_provenance(self):
        session.save_session(1, {'1': '4, since 2 + 2 = 4.'})
        answer = json.loads(self.output.read_text())['answers']['q1']
        self.assertTrue(generator.valid(answer, generator.fingerprint(self.question)))
        self.assertEqual(answer['provenance'], 'prebuilt-ai')
        self.assertEqual(answer['generationMethod'], 'in-session')
        with self.assertRaisesRegex(ValueError, 'current prebuilt'):
            session.save_session(1, {'1': 'Overwrite attempt'})
        self.assertEqual(json.loads(self.output.read_text())['answers']['q1'], answer)

    def test_invalid_batch_does_not_partially_save(self):
        second = dict(self.question, id='q2', number=2)
        self.inventory.write_text(json.dumps({'questions': [self.question, second]}))
        self.output.write_text(json.dumps({'answers': {}}))
        before = self.output.read_bytes()
        with self.assertRaisesRegex(ValueError, 'Invalid answer'):
            session.save_session(1, {'1': '4', '2': ''})
        self.assertEqual(self.output.read_bytes(), before)

    def test_textbook_answer_cannot_be_replaced(self):
        self.question['answers'] = [{'src': 'textbook.png'}]
        self.inventory.write_text(json.dumps({'questions': [self.question]}))
        with self.assertRaisesRegex(ValueError, 'textbook answer'):
            session.save_session(1, {'1': '4'})
        self.assertFalse(self.output.exists())

    def test_default_build_keeps_page_if_key_missing_or_stale(self):
        page = self.root / 'physics12-practice.html'
        page.write_text('existing working page')
        for saved in [{}, {'q1': {'answer': '4', 'sourceHash': 'stale'}}]:
            self.output.write_text(json.dumps({'answers': saved}))
            with self.assertRaisesRegex(ValueError, 'need prebuilt answers'):
                builder.build()
            self.assertEqual(page.read_text(), 'existing working page')


if __name__ == '__main__':
    unittest.main()
