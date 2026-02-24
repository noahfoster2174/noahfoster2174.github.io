# noahfoster2174.github.io

Personal portfolio site. Live at **[noahfoster2174.github.io](https://noahfoster2174.github.io)**.

## Stack

- Vanilla HTML5, CSS3, JavaScript — no frameworks, no build tools
- Hosted on [GitHub Pages](https://pages.github.com/)
- Strava run data via GitHub Actions (fetches every 6 hours → `strava.json`)
- Letterboxd film log via RSS (client-side, parsed through rss2json)

## Pages

| File | Description |
|------|-------------|
| `index.html` | Homepage — hero, featured project, CTAs |
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
