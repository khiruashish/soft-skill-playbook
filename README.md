# Soft Skill Playbook

A practical communication & confidence playbook for software developers — beginners to 15+ years —
built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and a custom 3D card layout.

**Live site:** https://khiruashish.github.io/soft-skill-playbook/

## Deployment

Every push to `main` builds the site with `mkdocs build --strict` and publishes it to GitHub Pages
(`.github/workflows/deploy.yml`). You can also run it manually from the **Actions** tab
(*Deploy to GitHub Pages → Run workflow*).

One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Run locally

```bash
git clone https://github.com/khiruashish/soft-skill-playbook.git
cd soft-skill-playbook
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000
```

## Build static site

```bash
mkdocs build --strict   # output in ./site
```

## What's inside

| Section | Pages |
|---|---|
| Master Prompt | A reusable AI coaching prompt to practise any conversation |
| Foundations | Communication principles, listening & questions, confidence, 90-day improvement plan, burnout & wellbeing |
| Workplace | Manager, juniors, CEO, peers, team lead meetings, global & remote teams, mentoring, team building, work from home, leave & boundaries, explaining issues, day-to-day, meetings, difficult conversations, client meetings, office party |
| Career | Interviews, first 90 days, performance review, promotion discussion, appraisal discussion, salary negotiation, resignation, handling layoffs |
| Everyday Life | Airport, train, hotel, restaurant, cab, doctor, bank & shopping, phone calls, small talk |
| Reference | Phrase bank, daily practice checklist |

The 3D effects (hero cube, tilting cards, layered depth) live in `docs/assets/css/3d.css` and
`docs/assets/js/tilt.js`, and switch off automatically for users who prefer reduced motion.
