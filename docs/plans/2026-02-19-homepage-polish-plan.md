# Homepage Polish + Page Transitions Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign the homepage with a full-viewport split-screen hero, live Strava stats, dark featured project card, curtain wipe page transitions on all pages, and remove quotes from about.html.

**Architecture:** Three static HTML files, all CSS inline in `<style>`, minimal vanilla JS. Page transitions use a shared CSS curtain pattern added to all three pages. No frameworks, no build tools.

**Tech Stack:** HTML5, CSS3, vanilla JS (IntersectionObserver, fetch), GitHub Pages

---

### Task 1: Remove Quotes from about.html

**Files:**
- Modify: `~/Sites/noahfoster2174.github.io/about.html`

**Step 1: Remove the quotes section HTML**

Find and delete this entire block (lines ~216–232):
```html
    <section class="quotes-section fade-in">
      <div class="container">
        <h2 class="section-label">Quotes</h2>
        <blockquote class="quote-featured">
          The way to get started is to quit talking and begin doing.
          <cite>— Walt Disney</cite>
        </blockquote>
        <ul class="quotes-list">
          <li>"It's not whether you get knocked down, it's whether you get up." — Vince Lombardi</li>
          <li>"Your time is limited, so don't waste it living someone else's life." — Steve Jobs</li>
        </ul>
      </div>
    </section>
```

**Step 2: Remove the quotes CSS**

Find and delete these rules from the `<style>` block:
```css
    /* ── Quotes ── */
    .quotes-section { padding: 3rem 0; border-bottom: 1px solid var(--border); }
    .quote-featured { font-family: 'Spectral', serif; font-size: 1.6rem; line-height: 1.45; max-width: 680px; margin: 0 auto 2rem; text-align: center; position: relative; }
    .quote-featured::before { content: '\201C'; font-size: 5rem; color: var(--red); line-height: 0; position: absolute; top: 1.5rem; left: -1rem; font-family: 'Spectral', serif; opacity: 0.15; }
    .quote-featured cite { display: block; font-size: 0.9rem; font-style: normal; color: var(--muted); margin-top: 0.75rem; }
    .quotes-list { list-style: none; display: flex; flex-direction: column; gap: 0.75rem; max-width: 560px; margin: 0 auto; }
    .quotes-list li { font-size: 0.95rem; color: var(--muted); padding-left: 1rem; border-left: 2px solid var(--border); }
```

**Step 3: Commit**
```bash
cd ~/Sites/noahfoster2174.github.io && git add about.html && git commit -m "feat: remove quotes section from about page"
```

---

### Task 2: Redesign Homepage Hero (split-screen, full viewport)

**Files:**
- Modify: `~/Sites/noahfoster2174.github.io/index.html`

**Step 1: Replace the CSS `<style>` block entirely**

Replace everything between `<style>` and `</style>` with:

