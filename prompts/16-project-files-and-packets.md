# The project folder: the files that are the memory, and the packet forms

Use for: setting up a goal's folder on the share before the first director call, and knowing what each file is for and who writes it.
Why: a fresh director per call and a fresh operator per phase work only if everything that matters is in files with one writer each; the two races and the "who decides what Fable sees" gap the adversarial review found are closed by these forms.

```text
Create <project>/ with these files before the first call. One writer per file.

Written by the window:
- REQUEST.md: the human's goal and every later instruction, verbatim, appended only, in sequence (no dates shown).
- ANSWERS.md: the human's answers to decisions, verbatim.
- RULES.md: the human's standing rules, one file, built once from the project's instructions (and any memory files of theirs); the director reads it on every call and it overrides the blocks.

Written by the director (through director.py):
- VISION.md (one page): strategy, the story so far, what the human is happy with and not, reliability seen per lane, reviewer and tool.
- PLAN.md: the end result the human judges; the FULL INVENTORY of the finished result mapped to phases; the dependency order; milestones and checkpoints; pre-rulings ("on an all-pass proceed to <phase>"); each next phase marked "hangs on the verdict" or "free of rework and inside the order"; out of scope; methods already failed twice.
- RESUME.md: START HERE, done, running, next, what remains, decisions waiting on the human.
- BRIEFS/<phase>.md: goal, inputs, exact steps, reads, what the output's consumer needs, the review it must pass, hand-back folder, cleanup.
- RULINGS/<phase>.md: `R-<n> | ruling | because reason`; RULINGS/INDEX.md is kept by director.py; a change says `supersedes R-<n>`.
- LESSONS.md: one line per lesson: cause category, what was missed, the check added, where it now lives.
- FOR_JOEL/POINTERS.md: one line per item: ATTENTION NEEDED, the full path, the one thing to do; decisions in the form: what, why now, cost of yes, cost of no, the picture.
- FOLLOW_UPS.md: unrequested work found on the way: part, what, why, found by. Nothing on it starts without the human's yes.

Written by the operator:
- STATE.md: RUNNING (phase, lane id, worktree, windows, jobs), REDIRECT_PENDING, PROBLEM lines.
- PACKETS/<phase>_handback.md: the lane's 20 lines and the three reviewers' tables verbatim; cap 120 lines; over it a Sonnet digest plus the full tables at a path and the cut logged.
- PACKETS/<phase>_problem.md: what failed (one line), evidence path, the two tries, what the lane and reviewers think the cause is, what it blocks.
- PACKETS/<milestone>_checkpoint.md: every phase's ruling status; items ready for the human with a path per view; decisions that are theirs; what remains.
- PACKETS/<item>_approval.md: the human's yes verbatim, the item, its method as run, the catches on the way.
- LEDGER.md rows per phase (director.py appends its own rows per call).

Written by director.py: DIRECTOR/<seq>_<kind>.md, the whole of every director answer.
```
