# Performance Review

<div class="ssp-banner" markdown>
**Your rating is mostly decided before the meeting.** It depends on what you did all year *and* how
well your manager knows about it. Track your wins, write a strong self-review, and treat the
conversation as planning for next year, not a verdict.
</div>

## The review cycle

<div class="ssp-stack">
<div>1. All year <span>— keep a wins file; align on goals; ask for feedback every quarter</span></div>
<div>2. Self-assessment <span>— write it with impact and numbers</span></div>
<div>3. Peer feedback <span>— choose reviewers wisely; write good reviews for others</span></div>
<div>4. Review meeting <span>— listen, clarify, discuss, agree on goals</span></div>
<div>5. After <span>— follow-up in writing; act on feedback; check in at 3 months</span></div>
</div>

## All year: the wins file

A simple note you update every Friday (5 minutes):

```text
## Nov 2026
- Shipped coupon validation → stopped ~₹40k/week leakage (PR #212)
- Led incident response for checkout outage; wrote post-mortem; 2 fixes shipped
- Mentored Kavya on Kafka; she now owns the consumer service
- Praise: "Clearest incident updates I've seen" — VP Eng, Slack, 12 Nov
```

!!! tip "No surprises, in either direction"
    Ask your manager every quarter: *"If reviews were today, where would I land, and what would
    move me up?"* That way, the review meeting doesn't surprise you.

## Writing your self-assessment

Use **Action → Impact → Evidence** for every point:

| ❌ Weak | ✅ Strong |
|---|---|
| "Worked on the checkout service." | "**Re-architected** checkout to use the outbox pattern, **cutting failed orders by 60%** (dashboard link)." |
| "Helped juniors." | "**Mentored 3 engineers** with weekly sessions; **2 now independently own services**." |
| "Fixed many bugs." | "**Closed 48 bugs**, including 5 P1s; **reduced support tickets by 30%**." |
| "Good team player." | "**Unblocked the payments team** twice by building a shared test harness, saving ~2 weeks." |

### Self-assessment template

```markdown
## Key achievements (3–5)
1. [Action] → [Impact with number] → [Evidence/link]

## Goals from last cycle
| Goal | Result | Status |
|---|---|---|
| Reduce p95 latency < 500 ms | 420 ms | ✅ Met |
| Lead one design review | Led 3 | ✅ Exceeded |
| Get AWS certification | Postponed (release crunch) | ⚠️ Moved to Q1 |

## Growth & learning
- What I learned, what I'd do differently

## Areas to improve
- One or two honest areas + what I'm already doing about them

## Goals for next cycle
- 2–4 specific, measurable goals, ideally tied to team goals

## Support I need
- e.g. more exposure to architecture decisions; conference budget
```

