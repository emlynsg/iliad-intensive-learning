"""Create blank notes from schedule metadata; never read course solution blocks."""
import json
from pathlib import Path
import subprocess

import yaml

root = Path(__file__).resolve().parents[1]
course = root / "iliad-intensive"
schedule = yaml.safe_load((course / "schedule.yaml").read_text(encoding="utf-8"))
commit = subprocess.check_output(["git", "-C", str(course), "rev-parse", "HEAD"], text=True).strip()
notes = root / "worksheets"
notes.mkdir(exist_ok=True)
index = [
    '---\ntitle: "Iliad worksheets"\n---\n',
    "Follow the course materials in order and write your attempts in the linked notes pages. "
    "These are blank working pages; the official worksheets remain the source of the questions.\n",
    "Start with **Foundations: Prerequisites**, then **A.1: AI Alignment Introduction**.\n",
    "Math rendering check (works offline): $\\sum_{k=1}^n k = \\frac{n(n+1)}{2}$.\n",
    f"Schedule: [local source](iliad-intensive/schedule.yaml), commit `{commit[:12]}`. "
    "[Live curriculum](https://iliad-intensive.org/) · "
    "[Material availability](https://iliad-intensive.org/admin/status/)\n",
]
count = 0
for cluster in schedule["clusters"]:
    index.append(f"\n## {cluster['label']}\n")
    for day in cluster.get("days", []):
        code = str(day["code"])
        index.append(f"\n### {code}: {day['title']}\n")
        slugs = day.get("worksheets", [])
        if not slugs:
            index.append("This day has no worksheet in this checkout; use its course document.\n")
        for slug in slugs or ["notes"]:
            filename = f"{code.replace('.', '')}-{slug}.qmd"
            title = f"{code}: {day['title']}" + (f" — {slug.replace('-', ' ').title()}" if len(slugs) > 1 else "")
            links = [f"[Course document]({day['doc']})"]
            if slugs:
                links.insert(0, f"[Official worksheet](https://iliad-intensive.org/{cluster['urlSlug']}/{slug}/)")
                sources = [p for p in (course / "tex" / slug).glob("main.*") if p.suffix in (".tex", ".mdx", ".md")]
                assert sources, f"No worksheet source found for {slug}"
                links.append(f"[Local source](../iliad-intensive/tex/{slug}/{sources[0].name}) (may contain solutions)")
            for field, label in [("sourceUrl", "Additional course repository"), ("slides", "Slides")]:
                if day.get(field):
                    links.append(f"[{label}]({day[field]})")
            path = notes / filename
            if not path.exists():
                path.write_text("---\ntitle: " + json.dumps(title, ensure_ascii=False) + "\n---\n\n" +
                    " · ".join(links) + "\n\n## Notes\n\n<!-- Definitions and assumptions in your own words. -->\n\n"
                    "## Attempts and proofs\n\n<!-- Add the exercise number, your attempt, and LaTeX mathematics here. -->\n\n"
                    "## Questions to revisit\n", encoding="utf-8")
            index.append(f"- [ ] [{title} — my notes](worksheets/{filename})\n")
            count += 1
index_path = root / "index.qmd"
if not index_path.exists():
    index_path.write_text("\n".join(index), encoding="utf-8")
else:
    print("Preserved existing index.qmd (including your checkboxes); add new links there if the schedule changed.")
print(f"Verified {count} worksheet/day notes pages from schedule {commit[:12]}")
