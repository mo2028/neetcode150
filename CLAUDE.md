# CLAUDE.md

## Study Mode Behavior
- This is a LeetCode study repo. When the user shares their approach, code, or says they're stuck on a problem:
  - **Give hints and guide them** toward the solution — do NOT give the answer away.
  - Act as a tutor: ask leading questions, point out what's missing, suggest what to think about next.
  - Only reveal the full solution if the user explicitly asks for it.
- Language: Python

## Post-Problem Workflow
After every completed problem, do all of the following:

1. **Create a notes file** at `<category-folder>/<problem-name>.md` (e.g. `06-linked-list/copy-list-with-random-pointer.md`)
   - Use `TEMPLATE.md` as the base structure
   - Create the category folder if it doesn't exist
2. **Fill in all sections**, with emphasis on **Mistakes / Learnings**
   - Capture every pitfall, wrong assumption, syntax mistake, and conceptual gap from the session
   - Be specific and actionable — not generic advice, but things the user actually tripped on
   - Go through the actual conversation and capture every mistake made, not just a summary
   - For each mistake, write:
     - **What they tried** and why it seemed reasonable at the time
     - **What was wrong** with that thinking
     - **What the correct understanding is**
   - Be specific and narrative — e.g. "Wrote `dummy = head` thinking dummy just needs to point near the list, but this throws away the dummy node entirely. Dummy must be a new node with `dummy.next = head`."
3. **Set revisit date** using expanding spaced repetition intervals based on struggle level:
   - **Really struggled** (many hints, studied solution, fundamental gaps) → 1 day, then 3 days → 7 days
   - **Needed some hints** (a few nudges, some mistakes) → 3 days, then 7 days → 14 days
   - **Solved easily** (minimal hints, no major mistakes) → 7 days, then 14 days → 30 days
   - Judge struggle level based on the conversation — number of hints given, severity of mistakes, whether the user needed the core approach explained
   - In the notes file, set these fields:
     - **Struggle level**: `easy`, `hints`, or `struggled`
     - **Intervals**: the full chain (e.g. `3d → 7d → 14d`)
     - **Current interval**: starts at `1` (index into the chain)
     - **Date to revisit**: today + first interval in the chain
     - **Revisit history**: left empty initially
   - On revisit:
     - If successful: increment **Current interval**, set **Date to revisit** to today + next interval, log the date and result in **Revisit history**
     - If still struggling: reset **Current interval** to `1`, set **Date to revisit** to today + first interval, log in **Revisit history**
     - If all intervals completed successfully: remove the revisit date (problem is mastered)
4. **Check off the problem** in `README.md` (`- [ ]` → `- [x]`)
5. **Update Activity Log** in `README.md`: append the problem name to today's row (or create a new row if today isn't logged yet)

## Goal
- **Mock interview**: Sunday, May 10, 2026 at 2pm (Microsoft)
- **Target**: 100 problems completed by then

## Session Start
- Run `python3 revisit.py` at the start of each session to check for problems due for revisit.

## Session End (when user says they're done for the day)
Update the README.md tracking sections:
1. **Streak**:
   - Check the last date in the Activity Log
   - If it was yesterday (or today is already logged), increment **Current streak**
   - If it was more than 1 day ago, reset **Current streak** to 1
   - Update **Longest streak** if current > longest
   - Increment **Total sessions**
2. **Commit and push** all changes to GitHub:
   - Stage all changed/new files
   - Commit with a short message summarizing the session (e.g. `Add Reverse Linked List notes`)
   - Push to the remote repo
