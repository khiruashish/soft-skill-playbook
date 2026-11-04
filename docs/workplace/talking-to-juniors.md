# Talking to Juniors

<div class="ssp-banner" markdown>
**Your job isn't to be the smartest person in the room. It's to make the room smarter.** How you treat
juniors decides whether they come to you with problems or hide them from you.
</div>

## Principles

1. **Psychological safety first.** Juniors who are scared to ask hide bugs.
2. **Explain the *why*, not just the *what*.** "Use a transaction here *because* two writes must succeed together."
3. **Ask before telling.** "What do you think is happening?" builds thinking. Giving the answer builds dependence.
4. **Praise in public, correct in private.**
5. **Be specific.** "Good job" teaches nothing. "Your test for the null-cart case caught a real bug, nice" does.

## Teaching: the "I do, we do, you do" model

<div class="ssp-stack">
<div>I do <span>— you demo while explaining your thinking out loud</span></div>
<div>We do <span>— pair programming; they drive, you guide</span></div>
<div>You do <span>— they do it alone; you review afterward</span></div>
</div>

## Scripts

=== "Onboarding a new junior"

    <div class="ssp-say" markdown>
    "Welcome! For the first two weeks, nobody expects you to ship big features. **Your only job is to
    learn and ask questions. There are no stupid ones here.** Let's do 15 minutes every day at 4 pm
    for whatever came up."
    </div>

=== "Code-review feedback"

    Use labels so they know how serious each comment is:

    ```text
    nit:        (optional, style) "nit: could rename `d` to `deliveryDate` for clarity."
    suggestion: (better approach)  "suggestion: a Map lookup would make this O(1) instead of O(n)."
    question:   (curious, not a demand) "question: what happens if the list is empty?"
    blocker:    (must fix) "blocker: this SQL is built by string concat — injection risk. Use a parameter."
    praise:     "praise: really clean separation of the domain logic here 👏"
    ```

=== "Feedback on a bigger problem"

    Use **SBI**: Situation → Behaviour → Impact → (then ask)

    <div class="ssp-say" markdown>
    "In yesterday's release **(situation)**, the PR was merged without tests **(behaviour)**. A bug
    reached production and took 2 hours to roll back **(impact)**. **What got in the way of adding
    tests?** How can I help next time?"
    </div>

=== "Delegating a task"

    <div class="ssp-say" markdown>
    "I'd like you to own the coupon-validation endpoint. **Goal:** reject expired and over-used
    coupons. **Done means:** endpoint + unit tests + docs. **Deadline:** Thursday. **Check-in:**
    let's sync Tuesday. You decide the design; I'm here if you get stuck."
    </div>

=== "When they're stuck but won't ask"

    <div class="ssp-say" markdown>
    "Hey, how's the migration going? **Getting stuck is completely normal on this one.** It took me
    two days the first time. Want to walk me through where you are?"
    </div>

=== "When they make a mistake"

    <div class="ssp-say" markdown>
    "This happens to everyone. I once took down staging for a whole afternoon. **Let's fix it
    together first, then talk about how to prevent it.**"
    </div>

=== "Saying no to their idea (kindly)"

    <div class="ssp-say" markdown>
    "I like that you're thinking about performance. Right now, the bottleneck is the database, not the
    JSON parsing, so a rewrite wouldn't help much. **Can you profile it and show me where the time
    goes?** If the data says otherwise, let's do it."
    </div>

## Mistakes to avoid

- ❌ "This is easy, just do X" (it isn't easy for them)
- ❌ Taking the keyboard and fixing it yourself
- ❌ Sarcasm in code reviews
- ❌ Only giving feedback when something goes wrong
- ❌ Answering in jargon without checking they understand

## Questions to ask juniors regularly

- "What's one thing you learned this week?"
- "What's confusing about our codebase that nobody explains?"
- "What would you like to work on next?"
- "How can I be a better mentor for you?"