!!! warning "Common self-review mistakes"
    Listing tasks instead of impact · being too modest ("I just helped a bit") · being vague about
    misses · forgetting work from early in the year (that's what the wins file is for) · writing
    10 pages. Keep it to 1–2.

## Peer reviews

=== "Giving peer feedback"

    Be **specific, balanced and useful**:

    ```text
    Strengths: Meena's incident leadership during the October outage was outstanding.
    Clear updates every 20 minutes kept leadership calm, and the post-mortem led to
    real fixes.

    To grow: In design reviews she sometimes moves to a solution before the
    problem is fully discussed. Pausing to ask "what else could we do?" would bring
    in more ideas from the team.
    ```

=== "Choosing your reviewers"

    - People who **saw your best work** closely
    - At least one person **from another team** (shows cross-team impact)
    - Ask them nicely, with context: *"Would you be open to reviewing me? It'd help if you could
      mention the search migration we did together."*

## The review meeting

### Mindset

Go in calm and curious. Your goal is to **understand the feedback** and **agree on a plan**, not to
win an argument.

### Scripts

=== "Opening"

    <div class="ssp-say" markdown>
    "Thanks for taking the time. **I'd like to hear your feedback first**, and then I'd love to
    talk about goals and what the next level looks like for me."
    </div>

=== "Good review"

    <div class="ssp-say" markdown>
    "Thank you, that means a lot. **What would it take to get to the next level** over the next
    cycle? I'd like to make sure I'm working on the right things."
    </div>

    Even with a great rating, ask for **one thing to improve**.

=== "Asking for clarity"

    <div class="ssp-say" markdown>
    "You mentioned I need to 'show more ownership.' **Could you give me an example** where I could
    have done that differently? I want to make sure I understand what it looks like."
    </div>

=== "Disagreeing with the rating"

    <div class="ssp-say" markdown>
    "I appreciate the feedback. **I see some of it differently**, and I'd like to share why. I led
    the checkout migration end to end, which was one of the team's top goals, and it reduced
    failures by 60%. **Could you help me understand how that was weighed?**"
    </div>

    Then, if it still feels unfair:

    <div class="ssp-say" markdown>
    "I'd like some time to reflect on this. **Could we follow up later this week?** And what's the
    process if I'd like the rating reconsidered?"
    </div>

    !!! danger "Don't"
        Raise your voice · compare yourself to named colleagues ("But Rahul got…") · threaten to
        quit · cry foul in team channels. Stay factual and calm, and put things in writing.

=== "Unexpected negative feedback"

    1. **Pause and breathe.** You don't need to respond instantly.
    2. "Thank you for being direct. **This is hard to hear, but I want to understand.**"
    3. "**Can you share specific examples?**"
    4. "**What would 'good' look like** in the next 3 months?"
    5. "Can we **check in monthly** on this?"

=== "Asking about promotion"

    <div class="ssp-say" markdown>
    "I'd like to be considered for promotion to Staff Engineer. **What gaps do you see between my
    work and that level?** Could we write down 2–3 concrete goals and a timeline, and check
    progress quarterly?"
    </div>

=== "Asking about compensation"

    <div class="ssp-say" markdown>
    "How does this rating translate into my compensation? Given my impact this year and the market
    for my role, **I'd like to discuss whether there's room for an adjustment.**"
    </div>

    See [Salary Negotiation](salary-negotiation.md) for full scripts.

### Questions to ask in every review

- "What's the **one thing** that would most increase my impact next year?"
- "What do you see as my **biggest strength**, and am I using it enough?"
- "How do **others** (peers, stakeholders) see my work?"
- "What does the **next level** look like in practice?"
- "**How can you support me** in getting there?"

## After the review

- [ ] Send a short **summary email** within 24 hours (feedback, goals, agreed support)
- [ ] Turn feedback into **2–3 goals** with measurable outcomes
- [ ] Put a **3-month check-in** in the calendar
- [ ] Start next year's **wins file** today

```text
Subject: Summary of our performance review

Hi Priya, thanks for the review today. To summarise:
• Strengths: incident leadership, mentoring
• Focus areas: earlier risk communication, more design-doc writing
• Goals: lead 2 design docs; flag schedule risks within 2 days
• Next step: check-in on 15 Feb; promotion discussion in the next cycle
Let me know if I've missed anything.
```

## When you're the reviewer (team leads & managers)

<div class="grid cards" markdown>

-   :material-file-document-edit:{ .lg .middle } __Prepare__

    ---

    Gather evidence across the whole year, not just the last month. Read their self-review first.

-   :material-message-check:{ .lg .middle } __No surprises__

    ---

    Nothing in the review should be news. Hard feedback belongs in regular 1:1s.

-   :material-scale-balance:{ .lg .middle } __Specific & fair__

    ---

    Use SBI (Situation-Behaviour-Impact). Judge outcomes and behaviour, not personality.

-   :material-arrow-up-bold-circle:{ .lg .middle } __Forward-looking__

    ---

    Spend half the time on growth and next-cycle goals.

</div>

<div class="ssp-say" markdown>
"Your rating this cycle is **Meets Expectations**. **Strength:** your code quality and reliability
work, especially the retry framework. **To grow to the next level:** I'd like to see you drive
decisions in design reviews, not just contribute. **Let's set one goal around that** and check in
every month. What support would help?"
</div>
