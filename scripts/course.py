#!/usr/bin/env python3
"""Single source of truth for the day-by-day course order.

Run after adding, removing or reordering a lesson:

    python scripts/course.py

It regenerates:
  * the `nav:` block in mkdocs.yml (between the course-nav markers)
  * docs/course/index.md          (the full roadmap)
  * docs/course/phase-<n>.md      (one overview page per phase)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# (key, tab title, full title, icon, blurb, [ (file, short title, one-line description), ... ])
PHASES = [
    ("1", "1 · English", "Phase 1 · English Basics", "material-alphabetical-variant",
     "Build sentences, ask and answer any question, and use the tenses and polite forms you need every day.",
     [
        ("english/01-introductions.md", "Greetings & Introducing Yourself", "Hello, goodbye, and a 30-second introduction about you"),
        ("english/02-sentence-building.md", "Building Sentences", "Word order, am/is/are, and turning ideas into clear sentences"),
        ("english/03-yes-no-questions.md", "Yes/No Questions", "Make questions with be, do/does, can, have, and answer them"),
        ("english/04-wh-questions.md", "Wh- Questions", "What, where, when, why, who, which, how: forming any question"),
        ("english/05-answering-questions.md", "Answering Questions", "Short answers, full answers, polite 'no', and 'I'm not sure'"),
        ("english/06-present-tense.md", "Present: Routines & Right Now", "Daily routine, what's happening now, and the questions for each"),
        ("english/07-past-tense.md", "Past: What Happened", "Talk about yesterday, last week, and your experience"),
        ("english/08-future-plans.md", "Future: Plans & Promises", "Will, going to, and plans with the present continuous"),
        ("english/09-polite-english.md", "Polite Requests & Offers", "Can, could, would, may: request, offer, permission, refusal"),
        ("english/10-joining-ideas.md", "Joining Ideas & Opinions", "And, but, because, so, if, when; agree, disagree, give opinions"),
        ("english/11-numbers-time-money.md", "Numbers, Time, Dates & Money", "Prices, phone numbers, times, dates and spelling out loud"),
        ("english/12-describing.md", "Describing People, Places & Problems", "Adjectives, comparisons, and describing what's wrong"),
        ("english/13-common-mistakes.md", "Common Mistakes & Fixes", "Articles, prepositions, tenses and Indian-English habits"),
     ]),
    ("2", "2 · Communication", "Phase 2 · Communication & Confidence", "material-account-voice",
     "The principles behind every good conversation, and the confidence to start one.",
     [
        ("foundations/communication-principles.md", "Communication Principles", "Point first, know your audience, PREP, SBAR, STAR"),
        ("foundations/listening-and-questions.md", "Listening & Asking Questions", "Active listening and the question types that unblock anything"),
        ("foundations/building-confidence.md", "Building Confidence", "Habits, body language and voice that make you sound sure"),
        ("everyday/small-talk-networking.md", "Small Talk & Networking", "Start, continue and politely end any conversation"),
        ("everyday/phone-calls.md", "Phone Calls", "Prepare, open, confirm and close a call with confidence"),
     ]),
    ("3", "3 · Everyday Life", "Phase 3 · Everyday Conversations", "material-earth",
     "Real conversations for travel, food, shopping, health, fitness, home, offices and social life.",
     [
        ("everyday/train.md", "Train & Railway Station", "Tickets, platforms, seats, the TTE, and missed trains"),
        ("everyday/metro-and-bus.md", "Metro & Bus", "Cards, routes, stops, changes and crowded rides"),
        ("everyday/airport.md", "Airport", "Check-in, security, immigration, boarding and lost bags"),
        ("everyday/flight.md", "On the Flight & Arrival", "Seats, cabin crew, connections, immigration and customs"),
        ("everyday/cab-and-directions.md", "Cab, Auto & Directions", "Booking, talking to drivers, asking the way"),
        ("everyday/hotel.md", "Hotel", "Check-in, room problems, requests and check-out"),
        ("everyday/sightseeing.md", "Sightseeing & Tourist Places", "Tickets, guides, photos and asking about places"),
        ("everyday/restaurant.md", "Restaurant & Café", "Tables, ordering, dietary needs, complaints and the bill"),
        ("everyday/food-delivery.md", "Food Delivery & Takeaway", "Ordering by phone, delivery issues and refunds"),
        ("everyday/grocery-shopping.md", "Grocery & Vegetable Market", "Supermarket, kirana, sabzi market, weights and prices"),
        ("everyday/shopping.md", "Shopping & Returns", "Clothes, electronics, trial rooms, bargaining and returns"),
        ("everyday/bank-and-shopping.md", "Bank & Money", "Accounts, cards, disputes, loans and transfers"),
        ("everyday/post-and-courier.md", "Post Office & Courier", "Sending parcels, tracking and missing deliveries"),
        ("everyday/hospital.md", "Hospital", "Registration, emergency, admission, visiting and billing"),
        ("everyday/doctor-and-pharmacy.md", "Doctor & Pharmacy", "Describing symptoms, questions to ask, medicines"),
        ("everyday/dentist-and-eye-clinic.md", "Dentist & Eye Clinic", "Toothache, cleaning, eye tests and glasses"),
        ("everyday/gym.md", "Gym", "Joining, trainers, equipment, routines and gym etiquette"),
        ("everyday/yoga.md", "Yoga Class", "Joining a class, following instructions, injuries and breathing"),
        ("everyday/sports.md", "Sports & Games", "Joining a game, booking courts, team talk and cricket chat"),
        ("everyday/renting-a-home.md", "Renting a Home", "House hunting, the landlord, rent, deposit and agreements"),
        ("everyday/neighbours-and-society.md", "Neighbours & Society", "Meeting neighbours, complaints, society meetings"),
        ("everyday/home-services.md", "Home Repairs & Services", "Plumber, electrician, AC repair, house help"),
        ("everyday/salon.md", "Salon & Barber", "Haircut, beard, styles and salon services"),
        ("everyday/customer-care.md", "Customer Care & Complaints", "Mobile, internet, app and service complaints"),
        ("everyday/government-office.md", "Government Office", "Passport, ID cards, licences and forms"),
        ("everyday/police-and-emergency.md", "Police & Emergencies", "Reporting theft, accidents, emergencies and FIRs"),
        ("everyday/school.md", "School & Parent-Teacher Meeting", "Admissions, teachers and your child's progress"),
        ("everyday/celebrations.md", "Invitations & Celebrations", "Inviting, accepting, wishes, weddings and birthdays"),
        ("everyday/movies-and-weekends.md", "Movies & Weekend Plans", "Making plans, booking tickets, talking about films"),
        ("everyday/vehicle.md", "Petrol Pump & Vehicle Service", "Fuel, tyres, service centre and breakdowns"),
     ]),
    ("4", "4 · Workplace", "Phase 4 · Workplace Communication", "material-briefcase",
     "Stand-ups, managers, juniors, CEOs, clients and every hard conversation in between.",
     [
        ("workplace/day-to-day.md", "Day-to-Day Communication", "Stand-ups, Slack, email, PRs and estimates"),
        ("workplace/talking-to-manager.md", "Talking to Your Manager", "1:1s, status, risks, help and feedback"),
        ("workplace/peers-and-cross-team.md", "Peers & Cross-Team", "PMs, QA, designers and other teams"),
        ("workplace/talking-to-juniors.md", "Talking to Juniors", "Teaching, code review and delegation"),
        ("workplace/explaining-issues.md", "Explaining an Issue", "Bug reports, incidents and non-tech explanations"),
        ("workplace/meetings-and-presentations.md", "Meetings & Presentations", "Speak up, run meetings and give demos"),
        ("workplace/team-lead-meetings.md", "Team Lead Meetings", "Meeting your lead, or running meetings as one"),
        ("workplace/talking-to-ceo.md", "Talking to the CEO", "Bottom line first, business impact, decisions"),
        ("workplace/client-meeting.md", "Client Meetings", "Discovery, delays, scope creep and follow-ups"),
        ("workplace/difficult-conversations.md", "Difficult Conversations", "Say no, disagree, conflict and criticism"),
        ("workplace/global-and-remote-teams.md", "Global & Remote Teams", "Time zones, async writing and cultures"),
        ("workplace/work-from-home.md", "Work from Home", "Asking for WFH, staying visible, video calls"),
        ("workplace/leave-and-boundaries.md", "Leave & Boundaries", "Asking for leave and protecting your time"),
        ("workplace/mentoring.md", "Mentoring", "Find a mentor, be a mentee, mentor others"),
        ("workplace/team-building.md", "Team Building", "Trust, safety, rituals and team activities"),
        ("workplace/office-party.md", "Office Party & Team Events", "Mingling, leaders, toasts and etiquette"),
     ]),
    ("5", "5 · Career", "Phase 5 · Career Moments", "material-stairs-up",
     "The conversations that shape your career, from the interview to your next big move.",
     [
        ("career/interviews.md", "Interviews", "Introduce yourself, STAR answers, questions to ask"),
        ("career/first-90-days.md", "First 90 Days", "Introductions, questions and your first win"),
        ("career/performance-review.md", "Performance Review", "Wins file, self-review and the review meeting"),
        ("career/promotion-discussion.md", "Promotion Discussion", "Criteria, evidence, sponsors and 'not yet'"),
        ("career/appraisal-discussion.md", "Appraisal Discussion", "Hike letters, low hikes and escalation"),
        ("career/salary-negotiation.md", "Salary Negotiation", "Know your numbers and negotiate the package"),
        ("career/resignation.md", "Resignation", "Telling your manager, notice and leaving well"),
        ("career/handling-layoffs.md", "Handling Layoffs", "What to ask, what to say, and what's next"),
        ("foundations/burnout.md", "Burnout & Wellbeing", "Spot it, talk about it and recover"),
        ("foundations/improving-soft-skills.md", "Your 90-Day Improvement Plan", "Self-assessment and your plan after the course"),
        ("course/graduation.md", "Final Review & Graduation", "Self-test, recap and what to practise next"),
     ]),
]

REFERENCE = [
    ("Phrase Bank", "reference/phrase-bank.md"),
    ("Daily Practice Checklist", "reference/daily-practice-checklist.md"),
]


def days():
    n = 0
    for phase in PHASES:
        for item in phase[5]:
            n += 1
            yield n, phase, item


TOTAL = sum(len(p[5]) for p in PHASES)


def rel(from_file: str, to_file: str) -> str:
    """Relative link between two docs-relative paths."""
    import os
    return os.path.relpath(to_file, os.path.dirname(from_file)).replace(os.sep, "/")


def gen_nav() -> str:
    lines = ["nav:", "  - Home: index.md", "  - Start Here:",
             "      - course/index.md", "      - Master Prompt: master-prompt.md"]
    numbered = {f: n for n, _, (f, _, _) in days()}
    for key, tab, _full, _icon, _blurb, items in PHASES:
        lines.append(f'  - "{tab}":')
        lines.append(f"      - course/phase-{key}.md")
        for f, title, _ in items:
            lines.append(f'      - "Day {numbered[f]} · {title}": {f}')
    lines.append("  - Reference:")
    for title, f in REFERENCE:
        lines.append(f"      - {title}: {f}")
    return "\n".join(lines) + "\n"


def write_nav():
    p = ROOT / "mkdocs.yml"
    s = p.read_text()
    start, end = "# >>> course-nav (generated by scripts/course.py)", "# <<< course-nav"
    if start in s:
        pre, rest = s.split(start, 1)
        _, post = rest.split(end, 1)
    else:
        pre, post = s.split("nav:", 1)[0], ""
    p.write_text(pre + start + "\n" + gen_nav() + end + post)


def write_roadmap():
    out = [
        "# Course Roadmap",
        "",
        '<div class="ssp-banner" markdown>',
        f"**{TOTAL} days, five phases, about 20–30 minutes a day.** Do one lesson a day, in order. Each",
        "lesson has a goal, the key language, a real conversation, and a practice task. Tick off each day",
        "as you finish it; your browser remembers your progress.",
        "</div>",
        "",
        '<p class="ssp-roadmap-progress">Your progress: 0 days done</p>',
        "",
        "## How each day works",
        "",
        '<div class="ssp-stack">',
        "<div>1. Learn <span>— read the lesson: key words, patterns and example sentences (10 min)</span></div>",
        "<div>2. Listen & read aloud <span>— read each conversation out loud, playing both roles (5 min)</span></div>",
        "<div>3. Practise <span>— do the exercises and check the answers (5 min)</span></div>",
        "<div>4. Role-play <span>— run the day's lesson with the course master prompt (5–10 min)</span></div>",
        "<div>5. Use it <span>— use at least one new sentence in real life today</span></div>",
        "</div>",
        "",
        "!!! tip \"Start with the master prompt\"",
        "    Copy the **course tutor prompt** from the [Master Prompt](../master-prompt.md) page into any AI",
        "    assistant, then just type `Start Day 1`. It will teach, role-play, quiz and correct you.",
        "",
        "## Phases",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]
    first = 1
    for key, _tab, full, icon, blurb, items in PHASES:
        last = first + len(items) - 1
        out += [f"-   :{icon}:{{ .lg .middle }} __{full}__", "", "    ---", "",
                f"    **Days {first}–{last}.** {blurb}", "",
                f"    [:octicons-arrow-right-24: Open phase](phase-{key}.md)", ""]
        first = last + 1
    out += ["</div>", "", "## All days", ""]
    for key, _tab, full, _icon, _blurb, items in PHASES:
        out += [f"### {full}", "", "| Day | Lesson | What you'll learn | Done |", "|---|---|---|---|"]
        for n, phase, (f, title, desc) in days():
            if phase[0] != key:
                continue
            out.append(f'| **{n}** | [{title}]({rel("course/index.md", f)}) | {desc} | '
                       f'<input type="checkbox" class="ssp-done" data-day="{n}" aria-label="Day {n} done"> |')
        out.append("")
    (DOCS / "course" / "index.md").write_text("\n".join(out))


def write_phase_pages():
    for n_phase, (key, _tab, full, icon, blurb, items) in enumerate(PHASES):
        out = [f"# {full}", "", '<div class="ssp-banner" markdown>', f"**{blurb}**", "</div>", "",
               '<div class="grid cards" markdown>', ""]
        for n, phase, (f, title, desc) in days():
            if phase[0] != key:
                continue
            out += [f"-   __Day {n} · {title}__", "", "    ---", "", f"    {desc}", "",
                    f"    [:octicons-arrow-right-24: Start Day {n}]({rel(f'course/phase-{key}.md', f)})", ""]
        out += ["</div>", ""]
        (DOCS / "course" / f"phase-{key}.md").write_text("\n".join(out))


if __name__ == "__main__":
    write_nav()
    write_roadmap()
    write_phase_pages()
    missing = [f for _, _, (f, _, _) in days() if not (DOCS / f).exists()]
    print(f"{TOTAL} days generated.")
    if missing:
        print("Missing lesson files:\n  " + "\n  ".join(missing))
