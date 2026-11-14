# Modern academic website implementation plan

> Execute in this session; review the whole branch before handing off.

**Goal:** Deliver a complete modern, flat multi-page group website on an independent review branch with a working hosted preview.

**Architecture:** A dependency-free Python builder produces static HTML from maintained JSON data and shared templates. CSS and small progressive-enhancement JavaScript are shared by all pages. Existing public URLs remain valid.

**Tech Stack:** Python standard library; static HTML/CSS/JavaScript; GitHub Pages; separate private Sites preview.

**Spec:** ../specs/2026-11-14-modern-academic-design.md

## Global constraints
- No changes to main or the GitHub Pages deployment configuration.
- Preserve publications, authors, scientific markup, statuses, people, photos, and valid links.
- Shared navy/off-white/teal flat design across every page.
- No invented research claims, people, contacts or admissions requirements.

## Review focus
- Publication migration must not drop authors, chemical subscripts or equal-contributor notes.
- Submitted/in-preparation work must stay distinct from published/accepted work.
- Search, year and topic filters must combine, reset, and show a useful empty state.
- Narrow screens must not overflow, and mobile navigation must work with keyboard and no JS.
- Preview publication must never alter main; existing legacy anchors must resolve.

## Tasks
- [ ] 1. Extract original content into data/research.json, people.json, publications.json, software.json; verify migration against base.
- [ ] 2. Implement scripts/build.py and shared assets/site.css, assets/site.js. Generate homepage, research, people, publications, software, recruitment, utility pages.
- [ ] 3. Check all local links/assets, source preservation and browser workflows at desktop/mobile sizes; inspect screenshots against concept. Review full diff and fix findings.
- [ ] 4. Commit/push codex/modern-academic-preview, open draft PR, publish separate private preview, verify deployment and unchanged main.

## Execution notes
Fresh clone provides isolation; no second worktree needed. User already approved A and branch preview, so proceed without another approval gate. Verify reversible visual edits with browser inspection rather than layout-mirroring unit tests.