```css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    :root {
      --red: #E22D32;
      --text: #1a1a1a;
      --muted: #555;
      --border: #e5e5e5;
    }

    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #fff; color: var(--text); line-height: 1.6; overflow-x: hidden; }

    header { border-bottom: 1px solid var(--border); padding: 2rem 0 1.5rem; position: relative; z-index: 1; }
    .container { max-width: 1000px; margin: 0 auto; padding: 0 2rem; }
    .site-title { font-family: 'Spectral', serif; font-size: 2.4rem; font-weight: 700; letter-spacing: -0.5px; }
    .site-title a { text-decoration: none; color: inherit; }
    .site-title span { display: inline-block; border-bottom: 3px solid var(--red); padding-bottom: 2px; }
    nav { margin-top: 0.75rem; display: flex; gap: 1.5rem; }
    nav a { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); text-decoration: none; font-weight: 600; }
    nav a:hover { color: var(--red); }
    nav a:focus-visible,
    .cta-link:focus-visible,
    .footer-contact a:focus-visible {
      outline: 2px solid var(--red);
      outline-offset: 3px;
      border-radius: 2px;
    }

    .section-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--red); margin-bottom: 1.5rem; }

    /* ── Hero ── */
    .hero {
      min-height: calc(100vh - 97px);
      display: flex;
      align-items: center;
      border-bottom: 1px solid var(--border);
    }
    .hero-inner {
      display: grid;
      grid-template-columns: 3fr 2fr;
      gap: 4rem;
      align-items: center;
      width: 100%;
      padding: 4rem 0;
    }
    @media (max-width: 700px) {
      .hero-inner { grid-template-columns: 1fr; gap: 2.5rem; padding: 3rem 0; }
    }

    /* Left: tagline */
    .hero-tagline {
      font-family: 'Spectral', serif;
      font-size: clamp(1.6rem, 3.5vw, 2.4rem);
      color: var(--muted);
      line-height: 1.4;
      opacity: 0;
      transform: translateY(24px);
      animation: heroReveal 0.7s ease 0.1s forwards;
    }
    .hero-tagline em { color: var(--red); font-style: normal; font-weight: 600; }

    @keyframes heroReveal {
      to { opacity: 1; transform: translateY(0); }
    }

    /* Right: stats panel */
    .hero-stats {
      border-left: 2px solid var(--red);
      padding-left: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      opacity: 0;
      animation: heroReveal 0.7s ease 0.35s forwards;
    }
    @media (max-width: 700px) {
      .hero-stats { border-left: none; border-top: 2px solid var(--red); padding-left: 0; padding-top: 1.5rem; flex-direction: row; flex-wrap: wrap; gap: 1.25rem 2rem; }
    }
    .stat-block { display: flex; flex-direction: column; gap: 0.1rem; }
    .stat-label { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--border); }
    .stat-value { font-size: 0.95rem; color: var(--text); font-weight: 500; }
    .stat-live .stat-label { color: var(--red); }
    .stat-live .stat-value { font-family: 'Spectral', serif; font-size: 1.3rem; font-weight: 700; }

    /* ── Intro ── */
    .intro-section { padding: 2rem 0; border-bottom: 1px solid var(--border); }
    .intro-line { font-family: 'Spectral', serif; font-size: 1.15rem; color: var(--muted); }

    /* ── Featured Project ── */
    .featured-section { padding: 3rem 0; border-bottom: 1px solid var(--border); }
    .featured-card {
      background: #1a1a1a;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3rem;
      padding: 3rem;
      align-items: center;
    }
    @media (max-width: 640px) {
      .featured-card { grid-template-columns: 1fr; gap: 1.5rem; padding: 2rem; }
    }
    .featured-title { font-family: 'Spectral', serif; font-size: 2rem; font-weight: 700; color: #fff; line-height: 1.2; margin-bottom: 0; }
    .featured-desc { font-size: 0.95rem; color: #999; line-height: 1.7; margin-bottom: 1.25rem; }
    .featured-cta { font-size: 0.85rem; font-weight: 700; color: var(--red); text-transform: uppercase; letter-spacing: 0.08em; }

    /* ── CTAs ── */
    .cta-section { padding: 3rem 0; }
    .cta-group { display: flex; gap: 2rem; flex-wrap: wrap; }
    .cta-link { font-family: 'Spectral', serif; font-size: 1.2rem; color: var(--text); text-decoration: none; border-bottom: 2px solid var(--red); padding-bottom: 2px; }
    .cta-link:hover { color: var(--red); }

    /* ── Footer ── */
    footer { border-top: 3px solid var(--red); padding: 2rem 0; }
    .footer-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
    .footer-copy { font-size: 0.85rem; color: var(--muted); }
    .footer-contact { display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; }
    .footer-contact a { font-size: 0.85rem; color: var(--muted); text-decoration: none; }
    .footer-contact a:hover { color: var(--red); }

    /* ── Scroll animations ── */
    .fade-in { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .fade-in.visible { opacity: 1; transform: translateY(0); }

    /* ── Page transition curtain ── */
    .curtain {
      position: fixed; inset: 0;
      background: var(--red);
      z-index: 9999;
      transform: translateY(-100%);
      pointer-events: none;
    }
    .curtain.enter { animation: curtainEnter 0.45s cubic-bezier(0.77,0,0.18,1) forwards; }
    .curtain.exit  { animation: curtainExit  0.35s cubic-bezier(0.77,0,0.18,1) forwards; pointer-events: all; }
    @keyframes curtainEnter { from { transform: translateY(0); } to { transform: translateY(-100%); } }
    @keyframes curtainExit  { from { transform: translateY(-100%); } to { transform: translateY(0); } }
```

**Step 2: Replace `<main>` entirely**

```html
  <main>
    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <p class="hero-tagline">Senior Finance Analyst at <em>Amazon Advertising</em>. Building toward sports. Running toward Tokyo.</p>
          <div class="hero-stats">
            <div class="stat-block">
              <span class="stat-label">Role</span>
              <span class="stat-value">Senior Finance Analyst</span>
              <span class="stat-value">Amazon Advertising</span>
            </div>
            <div class="stat-block">
              <span class="stat-label">Based</span>
              <span class="stat-value">New York City</span>
            </div>
            <div class="stat-block">
              <span class="stat-label">Goal</span>
              <span class="stat-value">Tokyo Marathon 2026</span>
            </div>
            <div class="stat-block stat-live" id="hero-miles" style="display:none">
              <span class="stat-label">This week</span>
              <span class="stat-value" id="hero-miles-value">—</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="intro-section fade-in">
      <div class="container">
        <p class="intro-line">I build at the intersection of finance, sports, and technology.</p>
      </div>
    </section>

    <section class="featured-section fade-in">
      <div class="container">
        <h2 class="section-label">Featured Project</h2>
        <div class="featured-card">
          <h3 class="featured-title">NYC Movie App</h3>
          <div class="featured-body">
            <p class="featured-desc">A personal tool that aggregates AMC, Alamo Drafthouse, and advance screening listings in one place — with support for film festivals and special events. Built for my NYC moviegoing habit.</p>
            <span class="featured-cta">In development →</span>
          </div>
        </div>
      </div>
    </section>

    <section class="cta-section fade-in">
      <div class="container">
        <div class="cta-group">
          <a href="about.html#projects" class="cta-link">See all projects →</a>
          <a href="about.html" class="cta-link">About me →</a>
        </div>
      </div>
    </section>
  </main>
```

