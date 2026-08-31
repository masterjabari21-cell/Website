# Jabari Weaver — Personal Website

A single-page personal site themed after Tyler, the Creator's *Call Me If You Get Lost*:
cream paper texture, powder blue / mustard / teal palette, luggage-tag & passport-stamp
styling, and a canvas animation of 4-point stars drifting down the page.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The whole site in one file: the "License of Travel" gate first, then hero, about, projects, experience, contact. The gate's menu cross-fades into the site with no page reload. |
| `serve.py` | Local dev server (no dependencies, Python 3 stdlib only). |

## Run it locally

```bash
python3 serve.py          # http://localhost:8000
python3 serve.py 5500     # custom port
```

Opens your browser automatically and serves with no-cache headers, so edits
appear on refresh. Ctrl+C to stop.

You can also just double-click `index.html` — the server is only needed if you
later add things browsers block on `file://` (fetch, modules, etc.).

## Fill in your content

Search `index.html` for `PLACEHOLDER` and the sections marked below:

On the gate (the licence card):

- Update the fields (`.lic-row`: date of birth, place of issue), the licence
  number (`.lic-no`), and the signature. To use a real photo, replace the
  `.photo-ph` div with `<img src="me.jpg" alt="..." />`. The menu under the
  card (About Me / Projects / Experience / Contact) fades straight into that
  section — no reload. The ✦ name in the site header brings the card back.
  Arriving with a hash (e.g. `/#work` from a shared link) skips the gate.

On the main site:

- **Hero** — the one-line intro under your name.
- **About** — 2–3 paragraphs + the "Traveler's Card" fields (location, role, focus, status).
- **Work** — replace the three luggage-tag cards with real projects (title, blurb, role/year/stack, link).
- **Résumé** — the timeline entries, the skills chips, and the "Download Résumé (PDF)" link
  (drop a `resume.pdf` in this folder and point the link at it).
- **Contact** — the GitHub / LinkedIn / Twitter URLs (email is already set).

Colors live in the `:root` block at the top of the `<style>` tag if you want to tune the palette.

## Deploy

It's static — any host works. GitHub Pages, Netlify drop, Cloudflare Pages,
or `Vercel`: just publish this folder.

---

Theme is an homage for a personal project and is not affiliated with or endorsed by
Tyler, the Creator or his labels.
