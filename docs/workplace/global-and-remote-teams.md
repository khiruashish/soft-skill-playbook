# Global & Remote Teams

<div class="ssp-banner" markdown>
**When your team spans time zones and cultures, writing well matters more than talking well.** Be
explicit, write things down, be clear about time zones, and don't assume others share your context.
</div>

## Principles

<div class="grid cards" markdown>

-   :material-text-box-check:{ .lg .middle } __Write it down__

    ---

    Decisions, context and next steps go in writing. Remote teams run on docs, not hallway chats.

-   :material-clock-outline:{ .lg .middle } __Respect time zones__

    ---

    Always state time zones. Rotate meeting times so the same people aren't always up late.

-   :material-message-alert:{ .lg .middle } __Over-communicate__

    ---

    No one can see you working. Post progress, blockers and status changes.

-   :material-earth:{ .lg .middle } __Explicit > implicit__

    ---

    Say "Yes, I'll do it by Thursday" rather than "I'll try". Avoid idioms and local slang.

</div>

## Cultural communication styles

| Style | Some cultures tend to… | Tips |
|---|---|---|
| **Direct vs indirect** | US / Netherlands / Germany: direct "No, that won't work" · India / Japan: softer "That may be difficult" | Learn to read both. If unsure, ask: "Just to confirm, is that a no?" |
| **Yes means…** | In India, "yes" can mean "I heard you", not "I agree / I can" | Say what you mean: "Yes, done by Friday" or "I can't commit to Friday; Monday is realistic." |
| **Hierarchy** | Some teams expect juniors to wait to be asked; others expect everyone to challenge | In global teams, speaking up and disagreeing politely is expected, including with seniors |
| **Small talk** | US: short, friendly · Europe: varies · India: personal questions are normal | Avoid salary, age, marriage questions with global colleagues |
| **Time** | Some cultures treat meeting start times as exact | Join on time; 2 minutes late is late |

!!! tip "The 'yes' trap"
    When a client asks "Can you deliver by Friday?" and the honest answer is "probably not", saying
    "yes" to be polite causes a much bigger problem on Friday. A **clear "no, but…"** builds more
    trust: *"Friday is too tight for full testing. Tuesday is realistic. Or we ship on Friday
    without the export feature."*

## Async communication

=== "Good async message"

    ```text
    Context: Cart API p95 jumped to 1.2 s after yesterday's deploy (graph attached).
    What I found: new N+1 query in getCartItems() — PR #251 fixes it.
    Need from you: review PR #251 by your EOD (Thu, 6 pm CET).
    If no reply: I'll merge with Meena's review at 10:00 IST Fri.
    ```

    **Context → finding → ask → deadline (with time zone) → default action.**

=== "Handoff across time zones"

    ```text
    🌅 End-of-day handoff (IST → US team)
    Done: payment retries merged & deployed to staging
    In progress: refund webhook — 70%, branch feat/refund-webhook
    Blocked: need Stripe test keys — @Mike can you share?
    Watch out: staging DB restarts at 02:00 UTC (maintenance)
    ```

=== "Recording instead of meeting"

    For demos and walkthroughs, record a **5-minute Loom-style video** plus a written summary.
    It saves a meeting at 10 pm for someone.

## Meetings across time zones

- Always write times with **zone**: "**Thu 4:30 pm IST / 12 pm CET / 6 am ET**"
- Prefer the **overlap window**; **rotate** inconvenient slots
- Share an **agenda and doc beforehand** so non-native speakers can prepare
- **Summarise in writing** afterwards; not everyone catches everything on a call
- Speak **slowly and clearly**; avoid idioms ("ballpark", "touch base", "low-hanging fruit") with
  mixed audiences, or explain them

## Accents and understanding each other

| Situation | Say |
|---|---|
| You didn't catch something | "Sorry, the audio cut out for me. Could you repeat the last part?" |
| Still didn't get it | "Could you type that in the chat? I want to get it exactly right." |
| Confirm understanding | "So you need the API by Tuesday your time, correct?" |
| They didn't understand you | Rephrase with simpler words, don't just repeat louder |
| Speaking fast from nerves | Slow down; pause between points; use the chat for numbers/names |

## Common Indian-English phrases in global teams

| Phrase | Global colleagues may hear | Use instead |
|---|---|---|
| "Do the needful" | Unclear request | "Could you please approve the PR?" |
| "I have a doubt" | "I disagree / don't believe it" | "I have a question" |
| "Revert back" | "Undo a change" | "Reply" / "Get back to me" |
| "Prepone" | Unknown word | "Move earlier" |
| "Kindly adjust" | Confusing | "Could you please…" |
| "Out of station" | Unclear | "Travelling" / "Out of town" |
| "Today itself" | Unusual phrasing | "Today" / "By end of today" |

See the full list in the [Phrase Bank](../reference/phrase-bank.md#upgrade-your-vocabulary).

## Practice conversation: Confirming across time zones

```dialogue
Mike: Can you get the fix in before our morning?
You: Just to confirm, your morning is 9 am Eastern time, which is 7:30 pm here in India. Is that right?
Mike: Yes, exactly.
You: Then yes, I'll have it merged by 6 pm IST, so it's on staging before you start.
Mike: Great. And if something goes wrong?
You: I'll post an update in the channel by 6:30 pm IST either way, with the status and next steps.
Mike: Perfect, thanks.
```
