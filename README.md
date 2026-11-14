# TMM Group website

Modern academic preview on `codex/modern-academic-preview`. Do not merge into `main` until the group owner approves the preview.

## Edit and build

Content lives in `data/`: publications, research themes, people, and software. HTML strings preserve scientific subscripts, italics and author notes. Shared page templates are in `scripts/build.py`, shared styles and interactions in `assets/`.

```sh
python scripts/build.py
python -m unittest discover -s tests -v
python -m http.server 4173 --bind 127.0.0.1
```

Python 3.10+ is sufficient; no third-party build dependency. Generated HTML is committed so GitHub Pages can continue serving the root directly. Commit data/template changes together with rebuilt pages.

## Preview and hosting

The preview uses a separate private Site; its hosting metadata and credentials are intentionally outside this repository. The normal GitHub Pages source and `main` remain unchanged. All content is rendered in HTML; navigation and publication reading work without JavaScript. JavaScript adds mobile menu controls and publication search/year/topic filtering.

## Content and imagery

Existing publication citations, member biographies, photographs, research figures and tool links are preserved. Research topic labels are editorial navigation aids. The navy hero lattice is an AI-generated decorative illustration and is not a model of a specific compound. The hero's `alt` is empty so it is not presented as scientific evidence.

Contact email is verified against [Gang Tang's official BIT profile](https://sis.bit.edu.cn/szdw/jsml/jsmljxxb/1lx/71d081cfa1474f3e88e61c4467d92de5.htm). Original accepted paper 50 has no publication URL; it is intentionally rendered without a dead link. Manuscripts retain their source statuses. Legacy URLs and homepage research anchors are preserved. Production analytics only loads on `tmm-group.github.io`, not on preview hosts.
