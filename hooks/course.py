"""MkDocs hook for the day-by-day course.

1. Renders ```dialogue fenced blocks as chat bubbles:

       ```dialogue
       Staff: Good morning! How can I help you?
       You: I'd like a ticket to Pune, please.
       (The clerk checks the system.)
       ```

   Lines are "Speaker: text". "You"/"Me" appear on the right. Lines in (brackets) are
   stage directions. **bold** and *italic* work inside a line.

2. Adds a "Day N of TOTAL" badge with a progress bar to every page whose nav title
   starts with "Day N · ".
"""
import html
import re

DIALOGUE = re.compile(
    r"^(?P<indent>[ \t]*)```dialogue[^\n]*\n(?P<body>.*?)^(?P=indent)```[ \t]*$",
    re.M | re.S,
)
SPEAKER = re.compile(r"^(?P<who>[A-Za-z][\w .'’/&()-]{0,28}):\s+(?P<text>.+)$")
DAY = re.compile(r"^Day (\d+) · (.+)$")
ME = {"you", "me"}

_total = 0


def _inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return text


def _render(match: re.Match) -> str:
    indent = match.group("indent")
    out = ['<div class="ssp-chat">']
    for raw in match.group("body").splitlines():
        line = raw.strip()
        if not line:
            continue
        m = SPEAKER.match(line)
        if line.startswith("(") or not m:
            out.append(f'<div class="ssp-chat-note">{_inline(line.strip("()"))}</div>')
            continue
        who = m.group("who").strip()
        side = "me" if who.lower() in ME else "them"
        out.append(
            f'<div class="ssp-msg ssp-{side}"><span class="ssp-who">{html.escape(who)}</span>'
            f'<span class="ssp-text">{_inline(m.group("text"))}</span></div>'
        )
    out.append("</div>")
    return "\n".join(indent + line for line in out)


def on_nav(nav, config, files):
    global _total
    _total = sum(1 for p in nav.pages if p.title and DAY.match(p.title))
    return nav


def on_page_markdown(markdown, page, config, files):
    markdown = DIALOGUE.sub(_render, markdown)
    m = DAY.match(page.title or "")
    if m and _total:
        n = int(m.group(1))
        phase = page.parent.title if page.parent else ""
        pm = re.match(r"^(\d+) · (.+)$", phase)
        if pm:
            phase = f"Phase {pm.group(1)} · {pm.group(2)}"
        pct = round(n * 100 / _total)
        key = page.file.src_uri[:-3]  # progress is stored per lesson page, not per day number
        badge = (
            f'<div class="ssp-day" data-day="{n}">'
            f'<div class="ssp-day-badge"><small>Day</small>{n}</div>'
            f'<div class="ssp-day-meta"><span>{html.escape(phase)} · Day {n} of {_total}</span>'
            f'<div class="ssp-progress"><span style="width:{pct}%"></span></div></div>'
            f'<label class="ssp-day-check"><input type="checkbox" class="ssp-done" data-day="{key}"> Done</label>'
            f"</div>\n\n"
        )
        footer = (
            "\n\n## Practise with AI\n\n"
            '!!! example "Today\'s role-play"\n'
            f"    Paste the [course tutor prompt](../master-prompt.md#1-course-tutor-use-every-day) into any AI\n"
            f"    assistant and type **`Start Day {n}`**. It will teach, role-play, quiz and correct you.\n"
            f"    Then tick **Done** at the top of this page.\n"
        )
        markdown = badge + markdown.rstrip("\n") + footer
    return markdown