**Step 3: Replace the `<script>` block (before `</body>`)**

```html
  <div class="curtain" id="curtain"></div>

  <noscript><style>.fade-in { opacity: 1; transform: none; }</style></noscript>
  <script>
    // ── Scroll animations ──
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

    // ── Live miles from Strava ──
    (async () => {
      try {
        const res = await fetch('strava.json');
        if (!res.ok) return;
        const activities = await res.json();
        if (!Array.isArray(activities)) return;
        const now = new Date();
        const daysFromMon = now.getDay() === 0 ? 6 : now.getDay() - 1;
        const weekStart = new Date(now);
        weekStart.setDate(now.getDate() - daysFromMon);
        weekStart.setHours(0, 0, 0, 0);
        const miles = activities
          .filter(a => new Date(a.start_date_local) >= weekStart)
          .reduce((sum, a) => sum + a.distance, 0) / 1609.34;
        if (miles > 0) {
          document.getElementById('hero-miles-value').textContent = miles.toFixed(1) + ' mi';
          document.getElementById('hero-miles').style.display = '';
        }
      } catch {}
    })();

    // ── Page transition curtain ──
    const curtain = document.getElementById('curtain');
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
  </script>
```

**Step 4: Commit**
```bash
cd ~/Sites/noahfoster2174.github.io && git add index.html && git commit -m "feat: redesign homepage with split-screen hero, dark project card, scroll animations"
```

---

### Task 3: Add Curtain Transition to about.html

**Files:**
- Modify: `~/Sites/noahfoster2174.github.io/about.html`

**Step 1: Add curtain CSS** to the `<style>` block, at the bottom before `</style>`:

```css
    /* ── Page transition curtain ── */
    .curtain { position: fixed; inset: 0; background: var(--red); z-index: 9999; transform: translateY(-100%); pointer-events: none; }
    .curtain.enter { animation: curtainEnter 0.45s cubic-bezier(0.77,0,0.18,1) forwards; }
    .curtain.exit  { animation: curtainExit  0.35s cubic-bezier(0.77,0,0.18,1) forwards; pointer-events: all; }
    @keyframes curtainEnter { from { transform: translateY(0); } to { transform: translateY(-100%); } }
    @keyframes curtainExit  { from { transform: translateY(-100%); } to { transform: translateY(0); } }
```

**Step 2: Add curtain div + transition JS** just before `</body>`:

```html
  <div class="curtain" id="curtain"></div>
  <script>
    // existing IntersectionObserver script stays above this
    const curtain = document.getElementById('curtain');
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
  </script>
```

**Step 3: Commit**
```bash
cd ~/Sites/noahfoster2174.github.io && git add about.html && git commit -m "feat: add curtain page transition to about page"
```

---

### Task 4: Add Curtain Transition to feed.html

**Files:**
- Modify: `~/Sites/noahfoster2174.github.io/feed.html`

**Step 1: Add curtain CSS** to the `<style>` block, at the bottom before `</style>`:

```css
    /* ── Page transition curtain ── */
    .curtain { position: fixed; inset: 0; background: var(--red); z-index: 9999; transform: translateY(-100%); pointer-events: none; }
    .curtain.enter { animation: curtainEnter 0.45s cubic-bezier(0.77,0,0.18,1) forwards; }
    .curtain.exit  { animation: curtainExit  0.35s cubic-bezier(0.77,0,0.18,1) forwards; pointer-events: all; }
    @keyframes curtainEnter { from { transform: translateY(0); } to { transform: translateY(-100%); } }
    @keyframes curtainExit  { from { transform: translateY(-100%); } to { transform: translateY(0); } }
```

**Step 2: Add curtain div + JS** just before `</body>` (after the existing `<script>` block):

```html
  <div class="curtain" id="curtain"></div>
  <script>
    const curtain = document.getElementById('curtain');
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
  </script>
```

**Step 3: Commit**
```bash
cd ~/Sites/noahfoster2174.github.io && git add feed.html && git commit -m "feat: add curtain page transition to feed page"
```

---

### Task 5: Push Everything

```bash
cd ~/Sites/noahfoster2174.github.io && git push origin master
```

Verify live:
- https://noahfoster2174.github.io — split-screen hero, dark project card, curtain transition
- https://noahfoster2174.github.io/about.html — no quotes, curtain transition
- https://noahfoster2174.github.io/feed.html — curtain transition
