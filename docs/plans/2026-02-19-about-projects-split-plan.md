# About + Projects Split Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Split about.html into two pages — a lean resume-adjacent about.html and a new projects.html — then update nav links across the whole site.

**Architecture:** Three self-contained HTML files (no framework, no build step). Each page shares the same header/footer/curtain pattern. Nav updated on all four pages (index, about, feed, projects). No shared CSS file — each page is standalone.

**Tech Stack:** Vanilla HTML/CSS/JS, GitHub Pages static hosting, same design system (Spectral font, `--red: #E22D32`, 1000px container).

---

## Context

### Current state
- `about.html` — bio section + building section + skills strip + cards grid (projects). All on one page.
- `index.html` — homepage with hero, featured card, CTA links. Nav Projects link → `about.html#projects`.
- `feed.html` — running + watching feed. Nav Projects link → `about.html#projects`.
- No `projects.html` exists yet.

### Target state
- `projects.html` — standalone page with just the 5 project cards + 1 placeholder.
- `about.html` — resume-adjacent: bio (photo + 1 paragraph), experience timeline (Amazon + Capital One), skills by category (Finance / Data & Analytics / Technology), CTA → projects.html.
- Nav on all four pages: About → `about.html`, Projects → `projects.html`, Feed → `feed.html`, LinkedIn → external.

### Design system (do not change)
- Colors: `--red: #E22D32`, `--text: #1a1a1a`, `--muted: #555`, `--border: #e5e5e5`
- Typography: `Spectral` serif for headings/display, system sans-serif for body
- Container: `max-width: 1000px; padding: 0 2rem;`
- Section separator: `border-bottom: 1px solid var(--border)`
- Section label: `.section-label` — 0.75rem, uppercase, red, 0.12em tracking
- Footer border-top: 3px solid var(--red)
- Curtain: fixed red overlay, curtainEnter (sweeps up) / curtainExit (sweeps down) keyframes

---

## Task 1: Create projects.html

**File:**
- Create: `~/Sites/noahfoster2174.github.io/projects.html`

**Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Projects — Noah Foster</title>
  <meta name="description" content="Projects by Noah Foster — web apps, automation tools, and financial modeling systems." />
  <meta property="og:title" content="Projects — Noah Foster" />
  <meta property="og:description" content="Web apps, automation tools, and financial modeling systems." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://noahfoster2174.github.io/projects.html" />
  <meta property="og:image" content="https://placehold.co/1200x630/E22D32/ffffff?text=Noah+Foster" />
  <meta property="og:site_name" content="Noah Foster" />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='4' fill='%23E22D32'/><text x='50%25' y='50%25' dominant-baseline='central' text-anchor='middle' font-family='Georgia,serif' font-weight='700' font-size='14' fill='white'>NF</text></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Spectral:wght@400;600;700&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    :root { --red: #E22D32; --text: #1a1a1a; --muted: #555; --border: #e5e5e5; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #fff; color: var(--text); line-height: 1.6; }

    header { border-bottom: 1px solid var(--border); padding: 2rem 0 1.5rem; }
    .container { max-width: 1000px; margin: 0 auto; padding: 0 2rem; }
    .site-title { font-family: 'Spectral', serif; font-size: 2.4rem; font-weight: 700; letter-spacing: -0.5px; }
    .site-title a { text-decoration: none; color: inherit; }
    .site-title span { display: inline-block; border-bottom: 3px solid var(--red); padding-bottom: 2px; }
    nav { margin-top: 0.75rem; display: flex; gap: 1.5rem; }
    nav a { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); text-decoration: none; font-weight: 600; }
    nav a:hover, nav a[aria-current] { color: var(--red); }
    nav a:focus-visible { outline: 2px solid var(--red); outline-offset: 3px; border-radius: 2px; }

    .skip-link { position: absolute; top: -100%; left: 1rem; background: var(--red); color: #fff; padding: 0.5rem 1rem; font-size: 0.85rem; font-weight: 700; text-decoration: none; border-radius: 0 0 4px 4px; z-index: 100; }
    .skip-link:focus { top: 0; }

    .section-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--red); margin-bottom: 1.5rem; }

    /* ── Cards ── */
    .cards-section { padding: 3rem 0; }
    .cards-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; }
    @media (max-width: 600px) { .cards-grid { grid-template-columns: 1fr; } }
    .card { transition: transform 0.2s ease, box-shadow 0.2s ease; }
    .card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,0,0,0.08); }
    .card img { width: 100%; height: 200px; object-fit: cover; display: block; border: 1px solid var(--border); }
    .card-body { padding: 1rem 0 0; }
    .card-title { font-family: 'Spectral', serif; font-size: 1.2rem; font-weight: 600; margin-bottom: 0.25rem; }
    .card-desc { font-size: 0.9rem; color: var(--muted); }
    .card-placeholder-img { width: 100%; height: 200px; background: #f5f5f5; border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; }
    .card-placeholder-img::after { content: '\2014'; font-size: 1.5rem; color: var(--border); }

    /* ── Footer ── */
    footer { border-top: 3px solid var(--red); padding: 2rem 0; }
    .footer-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
    .footer-copy { font-size: 0.85rem; color: var(--muted); }
    .footer-contact { display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; }
    .footer-contact a { font-size: 0.85rem; color: var(--muted); text-decoration: none; }
    .footer-contact a:hover { color: var(--red); }
    .footer-contact a:focus-visible { outline: 2px solid var(--red); outline-offset: 3px; border-radius: 2px; }

    /* ── Scroll animations ── */
    .fade-in { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .fade-in.visible { opacity: 1; transform: translateY(0); }

    /* ── Page transition curtain ── */
    .curtain { position: fixed; inset: 0; background: var(--red); z-index: 9999; transform: translateY(-100%); pointer-events: none; }
    .curtain.enter { animation: curtainEnter 0.45s cubic-bezier(0.77,0,0.18,1) forwards; }
    .curtain.exit  { animation: curtainExit  0.35s cubic-bezier(0.77,0,0.18,1) forwards; pointer-events: all; }
    @keyframes curtainEnter { from { transform: translateY(0); } to { transform: translateY(-100%); } }
    @keyframes curtainExit  { from { transform: translateY(-100%); } to { transform: translateY(0); } }
  </style>
  <noscript><style>.fade-in { opacity: 1; transform: none; }</style></noscript>
</head>
<body>
<a href="#main-content" class="skip-link">Skip to content</a>

  <header>
    <div class="container">
      <h1 class="site-title"><a href="index.html"><span>Noah Foster</span></a></h1>
      <nav aria-label="Main">
        <a href="about.html">About</a>
        <a href="projects.html" aria-current="page">Projects</a>
        <a href="feed.html">Feed</a>
        <a href="https://www.linkedin.com/in/noahbfoster/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      </nav>
    </div>
  </header>

  <main id="main-content">
    <section class="cards-section fade-in">
      <div class="container">
        <h2 class="section-label">Projects</h2>
        <div class="cards-grid">

          <div class="card">
            <img src="https://picsum.photos/seed/noahsite/600/400" alt="noahfoster.com" loading="lazy" width="600" height="400" onerror="this.style.background='#f5f5f5'" />
            <div class="card-body">
              <h3 class="card-title">noahfoster.com</h3>
              <p class="card-desc">This site — designed and built with Claude from scratch. My first project as I learn to code.</p>
            </div>
          </div>

          <div class="card">
            <img src="https://picsum.photos/seed/nycmovie/600/400" alt="NYC Movie App" loading="lazy" width="600" height="400" onerror="this.style.background='#f5f5f5'" />
            <div class="card-body">
              <h3 class="card-title">NYC Movie App</h3>
              <p class="card-desc">A personal tool that aggregates AMC, Alamo Drafthouse, and advance screening listings in one place — with support for film festivals and special events.</p>
            </div>
          </div>

          <div class="card">
            <img src="https://picsum.photos/seed/nycmetro/600/400" alt="NYC Metro App" loading="lazy" width="600" height="400" onerror="this.style.background='#f5f5f5'" />
            <div class="card-body">
              <h3 class="card-title">NYC Metro App</h3>
              <p class="card-desc">A real-time subway companion app for New York City, inspired by the transit tools I actually want to use. Built to practice API integration and mobile-first design.</p>
            </div>
          </div>

          <div class="card">
            <img src="https://picsum.photos/seed/hedgefund/600/400" alt="AI Hedge Fund" loading="lazy" width="600" height="400" onerror="this.style.background='#f5f5f5'" />
            <div class="card-body">
              <h3 class="card-title">AI Hedge Fund</h3>
              <p class="card-desc">Three competing strategies — Long/Short AI, Active Management AI, and myself as CIO — paper trading for six months before deploying real capital.</p>
            </div>
          </div>

          <div class="card">
            <img src="https://picsum.photos/seed/sportsbetting/600/400" alt="Sports Betting Models" loading="lazy" width="600" height="400" onerror="this.style.background='#f5f5f5'" />
            <div class="card-body">
              <h3 class="card-title">Sports Betting Models</h3>
              <p class="card-desc">A suite of data-driven models for NFL and NBA prop betting, with team-specific analysis for the Patriots, Celtics, and Red Sox.</p>
            </div>
          </div>

          <div class="card card--placeholder">
            <div class="card-placeholder-img"></div>
            <div class="card-body">
              <h3 class="card-title">Coming Soon</h3>
              <p class="card-desc">Next project in progress.</p>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-copy">© 2026 Noah Foster</span>
        <div class="footer-contact">
          <a href="mailto:noahfoster6@gmail.com">noahfoster6@gmail.com</a>
          <a href="https://www.linkedin.com/in/noahbfoster/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        </div>
      </div>
    </div>
  </footer>

  <div class="curtain" id="curtain"></div>
  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

    const curtain = document.getElementById('curtain');
    if (curtain) {
      curtain.classList.add('enter');
      document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto')) return;
        link.addEventListener('click', e => {
          e.preventDefault();
          curtain.classList.remove('enter');
          curtain.classList.add('exit');
          setTimeout(() => { window.location.href = href; }, 350);
        });
      });
    }
  </script>
