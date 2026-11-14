# Preview verification

Verified 2026-11-15 using the built-in browser against the local static output.

## Content and behavior
- 50 published/accepted records preserve original authors, titles, chemical markup, citation text and contribution notes; 5 manuscript records retain their original status.
- All local page/asset links resolve; old research, people, year and software fragments are retained.
- Combined keyword `neptrain`, year 2025 and machine-learning topic returns paper 38; year 2026 returns the empty state.
- Native Reset and Clear filters each restore 50 rows. Search `Zn3WN4` finds paper 36. Chemical subscripts and italic title words now remain inline.
- Mobile menu opens, navigates and closes. All 6 main routes checked at 1440, 390 and 320 pixels without horizontal overflow. Homepage additionally checked at 1024 pixels.
- A script-free copy of the publications page shows the navigation and all 50 records on mobile; unavailable filters stay hidden.

## Design comparison
Reference: generated concept exec-5316805c-861b-474d-9862-023401e78699.png in the conversation's generated_images folder. The user approved the written A direction; the generated concept is supporting visual guidance.

Inspected reference and browser screenshots with image viewing: navy/teal/off-white palette, large sans-serif type, split hero, flat research columns, horizontal publication rows, separated software columns, real photo grid, invitation and footer. Images and layout were checked on inner pages as well as homepage. 1024px matches the concept's native width; 1440px is the main desktop QA size.

Intentional differences: authentic research figures, portraits and publication copy replace concept placeholders; verified email replaces the concept's invented address; no fake resource links. Real content needs more vertical room than the abbreviated concept. System sans-serif avoids external font availability problems. The hero is decorative lattice imagery, not a scientific model.

Repaired: desktop mobile-menu button visibility; hero background seam with an edge mask; chemical markup separated by flex formatting; native-reset event timing; original software anchor aliases. No unresolved material layout issues observed. Above-the-fold copy follows the agreed group name, affiliation, research description and actions; no extra promotional claims.

## Review
Independent read-only review found the chemical-inline issue, legacy software IDs and native reset timing; all were fixed and rechecked. Initial publication count is derived from data. Native content/link tests pass (3/3), JS syntax check passes. External publication URLs were preserved, not exhaustively retested against publishers.

## Boundaries
The hosted review copy is a separate private Site. Third-party software and the separate DieDatabase application are linked, not modified. The initial review left main unchanged; the owner subsequently approved production publication on 2026-11-15.

## Approved revisions and launch checks

- Removed the large intro banners from the five inner pages, enlarged and unified navigation links, and removed the Join Us outline.
- Removed all per-paper topic captions while retaining publication filtering.
- Top-aligned portraits preserve complete heads. PhD, master's and alumni images now share a four-column desktop grid: 279 × 348.75 px at a 1440 px viewport. At 390 px, all three groups use 157.5 px-wide images in two columns. Gang Tang's profile remains larger.
- Inspected the three white-background portrait edits on the rendered site. Original image assets remain in the repository. Dong An's outer scanned border is hidden with a 1% display crop.
- Rebuilt all pages; 3/3 content, local link and legacy-anchor tests passed, as did JavaScript syntax and whitespace checks. Latest desktop and mobile checks found no horizontal overflow or console errors.
- Before publication, backed up the previous main commit `73018c4d656ce8e71ec7f06ddd2a17b718a0853d` to `codex/backup-main-before-redesign-2026-11-15`.
