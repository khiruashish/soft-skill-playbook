# Talking to Your Manager

<div class="ssp-banner" markdown>
**Your manager's three wishes: no surprises, clear status, and problems that arrive with options.** Give
them those three things and they'll trust you.
</div>

## What your manager actually needs

| They need | So you should |
|---|---|
| Predictability | Share status before they ask |
| Early warning | Raise risks the moment you see them, not on deadline day |
| Options, not just problems | Bring 2 possible solutions with every problem |
| Something to tell *their* boss | Summarise in 1–2 sentences they can forward |
| To know you're growing | Talk about goals and ask for feedback |

## The 1:1 meeting

### A simple agenda (send it the day before)

```text
1:1 agenda — [Date]
1. Wins this week: shipped X, fixed Y
2. In progress / risks: Z is at risk because…
3. Need from you: decision on A / intro to team B
4. Growth: feedback on my design review?
```

!!! tip "The 1:1 belongs to you"
    Don't let it turn into another status meeting. Keep 10 minutes for **growth, feedback, and career**.

## Scripts for common situations

=== "Giving a status update"

    <div class="ssp-say" markdown>
    "Quick update on the payments API: **on track for Friday**. Endpoints are done, tests are 80% done.
    One risk: we're still waiting on the bank sandbox credentials. If they don't arrive by Wednesday,
    we slip a day. I've followed up with their team."
    </div>

=== "Asking for help"

    <div class="ssp-say" markdown>
    "I've been stuck on the Kafka consumer lag for about 4 hours. I've tried increasing partitions and
    tuning the batch size. **Could you suggest someone who's worked on this, or spare 15 minutes?**"
    </div>

    !!! note "The 2-hour rule (beginners)"
        Struggle alone for up to ~2 hours, then ask, with what you tried. Asking too late costs more
        than asking too early.

=== "Raising a risk / delay"

    <div class="ssp-say" markdown>
    "I want to flag a risk early. **The search feature may slip by about 1 week.** The OpenSearch
    mapping needs a reindex we didn't plan for. Two options:<br>
    **A)** Ship on time without fuzzy search, add it next sprint.<br>
    **B)** Keep full scope, ship next Friday.<br>
    I'd recommend A. Which would you prefer?"
    </div>

=== "Pushing back on a deadline"

    <div class="ssp-say" markdown>
    "I want to hit this date, so let me be realistic about it. With the current scope, my estimate is
    3 weeks, not 2. **To make 2 weeks, we could** drop the export feature, or add one more developer
    for the UI. What matters most for this release?"
    </div>

=== "Admitting a mistake"

    <div class="ssp-say" markdown>
    "I made a mistake: my migration yesterday dropped an index, and that's why the reports were slow.
    **I've already restored it** and reports are back to normal. To prevent it happening again, I'm
    adding a migration check to CI. Sorry for the trouble."
    </div>

=== "Asking for feedback"

    <div class="ssp-say" markdown>
    "I'm working on my communication. **What's one thing I could do differently in design reviews?**"
    </div>

=== "Asking for a promotion / raise"

    <div class="ssp-say" markdown>
    "I'd like to talk about my growth. Over the last year I led the checkout migration, cut deploy
    time by 80%, and mentored two new joiners. **I believe I'm working at the senior level, and I'd
    like to be considered for promotion this cycle.** What gaps do you see, and what would make the
    case clear?"
    </div>

    !!! tip
        Bring your **wins file** with numbers. Ask for the gaps in writing. Agree on a timeline.

=== "Disagreeing with a decision"

    <div class="ssp-say" markdown>
    "Can I share a concern before we commit? Building our own auth will take 6–8 weeks and gives us
    security risk. Keycloak gets us 90% of it in a week. **If you still prefer custom, I'll commit to
    it fully** — I just want to make sure we've weighed this."
    </div>

    This is **disagree and commit**: voice it once, clearly, then support the decision.

## Mistakes to avoid

- :x: Hiding bad news until the deadline
- :x: "It's almost done" for 3 weeks running (give percentages or remaining tasks instead)
- :x: Complaining about teammates without a suggestion
- :x: Treating every 1:1 as a status report
- :x: Waiting for your manager to bring up your career

## Beginner vs experienced

=== "Beginner"

    - Over-communicate status. Silence makes people worry.
    - Write down what your manager asks so you don't have to ask twice.
    - Before a 1:1, prepare: *1 win, 1 blocker, 1 question.*

=== "Experienced"

    - **Manage up:** learn your manager's goals and pressures, and help them succeed.
    - Bring proposals, not just problems: "I'd like to own the reliability roadmap."
    - Give your manager feedback too: "It would help me if decisions came with the 'why'."
