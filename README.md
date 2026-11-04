# Soft Skill Playbook

A practical communication & confidence playbook for software developers — beginners to 15+ years —
built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and a custom 3D card layout.

**Live site:** https://khiruashish.github.io/soft-skill-playbook/

## Deployment

Every push to `main` builds the site with `mkdocs gh-deploy --strict` and pushes the result to the
`gh-pages` branch (`.github/workflows/deploy.yml`). You can also run it manually from the **Actions**
tab (*Deploy to GitHub Pages → Run workflow*).

One-time setup: **Settings → Pages → Build and deployment → Source: Deploy from a branch →
`gh-pages` / `(root)`**.

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

## What's inside: a 78-day course

| Phase | Days | Topics |
|---|---|---|
| Start here | — | Master prompts (course tutor, conversation generator, grammar trainer, communication coach), course roadmap |
| 1 · English Basics | 1–13 | Introductions, sentences, yes/no and wh- questions, answers, tenses, polite English, linking words, numbers/time/money, describing, common mistakes |
| 2 · Communication | 14–18 | Principles, listening, confidence, small talk, phone calls |
| 3 · Everyday Life | 19–51 | Train, metro & bus, travel visa, airport, flight, cab, hotel, sightseeing, restaurant, food delivery, grocery, shopping, bank, bank locker, insurance, post, hospital, doctor, dentist & eye, gym, yoga, sports, renting, neighbours, home services, salon, customer care, government office, police, school, celebrations, movies, vehicle |
| 4 · Workplace | 52–67 | Day-to-day, manager, peers, juniors, issues, meetings, team lead, CEO, clients, difficult conversations, remote teams, WFH, leave, mentoring, team building, office party |
| 5 · Career | 68–78 | Interviews, first 90 days, review, promotion, appraisal, salary, resignation, layoffs, burnout, improvement plan, graduation |

Every lesson has key language, a pattern, real conversations, practice with answers, a "speak today"
task, and an AI role-play prompt. Learners can tick days as done (stored in their browser).

## Editing the course

- **Day order lives in one place:** `scripts/course.py`. To add, remove or reorder a lesson, edit the
  `PHASES` list and run:

  ```bash
  python scripts/course.py
  ```

  It regenerates the `nav:` block in `mkdocs.yml`, the roadmap (`docs/course/index.md`) and the phase
  pages (`docs/course/phase-N.md`). Day numbers, badges and the "Start Day N" prompts update automatically.

- **Conversations** are written as fenced `dialogue` blocks and rendered as chat bubbles by
  `hooks/course.py`. Lines are `Speaker: text`; `You:` appears on the right; `(text in brackets)` is a
  stage direction:

  ````markdown
  ```dialogue
  Clerk: Good morning. How can I help you?
  You: I'd like a ticket to Pune, please.
  (The clerk checks the system.)
  ```
  ````

- The 3D styling lives in `docs/assets/css/3d.css` and `docs/assets/js/tilt.js`, and switches off for
  users who prefer reduced motion.
