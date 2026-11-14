# TMM Group website

Modern academic website for the Tang Materials Modeling Group. The group owner approved publication on 2026-11-15 after reviewing the redesign.

## Edit and build

Content lives in `data/`: publications, research themes, people, and software. HTML strings preserve scientific subscripts, italics and author notes. Shared page templates are in `scripts/build.py`, shared styles and interactions in `assets/`.

```sh
python scripts/build.py
python -m unittest discover -s tests -v
python -m http.server 4173 --bind 127.0.0.1
```

Python 3.10+ is sufficient; no third-party build dependency. Generated HTML is committed so GitHub Pages can continue serving the root directly. Commit data/template changes together with rebuilt pages.

## Preview and hosting

GitHub Pages publishes the committed static output from the root of `main` at https://tmm-group.github.io/. The earlier preview uses a separate private Site; its hosting metadata and credentials are outside this repository. All content is rendered in HTML; navigation and publication reading work without JavaScript. JavaScript adds mobile menu controls and publication search/year/topic filtering.

The previous production version is preserved in [`codex/backup-main-before-redesign-2026-11-15`](https://github.com/TMM-Group/TMM-Group.github.io/tree/codex/backup-main-before-redesign-2026-11-15), at commit `73018c4d656ce8e71ec7f06ddd2a17b718a0853d`. Keep this branch for restoration and comparison.

## Content and imagery

Existing publication citations, member biographies, original photographs, research figures and tool links are preserved. White-background versions of Gang Tang, Tao Hu and Yutong Li's portraits are stored as `team/*-white.png`; these were edited with the built-in image tool at the owner's request. The edit prompt requested only a pure white background while retaining the person's features, expression, clothing, pose and framing. The original files remain available. Dong An's scanned photo border is clipped only for display. PhD, master's and alumni portraits use the same grid and dimensions.

Research topic data supports filtering; topic labels are not shown below individual papers. The navy hero lattice is an AI-generated decorative illustration and is not a model of a specific compound. The hero's `alt` is empty so it is not presented as scientific evidence.

Contact email is verified against [Gang Tang's official BIT profile](https://sis.bit.edu.cn/szdw/jsml/jsmljxxb/1lx/71d081cfa1474f3e88e61c4467d92de5.htm). Original accepted paper 50 has no publication URL; it is intentionally rendered without a dead link. Manuscripts retain their source statuses. Legacy URLs and homepage research anchors are preserved. Production analytics only loads on `tmm-group.github.io`, not on preview hosts.
