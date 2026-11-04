# Email Writing

<div class="ssp-banner" markdown>
**Today's goal:** write clear, polite, professional emails that get a reply: the right subject line,
the point first, one clear ask, and the right tone for managers, clients and colleagues.
</div>

## The anatomy of a good email

<div class="ssp-stack">
<div>1. Subject <span>— what it's about and what you need: "[Decision needed by Fri] Payment provider for Q1"</span></div>
<div>2. Greeting <span>— Hi Priya, / Dear Mr. Rao, / Hello team,</span></div>
<div>3. Point first <span>— the main message or request in the first 1–2 lines</span></div>
<div>4. Details <span>— short paragraphs or bullets: context, options, facts</span></div>
<div>5. Clear ask + deadline <span>— "Could you confirm by Thursday 5 pm?"</span></div>
<div>6. Closing <span>— Thanks, / Best regards, + name (and signature)</span></div>
</div>

## Tone: choose the right level

| Formal (client, senior, first contact) | Neutral (most work email) | Friendly (close colleagues) |
|---|---|---|
| Dear Ms. Rao, | Hi Priya, | Hey Priya! |
| I am writing to inform you that… | Just a quick update on… | Quick one: |
| Please find attached… | I've attached… | Here's the file. |
| I would appreciate it if you could… | Could you please…? | Can you…? |
| Please do not hesitate to contact me. | Let me know if you have any questions. | Shout if anything's unclear! |
| Yours sincerely, / Kind regards, | Best regards, / Thanks, | Cheers, / Thanks! |

## Templates

=== "Request"

    ```text
    Subject: Request: staging DB access for the coupon release (by Wed)

    Hi Arun,

    Could you give me read access to the staging database by Wednesday? I need it to test the
    coupon release planned for Friday.

    Details: user ashish.g, read-only access to the orders and coupons schemas.

    Thanks,
    Ashish
    ```

=== "Status update"

    ```text
    Subject: Weekly update — Checkout team (3–7 Nov)

    Hi all,

    Summary: on track for the 15 Nov release; one risk below.

    ✅ Done: coupon validation, 3 cart bugs fixed
    🔄 In progress: delivery-slot API (70%)
    ⚠️ Risk: map vendor key still pending — needed by 10 Nov
    🙋 Need: decision on slot-cache TTL (5 vs 15 min) from Priya

    Thanks,
    Ashish
    ```

=== "Follow-up"

    ```text
    Subject: Re: API contract review

    Hi Neha,

    Just following up on the API contract I shared on Monday. We need the review by Thursday to
    keep the launch date. If it's easier, I'm happy to walk you through it in a 15-minute call.

    Thanks,
    Ashish
    ```

=== "Apology / mistake"

    ```text
    Subject: Correction: report sent this morning

    Hi team,

    The report I sent at 9 am had the wrong date range (October instead of November). Please use
    the corrected version attached. Sorry for the confusion. I've added a check so this doesn't
    happen again.

    Best,
    Ashish
    ```

=== "Saying no"

    ```text
    Subject: Re: Help with the analytics dashboard

    Hi Rahul,

    Thanks for thinking of me. I can't take this on before the 15th because I'm on the release.
    After that, I'd be happy to help. Alternatively, Kavya has built similar dashboards and may
    be able to help sooner.

    Best regards,
    Ashish
    ```

## Rules that save you

- **One email, one topic.** Two topics → two emails (or clearly numbered sections).
- **Under 150 words** for most emails. If it's longer, add a 2-line summary at the top.
- **Bold the ask** or put it on its own line.
- **Reply all** only when everyone needs it. **BCC** for large external lists.
- **Check before sending:** names, attachments, dates, time zones, tone.
- **Don't write angry emails.** Write them, wait an hour, then rewrite or call instead.

## Phrases to replace

| Instead of | Write |
|---|---|
| Please do the needful. | Could you please approve the request? |
| Kindly revert back. | Please reply by Thursday. / Let me know by Thursday. |
| PFA. | I've attached the report. |
| As per my last email… (sounds annoyed) | As mentioned on Monday… / Just following up on… |
| Sorry for the late reply. | Thanks for your patience. |
| I hope this email finds you well. (overused) | Hi Priya, (just start) |

## Conversation: asking a colleague to review an important email

```dialogue
You: Meena, could you look at this email before I send it to the client? It's about the delay.
Meena: Sure. Hmm. The first paragraph is all about the bank's API change.
You: I wanted to explain why it happened.
Meena: Put the new date and the plan first. The reason can be one line after that.
You: Good point. So: "The payment feature will be ready on the 22nd. Everything else stays on the 15th."
Meena: Much better. And make the subject line clear, something like "Updated timeline: payment feature on 22 Nov".
You: Got it. Should I say sorry?
Meena: Yes, once, briefly. Then focus on the plan.
You: Thanks, Meena. I'll fix it and send it in ten minutes.
```

## Practice

Rewrite this email to be clear and polite:
*"Hi, PFA the doc. Kindly check and revert back ASAP. Also the meeting is shifted. Do the needful."*

??? success "Sample answer"
    Subject: Review needed: payment design doc (by Thu) + meeting moved to Fri 3 pm

    Hi Priya, I've attached the payment design doc. Could you review it by Thursday? Also, our
    design meeting has moved to Friday at 3 pm. Thanks, Ashish