</body>
</html>
```

**Step 2: Verify**

Open `projects.html` in a browser. Confirm:
- Header, nav, footer render correctly
- Projects link in nav is red (aria-current="page")
- 5 project cards + 1 placeholder visible in 2-column grid
- Curtain wipes in on load

**Step 3: Commit**

```bash
cd ~/Sites/noahfoster2174.github.io
git add projects.html
git commit -m "feat: add projects.html as standalone page"
```

---

## Task 2: Redesign about.html (resume-adjacent)

**File:**
- Modify: `~/Sites/noahfoster2174.github.io/about.html` — full replacement

**Step 1: Replace the entire file with this content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About — Noah Foster</title>
  <meta name="description" content="About Noah Foster — Senior Finance Analyst at Amazon Advertising, building toward sports." />
  <meta property="og:title" content="About — Noah Foster" />
  <meta property="og:description" content="Senior Finance Analyst at Amazon Advertising. Building toward sports. Running toward Tokyo." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://noahfoster2174.github.io/about.html" />
  <meta property="og:image" content="https://placehold.co/1200x630/E22D32/ffffff?text=Noah+Foster" />
  <meta property="og:site_name" content="Noah Foster" />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='4' fill='%23E22D32'/><text x='50%25' y='50%25' dominant-baseline='central' text-anchor='middle' font-family='Georgia,serif' font-weight='700' font-size='14' fill='white'>NF</text></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Spectral:wght@400;600;700&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    :root { --red: #E22D32; --text: #1a1a1a; --muted: #555; --border: #e5e5e5; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #fff; color: var(--text); line-height: 1.6; }

    header { border-bottom: 1px solid var(--border); padding: 2rem 0 1.5rem; }
    .container { max-width: 1000px; margin: 0 auto; padding: 0 2rem; }
    .site-title { font-family: 'Spectral', serif; font-size: 2.4rem; font-weight: 700; letter-spacing: -0.5px; }
    .site-title a { text-decoration: none; color: inherit; }
    .site-title span { display: inline-block; border-bottom: 3px solid var(--red); padding-bottom: 2px; }
    nav { margin-top: 0.75rem; display: flex; gap: 1.5rem; }
    nav a { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); text-decoration: none; font-weight: 600; }
    nav a:hover, nav a[aria-current] { color: var(--red); }
    nav a:focus-visible { outline: 2px solid var(--red); outline-offset: 3px; border-radius: 2px; }

    .skip-link { position: absolute; top: -100%; left: 1rem; background: var(--red); color: #fff; padding: 0.5rem 1rem; font-size: 0.85rem; font-weight: 700; text-decoration: none; border-radius: 0 0 4px 4px; z-index: 100; }
    .skip-link:focus { top: 0; }

    .section-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--red); margin-bottom: 1.5rem; }

    /* ── Bio ── */
    .bio-section { padding: 3.5rem 0; border-bottom: 1px solid var(--border); }
    .bio-grid { display: grid; grid-template-columns: 200px 1fr; gap: 3rem; align-items: start; }
    @media (max-width: 640px) { .bio-grid { grid-template-columns: 1fr; } }
    .bio-photo { width: 200px; height: 200px; border-radius: 50%; object-fit: cover; display: block; border: 3px solid var(--border); }
    .bio-text p { font-size: 1rem; color: var(--muted); line-height: 1.75; }

    /* ── Experience ── */
    .experience-section { padding: 3rem 0; border-bottom: 1px solid var(--border); }
    .exp-list { display: flex; flex-direction: column; gap: 2.5rem; }
    .exp-item { display: grid; grid-template-columns: 200px 1fr; gap: 3rem; align-items: start; }
    @media (max-width: 640px) { .exp-item { grid-template-columns: 1fr; gap: 0.5rem; } }
    .exp-meta { display: flex; flex-direction: column; gap: 0.2rem; }
    .exp-company { font-weight: 700; font-size: 0.95rem; }
    .exp-period { font-size: 0.8rem; color: var(--muted); }
    .exp-role { font-size: 0.9rem; font-weight: 600; color: var(--red); margin-bottom: 0.6rem; }
    .exp-bullets { list-style: none; display: flex; flex-direction: column; gap: 0.35rem; }
    .exp-bullets li { font-size: 0.9rem; color: var(--muted); padding-left: 1.1rem; position: relative; line-height: 1.5; }
    .exp-bullets li::before { content: '—'; position: absolute; left: 0; color: var(--border); }

    /* ── Skills ── */
    .skills-section { padding: 3rem 0; border-bottom: 1px solid var(--border); }
    .skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
    @media (max-width: 600px) { .skills-grid { grid-template-columns: 1fr; gap: 1.5rem; } }
    .skills-cat-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text); margin-bottom: 0.75rem; }
    .skills-list { list-style: none; display: flex; flex-direction: column; gap: 0.4rem; }
    .skills-list li { font-size: 0.9rem; color: var(--muted); }

    /* ── CTA ── */
    .about-cta-section { padding: 3rem 0; }
    .cta-link { font-family: 'Spectral', serif; font-size: 1.2rem; color: var(--text); text-decoration: none; border-bottom: 2px solid var(--red); padding-bottom: 2px; }
    .cta-link:hover { color: var(--red); }
    .cta-link:focus-visible { outline: 2px solid var(--red); outline-offset: 3px; border-radius: 2px; }

    /* ── Footer ── */
    footer { border-top: 3px solid var(--red); padding: 2rem 0; }
    .footer-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
    .footer-copy { font-size: 0.85rem; color: var(--muted); }
    .footer-contact { display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; }
    .footer-contact a { font-size: 0.85rem; color: var(--muted); text-decoration: none; }
    .footer-contact a:hover { color: var(--red); }
    .footer-contact a:focus-visible { outline: 2px solid var(--red); outline-offset: 3px; border-radius: 2px; }

    /* ── Scroll animations ── */
    .fade-in { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .fade-in.visible { opacity: 1; transform: translateY(0); }

    /* ── Page transition curtain ── */
    .curtain { position: fixed; inset: 0; background: var(--red); z-index: 9999; transform: translateY(-100%); pointer-events: none; }
    .curtain.enter { animation: curtainEnter 0.45s cubic-bezier(0.77,0,0.18,1) forwards; }
    .curtain.exit  { animation: curtainExit  0.35s cubic-bezier(0.77,0,0.18,1) forwards; pointer-events: all; }
    @keyframes curtainEnter { from { transform: translateY(0); } to { transform: translateY(-100%); } }
    @keyframes curtainExit  { from { transform: translateY(-100%); } to { transform: translateY(0); } }
  </style>
  <noscript><style>.fade-in { opacity: 1; transform: none; }</style></noscript>
</head>
<body>
<a href="#main-content" class="skip-link">Skip to content</a>

  <header>
    <div class="container">
      <h1 class="site-title"><a href="index.html"><span>Noah Foster</span></a></h1>
      <nav aria-label="Main">
        <a href="about.html" aria-current="page">About</a>
        <a href="projects.html">Projects</a>
        <a href="feed.html">Feed</a>
        <a href="https://www.linkedin.com/in/noahbfoster/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      </nav>
    </div>
  </header>

  <main id="main-content">

    <section class="bio-section fade-in">
      <div class="container">
        <div class="bio-grid">
          <img src="photo.jpg" alt="Noah Foster" class="bio-photo" onerror="this.src='https://placehold.co/300x300/f5f5f5/555?text=NF'" />
          <div class="bio-text">
            <h2 class="section-label">About</h2>
            <p>Senior Finance Analyst at Amazon Advertising in New York, where I lead valuation and deal structuring for Fortune 100 global advertising partnerships. My long-term goal is a front-office finance role in professional sports — and I'm building toward it by learning to code, training for the 2026 Tokyo Marathon, and working through a personal project roadmap.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="experience-section fade-in">
      <div class="container">
        <h2 class="section-label">Experience</h2>
        <div class="exp-list">

          <div class="exp-item">
            <div class="exp-meta">
              <span class="exp-company">Amazon Advertising</span>
              <span class="exp-period">2023 – Present · New York</span>
            </div>
            <div>
              <div class="exp-role">Senior Finance Analyst</div>
              <ul class="exp-bullets">
                <li>Lead valuation and deal structuring for Fortune 100 global advertising partnerships</li>
                <li>Manage partnerships ranging up to $385MM annually</li>
              </ul>
            </div>
          </div>

          <div class="exp-item">
            <div class="exp-meta">
              <span class="exp-company">Capital One</span>
              <span class="exp-period">2019 – 2023</span>
            </div>
            <div>
              <div class="exp-role">Finance Analyst</div>
              <ul class="exp-bullets">
                <li>Deal finance, partnership valuations, and capital markets</li>
                <li>Four years across multiple finance functions</li>
              </ul>
            </div>
          </div>

        </div>
      </div>
    </section>

    <section class="skills-section fade-in">
      <div class="container">
        <h2 class="section-label">Skills</h2>
        <div class="skills-grid">

          <div class="skills-cat">
            <h3 class="skills-cat-label">Finance</h3>
            <ul class="skills-list">
              <li>Financial Modeling</li>
              <li>Deal Structuring</li>
              <li>Partnership Valuations</li>
              <li>Capital Markets</li>
            </ul>
          </div>

          <div class="skills-cat">
            <h3 class="skills-cat-label">Data &amp; Analytics</h3>
            <ul class="skills-list">
              <li>Python</li>
              <li>SQL</li>
              <li>Snowflake</li>
              <li>Tableau</li>
              <li>Bloomberg</li>
            </ul>
          </div>

          <div class="skills-cat">
            <h3 class="skills-cat-label">Technology</h3>
            <ul class="skills-list">
              <li>AWS</li>
              <li>Claude Code</li>
              <li>React</li>
              <li>Git / GitHub</li>
            </ul>
          </div>

        </div>
      </div>
    </section>

    <section class="about-cta-section fade-in">
      <div class="container">
        <a href="projects.html" class="cta-link">See my projects →</a>
      </div>
    </section>

  </main>

  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-copy">© 2026 Noah Foster</span>
        <div class="footer-contact">
          <a href="mailto:noahfoster6@gmail.com">noahfoster6@gmail.com</a>
          <a href="https://www.linkedin.com/in/noahbfoster/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        </div>
      </div>
    </div>
  </footer>

  <div class="curtain" id="curtain"></div>
  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

    const curtain = document.getElementById('curtain');
    if (curtain) {
      curtain.classList.add('enter');
      document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto')) return;
        link.addEventListener('click', e => {
          e.preventDefault();
          curtain.classList.remove('enter');
          curtain.classList.add('exit');
          setTimeout(() => { window.location.href = href; }, 350);
        });
      });
    }
  </script>
</body>
</html>
```

