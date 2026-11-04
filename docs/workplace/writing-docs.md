# Writing Docs & Proposals

<div class="ssp-banner" markdown>
**Today's goal:** write design docs, proposals and READMEs that busy people actually read, so you can
get decisions made and influence without being in every meeting.
</div>

## Why writing matters for engineers

Senior engineers influence through **writing**. A clear one-page proposal reaches more people than any
meeting. It's also how remote and global teams make decisions.

## The one-page proposal

<div class="ssp-stack">
<div>1. Summary (TL;DR) <span>— the problem, your recommendation and the ask, in 3 lines</span></div>
<div>2. Problem <span>— what's wrong today, with evidence (numbers, incidents, user pain)</span></div>
<div>3. Options <span>— 2–3 options with pros, cons, cost and risk</span></div>
<div>4. Recommendation <span>— which option, and why</span></div>
<div>5. Plan & ask <span>— timeline, people, the decision you need, and by when</span></div>
</div>

## Design doc template

```markdown
# Design: Delivery slot reservation

**Author:** Ashish · **Reviewers:** Meena, Arun · **Status:** Draft · **Decision by:** 20 Nov

## TL;DR
Customers lose slots during checkout because slots aren't reserved. We propose a 10-minute
reservation in Redis. Needs 2 engineers for 2 sprints.

## Context & problem
- 8% of checkouts fail with "slot no longer available" (dashboard link)
- Peak hours: up to 15%

## Goals / non-goals
- Goal: reserve a slot for 10 minutes once selected
- Non-goal: changing how slots are generated

## Options
| Option | Pros | Cons |
|---|---|---|
| A. DB row lock | Simple | Doesn't scale at peak |
| B. Redis reservation with TTL | Fast, auto-expires | New dependency to monitor |

## Recommendation
Option B, because…

## Risks & rollout
Feature flag, 10% of users first; rollback by disabling the flag.

## Open questions
- What happens if payment takes longer than 10 minutes?
```

## Writing tips

| Do | Avoid |
|---|---|
| Put the **summary first** | Building up to the point on page 3 |
| Use **headings, bullets, tables** | Long paragraphs |
| Show **evidence**: numbers, links, quotes | "Everyone knows this is slow" |
| Be explicit about **trade-offs** | Presenting only your favourite option |
| End with **open questions and a decision date** | Docs that never get decided |
| Write for **someone new** to the topic | Unexplained acronyms and internal jargon |

## Asking for and handling review comments

- "**Could you review** the slot-reservation doc by Thursday? **I'm mainly looking for feedback on** the
  Redis option and the rollout plan."
- Reply to comments: "**Good point**, I've added it to Risks." / "**I considered that**, but chose B
  because… What do you think?" / "**Let's discuss this one** in the review meeting."

## Conversation: getting a decision from a proposal

```dialogue
You: Thanks for joining. Did everyone get a chance to read the proposal?
Arun: Yes. I like option B, but I'm worried about Redis going down.
You: Good point. If Redis is down, we fall back to no reservation, which is how it works today. I've added that to the Risks section.
Meena: What's the cost?
You: Two engineers for two sprints, and about ₹6,000 a month for the Redis cluster.
Lead: And the expected impact?
You: We expect slot failures to drop from 8% to under 1%, which is roughly 1,500 more successful orders a week.
Lead: Sounds good. Any objections? … No? Then let's go with option B.
You: Great. I'll update the doc status to "Approved" and create the tickets today.
```

## Practice

Write the 3-line TL;DR for a change you'd like to make in your team: problem, recommendation, ask.

## Speak today

- [ ] Add a TL;DR to the top of one document you've written
- [ ] Ask one colleague for review with a specific question
