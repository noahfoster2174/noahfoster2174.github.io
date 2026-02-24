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
Design polish complete. All four pages live with warm palette, micro-transitions, hover states, and contrast-passing text. Needs:
- Real photos (profile photo, project images)
- Content updates as projects evolve

Do not add new features or pages until existing content is finalized.

## Docs
Design history and planning iterations live in Noze: projects/personal-site/docs/

## GitHub
Repo: github.com/noahfoster2174/noahfoster2174.github.io (public)