**Step 2: Verify**

Open `about.html` in a browser. Confirm:
- Bio: photo + 1 paragraph (no building section, no old skill tags, no cards)
- Experience: Amazon (2023–Present) then Capital One (2019–2023), two bullet each
- Skills: three columns — Finance / Data & Analytics / Technology
- CTA "See my projects →" at the bottom
- About link in nav is red (aria-current="page")
- Curtain wipes in on load

**Step 3: Commit**

```bash
cd ~/Sites/noahfoster2174.github.io
git add about.html
git commit -m "redesign: about.html as resume-adjacent (bio, experience, skills)"
```

---

## Task 3: Update nav links on index.html and feed.html

**Files:**
- Modify: `~/Sites/noahfoster2174.github.io/index.html`
- Modify: `~/Sites/noahfoster2174.github.io/feed.html`

**Step 1: In index.html — update two links**

Change the nav Projects link (line ~161):
```
OLD: <a href="about.html#projects">Projects</a>
NEW: <a href="projects.html">Projects</a>
```

Change the CTA "See all projects" link (line ~218):
```
OLD: <a href="about.html#projects" class="cta-link">See all projects →</a>
NEW: <a href="projects.html" class="cta-link">See all projects →</a>
```

**Step 2: In feed.html — update the nav Projects link**

Find the nav block (around line 50–60) and change:
```
OLD: <a href="about.html#projects">Projects</a>
NEW: <a href="projects.html">Projects</a>
```

**Step 3: Verify**

- Open `index.html` — clicking "Projects" in nav and "See all projects →" CTA both go to `projects.html`
- Open `feed.html` — clicking "Projects" in nav goes to `projects.html`
- No remaining `about.html#projects` references across any file

Run this check:
```bash
grep -r "about.html#projects" ~/Sites/noahfoster2174.github.io/*.html
```
Expected: no output (zero matches).

**Step 4: Commit**

```bash
cd ~/Sites/noahfoster2174.github.io
git add index.html feed.html
git commit -m "fix: update nav/cta links to point to projects.html"
```

---

## Task 4: Push to GitHub Pages

**Step 1: Push**

```bash
cd ~/Sites/noahfoster2174.github.io
git push
```

**Step 2: Verify live**

After ~30s, open https://noahfoster2174.github.io in browser. Confirm:
- Nav: About, Projects, Feed, LinkedIn all work
- About → resume-adjacent (bio, experience, skills, CTA)
- Projects → standalone cards page
- Feed → unchanged
- Curtain transitions between pages work
