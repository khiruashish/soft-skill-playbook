# Promotion Discussion

<div class="ssp-banner" markdown>
**Promotions are rarely given for doing your current job well. They come from showing you already work
at the next level, and from making sure the people who decide can see it.** Ask early, agree on
criteria, gather evidence, and get your manager to argue your case for you.
</div>

!!! info "How this differs from related pages"
    [Performance Review](performance-review.md) covers your rating · [Appraisal Discussion](appraisal-discussion.md)
    covers the hike · this page covers **moving up a level**: the months-long conversation that leads to
    it, and what to do when the answer is "not yet".

## How promotions actually work

<div class="ssp-stack">
<div>1. Criteria <span>— the company's level definitions (career ladder)</span></div>
<div>2. Evidence <span>— sustained work at the next level, usually 6–12 months</span></div>
<div>3. Sponsor <span>— your manager (and ideally a skip-level) who argues your case</span></div>
<div>4. Committee / calibration <span>— managers compare cases; often you're not in the room</span></div>
<div>5. Budget & timing <span>— cycles, headcount, open roles</span></div>
</div>

The key insight: **you're not in the room when the decision is made.** Your job is to give your
manager a case so clear they can argue it in two minutes.

## What typically changes between levels

| From → To | The shift | Evidence that shows it |
|---|---|---|
| Junior → Mid | From "needs guidance" to "works independently" | Delivers features end to end with little help |
| Mid → Senior | From "delivers tasks" to "owns outcomes" | Owns a service/feature area; makes good design calls; mentors |
| Senior → Staff / Lead | From "owns a component" to "shapes the team or several teams" | Drives cross-team technical direction; multiplies others; solves ambiguous problems |
| Engineer → Manager | From "my output" to "the team's output" | Has led people informally; handles conflict; hires; gives feedback well |

!!! tip "Get your company's ladder"
    Ask your manager or HR for the written **level expectations**. If there are none, write down
    together what the next level means at your company. Without written criteria, the decision
    becomes subjective.

## The promotion conversation, step by step

=== "1. Starting the conversation (6–12 months before)"

    <div class="ssp-say" markdown>
    "I'd like to work towards **Senior Engineer**. **Could you help me understand what the gap is**
    between where I am now and that level? I'd like to agree on 2–3 concrete things I can work on,
    and check in on them regularly."
    </div>

    Ask this **early**, not two weeks before the promotion cycle.

=== "2. Agreeing on criteria"

    <div class="ssp-say" markdown>
    "So, to summarise: **lead the design and delivery of the delivery-slot service, mentor at least
    one engineer, and lead incident response independently.** If I do those well by June, would
    that make a strong case? **Can I write this down and share it with you?**"
    </div>

    Then send a short email so you both have a written record.

=== "3. Regular check-ins"

    <div class="ssp-say" markdown>
    "Quick promotion check-in: **I've completed the slot-service design and it's in production.
    Mentoring with Kavya is going well.** On a scale of 1–10, how close am I to the case we
    discussed? What's missing?"
    </div>

    Do this monthly or quarterly in your 1:1.

=== "4. Ask for a sponsor"

    <div class="ssp-say" markdown>
    "Would you be willing to **put me forward in this cycle**? I've drafted a promotion document with
    the evidence. Could you review it and tell me what would make it stronger?"
    </div>

    Also ask for **visibility**: "Could I present the slot-service design at the architecture
    review?" Committee members should know your work before your name comes up.

=== "5. Asking directly at cycle time"

    <div class="ssp-say" markdown>
    "The promotion cycle opens next month. **I believe I'm working at the senior level, and I'd like
    to be considered.** Here's my summary of the evidence against the criteria we agreed on. Do you
    agree, and are you comfortable nominating me?"
    </div>

## The promotion document (brag doc)

Make your manager's job easy: one page, mapped to the criteria.

```markdown
# Promotion case — Ashish Gupta → Senior Engineer

## Summary (3 lines)
Has operated at senior level for ~9 months: owns the delivery-slot service end to end,
leads incidents, and mentors two engineers.

## Evidence against criteria
| Criterion | Evidence |
|---|---|
| Technical ownership | Designed & shipped slot service (design doc link); 99.95% uptime since launch |
| Scope & impact | Enabled 3 new cities; reduced failed deliveries 18% |
| Influence | Led 3 design reviews; proposal adopted by payments team |
| Mentoring | Mentored Kavya & Arun; Kavya now owns consumer service |
| Operational excellence | Incident lead for 4 SEV-2s; post-mortems with 9 follow-ups shipped |

## Feedback from others
- "Ashish's design review raised the bar for the whole team." — Staff Engineer, Platform
- "Best incident communication I've seen." — VP Engineering

## Areas still growing
- Cross-org influence: starting with the 2027 architecture working group
```

## When the answer is "not yet"

=== "Get specifics"

    <div class="ssp-say" markdown>
    "I'm disappointed, but I want to use this well. **What specifically was missing in my case?**
    Was it the evidence, the criteria, or timing and budget?"
    </div>

    Those are three different problems:

    | Reason | What it means | Your move |
    |---|---|---|
    | **Evidence gap** | You aren't yet doing the next-level work | Agree on concrete projects that close the gap |
    | **Visibility gap** | You did it, but the deciders didn't see it | Present work, write docs, get skip-level exposure |
    | **Budget / timing** | Case is fine, there's no slot | Get the commitment in writing for the next cycle |

=== "Get a commitment"

    <div class="ssp-say" markdown>
    "**If I close those gaps, can we agree I'll be put forward next cycle?** I'd like to write down
    the specific goals and review them every month together."
    </div>

=== "Repeated \"not yet\""

    <div class="ssp-say" markdown>
    "This is the second cycle where the goals were met but the promotion didn't happen. **I want to
    grow here, and I'd like to understand honestly whether a promotion is realistic in the next
    6 months.** If not, I'd appreciate knowing why."
    </div>

    Ask honestly and calmly. If the honest answer is "no", you have a decision to make: see
    [Resignation](resignation.md), and leave well if that's your choice.

!!! danger "Don't"
    - Compare yourself to named colleagues ("Rahul got promoted, why not me?")
    - Use a resignation threat as a lever, unless you're truly ready to leave
    - Go silent and resentful; ask for specifics instead
    - Expect a promotion for **tenure** alone ("I've been here 4 years")

## After you're promoted

- **Thank** your manager and sponsors, and the people who helped.
- **Ask:** "What does great look like at this new level, in the first 6 months?"
- Expect to feel **out of your depth** at first. That's normal; it's what growth feels like.
- **Help someone else** get their promotion. Sponsoring others is part of being senior.

## For leads: sponsoring your people

- Have the **career conversation** with every report at least twice a year.
- Turn the level definitions into **concrete, personal goals**.
- **Create opportunities**: give stretch projects and visibility, and mention their names in rooms
  they're not in.
- Be **honest** about the gap and about timing. False hope damages trust more than "not yet".
- Write the case **together**, and tell them the outcome **personally** before any announcement.
