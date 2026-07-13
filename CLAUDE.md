# Noah Foster — Personal Site

Portfolio website. Static site hosted on GitHub Pages.

## Stack
- HTML5, CSS3, vanilla JavaScript — no frameworks, no bundlers, no build steps
- GitHub Pages (noahfoster2174.github.io)
- GitHub Actions data pipelines (all commit only-if-changed, staggered crons, pull --rebase before push):
  - strava.yml (:00 every 6h) → strava.json (last 5 runs) + strava-history.json (full run history via scripts/strava_sync.py)
  - letterboxd.yml (:30 every 6h) → letterboxd.json
  - github.yml (:45 every 6h) → github.json (recent Noah-authored commits per repo via scripts/build_github_json.py; bot commits excluded)
- GitHub Actions health check: health.yml (Mon+Thu) fails loudly → GitHub emails Noah when pages aren't 200, JSON is invalid, or strava.json commit age > 7 days. Forced-failure test: dispatch with max_age_days=0.

## External Integrations
- Strava API (athlete 129221305)
- Letterboxd RSS (user: noahfoster) — account currently has 0 films logged; the feed section hides itself until films appear

## Pages
- index.html    — title card only: name + links, no copy at all (Noah's explicit call 2026-07-13; do not add self-description, stats, or features here)
- about.html    — bio, work experience, skills
- projects.html — project cards
- feed.html     — Strava runs + Letterboxd films (safe DOM rendering, no innerHTML)
- strava.json   — cached Strava data (auto-updated by GitHub Actions)

## Design System
- CSS variables (`:root` on each page, no shared stylesheet):
  - `--accent: #2D6A4F` — forest green accent (renamed from --red)
  - `--text: #1A1A1A` — charcoal body text
  - `--muted: #5E6E5E` — sage gray secondary text
  - `--border: #D5DCD5` — soft sage borders
  - `--bg: #F7F6F1` — warm cream background
  - `--surface: #EDECE7` — sage-tinted surfaces
  - `--dark: #1A2B22` — deep forest dark backgrounds
  - `--light-text: #A8B5A8` — muted sage text on dark backgrounds
- Palette: Forest + Cream — deep green accent on warm cream, sage-tinted grays
- Fonts: Spectral (serif, headings/accents) + system sans-serif (body)
- Transitions: 0.15s ease on all interactive text elements (nav, CTAs, links, pills, filters)
- Page transition: green curtain animation between internal pages (0.35–0.45s)
- Scroll animations: fade-in with IntersectionObserver

## Status
Live-data upgrade shipped 2026-07-12: weekly mileage graph + honest average on feed (from strava-history.json, client-built SVG), commit-activity signals on Currently Building (github.json), health-check monitoring, real OG image (assets/og.png), zero external runtime dependencies except Google Fonts and Letterboxd poster URLs. Homepage simplified 2026-07-13 to a plain intro — all live data now lives on the feed.

Timezone rule for Strava data: start_date_local carries a fake "Z" suffix (value is local time). Always bucket by the yyyy-mm-dd substring; never new Date(fullTimestamp).

Needs:
- Real profile photo: drop a square JPG (>=600px) named photo.jpg in the repo root — no code change needed (falls back to an inline SVG monogram until then)
- Reelz screenshot to replace the SVG motif in the homepage featured card (swap the svg for an img in .featured-visual)
- Films: Noah logs films on Letterboxd going forward; the feed section auto-fills from letterboxd.json (hidden while empty)

## Docs
Design history and planning iterations live in Noze: projects/personal-site/docs/

## GitHub
Repo: github.com/noahfoster2174/noahfoster2174.github.io (public)
