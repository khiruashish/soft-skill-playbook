# Team Lead Meetings

<div class="ssp-banner" markdown>
**Two sides of the same table.** If you report to a team lead, this page shows how to use your time
with them well. If you *are* the team lead, it shows how to run 1:1s, stand-ups, sprint planning and
retros that people find useful rather than tiring.
</div>

=== ":material-account: Meeting your team lead"

    ## What your team lead needs from you

    | They need | You give |
    |---|---|
    | Visibility | Short, regular status, before they ask |
    | Early risks | "This might slip" on day 2, not day 10 |
    | Technical judgement | Options and trade-offs, not just "it's hard" |
    | Ownership | "I'll handle it" and follow-through |
    | Honest feedback | What's working and what isn't in the team |

    ## Your 1:1 with the team lead

    ```text
    1:1 — Team lead — [Date]
    1. Progress: search filters done; sorting 70%
    2. Blocker: need decision on pagination (cursor vs offset)
    3. Tech question: should we cache category tree in Redis?
    4. Growth: can I lead the next design review?
    5. Team: onboarding docs are outdated — happy to fix
    ```

    ## Scripts

    === "Getting a technical decision"

        <div class="ssp-say" markdown>
        "I need a decision on pagination. **Option A:** offset, which is simple but slow past page
        100. **Option B:** cursor, which is fast but can't jump to an arbitrary page. Product says
        users rarely go past page 5, **so I recommend cursor.** Okay to go ahead?"
        </div>

    === "Asking for more responsibility"

        <div class="ssp-say" markdown>
        "I'd like to grow toward a senior role. **Could I own the delivery-slot service end to end**,
        from design to on-call? I'd check in with you on the design before building."
        </div>

    === "Too much work"

        <div class="ssp-say" markdown>
        "I have the search work, two production bugs and the interview loop this week. **I can't do
        all of it well.** Which should I drop or push to next week?"
        </div>

    === "Giving feedback to your lead"

        <div class="ssp-say" markdown>
        "Can I share some feedback? **When requirements change mid-sprint, it'd help to know the
        reason.** Last week the team rewrote the cart API twice without context, and people felt
        frustrated. A quick note on the 'why' would make a big difference."
        </div>

    === "Concern about a teammate"

        <div class="ssp-say" markdown>
        "I want to raise something carefully. **I've noticed the integration tests have been skipped
        on the last few PRs**, and it caused yesterday's staging break. I've mentioned it to Arun
        directly. Could we talk about a team-wide rule so it doesn't feel personal?"
        </div>

        Talk to the person first. Escalate the **pattern**, not the person.

    ## Mistakes to avoid

    - ❌ Showing up to the 1:1 with nothing to discuss
    - ❌ Bringing problems without any proposed solution
    - ❌ Agreeing in the meeting and complaining after it
    - ❌ Using the 1:1 only for status (that's what stand-up is for)

=== ":material-account-group: Running meetings as a team lead"

    ## The meeting toolkit

    | Meeting | Frequency | Length | Goal |
    |---|---|---|---|
    | Daily stand-up | Daily | 15 min | Sync & unblock |
    | 1:1 | Weekly / bi-weekly | 30 min | Trust, growth, early warnings |
    | Sprint planning | Every sprint | 60–90 min | Commit to realistic scope |
    | Backlog refinement | Weekly | 45 min | Clarify & estimate upcoming work |
    | Retrospective | Every sprint | 45–60 min | Improve how we work |
    | Tech / design review | As needed | 45 min | Make good technical decisions together |

    ## 1:1s with your team members

    **Their meeting, not yours.** Let them set most of the agenda; you listen 70% of the time.

    **Great 1:1 questions:**

    - "What's on your mind this week?"
    - "What's **blocking you** or slowing you down?"
    - "What's **one thing** I could do to make your work easier?"
    - "What are you **enjoying** most right now? Least?"
    - "Where do you want to be in **a year**? What could get you there?"
    - "Is there anything in the team that **bothers you** that I might not see?"

    !!! tip "Never cancel 1:1s"
        Reschedule if you must. Cancelling repeatedly tells people they're not a priority.

    ## Stand-up: keep it tight

    <div class="ssp-say" markdown>
    "Morning, everyone! Same format: **done, doing, blockers.** Let's keep detailed discussions for
    after. Kavya, want to start?"
    </div>

    Redirect long discussions: *"Great point. Ravi and Meena, can you two take that right after?"*

    ## Sprint planning

    <div class="ssp-say" markdown>
    "Our sprint goal: **launch delivery-slot booking in Pune.** Last 3 sprints we averaged 34 points,
    and 2 people are on leave, so **let's commit to about 26.** Anything that doesn't serve the goal
    goes to the stretch list."
    </div>

    - Start with the **goal**, then pick stories
    - Plan around **real capacity** (leave, on-call, interviews)
    - Make sure every story has **clear acceptance criteria**
    - Ask the quiet people: *"Arun, does that estimate feel right to you?"*

    ## Retrospectives that actually change things

    **Format: Start / Stop / Continue** (or Went well / Didn't go well / Ideas)

    <div class="ssp-say" markdown>
    "**The goal is to improve the system, not to blame anyone.** What happens in the retro is safe
    to say here. Let's take 5 minutes to write silently, then share."
    </div>

    - Pick **at most 2 action items**, each with an owner
    - **Start the next retro by reviewing** last retro's actions
    - Rotate the facilitator so everyone gets a turn

    ## Design reviews

    - Ask the author to **share the doc 24 hours before**
    - **Speak last** as the lead, so you don't anchor the room
    - Ask: *"What alternatives did we consider? What's the riskiest part? How do we roll back?"*
    - End with a **decision**, or with exactly what's needed to make one

    ## Handling team dynamics in meetings

    | Situation | What to say |
    |---|---|
    | One person dominates | "Thanks, Rahul. Let's hear from someone who hasn't spoken yet. Priya?" |
    | Someone stays silent | (Later, 1:1) "I'd love to hear your view in meetings. Would it help if I asked you directly?" |
    | Two people argue | "You both have valid points. Let's write down the trade-offs and decide with data." |
    | Meeting going off-topic | "Let's park that. I'll add it to the next refinement." |
    | Blame starts | "Let's focus on what in the process allowed this, not who." |
    | Bad news for the team | "I'll be straight with you: the deadline moved up 2 weeks. Here's what I know and what I'm pushing back on." |

    ## Communicating up and down

    | To the team | To your manager / leadership |
    |---|---|
    | Context: *why* we're doing this | Outcomes, risks, decisions needed |
    | Shield from noise and churn | Advocate for the team's capacity |
    | Credit individuals publicly | Report problems with your plan to fix them |
    | Be honest about uncertainty | Escalate early with options |

    ## New team lead: first 30 days

    - [ ] **1:1 with every team member:** "What should I keep? What should I change?"
    - [ ] Learn the **current processes** before changing any
    - [ ] Meet key **stakeholders** (PM, QA, other leads)
    - [ ] Agree on **expectations** with your manager
    - [ ] Fix **one small irritation** quickly to build trust
    - [ ] Shift from "**I** did" to "**we** did". Your success is now the team's success.

## Practice conversation: Asking your team lead for a decision

```dialogue
You: I need a quick decision on pagination for the search API.
Lead: Okay, what are the options?
You: Offset pagination is simple but slow after page 100. Cursor pagination is fast but users can't jump to a page number.
Lead: What do users actually do?
You: Product data says 98% never go past page 5. So I recommend cursor.
Lead: Makes sense. Go with cursor, and note the decision in the design doc.
You: Will do. Thanks.
```
