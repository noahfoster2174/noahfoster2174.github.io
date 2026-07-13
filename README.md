# noahfoster2174.github.io

Personal portfolio site. Live at **[noahfoster2174.github.io](https://noahfoster2174.github.io)**.

## Stack

- Vanilla HTML5, CSS3, JavaScript — no frameworks, no build tools
- Hosted on [GitHub Pages](https://pages.github.com/)
- Strava run data via GitHub Actions (every 6h → `strava.json` last-5-runs + `strava-history.json` full history feeding the weekly mileage graph)
- Letterboxd film log via GitHub Actions (every 6h → `letterboxd.json`; the feed section hides itself while the log is empty)
- GitHub commit activity via GitHub Actions (every 6h → `github.json`, Noah-authored commits only)
- Health check via GitHub Actions (Mon+Thu): fails loudly — and GitHub emails the owner — if pages aren't 200, any JSON is invalid, or `strava.json` hasn't been committed in 7 days. Test it: dispatch with `max_age_days: 0`.

## Pages

| File | Description |
|------|-------------|
| `index.html` | Homepage — a title card: name and links, nothing else |
| `about.html` | Bio, work experience, skills |
| `projects.html` | Project cards |
| `feed.html` | Live Strava runs + Letterboxd film log |

## Local development

No build step needed. Open any `.html` file directly in a browser, or serve locally to avoid CORS issues with `strava.json`:

```bash
python -m http.server 8000
# → http://localhost:8000
```

## Strava integration

Recent runs are cached in `strava.json` by a GitHub Actions workflow at `.github/workflows/strava.yml`. The workflow refreshes the Strava access token using stored secrets, fetches the last 5 runs, and commits the result if changed.

## Letterboxd integration

Recent films are cached in `letterboxd.json` by `.github/workflows/letterboxd.yml`, which parses the public RSS feed (no secrets needed) and commits the result if changed. `feed.html` reads the local JSON and hides the Recently Watched section when the list is empty.

## GitHub activity integration

`.github/workflows/github.yml` runs `scripts/build_github_json.py` (built-in `GITHUB_TOKEN`, no extra secrets) to cache recent Noah-authored commits per repo in `github.json`. Bot commits from the data pipelines are excluded, so the "Currently Building" signals on the feed reflect real work. Scheduled crons are staggered (`:00` Strava, `:30` Letterboxd, `:45` GitHub) and every workflow rebases before pushing to avoid races.

## Profile photo

Drop a square JPG (≥600px) named `photo.jpg` in the repo root and the About page picks it up automatically; until then it falls back to an inline SVG monogram (no external services).

## Timezone note

Strava's `start_date_local` values end in a fake `Z` — they are local times, not UTC. All client code buckets runs by the `yyyy-mm-dd` substring, and `strava-history.json` stores timestamps with the `Z` stripped. Don't parse full timestamps with `new Date()`.

**Required GitHub secrets** (Settings → Secrets → Actions):

| Secret | Description |
|--------|-------------|
| `STRAVA_CLIENT_ID` | From strava.com/settings/api |
| `STRAVA_CLIENT_SECRET` | From strava.com/settings/api |
| `STRAVA_REFRESH_TOKEN` | Generated via OAuth exchange |

## Design system

| Token | Value | Usage |
|-------|-------|-------|
| `--accent` | `#2D6A4F` | Forest green accent, borders, highlights |
| `--text` | `#1A1A1A` | Charcoal body text |
| `--muted` | `#5E6E5E` | Sage gray secondary text |
| `--border` | `#D5DCD5` | Soft sage dividers, card borders |
| `--bg` | `#F7F6F1` | Warm cream background |
| `--surface` | `#EDECE7` | Sage-tinted surfaces |
| `--dark` | `#1A2B22` | Deep forest dark backgrounds |
| `--light-text` | `#A8B5A8` | Muted sage text on dark backgrounds |

Palette: Forest + Cream — deep green accent on warm cream, sage-tinted grays

Fonts: [Spectral](https://fonts.google.com/specimen/Spectral) (serif, headings) + system sans-serif (body)
