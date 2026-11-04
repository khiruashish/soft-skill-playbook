# Team Building

<div class="ssp-banner" markdown>
**A team is built through small, repeated moments, not offsite games:** how people greet each other,
how mistakes are handled, who gets credit, and whether it's safe to say "I don't know". Everyone helps
build it, not only the lead.
</div>

## What makes a strong team

<div class="ssp-stack">
<div>1. Psychological safety <span>— people can ask, admit mistakes and disagree without fear</span></div>
<div>2. Dependability <span>— people do what they said, on time</span></div>
<div>3. Clarity <span>— everyone knows the goals, roles and how decisions are made</span></div>
<div>4. Meaning <span>— the work matters to the people doing it</span></div>
<div>5. Impact <span>— people can see their work makes a difference</span></div>
</div>

These come from widely cited research on what effective teams have in common. Psychological safety is
the foundation the rest depend on.

## As a team member: what you can do

<div class="grid cards" markdown>

-   :material-hand-heart:{ .lg .middle } __Help first__

    ---

    Review PRs quickly, answer questions in channels, pair with someone who's stuck.

-   :material-account-voice:{ .lg .middle } __Admit mistakes__

    ---

    "That bug was mine. Here's the fix." When one person does this, others feel safe to do it too.

-   :material-star-circle:{ .lg .middle } __Give credit__

    ---

    Thank people by name, publicly, for specific work.

-   :material-account-plus:{ .lg .middle } __Include people__

    ---

    Invite the new joiner to lunch. Ask the quiet person for their view.

</div>

## As a team lead: building the team

### Set it up clearly

=== "Team charter (first team meeting)"

    Agree these together and write them down:

    ```markdown
    ## Our team charter
    **Mission:** Make checkout fast and reliable for every customer.
    **How we work:**
    - Core hours 11–5 IST; async outside that
    - PRs reviewed within 1 working day
    - Disagree in the room, commit outside it
    - Blameless post-mortems
    **How we decide:** Owner decides after consulting; lead breaks ties
    **How we communicate:** Slack for quick, docs for decisions, call for conflict
    ```

=== "Opening script"

    <div class="ssp-say" markdown>
    "I'd like us to agree on **how we want to work together**, not rules from me. What's one thing
    from a past team that worked really well, and one thing you never want to see again?"
    </div>

=== "Roles & ownership"

    Give everyone **one clear area to own** (a service, a process, the on-call runbook). Ownership
    builds commitment faster than any activity.

### Build psychological safety

| Do | Say |
|---|---|
| Model not knowing | "I don't know. Who's worked with this before?" |
| Thank people for bad news | "Thanks for flagging this early. That's exactly what I want." |
| Invite dissent | "What are we missing? Who sees it differently?" |
| Speak last in discussions | (Let others share first so you don't anchor them) |
| Handle mistakes as learning | "What in our process allowed this? How do we fix the process?" |
| Shut down disrespect quickly | "Let's keep it about the idea, not the person." |

## Rituals that build the team (low effort, high value)

| Ritual | How | Why it works |
|---|---|---|
| **Weekly wins** | 5 min on Friday: everyone shares one win | Visibility + celebration |
| **Kudos channel** | `#kudos` for public thanks | Recognition, especially across teams |
| **Demo day** | Monthly; anyone shows anything they built | Pride, learning, cross-pollination |
| **Retro** | Every sprint; act on 1–2 items | People see their input changes things |
| **Pairing / mob sessions** | 1–2 hours a week | Knowledge sharing, relationships |
| **Lunch & learn** | Rotating speaker, 30 min | Everyone teaches, everyone grows |
| **Onboarding buddy** | Each new joiner gets a buddy for 30 days | Fast integration, a friend from day 1 |
| **Team lunch / chai** | Monthly, no work talk | Personal connection |

## Team activities

=== "In-office / offsite"

    - **Hackathon day:** small mixed teams, a fun or useful problem, a demo at the end
    - **Cooking / cricket / bowling outing:** shared fun, without forced "trust falls"
    - **Volunteering day:** builds shared meaning
    - **Strategy offsite:** half the day on the team's direction, half on fun

=== "Remote / hybrid"

    - **Virtual coffee roulette:** random pairs, 15 minutes, every week
    - **Online games:** quizzes, Pictionary-style drawing games, coding puzzles
    - **"Show your desk / pet / hometown"** in 2 minutes at the start of a meeting
    - **Async photo channel:** weekend pictures, food, travel
    - **In-person meetup** once or twice a year if possible

=== "Icebreakers that aren't awkward"

    - "What's one thing you're looking forward to this month?"
    - "What was your first ever computer or phone?"
    - "Best bug you've ever found or caused?"
    - "One app you couldn't live without?"
    - "What did you want to be when you were 10?"

!!! warning "Make activities inclusive"
    Not everyone drinks, eats every food, can stay late, or enjoys physical games. Mix the timings
    (some during work hours), the formats and the venues, and **never make fun activities
    compulsory**.

## Handling team problems

| Problem | What to say / do |
|---|---|
| Two people in conflict | Meet each one privately, then together: "You both want the release to succeed. Let's agree how you'll work together." |
| Silos ("my code, your code") | Rotate code reviews and on-call; pair across areas |
| One person carrying the team | Share their knowledge (docs, pairing) and spread the load before they burn out |
| Low morale after a hard period | Acknowledge it honestly: "The last two months were tough." Celebrate what was achieved; give real rest |
| New joiner not fitting in | Assign a buddy, involve them in pairing, check in privately every week |
| Cliques forming | Mix pairs and project groups on purpose; include everyone in decisions |

## Celebrating the team

<div class="ssp-say" markdown>
"Before we close: **thank you, everyone.** We shipped slot booking in 3 cities with zero downtime.
**Special shout-out to Kavya** for the load testing that caught the race condition, **and to Arun**
for staying calm through two incidents. Lunch is on me on Friday!"
</div>

Be specific, name the people, and celebrate **effort and learning**, not only outcomes.

## Signs your team is healthy

- [ ] People ask "stupid" questions in public channels
- [ ] Bad news reaches the lead early
- [ ] Disagreements happen openly in meetings, not in private complaints afterwards
- [ ] People help each other without being asked
- [ ] Retro actions actually get done
- [ ] People laugh together at least once a week

## Practice conversation: Setting up a team charter

```dialogue
Lead: I'd like us to agree on how we work together. What worked well in your past teams?
Kavya: Fast code reviews. It's frustrating waiting three days.
Arun: Blameless post-mortems. In my last team, people hid mistakes.
You: Clear decisions. Sometimes we discuss for weeks and nobody decides.
Lead: Great points. So: reviews within one working day, blameless post-mortems, and the owner decides after consulting?
You: Yes. And maybe a short "weekly wins" on Fridays?
Lead: Love it. I'll write it up and share it today.
```
