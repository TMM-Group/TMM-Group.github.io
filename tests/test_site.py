import json
import re
import subprocess
import unittest
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.refs = []
        self.ids = set()
        self.h1 = 0
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag == 'h1': self.h1 += 1
        for key in ('src', 'href'):
            if attrs.get(key): self.refs.append(attrs[key])

def plain(text):
    return re.sub(r'\s+', '', unescape(re.sub('<[^>]+>', '', text)))

class SiteTests(unittest.TestCase):
    def test_all_original_publication_content_preserved(self):
        path = ROOT / 'data/publications.json'
        self.assertTrue(path.exists(), 'Structured publications have not been migrated')
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(len(data['published']), 50)
        self.assertEqual(len(data['manuscripts']), 5)
        original = subprocess.check_output(['git', 'show', '73018c4d656ce8e71ec7f06ddd2a17b718a0853d:papers/index.html'], cwd=ROOT).decode()
        originals = re.findall(r'<p><strong>\[\d+\]</strong>(.*?)</p>', original, re.S)
        for src, item in zip(originals, data['published']):
            reconstructed = item['authors'] + item['title'] + item['citation'] + item['notes']
            # Only separating punctuation/layout may change.
            normalize = lambda t: re.sub(r'[.,;]', '', plain(t))
            self.assertEqual(normalize(src), normalize(reconstructed), item['id'])
    def test_pages_local_links_and_assets(self):
        files = [ROOT / p for p in ['index.html','research/index.html','team/index.html','papers/index.html','codes/index.html','join-us/index.html','404.html','categories/index.html','tags/index.html','page/1/index.html']]
        for file in files:
            self.assertTrue(file.exists(), str(file))
            parsed = Page(file.read_text(encoding='utf-8'))
            self.assertEqual(parsed.h1, 1, str(file))
            for ref in parsed.refs:
                url = urlsplit(ref)
                if url.scheme or url.netloc: continue
                target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else file.parent / unquote(url.path)
                if not url.path: target = file
                if target.is_dir(): target /= 'index.html'
                self.assertTrue(target.exists(), f'{file}: missing {ref}')
                if url.fragment and target.suffix == '.html':
                    self.assertIn(unquote(url.fragment), Page(target.read_text(encoding='utf-8')).ids, f'{file}: {ref}')
    def test_deployment_metadata_and_legacy_anchors(self):
        for name in ['index.html','team/index.html','papers/index.html','codes/index.html','join-us/index.html']:
            html = (ROOT / name).read_text(encoding='utf-8')
            self.assertNotIn('localhost:1313', html)
            self.assertNotIn('livereload', html)
            self.assertIn('TMM Group', html)
        for anchor in ['research-areas','1-photovoltaics','2-ferroelectrics-and-piezoelectrics','3-machine-learning']:
            self.assertIn(anchor, Page((ROOT/'index.html').read_text(encoding='utf-8')).ids)
        for anchor in ['1. mlrap','2. DieDatabase','3. NepTrainKit']:
            self.assertIn(anchor, Page((ROOT/'codes/index.html').read_text(encoding='utf-8')).ids)

if __name__ == '__main__': unittest.main()
