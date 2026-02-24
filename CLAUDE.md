# Noah Foster — Personal Site

Portfolio website. Static site hosted on GitHub Pages.

## Stack
- HTML5, CSS3, vanilla JavaScript — no frameworks, no bundlers, no build steps
- GitHub Pages (noahfoster2174.github.io)
- GitHub Actions: Strava data pipeline (fetches runs every 6h → strava.json)

## External Integrations
- Strava API (athlete 129221305)
- Letterboxd RSS (user: noahfoster)

## Pages
- index.html    — minimal homepage (hero, featured project, two CTAs)
- about.html    — bio, work experience, skills
- projects.html — project cards
- feed.html     — Strava runs + Letterboxd films (safe DOM rendering, no innerHTML)
- strava.json   — cached Strava data (auto-updated by GitHub Actions)

## Design System
- CSS variables (`:root` on each page, no shared stylesheet):
  - `--red: #E22D32` — brand accent
  - `--text: #1a1a1a` — body text
  - `--muted: #666` — secondary text
  - `--border: #e5e5e5` — borders, dividers
  - `--bg: #f8f7f4` — warm cream background
  - `--surface: #f5f5f5` — card/hover surfaces
  - `--dark: #141414` — dark card backgrounds
  - `--light-text: #aaa` — text on dark backgrounds
- Fonts: Spectral (serif, headings/accents) + system sans-serif (body)
- Transitions: 0.15s ease on all interactive text elements (nav, CTAs, links, pills, filters)
- Page transition: red curtain animation between internal pages (0.35–0.45s)
- Scroll animations: fade-in with IntersectionObserver

## Status
Design polish complete. All four pages live with warm palette, micro-transitions, hover states, and contrast-passing text. Needs:
- Real photos (profile photo, project images)
- Content updates as projects evolve

Do not add new features or pages until existing content is finalized.

## Docs
Design history and planning iterations live in Noze: projects/personal-site/docs/

## GitHub
Repo: github.com/noahfoster2174/noahfoster2174.github.io (public)
