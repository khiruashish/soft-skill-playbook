# Explaining an Issue

<div class="ssp-banner" markdown>
**A well-explained problem is half-solved.** Use these templates for bug reports, incidents, root-cause
analysis, and explaining tech to people who aren't technical.
</div>

## The universal structure

<div class="ssp-stack">
<div>1. What's happening <span>— the symptom, in one line</span></div>
<div>2. Who/what is affected <span>— users, revenue, systems, scale</span></div>
<div>3. Since when <span>— start time, trigger if known</span></div>
<div>4. What we know / don't know <span>— facts vs hypotheses</span></div>
<div>5. What we're doing <span>— actions + owners</span></div>
<div>6. What's needed + next update <span>— your ask and when you'll report back</span></div>
</div>

## Templates

=== "Bug report (to a developer)"

    ```markdown
    **Title:** Cart total ignores coupon when quantity > 10

    **Steps to reproduce**
    1. Add 11 units of any item
    2. Apply coupon SAVE10
    3. Go to checkout

    **Expected:** Total reduced by 10%
    **Actual:** Total unchanged; coupon shows "applied"
    **Environment:** staging, build 2026.11.03, Chrome 131
    **Evidence:** screenshot + request ID `req-8f2a…`
    **Impact:** bulk buyers (≈4% of orders) overpay
    **Suspected area:** `PricingService.applyCoupon()` — quantity cap at 10?
    ```

=== "Incident update (Slack / status)"

    ```text
    🔴 INCIDENT — Checkout errors (SEV-2)
    Status: Investigating | Started: 19:10 IST | Next update: 19:40
    Impact: ~8% of checkout attempts failing with payment timeout
    Known: began after 19:00 payment-SDK deploy
    Doing: rolling back SDK (owner: Ravi), monitoring error rate (owner: Meena)
    Need: nothing yet
    ```

    Then keep updating on schedule, **even if there's no news**: "No change. Rollback 60% complete.
    Next update 20:00."

=== "Root-cause summary (post-mortem)"

    ```markdown
    ## Summary
    Checkout failed for 40 min (19:10–19:50) — ~1,200 orders affected.

    ## Timeline
    19:00 deploy · 19:10 alerts · 19:18 incident declared · 19:35 rollback · 19:50 recovered

    ## Root cause
    New SDK default timeout (2 s) was lower than our bank's p95 (2.6 s) under load.

    ## What went well / what didn't
    + Alerting fired within 2 min
    − Deploy happened at peak time; no canary

    ## Action items
    | Action | Owner | Due |
    |---|---|---|
    | Canary deploys for payment service | Ravi | 15 Nov |
    | Block peak-hour deploys in CI | Meena | 10 Nov |
    ```

    !!! tip "Blameless language"
        Write "The deploy pipeline allowed a peak-hour release", not "Ravi deployed at peak time".
        Fix the system, not the person.

=== "SBAR (spoken, to a manager)"

    <div class="ssp-say" markdown>
    **Situation:** "Order emails aren't being sent."<br>
    **Background:** "Since 10 am, after the email provider rotated our API key."<br>
    **Assessment:** "About 3,000 customers haven't got confirmations. No orders are lost."<br>
    **Recommendation:** "I've requested a new key; ETA 30 min. Meanwhile, should support post a
    banner?"
    </div>

## Explaining tech to non-tech people

Use **one analogy + one number + one action**.

| Concept | Analogy |
|---|---|
| Cache | "A sticky note on your desk, so you don't walk to the filing cabinet every time." |
| Database index | "The index at the back of a book. Without it, you read every page." |
| Load balancer | "A restaurant host seating guests across all the waiters, not just one." |
| Message queue (Kafka) | "A post office. Senders drop letters; receivers collect them at their own pace." |
| Tech debt | "Skipping car servicing. Fine for a while, then a big expensive breakdown." |
| Microservices | "Separate shops in a mall instead of one giant store. One can close for repairs without shutting the mall." |
| API | "A waiter: you order from the menu; you don't walk into the kitchen." |
| Encryption | "A locked box only the receiver has the key to." |
| Race condition | "Two people booking the last train seat at the same second." |

!!! example "Putting it together"
    "The site was slow because our **'sticky note' (cache)** got wiped during the update, so every
    page went to the **'filing cabinet' (database)**. Pages took 6 seconds instead of 1. We've
    refilled it, and we're adding a check so updates don't wipe it again."

## Mistakes when explaining issues

- ❌ "It's broken" (what is? for whom? since when?)
- ❌ Mixing guesses with facts. Say "We **know**…" and "We **suspect**…"
- ❌ Going silent during an incident. Silence feels worse than bad news.
- ❌ Blaming a person or team in public
- ❌ Too much detail for the audience (see [altitude rule](../foundations/communication-principles.md#2-know-your-audience-the-altitude-rule))

## Practice conversation: Explaining an outage to a non-tech manager

```dialogue
Manager: Customers say the app was slow this morning. What happened?
You: Between 9 and 9:40, pages took six seconds to load instead of one. About 15% of users were affected.
Manager: Why?
You: Our cache, which is like a sticky note so we don't go to the filing cabinet every time, was cleared during an update.
Manager: Is it fixed?
You: Yes. We refilled the cache at 9:40, and everything is normal now.
Manager: Will it happen again?
You: We're adding a check so updates can't clear the cache. It'll be done by Friday.
```
