# Problem Solving & Decisions

<div class="ssp-banner" markdown>
**Today's goal:** talk through problems clearly: define the problem, think out loud, compare options,
make a decision with others, and explain *why* you decided.
</div>

## A simple problem-solving flow

<div class="ssp-stack">
<div>1. Define <span>— what exactly is the problem? Who does it affect? How do we know?</span></div>
<div>2. Find the cause <span>— ask "why" until you reach the root cause</span></div>
<div>3. Options <span>— at least 2–3 possible solutions</span></div>
<div>4. Decide <span>— compare by impact, effort, risk and time</span></div>
<div>5. Act & review <span>— try it, measure it, adjust</span></div>
</div>

## The 5 Whys

> **Problem:** The release was late.
> **Why?** Testing took 3 extra days. → **Why?** We found 12 bugs at the end. → **Why?** Features weren't
> tested until the end. → **Why?** QA joined only in the last week. → **Why?** We don't plan QA in sprint
> planning. → **Root cause:** QA isn't part of planning. **Fix:** add QA to sprint planning.

## Phrases for thinking out loud

| Stage | Phrases |
|---|---|
| Defining | "Let's be clear about the problem first." / "What do we know for sure?" |
| Exploring | "What if…?" / "Another option could be…" / "Have we considered…?" |
| Evaluating | "The trade-off is…" / "The biggest risk here is…" / "This is quicker, but…" |
| Deciding | "Given the deadline, I'd go with…" / "Let's decide by Friday." / "Can we live with this risk?" |
| Disagreeing | "I see it differently, because…" / "What evidence would change your mind?" |
| Committing | "I'm not fully convinced, but I'll commit to it. Let's review in two weeks." |

## Compare options: a quick decision table

| Option | Impact | Effort | Risk | Time |
|---|---|---|---|---|
| A. Add more servers | Medium | Low | Low | 1 day |
| B. Add caching | High | Medium | Medium | 1 week |
| C. Rewrite the service | High | High | High | 2 months |

<div class="ssp-say" markdown>
"**I recommend B.** It has the highest impact for reasonable effort. **We can do A today** as a short-term
fix while we build B. **C isn't worth the risk** right now."
</div>

## Explaining a decision

<div class="ssp-formula">Decision → <em>why</em> → what we considered → what would make us change it</div>

<div class="ssp-say" markdown>
"We've decided to use Postgres instead of Mongo **because** our data is highly relational and we need
transactions. **We considered** Mongo for flexibility, but reporting would be much harder. **We'll
revisit** if we start storing large unstructured documents."
</div>

## Conversation: solving a problem as a team

```dialogue
Lead: The checkout page is slow again. Ideas?
You: Before we jump to solutions, can we define "slow"? The dashboard shows p95 went from 800 ms to 2.4 seconds since Tuesday.
Arun: Tuesday was the release with the new recommendations widget.
You: So the widget is a likely cause. Do we know for sure?
Meena: I checked: the widget makes three extra API calls, one after another.
You: Okay, three options: remove the widget, make the calls in parallel, or load the widget after the page.
Lead: Which do you recommend?
You: Load it after the page. It's quick to build, and the widget still works. Parallel calls help, but they don't fix the root issue.
Lead: Agreed. Meena, can you do that today?
Meena: Yes.
You: I'll watch the p95 tomorrow and share the numbers in the channel.
```

## Practice

Take one recurring problem in your team and apply the 5 Whys. Then write 3 options and a recommendation
in the decision-table format.

## Speak today

- [ ] In your next discussion, say "Let's define the problem first"
- [ ] Explain one decision using: decision → why → what we considered
