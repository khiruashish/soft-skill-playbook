# Communication Principles

<div class="ssp-banner" markdown>
**Communication is not what you say. It's what the other person understands.** Seven rules, then
frameworks you can reuse anywhere.
</div>

## The communication stack

Each layer depends on the one under it. Hover a layer to bring it forward.

<div class="ssp-stack">
<div>6. Trust <span>— built when layers 1–5 stay consistent over time</span></div>
<div>5. Confidence <span>— steady voice, no over-apology, ownership</span></div>
<div>4. Tone <span>— polite, firm, warm, matched to the moment</span></div>
<div>3. Structure <span>— point first, then reasons, then the ask</span></div>
<div>2. Clarity <span>— simple words, one idea per sentence</span></div>
<div>1. Listening <span>— understand before you try to be understood</span></div>
</div>

## The 7 rules

### 1. Lead with the point (BLUF: Bottom Line Up Front)

Developers often tell the story in order: *"So I was looking at the logs, and then I noticed..."*. Busy
listeners stop paying attention before the point arrives.

| ❌ Story first | ✅ Point first |
|---|---|
| "So yesterday I was debugging and I found the cache wasn't… and then I checked the config and…" | "**The release is blocked by a cache bug. I need 1 more day.** Here's what happened…" |

### 2. Know your audience: the altitude rule

Pitch the same issue at a different height for each listener:

| Audience | Cares about | Talk about |
|---|---|---|
| CEO / Exec | Revenue, customers, risk, reputation | Impact, decision needed, timeline |
| Manager | Delivery, team health, surprises | Status, risks, options, what you need |
| Peer engineer | How it works, trade-offs | Design, code, data |
| Junior | Learning, doing it right, not looking silly | Steps, reasons, encouragement |
| Customer / stranger | Their problem solved | Plain language, next step |

### 3. One idea per sentence

Short sentences sound confident. Long sentences sound like you're still working out what you think.

### 4. Specific beats vague

- Vague: "It's kind of slow." → Specific: "**p95 latency went from 200 ms to 1.4 s** after Tuesday's deploy."
- Vague: "Soon." → Specific: "**By Thursday 5 pm.**"

### 5. Always end with an ask or a next step

Every message should answer *"what do you want from me?"*

> "…so **can you approve** the extra day?" · "…**I'll update you at 4 pm.**" · "…**no action needed**, FYI only."

### 6. Polite ≠ weak. Firm ≠ rude.

| Too weak | Balanced | Too harsh |
|---|---|---|
| "Sorry, I might be wrong, but maybe…" | "I see it differently. Here's why." | "That's wrong." |
| "If it's okay, could I possibly…" | "Could I take 10 minutes on this?" | "I need this now." |

### 7. Confirm understanding

Close important conversations with a recap:
*"Just to confirm: I'll fix the cache by Thursday, and you'll tell the product team. Right?"*

## Reusable frameworks

=== "PREP (give an opinion)"

    **P**oint → **R**eason → **E**xample → **P**oint again

    > "I recommend Postgres over Mongo **(P)**. Our data is relational: orders, items, payments
    > **(R)**. Last year's reporting rewrite took 3 months because of joins in Mongo **(E)**. So
    > Postgres is the safer choice **(P)**."

=== "SBAR (report an issue)"

    **S**ituation → **B**ackground → **A**ssessment → **R**ecommendation

    > "Checkout is failing for 8% of users **(S)**. It started after the 2 pm payment-SDK upgrade
    > **(B)**. I think the new SDK times out under load **(A)**. I recommend we roll back now and
    > investigate tomorrow **(R)**."

=== "STAR (tell a story / interview)"

    **S**ituation → **T**ask → **A**ction → **R**esult

    > "Our deploys took 2 hours **(S)**. I was asked to cut that down **(T)**. I parallelised the test
    > suite and added caching **(A)**. Deploys now take 18 minutes **(R)**."

=== "What / So what / Now what (status)"

    > **What:** API migration is 70% done.
    > **So what:** We're on track, but the auth piece is risky.
    > **Now what:** I'll pair with Priya on auth tomorrow; update on Friday.

## Words to cut and words to use

| Cut (filler / weak) | Use instead |
|---|---|
| basically, actually, like, you know | *(silence, a short pause)* |
| "I think maybe we could…" | "I suggest we…" / "My recommendation is…" |
| "Sorry to bother you" | "Do you have 5 minutes for…?" |
| "Does that make sense?" | "What questions do you have?" |
| "I'll try" | "I will" / "I can't commit to that, but I can…" |
| "It's not my fault" | "Here's what happened and what I'm doing about it." |
| "No problem" (after thanks) | "Happy to help." |

## Practice conversation: Point first, with your manager

```dialogue
Manager: How's the payment integration going?
You: It'll be one day late: Thursday instead of Wednesday. The bank's sandbox was down for six hours yesterday.
Manager: Okay. Is anything else at risk?
You: No. The rest is on track, and the tests are done.
Manager: Do you need anything from me?
You: Yes, could you ask the bank for a backup sandbox? Then it won't happen again.
Manager: Sure, I'll email them today.
```
