# The token ledger (add to the orchestrator prompt; one entry per phase)

Use for: knowing what the work cost, what was wasted, what was lost to redo, and what was forgotten, so the next run is cheaper.
Why: without it the only number anyone sees is the weekly total.

```text
Keep a ledger file beside the resume. One row per phase or review, with the lane's own token estimate (from the task notification or the lane's hand-back):
- SPENT FOR THE RESULT: tokens that produced something kept.
- WASTED: tokens that produced nothing kept (a review that confirmed what was known, a run on wrong settings, a lane that stalled).
- LOST TO REDO: tokens on work that had to be redone because an earlier step was wrong or out of order; name the earlier step.
- FORGOT: a thing that should have been checked or built earlier and was found later; its cause (consumer not checked, order wrong, plan gap) and the guard added.
At every milestone the orchestrator sums the four and writes one paragraph: where the tokens were useful, what effort level would have done, what changes next time.
```

## The first entry: the MotionBricks unarmed movement set (2026-11-07, approximate, from the lanes' own reports)

| Item | Tokens | Kind | Note |
|---|---|---|---|
| Plan v1, v2, v3 (one planner lane, resumed) | 1.5 M | spent | the plan in force |
| Plan reviews rounds 1 and 2, with verifiers | 7.7 M | 2.7 M spent, 5 M wasted | the reviewers found the gaps; the 80 verifiers mostly confirmed them |
| Reads script: built, reviewed, fixed, re-reviewed, fixed, re-reviewed (three rounds, two fix lanes, a floor lane) | 9.0 M | 2.5 M spent, 6.5 M lost to redo | cause: reads written to a list with synthetic self-tests; a floor defect under them; fixed by a recorded corpus of approved takes |
| Baseline built before the reads passed review (P0c) | 1.0 M | 0.5 M lost to redo | order: a later step's numbers on an unreviewed gate |
| Build lanes P0a to P5, sources, sides, feet, pictures, window import (about 20 lanes) | 14 M | spent | the branch's state |
| The Fable orchestrator | 59 percent of the weekly | partly wasted | reading every full output at xhigh; the fix is the context discipline block (summaries and compact tables only, a fresh orchestrator per milestone) and an Opus 5.5 orchestrator at high for day-to-day running |

Forgot-counter: 3. (1) The renderer cannot draw the body's shapes (sparse glTF accessors): found at the face phase, after every earlier render had shown a body without its correctives; guard: the consumer check (one frame drawn with a known shape before any phase that depends on it). (2) The review renderer replayed the match instead of drawing the recorded pose, and its build pointed at a deleted worktree so the tool never started: found after a phase's pictures were wrong; guard: a render selfcheck against the record on every picture. (3) The first motion video reached me only after eight phases; guard: the review points (06).

Order errors: 2. The stance built from a weapon guard's legs without my look first (cost: one re-pose and a second still); the baseline on unreviewed reads (cost: one re-read).
