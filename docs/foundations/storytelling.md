# Storytelling

<div class="ssp-banner" markdown>
**Today's goal:** turn facts into short stories people remember, for interviews, presentations,
team updates and everyday conversation.
</div>

## Why stories work

People forget bullet points but remember **stories**: a person, a problem, a struggle and a result. A
30-second story makes your point stick in an interview, a demo, or a request for budget.

## The simple story arc

<div class="ssp-stack">
<div>1. Setting <span>— when, where, who ("Last Diwali sale…")</span></div>
<div>2. Problem <span>— what went wrong or what was at stake</span></div>
<div>3. Struggle <span>— what you tried; tension and choices</span></div>
<div>4. Turning point <span>— the key action or insight</span></div>
<div>5. Result & lesson <span>— what changed, with a number, and what you learned</span></div>
</div>

!!! example "From facts to story"
    **Facts:** "We added canary deploys. Outages went down."

    **Story:** "**Last Diwali**, our biggest sales day, a deploy at 7 pm **took checkout down for 40
    minutes**. **We lost about 1,200 orders.** The next morning, the team was exhausted and the CEO
    wanted answers. **We realised** the problem wasn't the code; it was releasing to everyone at
    once. **So we started** releasing to 5% of users first. **This Diwali, we deployed eleven times
    and had zero outages.** Small, careful steps beat big brave ones."

## Story tools

| Tool | Example |
|---|---|
| Start in the middle | "At 7:10 pm, the alerts started." |
| Use a real detail | "…the dashboard turned completely red." |
| Include dialogue | "My manager asked, 'How long until it's back?'" |
| Use numbers | "1,200 orders", "40 minutes", "zero outages" |
| End with one lesson | "Small, careful steps beat big brave ones." |
| Keep it short | 30–90 seconds for most work stories |

## Where to use stories

| Situation | Story type |
|---|---|
| Interview | A STAR story: Situation, Task, Action, Result (see [Interviews](../career/interviews.md)) |
| Presentation | Open with a short story instead of an agenda slide |
| Asking for budget | The customer or team pain, in one real example |
| Team update | "Here's what happened with one customer this week…" |
| Small talk | A funny or surprising travel or weekend story |

## Useful phrases

- "**Let me tell you about** the time we…"
- "**It all started when**…"
- "**At first**, we thought… **but then** we realised…"
- "**That's when** we decided to…"
- "**In the end**… / **Looking back**, the lesson was…"

## Conversation: telling a story in an interview

```dialogue
Interviewer: Tell me about a time you made a mistake.
You: Sure. Two years ago, I ran a database migration on a Friday evening without testing it on a copy of production data.
Interviewer: What happened?
You: It locked the orders table for twelve minutes. Customers couldn't place orders, and my phone started ringing.
Interviewer: How did you handle it?
You: I rolled it back first, then told my manager exactly what I'd done. The next week, I added a rule to CI: every migration runs on a production snapshot first.
Interviewer: And the result?
You: We haven't had a migration outage since then. The lesson for me was: own the mistake quickly, then fix the system, not just the bug.
```

## Practice

Write a 60-second story about a problem you solved at work, using the 5-step arc. Tell it aloud and time it.

## Speak today

- [ ] Prepare one work story and one personal story you can tell in under a minute
- [ ] Start your next update or presentation with a short story instead of an agenda
