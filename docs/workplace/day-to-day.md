# Day-to-Day Communication

<div class="ssp-banner" markdown>
**People judge you on the small things you do every day: the stand-up, the Slack reply, the PR
description.** These habits build your reputation faster than one big presentation.
</div>

## Daily stand-up

=== "Format"

    ```text
    Yesterday: finished the coupon API, PR #212 in review
    Today:     integrate with cart, write tests
    Blockers:  need staging DB access — @Ops, can you help after stand-up?
    ```

    **Rules:** 30–60 seconds. Outcomes, not activities. Take blockers offline.

=== "❌ Weak vs ✅ strong"

    | ❌ Weak | ✅ Strong |
    |---|---|
    | "Yesterday I was working on the bug, still working on it." | "The login bug is narrowed to the token refresh. Fix by noon today." |
    | "No blockers." (when you're stuck) | "I'm stuck on the PDF library. 10 minutes with anyone who's used it?" |
    | 5-minute technical deep-dive | "Found an interesting caching issue. I'll share in #backend." |

## Slack / Teams messages

### Golden rules

1. **Don't just say "Hi".** Write the whole question in one message.
2. **Point first, details after.**
3. **Use threads.** Don't flood the channel.
4. **Say how urgent it is:** "FYI", "When you get a chance", or "Urgent: blocking the release".
5. **Close the loop:** "Resolved, thanks!" so nobody else spends time on it.

| ❌ Instead of | ✅ Write |
|---|---|
| "Hi" … (waits 10 min) … "are you there?" | "Hi Ravi, quick one: is the `orders` topic partitioned by customerId or orderId? Writing a consumer and want to keep ordering." |
| "The build is broken" | "Main build failing since 11:20 on `InventoryIT`, looks like a Testcontainers timeout. Looking into it; will update here." |
| "Can we talk?" | "Can we talk for 10 min today about the sprint scope? Nothing urgent, just want to align." |

## Email

```text
Subject: [Decision needed by Fri] Choose payment provider for Q1

Hi Priya,

Recommendation: go with Razorpay. Cheaper fees (1.8% vs 2.2%) and the SDK we need.

Options compared: (table / link)
Risk: migration takes ~2 weeks; I've planned it for early Dec.

Could you confirm by Friday so we can start the integration?

Thanks,
Ashish
```

**Tips:** the subject line says what you need · the first line gives the answer · under 150 words ·
one ask · a clear deadline.

## Pull request descriptions

```markdown
## What
Adds coupon validation to the checkout flow.

## Why
Expired coupons were being accepted (bug #341), costing ~₹40k/week.

## How
- New `CouponValidator` domain service
- Checks expiry + usage limits before pricing

## Testing
- Unit tests for 6 edge cases
- Manual test on staging with expired coupon ✅

## Risks / Notes for reviewers
Touches the pricing path. Please look closely at `applyDiscount()`.
```

## Estimates

- Give **ranges**, not single numbers: "3 to 5 days".
- Say what the estimate **assumes**: "…assuming the API contract doesn't change."
- Re-estimate **out loud** when things change: "New info. It's now 7 days, here's why."
- "**I don't know yet. I'll spike for half a day and give you an estimate tomorrow**" is a good answer.

## Useful everyday phrases

| Situation | Say |
|---|---|
| You didn't understand | "Sorry, could you say that again? I want to make sure I get it right." |
| Buying time | "Good question. Let me check and get back to you by 3." |
| Polite reminder | "Gentle nudge on this. Any update?" |
| Saying you're busy | "I'm heads-down on the release till 4. Can I look after that?" |
| Agreeing | "Makes sense, let's go with that." |
| Partially agreeing | "I agree with the approach. One concern about the timeline…" |
| Ending a long call | "I think we've covered it. I'll send a summary in 10 minutes." |
| Taking ownership | "I'll own this. Expect an update by end of day." |

## End-of-day / weekly update (to manager)

```text
Week of 3 Nov
✅ Done: coupon validation (shipped), fixed 3 cart bugs
🔄 In progress: delivery-slot API (60%), on track for Weds
⚠️ Risk: map vendor API key still pending
🙋 Need: decision on slot-caching TTL (5 vs 15 min)
```

## Practice conversation: Stand-up update

```dialogue
Lead: Ashish, your update?
You: Yesterday I finished the coupon validation API, and the PR is in review. Today I'll connect it to the cart.
Lead: Any blockers?
You: One. I need access to the staging database. Ravi, could you help after the stand-up?
Ravi: Sure, I'll add you in ten minutes.
You: Thanks. That's all from me.
```
