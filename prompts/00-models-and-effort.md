# Models, effort levels, and making sure the newest family is used

Use for: picking the model and effort before any prompt below, and catching an agent that silently runs an older model.
Why: the orchestrator's reading volume and the per-finding verifiers were the cost drivers, not the lanes' effort; and an agent on an older family gives older results at the same price.

```text
MODEL AND EFFORT (set with /model and /effort in the session; per agent in a brief with model and effort)

Fable 5.1 (claude-fable-5-1), xhigh    Orchestrator only for: a plan with 4 or more phases, a gate (a read, a check, a schema that later phases trust), or a ruling after two failed methods. Nothing else.
Opus 5.5 (claude-opus-5-5), high       Day-to-day orchestrator; hard lanes (code paths, tool settings); every hand-back review.
Opus 5.5, xhigh                        Writing a plan; a lane stuck twice; building a gate.
Sonnet 5.5 (claude-sonnet-5-5), medium Mechanical lanes: exports, scripts from a spec, docs, pictures, data tables, digests, cleanup with a log.
Haiku 5.5 (claude-haiku-5-5), low      Small bounded tasks: a file move, a log line, a list from a folder.
AGY (Gemini) and Grok                  Reviewers first and often: your own subscriptions, no Claude tokens. AGY reads pictures and frame strips; Grok reads code and numbers (pictures only where its CLI accepts images: check once and record).

THE NEWEST FAMILY, EVERY TIME:
- At the start of a session: /model shows the model; it must be the Claude 5 family (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5). If it is not, set it before anything runs.
- In every agent brief: name the model by family alias (opus, sonnet, haiku), which resolves to the newest; never an old dated ID.
- Every lane's hand-back states the model it ran on, and the orchestrator checks it: a lane that reports anything but the 5 family is a defect and its work is not trusted until re-run.

EFFORT REVIEW (the only full statement of the rule; every other file cites it. A lane kind's effort is its current verdict; the defaults in RULES below are a kind's starting verdict):
- Lane kinds: planner; product code (changes Game/, Engine/ or a shared script another phase reads); docs; mechanical; adversarial reviewer; driver. The brief's lane line names the kind. A kind not listed starts at the RULES default for what it does. The kind is the heaviest thing the lane touches: a lane that edits a shared script another phase reads is product code, whatever else it does (mb_movement_v2 R-80).
- When: at every packet word (done, all-pass, checkpoint, blocked, stopped, a fix round) and in a table at every checkpoint, by the director, from the ledger and the review counts.
- Count: blockers of the lane's own making are the accepted blockers in the review files, counted before the answer pass; the packet carries that count on its own line.
- Ladder, one line across models: Sonnet low -> Sonnet medium -> Sonnet high -> Opus high -> Opus xhigh, one step at a time (a raise from Sonnet high is the model switch to Opus high); above Opus xhigh is the director's three-model look (block 13).
- Raise one step for that kind on a blocker of the lane's own making, a bar failed twice (the lane's run and its answer pass together), or a blocked or stopped return.
- A kind with a fix round pending holds its level until that round's review rules; the ruling then raises or keeps it.
- Lower one step for the next lane of that kind after two lanes of that kind in a row returned with no blocker of their own and redo 0.
- The lowered lane's first packet is the proof: a failed bar, redo above 0 or a blocker of its own making sends the kind back up one step and holds it there until the next checkpoint.
- The lowering proof (the first lane at a lowered level) is never a lane with a Joel item; once the proof passed, a Joel-item lane may run at that level.
- The verdict is keep, raise or lower for the kind, one line in the ledger (block 11), copied to the next brief's lane line.

RULES: one lane per phase, a fresh lane at each phase boundary (a lane re-reads its whole history every step); a lane over about 0.7 M tokens is split; verifiers only in a verified round the orchestrator rules (block 08); the lane's model and effort are the orchestrator's call per lane, written on its brief, by default (a kind's starting verdict, which EFFORT REVIEW then moves) Opus 5.5 xhigh for a planner or a lane stuck twice, Opus 5.5 high for a phase that changes the product's code or a shared script another phase reads, Sonnet 5.5 medium otherwise, the stronger when two apply; nothing at xhigh that a written brief can make medium.
```
