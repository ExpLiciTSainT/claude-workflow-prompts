# The project folder: the files that are the memory, and the packet forms

Use for: setting up a goal's folder on the share before the director's first turn, and knowing what each file is for and who writes it.
Why: two small windows and throwaway lanes work only if everything that matters is in files with one writer each.

```text
Create <project>/ before the first brief. One writer per file; a line for a file you do not own goes to its writer.

Written by the director window (Fable):
- REQUEST.md: the human's goal and every later instruction, verbatim, appended only.
- VISION.md (one page): strategy, the story so far, what the human is happy with and not, reliability seen per lane, reviewer and tool.
- PLAN.md: the end result the human judges; the FULL INVENTORY of the finished result mapped to phases; the order table with a "starts after" column naming an output, never a phase (a phase ahead of the human's order carries its dependency line); milestones; pre-rulings ("on an all-pass proceed to <phase>"); each next phase "hangs on the verdict" or "free of rework and inside the order"; out of scope; methods already failed twice.
- RESUME.md: START HERE, the pipeline step of each phase, done, running, next, what remains, decisions waiting on the human.
- BRIEFS/<phase>.md: the fields of block 13's brief, the pipeline step, its guard rows and the lane line included; its header's two lines first: "shares with the phases running beside it: files / machine / GPU / the unfinished output it builds on" and "starts when: <the specific output it needs>".
- RULINGS/<phase>.md: `R-<n> | ruling | because reason`; a change says `supersedes R-<n>`.
- LESSONS.md: one line per lesson: cause category, what was missed, the check added, where it now lives; a lesson a later ruling retires is marked RETIRED on its line.
- FOR_JOEL/POINTERS.md: at a checkpoint, one line per item: ATTENTION NEEDED, the full path, the one thing to do; decisions in block 09's form.
- FOLLOW_UPS.md: unrequested work found on the way: part, what, why, found by. Nothing on it starts without the human's yes.

Written by the driver window:
- STATE.md: DIRECTOR (the director's address); RUNNING per phase (phase, brief, lane id, model, the lane's RUNNING.md path), cleared when the lane's final return is relayed; PROBLEM lines; any line the director sends by "record".
- LEDGER.md: one row per phase (the lane's and each reviewer's tokens; wasted, redo, forgot from the lane's return; then, by "record" after the director's ruling, the effort columns in this order: lane kind, model, effort, blockers of its own making, verdict keep / raise / lower, block 00; a ledger header names them once); the director's milestone paragraph by "record".
- <hand-back folder>/review_gemini.md, review_grok.md, review_opus.md (and review_gemini_2.md on changed items): the reviewers the driver spawns write them, one line per finding; the gemini and grok files open with the CLI command and the raw output's path; the gemini file names a raw that `outside_review.py verify` accepted (its stamp).
- PACKETS/<phase>_workflow.md: a verified review's result verbatim.
- The review folder: the driver copies the staged items on "place", never replacing a file.

Written by the phase lane:
- <hand-back folder>/RUNNING.md: its jobs, worktree and windows before every wait; "waiting for answer" after the first return; cleared at the final return.
- <hand-back folder>/RECORD.md: what was done, every number with the file it came from, the answer to every finding.
- <hand-back folder>/for_review/: the items the human judges, staged, never placed by the lane.
- PACKETS/<phase>_handback.md: INTERIM before any forced return, FINAL after the answer pass; at most 120 lines: the 20-line return, the counts per reviewer, one line "blockers of its own making: <n>" (the accepted blockers in the review files, counted before the answer pass; block 00), every standing dispute one line each with file and line, the staged items, the paths, the ledger; over 120, the tables at a path and the cut logged.
- PACKETS/<phase>_problem.md: what failed (one line), evidence path, the tries, the cause, what it blocks.
- PACKETS/<milestone>_checkpoint.md (a brief that closes a milestone): every phase's status; items ready for the human with a path per view; what remains.

The review folder: only unreviewed items; videos named by what moves, stills by what they show with "still" in the name; one folder per round; one file per motion at a time; a motion that passes again gets the next number once the file the human ruled on has left the folder in the turn of the verdict; nothing is overwritten.
Merges: a lane pushes its branch and opens its PR, never merges; the director rules each merge and sends "merge"; the driver merges; the next brief is written on the merged head.
Traffic between the windows: one SendMessage per hand-off, first line one of the fixed forms (director to driver: director, run, record, merge, place, workflow, stop; driver to director: ready, packet, recorded, merged, placed, blocked, stopped, workflow done, human), 20 lines at most under it, always with the file path it refers to. Driver to lane: answer, continue. Everything else is in the files.
```

RETIRED in this block (mb_movement_v2 R-45 and the `record` form): "Written by the driver window and its operators"; the director writing LEDGER.md's milestone paragraph itself; the lane writing STATE.md's RUNNING line; a merge as the next brief's first step.
