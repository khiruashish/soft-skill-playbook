# Talking to the CEO & Executives

<div class="ssp-banner" markdown>
**Executives have 30 seconds of attention for your topic and 100 other problems waiting.** Lead with the
answer, translate tech into business, and make the decision easy for them.
</div>

## What executives care about

<div class="grid cards" markdown>

-   :material-currency-inr:{ .lg .middle } __Money__

    ---

    Revenue, cost, ROI. "This saves ₹12 lakh a year in cloud spend."

-   :material-account-heart:{ .lg .middle } __Customers__

    ---

    Experience, churn, NPS. "Checkout failures dropped 60%."

-   :material-shield-alert:{ .lg .middle } __Risk__

    ---

    Security, compliance, outages, reputation.

-   :material-rocket-launch:{ .lg .middle } __Speed__

    ---

    Time-to-market, competitive edge.

</div>

## The executive formula

<div class="ssp-stack">
<div>1. Headline <span>— the answer or the ask in one sentence</span></div>
<div>2. Impact <span>— money, customers, risk, in numbers</span></div>
<div>3. Options <span>— 2 or 3, with your recommendation</span></div>
<div>4. Ask <span>— the exact decision you need, and by when</span></div>
</div>

## Translate tech into business

| Engineer says | CEO hears | Say instead |
|---|---|---|
| "We need to refactor the monolith." | "Engineers want to play with code." | "Every new feature takes 3 weeks instead of 1. Splitting the system doubles our release speed." |
| "We have tech debt." | "Vague complaint." | "Fixing 3 fragile areas cuts outages by about half, and each outage costs us ~₹4 lakh." |
| "p99 latency is 3 seconds." | "?" | "1 in 100 customers waits 3 seconds at checkout, and 20% of those abandon." |
| "We need Kubernetes." | "Expensive buzzword." | "We can handle sale-day traffic without manual work, and stop over-paying for idle servers." |
| "The DB is a single point of failure." | "?" | "If one server dies, the whole site is down for hours. A backup costs ₹30k/month." |

## Scripts

=== "30-second elevator update"

    <div class="ssp-say" markdown>
    "**The new delivery-tracking feature launches Monday.** Early tests show 25% fewer 'where is my
    order' calls. One risk: map API costs may rise 15%, and we have a fallback ready. **No decision
    needed today.**"
    </div>

=== "Explaining an outage"

    <div class="ssp-say" markdown>
    "**Yesterday, checkout was down for 40 minutes, from 7:10 to 7:50 pm.** About 1,200 orders
    failed, roughly ₹9 lakh in sales. Cause: a database update ran during peak hours. We've
    recovered, and 70% of affected customers have already re-ordered after our coupon email.
    **To prevent repeats**, all DB changes now go through an automated check and run only off-peak.
    **I'd like approval for 2 sprints of reliability work.** Can I count on that?"
    </div>

=== "Asking for budget / headcount"

    <div class="ssp-say" markdown>
    "**I'm asking for 2 more backend engineers for Q1.** Right now the team spends 40% of its time on
    support tickets, so the loyalty program slips to Q3. With 2 hires, it ships in Q2, which product
    estimates adds ₹1.5 crore in annual repeat revenue. Cost is about ₹60 lakh a year. **Can we
    approve this by the 15th** so we can start hiring?"
    </div>

=== "Answering \"Why is this late?\""

    <div class="ssp-say" markdown>
    "**It's 2 weeks late because the payment partner changed their API mid-project.** We've finished
    the rework, and the new date is the 22nd, with high confidence. Going forward, we're adding
    partner-change checks to our planning."
    </div>

    No blame, no long story. Cause, new date, and the fix for next time.

=== "When you don't know the answer"

    <div class="ssp-say" markdown>
    "**I don't have that number right now. I'll get it to you by 3 pm today.**"
    </div>

    Never guess numbers in front of executives.

## Before you walk in: checklist

- [ ] Can I say my main point in **one sentence**?
- [ ] Do I have **numbers** (₹, %, users, hours)?
- [ ] Do I have **2–3 options** and a recommendation?
- [ ] Do I know the **exact decision** I'm asking for?
- [ ] Have I **pre-wired** it with my manager and other key people?
- [ ] Is there a **1-page summary** I can leave behind?
- [ ] Have I prepared answers for **"What if we do nothing?"** and **"What's the risk?"**

## Mistakes to avoid

- :x: Starting with background ("So, in 2023 we chose MongoDB because…")
- :x: Jargon without translation
- :x: Showing 30 slides when 3 will do
- :x: Surprising your manager by going over their head
- :x: Getting defensive when interrupted. Interruptions are normal. Answer and move on.

## For experienced engineers

- Learn the company's top **3 goals this year** and tie every proposal to one of them.
- Say less. **"Yes, it's on track"** is a complete answer if that's what was asked.
- Build relationships *before* you need them: a coffee chat with a VP is worth more than a slide deck.
- Bring the **"so what"** for the business, not just the technical "what".
