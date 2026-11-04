# LinkedIn Profile

<div class="ssp-banner" markdown>
**Today's goal:** write a LinkedIn profile that tells recruiters in 10 seconds who you are and what you're
good at, and learn to write connection requests, posts and messages that people actually answer.
</div>

## The 10-second test

A recruiter looks at your **photo, headline and the first 2 lines of your About section**, then decides
whether to read on. Get those three right first.

<div class="ssp-stack">
<div>1. Photo & banner <span>— clear face, plain background, smiling; a simple banner about your work</span></div>
<div>2. Headline <span>— role + key skills + what you deliver (not just "Software Engineer at X")</span></div>
<div>3. About <span>— a short story: what you do, your best results, what you're looking for</span></div>
<div>4. Experience <span>— results with numbers, not a list of duties</span></div>
<div>5. Skills, recommendations, activity <span>— proof from other people, and signs you're active</span></div>
</div>

## Headline: formulas that work

<div class="ssp-formula">Role · <em>Core skills</em> · Result or domain</div>

| ❌ Weak | ✅ Strong |
|---|---|
| Software Engineer at XYZ | Senior Backend Engineer · Java, Kafka, AWS · Building payment systems for 2M+ daily transactions |
| Looking for opportunities | Full-Stack Developer (React, Node.js) · Open to Bengaluru & Remote roles |
| Fresher | Computer Science Graduate · Java & Spring Boot · Built a grocery delivery app as a final-year project |
| Tech Lead | Engineering Lead · Grew a team from 3 to 12 · Microservices, reliability, mentoring |

## About section: a simple template

```text
I'm a [role] with [X] years of experience building [what] for [whom/industry].

Recently, I [biggest achievement with a number], and [second achievement].
I enjoy [the kind of problems you like], and I'm known for [a strength others mention].

Skills: [5–8 key skills]

I'm currently [open to / interested in] [type of role] in [location / remote].
Feel free to reach out at [email].
```

!!! example "Example"
    I'm a backend engineer with nine years of experience building high-scale systems for fintech and
    e-commerce. Recently, I led the re-architecture of a grocery checkout that cut failed orders by 60%,
    and I reduced our cloud costs by ₹35 lakh a year. I enjoy turning messy, slow systems into simple,
    reliable ones, and I'm known for clear incident communication and mentoring new engineers.
    Skills: Java, Spring Boot, Kafka, PostgreSQL, AWS, system design. I'm open to Staff Engineer roles
    in Bengaluru or remote.

## Experience: duties vs results

| ❌ Duties | ✅ Results |
|---|---|
| Worked on the checkout service. | Re-architected checkout with the outbox pattern, **cutting failed orders by 60%**. |
| Responsible for code reviews. | Introduced review guidelines that **halved review time** (3 days → 1.5 days). |
| Handled production issues. | Led **20+ incidents** as incident commander; wrote post-mortems that removed 3 recurring failures. |

Use **action verbs**: built, led, launched, reduced, improved, migrated, automated, mentored, designed, scaled.

## Writing messages people answer

=== "Connection request (300 characters)"

    ```text
    Hi Neha, I enjoyed your talk on consumer lag at Kafka Summit. I'm working on similar
    problems in grocery delivery. I'd love to connect and follow your work. — Ashish
    ```

    **Why it works:** personal, specific, short, and it doesn't ask for anything yet.

=== "Asking for a referral"

    ```text
    Hi Arjun, hope you're well! I saw that Brightsoft is hiring a Senior Backend Engineer
    (job ID 4471). I have 9 years in Java and Kafka, and I led a checkout re-architecture
    that cut failures by 60%. Would you be comfortable referring me? I've attached my CV and
    a 3-line summary you can forward. Totally fine if not — thanks either way!
    ```

=== "Replying to a recruiter"

    ```text
    Hi Riya, thanks for reaching out! The role sounds interesting. Could you share the
    job description, the team I'd be working with, and the budgeted range? I'm currently
    on a 60-day notice period. Happy to set up a call this week — Tuesday or Thursday
    after 5 pm works for me.
    ```

=== "Saying no politely"

    ```text
    Hi Riya, thanks for thinking of me. I'm not looking for a change right now, but I'd
    be glad to stay in touch for the future. All the best with the search!
    ```

## Posting: share without bragging

<div class="ssp-formula">Hook → <em>what happened</em> → what you learned → a question</div>

```text
Our checkout failed 1,200 orders in 40 minutes last year. Here's what we changed. 🧵

The cause: a payment SDK timeout of 2s, under a bank latency of 2.6s at peak.
We fixed it with canary deploys, peak-hour deploy blocks and better alerts.
Biggest lesson: the fix was 20% code and 80% process.

How does your team stop risky deploys during peak traffic?
```

!!! warning "Don't"
    Share confidential numbers, customer names or internal screenshots · criticise your employer ·
    post only "#OpenToWork" with no details · send a referral request to a stranger as your first message.

## Conversation: networking message turns into a call

```dialogue
Neha: Hi Ashish, thanks for connecting! Glad the talk was useful.
You: It really was. We had the same consumer lag problem last month. Could I ask you one question about it?
Neha: Sure, go ahead.
You: Did you increase partitions, or change the consumer batch size first?
Neha: Batch size first. Partitions only helped after we fixed slow processing.
You: That's exactly what I suspected. Thank you! Would you be open to a 15-minute call sometime? I'd love to hear how you scaled it.
Neha: Happy to. How about Friday at 4?
You: Friday at 4 works. I'll send an invite. Thanks, Neha!
```

## Practice

Rewrite your headline using **Role · Core skills · Result or domain**, and write the first two lines of
your About section.

## Speak today

- [ ] Update your headline and the first two lines of your About section
- [ ] Rewrite one experience line from a duty to a result with a number
- [ ] Send one personalised connection request
