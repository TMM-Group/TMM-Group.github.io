"""Build the GitHub Pages site. Run: python scripts/build.py (no dependencies)."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://tmm-group.github.io'
SCHOLAR = 'https://scholar.google.com/citations?user=qaQa3T4AAAAJ&hl=zh-CN'
PROFILE = 'https://sis.bit.edu.cn/szdw/jsml/jsmljxxb/1lx/71d081cfa1474f3e88e61c4467d92de5.htm'
ARROW = '<svg class="arrow" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" stroke="currentColor" stroke-width="1.6"/></svg>'
def data(name): return json.loads((ROOT / 'data' / f'{name}.json').read_text(encoding='utf-8'))
def e(value): return escape(str(value), quote=True)
def text(html): return re.sub('<[^>]+>', '', html)
research, people, publications, software = [data(n) for n in ['research','people','publications','software']]

def link(url,label,cls='text-link'):
    return f'<a class="{cls}" href="{e(url)}"><span>{label}</span>{ARROW}</a>'

def img(src,alt,cls='',eager=False):
    return f'<img src="/{e(src)}" alt="{e(alt)}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def navigation(current):
    items=[('research','Research','/research/'),('team','People','/team/'),('papers','Publications','/papers/'),('codes','Software','/codes/'),('join-us','Join Us','/join-us/')]
    links=''.join(f'<a href="{url}" {"aria-current=page" if key==current else ""} class="{"nav-join" if key=="join-us" else ""}">{label}</a>' for key,label,url in items)
    return f'''<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="container nav-shell"><a class="brand" href="/" aria-label="TMM Group home">TMM<span class="brand-dot">.</span> <span class="brand-light">GROUP</span></a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation" hidden>Menu <span aria-hidden="true">☰</span></button><nav id="navigation" class="main-nav" aria-label="Main navigation">{links}</nav></div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="container footer-grid"><div><a class="brand" href="/">TMM<span class="brand-dot">.</span> GROUP</a><p>Tang Materials Modeling Group<br>Beijing Institute of Technology</p></div><div><p class="footer-label">Find us</p><p>School of Interdisciplinary Science<br>Beijing, China</p><a href="mailto:gtang@bit.edu.cn">gtang@bit.edu.cn</a></div><div><p class="footer-label">Connect</p>{link('https://github.com/TMM-Group','GitHub')}{link(SCHOLAR,'Google Scholar')}{link(PROFILE,'University profile')}</div></div><div class="container footer-bottom"><span>© 2026 Tang Materials Modeling Group</span><a href="#top">Back to top ↑</a></div></footer>'''

def page(path,title,description,body,current='',noindex=False):
    url=ORIGIN + ('/' if path=='index.html' else '/'+path.replace('index.html',''))
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{e(title)} | TMM Group</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{url}"><meta property="og:title" content="{e(title)} | TMM Group"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN}/assets/lattice.png"><meta name="theme-color" content="#10243A">{'<meta name="robots" content="noindex">' if noindex else ''}<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head>
<body id="top">{navigation(current)}<main id="main">{body}</main>{footer()}</body></html>'''
    target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(html+'\n',encoding='utf-8')

def heading(title,description,extra=''):
    return f'<section class="page-intro"><div class="container"><h1>{title}</h1><p class="intro-copy">{description}</p>{extra}</div></section>'

def section_heading(title,subtitle='',url='',label='Explore'):
    return f'<div class="section-heading"><div><h2>{title}</h2>{f"<p>{subtitle}</p>" if subtitle else ""}</div>{link(url,label) if url else ""}</div>'

def invitation():
    return f'<section class="invitation"><div class="container invitation-inner"><div><h2>Discover what comes next.</h2><p>Explore new materials. Develop new ideas. Join our group.</p></div>{link("/join-us/","Join our group","button button-light")}</div></section>'

def research_tile(r,index):
    return f'<article class="research-tile" id="{r["id"]}"><a class="figure-link" href="/research/#{r["id"]}" aria-label="Explore {e(r["title"])}">{img(r["image"],r["title"]+" research figure")}</a><span class="section-number">0{index+1}</span><h3>{link("/research/#"+r["id"],r["title"],"heading-link")}</h3><p>{r["summary"]}</p></article>'

def home():
    hero=f'''<section class="hero"><div class="container hero-grid"><div class="hero-copy"><h1>Tang Materials<br>Modeling Group</h1><p class="hero-description">Understanding and designing functional materials through computation and machine learning.</p><p class="hero-affiliation">Beijing Institute of Technology</p><div class="button-row">{link('/research/','Explore Research','button')}{link('/team/','Meet the Team','button button-outline')}</div></div><div class="hero-art">{img('assets/lattice.png','',eager=True)}</div></div></section>'''
    research_html=f'<section class="section" id="research-areas"><div class="container">{section_heading("Research","From atomic interactions to material functionality.","/research/","Our research") }<div class="research-grid">'+''.join(research_tile(r,i) for i,r in enumerate(research))+'</div></div></section>'
    selected=[]
    for number,image in [(25,'photovoltaics.jpg'),(36,'ferroelectrics-piezoelectrics.jpg'),(38,'codes/neptrainkit.png')]:
        p=next(p for p in publications['published'] if p['id']==number)
        selected.append(f'<article class="selected-paper">{img(image,"", "paper-thumbnail")}<div><p class="paper-meta">{p["citation"]}</p><h3>{link(p["link"],p["title"],"heading-link")}</h3></div>{link(p["link"],"Read paper","paper-read text-link")}</article>')
    pubs=f'<section class="section section-tint"><div class="container">{section_heading("Selected publications","A closer look at our work.","/papers/","All publications")}<div class="selected-list">'+''.join(selected)+'</div></div></section>'
    tools=f'<section class="section"><div class="container">{section_heading("Software &amp; data","Open tools for materials research.","/codes/","Explore our tools")}<div class="software-grid">'+''.join(f'<article><span class="section-number">0{i+1}</span><h3>{s["name"]}</h3><p>{s["summary"]}</p>{link("/codes/#"+s["id"],"Explore "+s["name"])}</article>' for i,s in enumerate(software))+'</div></div></section>'
    members=[dict(image='team/tg.jpg',name='Gang Tang')]+[p for g in people['groups'][:2] for p in g['people']][:5]
    team=f'<section class="section section-tint"><div class="container">{section_heading("Our people","A shared curiosity about the physics of materials.","/team/","Meet the team")}<div class="people-strip">'+''.join(f'<a href="/team/">{img(p["image"],p["name"])}<span>{p["name"]}</span></a>' for p in members)+'</div></div></section>'
    page('index.html','Tang Materials Modeling Group','Computational materials physics, machine learning and open-source tools at Beijing Institute of Technology.',hero+research_html+pubs+tools+team+invitation())

def research_page():
    sections=[]
    for i,r in enumerate(research):
        paragraphs=''.join(f'<p>{p}</p>' for p in r['paragraphs'])
        refs=''.join(f'<li>{link(a["link"],a["title"])}</li>' for a in r['references'])
        sections.append(f'<section class="research-detail" id="{r["id"]}"><div class="research-overview"><span class="section-number">0{i+1}</span><h2>{r["title"]}</h2><p class="lead">{r["summary"]}</p><figure>{img(r["image"],r["title"]+" research figure")}<figcaption>Research from the TMM Group</figcaption></figure></div><div class="research-body">{paragraphs}<h3>Related publications</h3><ul class="reference-list">{refs}</ul></div></section>')
    jump='<nav class="jump-links" aria-label="Research topics">'+''.join(f'<a href="#{r["id"]}">{r["title"]}</a>' for r in research)+'</nav>'
    body=heading('Research','We combine first-principles calculations, data-driven approaches and machine learning to understand and discover functional materials.',jump)+'<div class="container">'+''.join(sections)+'</div>'+invitation()
    page('research/index.html','Research','Photovoltaics, ferroics, dielectric materials and machine learning research in the TMM Group.',body,'research')

def team_page():
    pi=f'''<section class="pi-section" id="dr-gang-tang"><div class="pi-photo">{img('team/tg.jpg','Dr. Gang Tang',eager=True)}</div><div class="pi-copy"><p class="section-number">Principal investigator</p><h2>Gang Tang</h2><p class="lead">Associate Professor<br>Beijing Institute of Technology</p><p>Gang Tang is an Associate Professor at the School of Interdisciplinary Science, Beijing Institute of Technology. His research focuses on using materials simulation, machine learning, and data science to design new materials for tackling critical challenges, including photovoltaics, ferroelectrics, piezoelectrics, and thermoelectrics.</p><p>Gang Tang received his PhD from Beijing Institute of Technology in 2019. After completing a postdoctoral position in the Department of Physics at the University of Liège, Belgium, under the supervision of Prof. Philippe Ghosez, he was appointed as an Associate Professor at the School of Interdisciplinary Science, Beijing Institute of Technology, in December 2021.</p><div class="inline-links">{link(SCHOLAR,'Scholar')}{link('https://github.com/obaica','GitHub')}{link('https://x.com/GangTang7','X / Twitter')}{link('mailto:gtang@bit.edu.cn','Email')}</div></div></section>'''
    groups=[]
    for g in people['groups']:
        cards=''.join(f'<article class="person" id="{p["id"]}">{img(p["image"],p["name"])}<h3>{p["name"]}</h3><p>{p["description"]}</p></article>' for p in g['people'])
        groups.append(f'<section class="people-section" id="{g["id"]}">{section_heading(g["title"])}<div class="people-grid {"alumni-grid" if g["id"]=="Alumni" else ""}">{cards}</div></section>')
    jump='<nav class="jump-links" aria-label="People groups">'+''.join(f'<a href="#{g["id"]}">{g["title"]}</a>' for g in people['groups'])+'</nav>'
    page('team/index.html','People','Meet Gang Tang and the students and alumni of the Tang Materials Modeling Group.',heading('Our people','The researchers behind our science.',jump)+'<div class="container">'+pi+''.join(groups)+'</div>'+invitation(),'team')

def paper_row(p):
    searchable=text(p['title']+' '+p['authors']+' '+p['citation'])
    title=link(p['link'],p['title'],'heading-link') if p['link'] else p['title']
    notes=f'<span class="paper-notes">{p["notes"]}</span>' if p['notes'] else ''
    status='<span class="status">Accepted</span>' if p['status']=='accepted' else ''
    return f'<article class="publication" id="paper-{p["id"]}" data-publication data-year="{p["year"]}" data-topics="{e("|".join(p["topics"]))}" data-search="{e(searchable)}"><span class="pub-number">{p["id"]:02}</span><div><h3>{title}</h3><p class="authors">{p["authors"]}</p><p class="citation">{p["citation"]} {status}</p>{notes}<p class="topic-text">{" · ".join(p["topics"])}</p></div></article>'

def papers_page():
    published=publications['published'];years=list(dict.fromkeys(p['year'] for p in published));topics=sorted(set(t for p in published for t in p['topics']))
    yearopts=''.join(f'<option value="{y}">{y}</option>' for y in years)
    topicopts=''.join(f'<option>{e(t)}</option>' for t in topics)
    filters=f'''<form class="publication-filters" id="publication-filters" hidden role="search"><label class="search-field">Search publications<input id="paper-search" type="search" placeholder="Title, author or keyword…" autocomplete="off"></label><label>Year<select id="paper-year"><option value="all">All years</option>{yearopts}</select></label><label>Research topic<select id="paper-topic"><option value="all">All topics</option>{topicopts}</select></label><button type="reset" class="reset-button">Reset</button></form><div class="results-bar"><p id="result-count" role="status" aria-live="polite">{len(published)} publications &amp; accepted papers</p><a href="#Submitted">Manuscripts in progress ↓</a></div>'''
    nav='<aside class="year-nav"><span class="section-number">Browse by year</span><nav aria-label="Publication years">'+''.join(f'<a href="#{y}">{y}</a>' for y in years)+'</nav></aside>'
    groups=''.join(f'<section class="publication-year" id="{y}" data-year-group><h2>{y}</h2>'+''.join(paper_row(p) for p in published if p['year']==y)+'</section>' for y in years)
    empty='<div class="empty-state" id="empty-results" hidden><h2>No matching publications</h2><p>Try a different keyword, year or research topic.</p><button class="button" id="clear-filters" type="button">Clear filters</button></div>'
    manuscripts=''.join(f'<li><span class="status">{m["status"].capitalize()}</span><p>{m["html"]}</p></li>' for m in publications['manuscripts'])
    body=heading('Publications','Research in materials physics, from fundamental understanding to computational discovery.',link(SCHOLAR,'View Google Scholar'))+f'<div class="container publications-container">{filters}<div class="publication-layout">{nav}<div>{groups}{empty}<section id="Submitted" class="manuscripts"><h2>Manuscripts in progress</h2><p class="muted">Submitted and in-preparation work, listed separately from published and accepted papers.</p><ul>{manuscripts}</ul></section></div></div></div>'
    page('papers/index.html','Publications','Browse and search TMM Group publications by year, author and research topic.',body,'papers')

def software_page():
    sections=[]
    for i,s in enumerate(software):
        actions=''.join(link(a['url'],'Explore database' if a['label']=='Link' else a['label'],'button' if j==0 else 'text-link') for j,a in enumerate(s['links']))
        sections.append(f'<section class="software-detail" id="{s["id"]}"><span class="legacy-anchor" id="{i+1}. {s["id"]}" aria-hidden="true"></span><div class="software-visual">{img(s["image"],s["name"]+" interface and workflow")}</div><div><span class="section-number">0{i+1} / {"Database" if i==1 else "Open-source software"}</span><h2>{s["name"]}</h2><p class="lead">{s["summary"]}</p><p>{s["description"]}</p><div class="button-row">{actions}</div></div></section>')
    body=heading('Software &amp; data','Tools we develop and contribute to, helping researchers manage, analyse and interpret materials simulations.',link('https://github.com/TMM-Group','TMM Group on GitHub'))+'<div class="container">'+''.join(sections)+'</div>'+invitation()
    page('codes/index.html','Software & Data','Explore MLRAP, DieDatabase and NepTrainKit: open resources for materials research.',body,'codes')

def join_page():
    body=heading('Join our group','Bring your curiosity. Help us understand what materials can do.')+f'''<section class="section"><div class="container join-layout"><div><h2>Study with us</h2><p class="lead">We offer 1–2 master’s positions each year in condensed matter physics.</p><p>Our work brings together first-principles calculations, computational materials physics and machine learning. Explore our research and recent publications to learn more about the questions we investigate.</p><div class="inline-links">{link('/research/','Our research')}{link('/papers/','Recent publications')}</div><div class="join-chinese" lang="zh-CN"><h3>欢迎加入我们</h3><p>课题组每年招收 1–2 名凝聚态物理方向硕士研究生。欢迎对计算材料物理与机器学习感兴趣的同学联系唐刚老师，了解研究方向和招生详情。</p></div></div><aside class="contact-panel"><span class="section-number">Get in touch</span><h2>Gang Tang</h2><p>Associate Professor<br>Beijing Institute of Technology</p><a class="contact-email" href="mailto:gtang@bit.edu.cn">gtang@bit.edu.cn</a><p>Please get in touch by email for details about current opportunities.</p>{link('mailto:gtang@bit.edu.cn','Write an email','button')}{link(PROFILE,'University profile')}</aside></div></section><section class="section section-tint"><div class="container join-bottom"><h2>Get to know TMM.</h2><p>Meet the people and explore the open tools behind our research.</p><div class="inline-links">{link('/team/','Meet the team')}{link('/codes/','Software & data')}</div></div></section>'''
    page('join-us/index.html','Join Us','Master’s opportunities in condensed matter physics and computational materials research at TMM Group, Beijing Institute of Technology.',body,'join-us')

def utilities():
    body=heading('Find your way','Explore the research, people and publications of the TMM Group.')+'<section class="section"><div class="container utility-links">'+''.join(link(url,label) for url,label in [('/','Home'),('/research/','Research'),('/team/','People'),('/papers/','Publications'),('/codes/','Software & data'),('/join-us/','Join us')])+'</div></section>'
    for p in ['categories/index.html','tags/index.html','page/1/index.html']: page(p,'Explore TMM', 'Explore the TMM Group website.',body,noindex=True)
    page('404.html','Page not found','Find the TMM Group page you need.',heading('Page not found','This address may have changed. Let’s get you back to the science.')+f'<section class="section"><div class="container">{link("/","Back to homepage","button")}</div></section>',noindex=True)
    paths=['','research/','team/','papers/','codes/','join-us/']
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}/{p}</loc></url>' for p in paths)+'</urlset>\n',encoding='utf-8')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n',encoding='utf-8')

if __name__=='__main__':
    home(); research_page(); team_page(); papers_page(); software_page(); join_page(); utilities()
    print('Built 6 main pages, 3 legacy pages, 404, sitemap and robots.txt.')
