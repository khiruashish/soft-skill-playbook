# Difficult Conversations

<div class="ssp-banner" markdown>
**The conversation you're avoiding is usually the one you most need to have.** Stay calm, be specific,
focus on the issue and not the person, and look for what both of you want.
</div>

## The 5-step model

<div class="ssp-stack">
<div>1. Prepare <span>— facts, your goal, their likely view</span></div>
<div>2. Open safely <span>— "I'd like to talk about X. I want us both to come out of this better."</span></div>
<div>3. Share facts, then feelings <span>— "When X happened, I felt Y"</span></div>
<div>4. Listen & understand <span>— "Help me understand your side."</span></div>
<div>5. Agree on next steps <span>— specific, written, with owners</span></div>
</div>

## Scripts

=== "Saying no"

    <div class="ssp-say" markdown>
    "I can't take this on this sprint without dropping the payments work. **Which should come first?**"
    </div>

    Other ways to say no:

    - "Not right now, but I can look at it on Monday."
    - "I'm not the best person for this. Priya knows that system better."
    - "I can do part of it: the API, but not the UI."

=== "Disagreeing with a senior"

    <div class="ssp-say" markdown>
    "I respect your experience here, so I want to share a different view. **I'm worried that** skipping
    integration tests will push bugs into production during the sale. **Could we** keep tests for the
    checkout path only? It adds half a day."
    </div>

=== "Conflict with a peer"

    <div class="ssp-say" markdown>
    "Can we talk about the last few code reviews? **I've noticed** my PRs sit for 3–4 days, and some
    comments felt quite harsh. **I might be misreading it.** How do you see it? I'd like us to work
    better together."
    </div>

=== "Receiving criticism"

    1. **Breathe.** Don't reply instantly.
    2. **Thank them:** "Thanks for telling me directly."
    3. **Clarify:** "Can you give me an example?"
    4. **Own what's true:** "You're right, I missed that."
    5. **Commit:** "Next time I'll…"

    !!! warning "Avoid"
        "Yes, but…", "That's not fair", or bringing up their mistakes. Even if they're partly wrong,
        **understand first, respond later** (you can follow up the next day).

=== "Someone takes credit for your work"

    <div class="ssp-say" markdown>
    (Privately) "In the demo, the caching work was presented as yours. I built most of it. **I'd
    appreciate it if we credit each other accurately going forward.** Can we agree on that?"
    </div>

    (Publicly, at the next chance) "As I mentioned when I built the cache layer…"

=== "An angry stakeholder"

    <div class="ssp-say" markdown>
    "I understand you're frustrated. This outage hurt your customers. **Here's what we know, what
    we're doing, and when you'll hear from me next.**"
    </div>

    Acknowledge the emotion → give facts → commit to the next update. Don't argue about blame.

## Phrases that calm things down

| Instead of | Say |
|---|---|
| "You're wrong." | "I see it differently." |
| "You always…" | "In the last two sprints, I noticed…" |
| "That's not my job." | "I can't own that, but let me connect you with someone who can." |
| "Calm down." | "I can see this matters a lot. Let's figure it out." |
| "Whatever, fine." | "I'm not fully convinced, but I'll commit to it. Let's review in 2 weeks." |

## Practice conversation: Disagreeing with a senior colleague

```dialogue
Senior: Let's skip the integration tests this sprint. We don't have time.
You: I see why. Can I share a concern?
Senior: Go ahead.
You: The sale is next week. Without integration tests on checkout, we could push a bug that costs us orders.
Senior: But the tests take two days.
You: What if we only test the checkout path? That takes half a day.
Senior: Okay, that's a fair compromise. Let's do checkout only.
You: Thanks. I'll set it up today.
```
