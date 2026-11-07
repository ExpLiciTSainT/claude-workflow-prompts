# The project folder: the files that are the memory, and the packet forms

Use for: setting up a goal's folder on the share before the director's first turn, and knowing what each file is for and who writes it.
Why: two small windows and throwaway operators work only if everything that matters is in files with one writer each; the two write races and the "who decides what Fable sees" gap the adversarial review found are closed by these forms.

```text
Create <project>/ before the first brief. One writer per file.

Written by the director window (Fable):
- REQUEST.md: the human's goal and every later instruction, verbatim, appended only, so a restarted window has them.
- VISION.md (one page): strategy, the story so far, what the human is happy with and not, reliability seen per lane, reviewer and tool.
- PLAN.md: the end result the human judges; the FULL INVENTORY of the finished result mapped to phases; the dependency order; milestones and checkpoints; pre-rulings ("on an all-pass proceed to <phase>"); each next phase marked "hangs on the verdict" or "free of rework and inside the order"; out of scope; methods already failed twice.
- RESUME.md: START HERE, done, running, next, what remains, decisions waiting on the human.
- BRIEFS/<phase>.md: goal, inputs, exact steps, reads, OUTPUTS each with its path, what each output's consumer needs, the review it must pass, operator model, lane model, hand-back folder, the items the human judges, cleanup, "closes milestone <m>" where it does.
- RULINGS/<phase>.md: `R-<n> | ruling | because reason`; a change says `supersedes R-<n>`.
- LESSONS.md: one line per lesson: cause category, what was missed, the check added, where it now lives.
- FOR_JOEL/POINTERS.md: written at a checkpoint, one line per item: ATTENTION NEEDED, the full path, the one thing to do; decisions in the form: what, why now, cost of yes, cost of no, the picture.
- FOLLOW_UPS.md: unrequested work found on the way: part, what, why, found by. Nothing on it starts without the human's yes.
- LEDGER.md: the milestone paragraph only, at a checkpoint, when nothing runs (the driver appends the rows).

Written by the driver window and its operators:
- STATE.md: DIRECTOR (the director window's address); RUNNING (by the driver: phase, brief, operator id; by the operator: lane id, worktree, windows, jobs; cleared by the operator on return); PROBLEM lines.
- PACKETS/<phase>_handback.md: the lane's 20 lines and the three reviewers' tables verbatim; cap 120 lines; over it a Sonnet digest plus the full tables at a path and the cut logged.
- PACKETS/<phase>_problem.md: what failed (one line), evidence path, the tries, what the lane and reviewers think the cause is, what it blocks.
- PACKETS/<phase>_workflow.md: the review workflow's result verbatim (driver).
- PACKETS/<milestone>_checkpoint.md (operator, on a brief that closes a milestone): every phase's status; items ready for the human with a path per view; what remains.
- LEDGER.md: one row per phase (driver, from the operator's return).

Traffic between the windows: one SendMessage per hand-off, first line one of the fixed forms in blocks 13 and 14 (director to driver: director, run, workflow, stop; driver to director: ready, packet, blocked, stopped, workflow done, human), 20 lines at most under it, always with the file path it refers to. Everything else is in the files.
```
