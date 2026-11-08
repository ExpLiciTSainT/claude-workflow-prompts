# The project folder: the files that are the memory, and the packet forms

Use for: setting up a goal's folder on the share before the director's first turn, and knowing what each file is for and who writes it.
Why: two small windows and throwaway lanes work only if everything that matters is in files with one writer each.

```text
Create <project>/ before the first brief. One writer per file; a line for a file you do not own goes to its writer.

Written by the director window (Fable):
- REQUEST.md: the human's goal and every later instruction, verbatim, appended only.
- VISION.md (one page): strategy, the story so far, what the human is happy with and not, reliability seen per lane, reviewer and tool.
- PLAN.md: the end result the human judges; the FULL INVENTORY of the finished result mapped to phases; the dependency order (a phase ahead of the human's order carries its dependency line); milestones; pre-rulings ("on an all-pass proceed to <phase>"); each next phase "hangs on the verdict" or "free of rework and inside the order"; out of scope; methods already failed twice.
- RESUME.md: START HERE, done, running, next, what remains, decisions waiting on the human.
- BRIEFS/<phase>.md: the fields of block 13's brief, the lane line included.
- RULINGS/<phase>.md: `R-<n> | ruling | because reason`; a change says `supersedes R-<n>`.
- LESSONS.md: one line per lesson: cause category, what was missed, the check added, where it now lives.
- FOR_JOEL/POINTERS.md: at a checkpoint, one line per item: ATTENTION NEEDED, the full path, the one thing to do; decisions in block 09's form.
- FOLLOW_UPS.md: unrequested work found on the way: part, what, why, found by. Nothing on it starts without the human's yes.

Written by the driver window:
- STATE.md: DIRECTOR (the director's address); RUNNING per phase (phase, brief, lane id, model); PROBLEM lines; any line the director sends by "record". The lane writes only its own RUNNING line (jobs, worktree, windows) and clears it on its final return.
- LEDGER.md: one row per phase (the lane's and each reviewer's tokens; wasted, redo, forgot from the lane's return); the director's milestone paragraph by "record".
- <hand-back folder>/review_gemini.md, review_grok.md, review_opus.md: the reviewers the driver spawns write them, one line per finding; review_gemini.md opens with the agy command and the raw output's path.
- PACKETS/<phase>_workflow.md: a verified review's result verbatim.

Written by the phase lane:
- <hand-back folder>/RECORD.md: what was done, every number with the file it came from, the answer to every finding.
- PACKETS/<phase>_handback.md: INTERIM before any forced return, FINAL after the answer pass; at most 120 lines: the 20-line return, the counts, the paths, the ledger; over 120, the tables at a path and the cut logged.
- PACKETS/<phase>_problem.md: what failed (one line), evidence path, the tries, the cause, what it blocks.
- PACKETS/<milestone>_checkpoint.md (a brief that closes a milestone): every phase's status; items ready for the human with a path per view; what remains.

The review folder: only unreviewed items; videos named by what moves, stills by what they show with "still" in the name; one folder per round.
Merges: a lane pushes its branch and opens its PR, never merges; the director rules each merge; the merge is the first step of the next brief that builds on it.
Traffic between the windows: one SendMessage per hand-off, first line one of the fixed forms (director to driver: director, run, record, workflow, stop; driver to director: ready, packet, recorded, blocked, stopped, workflow done, human), 20 lines at most under it, always with the file path it refers to. Driver to lane: answer, continue. Everything else is in the files.
```

RETIRED in this block (mb_movement_v2 R-45 and the `record` form): "Written by the driver window and its operators"; the director writing LEDGER.md's milestone paragraph itself.
