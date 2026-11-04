# Client Meetings

<div class="ssp-banner" markdown>
**The client is buying confidence as much as software.** Prepare well, listen more than you talk, never
promise what you can't deliver, and always leave with clear next steps.
</div>

## The client meeting lifecycle

<div class="ssp-stack">
<div>1. Prepare <span>— goal, agenda, attendees, their context, your numbers</span></div>
<div>2. Open <span>— introductions, agenda, time check</span></div>
<div>3. Discover / Present <span>— ask questions, then show progress or solution</span></div>
<div>4. Handle concerns <span>— listen, acknowledge, answer, confirm</span></div>
<div>5. Close <span>— recap decisions, owners, dates</span></div>
<div>6. Follow up <span>— minutes within 24 hours</span></div>
</div>

## Before the meeting: checklist

- [ ] **Goal:** what must be decided or agreed by the end?
- [ ] **Agenda** sent at least a day in advance
- [ ] **Who's attending**, and their roles (LinkedIn check)
- [ ] **Internal alignment:** agree with your manager / account manager on who says what, and what we
      will *not* commit to
- [ ] **Demo tested** on the same network and device you'll use, plus a backup recording
- [ ] **Numbers ready:** progress %, timelines, open issues
- [ ] **Likely questions** and your answers (especially about delays and cost)

## Opening the meeting

<div class="ssp-say" markdown>
"Good morning, everyone, and thanks for your time. I'm Ashish, the tech lead for the mobile app.
**Today we'd like to cover three things:** sprint progress, a demo of the new checkout, and two
decisions we need from you on payment options. **We have 45 minutes. Does that agenda work for you?**"
</div>

## Discovery: understand what they need

| Question | Why |
|---|---|
| "What does success look like for you in 3 months?" | Learn their real goal |
| "What's the biggest pain point for your users today?" | Find priorities |
| "Who else needs to approve this?" | Know the decision-makers |
| "What happens if this launches a month later?" | Find out how firm the deadline is |
| "Are there any constraints we should know about: budget, compliance, systems?" | Avoid surprises |
| "How do you measure that today?" | Get a baseline |

!!! tip "Talk 30%, listen 70%"
    Take notes visibly. Repeat back key points: "So the must-have for launch is UPI and COD.
    Wallets can come later. Correct?"

## Scripts for tough moments

=== "Reporting a delay"

    <div class="ssp-say" markdown>
    "I want to be transparent with you. **The payment integration will be 1 week later than
    planned**: the 22nd instead of the 15th. The bank changed their API last week. **Everything
    else is on track.** To reduce the impact, we can release the rest of the app on the 15th
    with COD only. Would that work for you?"
    </div>

    Tell them early, explain the cause in one line, give a new date, and offer an option.

=== "Client asks for something out of scope"

    <div class="ssp-say" markdown>
    "That's a great idea, and I can see how it helps your sales team. **It's outside the current
    scope**, so I don't want to promise it without checking the impact. **I'll come back by
    Thursday with an estimate and options**: either adding it as a change request, or swapping it
    for something lower-priority."
    </div>

=== "You don't know the answer"

    <div class="ssp-say" markdown>
    "Good question. I don't want to give you a wrong answer, so **let me confirm with our security
    team and get back to you by tomorrow evening.**"
    </div>

=== "Client is unhappy / angry"

    <div class="ssp-say" markdown>
    "I understand, and I'm sorry this affected your customers during the weekend sale. **You're
    right to be concerned.** Here's what happened, what we've already fixed, and what we're
    changing so it doesn't happen again. **I'll personally send you a daily update until it's
    fully closed.**"
    </div>

    Don't argue, don't blame the client's team, don't get defensive. Acknowledge, take ownership,
    give a plan.

=== "Client pushes for an unrealistic deadline"

    <div class="ssp-say" markdown>
    "We want to hit that date as much as you do. **With the current scope, the earliest
    high-quality release is the 30th.** To launch on the 15th, **we could** go live with the core
    ordering flow and add loyalty points two weeks later. Which matters more for your launch:
    the date or the full feature set?"
    </div>

=== "Saying no to a technical demand"

    <div class="ssp-say" markdown>
    "I understand why storing card details looks simpler. **We'd recommend against it.** It would
    bring your app under full PCI-DSS compliance, which adds months and cost. **Tokenisation via the
    payment gateway gives you the same user experience with none of that risk.**"
    </div>

## Closing the meeting

<div class="ssp-say" markdown>
"Let me quickly recap. **Decisions:** we launch with UPI and COD; wallets in phase 2. **Actions:** we
share the updated timeline by Wednesday; your team sends the bank sandbox credentials by Friday.
**Next meeting:** Monday at 11. **Did I miss anything?**"
</div>

## Follow-up email (within 24 hours)

```text
Subject: Minutes — Sprint 6 review | Decisions & next steps

Hi Rohan,

Thanks for your time today. Summary below:

Decisions
• Launch with UPI + COD; wallets moved to phase 2

Action items
• [Us] Updated timeline — Ashish — Wed 6 Nov
• [You] Bank sandbox credentials — Rohan's team — Fri 8 Nov

Open questions
• Data-retention period for order history (awaiting your legal team)

Next meeting: Mon 11 Nov, 11:00 IST

Please let me know if I've missed anything.

Best regards,
Ashish
```

## Client etiquette

| :white_check_mark: Do | :x: Don't |
|---|---|
| Join 2–3 minutes early, camera on | Argue with your own team in front of the client |
| Use the client's terms ("orders", not "OrderAggregate") | Criticise the client's existing systems or vendors |
| Agree internally on who answers what | Commit to dates or features without checking |
| Write down every promise you make | Discuss internal problems or other clients |
| Say "we", not "they" (for your own company) | Use heavy jargon or acronyms without explaining them |

## Beginner vs experienced

=== "Beginner"

    - You may be there to **listen and take notes**. Do that brilliantly; it's valued.
    - Speak when asked about your area: short, factual, confident.
    - If unsure whether you can share something, say: "Let me check with Priya and confirm."

=== "Experienced"

    - **Pre-wire** the meeting: call the client's key person beforehand about anything sensitive.
    - Bring **options with trade-offs**, not just status.
    - Build the relationship beyond projects: ask about their goals, their pressures, their boss.
    - Protect your team from scope creep, politely and firmly.
