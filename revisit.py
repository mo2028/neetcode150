import os
import re
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
today = date.today()

to_revisit = []

for dirpath, _, filenames in os.walk(ROOT):
    for f in filenames:
        if not f.endswith(".md") or f in ("README.md", "TEMPLATE.md"):
            continue
        filepath = os.path.join(dirpath, f)
        with open(filepath) as fh:
            content = fh.read()

        match = re.search(r"\*\*Date to revisit\*\*:\s*(\d{4}-\d{2}-\d{2})", content)
        if not match:
            continue

        revisit_date = date.fromisoformat(match.group(1))
        revisited = bool(re.search(r"\*\*Revisited\?\*\*:\s*Yes", content))

        if not revisited and revisit_date <= today:
            category = os.path.basename(dirpath)
            problem = f.replace(".md", "").replace("-", " ").title()
            to_revisit.append((revisit_date, category, problem, filepath))

to_revisit.sort()

if to_revisit:
    print(f"Problems to revisit today ({today}):\n")
    for revisit_date, category, problem, filepath in to_revisit:
        overdue = (today - revisit_date).days
        tag = f" ({overdue}d overdue)" if overdue > 0 else ""
        print(f"  - {problem} [{category}]{tag}")
        print(f"    {filepath}\n")
else:
    print(f"No problems to revisit today ({today}). You're all caught up!")
