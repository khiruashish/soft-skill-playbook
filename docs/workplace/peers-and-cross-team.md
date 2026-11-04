# Peers & Cross-Team Communication

<div class="ssp-banner" markdown>
**Most of the time you have influence but no authority.** You can't order the product manager, the QA lead
or another team around. You persuade them by building a relationship and making your ask easy to say yes to.
</div>

## Know what each role cares about

| Role | Cares about | Speak their language |
|---|---|---|
| Product Manager | User value, scope, dates | "This lets users do X; trade-off is Y." |
| Designer | User experience, consistency | "This interaction is expensive. Could a simpler pattern work?" |
| QA | Coverage, edge cases, stability | "Here are the risky areas to test first." |
| DevOps / SRE | Reliability, on-call pain | "Here's the runbook and the alerts." |
| Other dev team | Their own roadmap, API stability | "Here's the contract change, and here's the migration window." |
| Sales / Support | Customer promises | "This ships on the 15th; here's what to tell customers." |

## Scripts

=== "Asking another team for something"

    <div class="ssp-say" markdown>
    "Hi Neha, I'm on the checkout team. **We need a new `reserveStock` endpoint by the 20th** to launch
    flash sales. I've drafted the API contract (link). Could your team review it this week? If it
    helps, we can raise the PR ourselves and you just review."
    </div>

=== "Negotiating scope with a PM"

    <div class="ssp-say" markdown>
    "I love this feature. In the 2 weeks we have, we can deliver **filters and sorting**, but not
    **saved searches**. Which matters more for the launch? We can add saved searches in the next
    sprint."
    </div>

=== "Disagreeing in a design review"

    <div class="ssp-say" markdown>
    "I see the benefit of event sourcing here. **My concern is** the extra complexity for a team of
    three. **What if** we start with a simple outbox table and move to event sourcing if audit needs
    grow? Happy to be convinced otherwise."
    </div>

=== "Following up when they've gone silent"

    <div class="ssp-say" markdown>
    "Hi Arjun, following up on the contract review from Monday. **We need it by Thursday to keep the
    launch date.** If you're swamped, a 10-minute call might be faster. Does tomorrow at 11 work?"
    </div>

=== "Thanking publicly"

    <div class="ssp-say" markdown>
    "Big thanks to @Kavya from the platform team. She stayed late to fix the Kafka config so we could
    release on time. 🙏"
    </div>

## Building cross-team relationships

- **Coffee chats:** 20 minutes with one person from another team each month.
- **Help first:** review their PR or answer their question before you need something from them.
- **Close the loop:** tell people what happened with their input ("We used your idea, and it worked").
- **Assume good intent:** a slow reply usually means they're busy, not that they don't care.
