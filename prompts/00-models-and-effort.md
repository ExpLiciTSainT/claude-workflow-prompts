# Models, effort levels, and making sure the newest family is used

Use for: picking the model and effort before any prompt below, and catching an agent that silently runs an older model.
Why: the orchestrator's reading volume and the per-finding verifiers were the cost drivers, not the lanes' effort; and an agent on an older family gives older results at the same price.

```text
MODEL AND EFFORT (set with /model and /effort in the session; per agent in a brief with model and effort)

Fable 5.1 (claude-fable-5-1), xhigh    Orchestrator only for: a plan with 4 or more phases, a gate (a read, a check, a schema that later phases trust), or a ruling after two failed methods. Nothing else.
Opus 5.5 (claude-opus-5-5), high       Day-to-day orchestrator; hard lanes (code paths, tool settings, anything that failed once); every hand-back review.
Opus 5.5, xhigh                        Writing a plan; a lane stuck twice; building a gate.
Sonnet 5.5 (claude-sonnet-5-5), medium Mechanical lanes: exports, scripts from a spec, docs, pictures, data tables, digests, cleanup with a log.
Haiku 5.5 (claude-haiku-5-5), low      Small bounded tasks: a file move, a log line, a list from a folder.
AGY (Gemini) and Grok                  Reviewers first and often: your own subscriptions, no Claude tokens. AGY reads pictures and frame strips; Grok reads code and numbers (pictures only where its CLI accepts images: check once and record).

THE NEWEST FAMILY, EVERY TIME:
- At the start of a session: /model shows the model; it must be the Claude 5 family (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5). If it is not, set it before anything runs.
- In every agent brief: name the model by family alias (opus, sonnet, haiku), which resolves to the newest; never an old dated ID.
- Every lane's hand-back states the model it ran on, and the orchestrator checks it: a lane that reports anything but the 5 family is a defect and its work is not trusted until re-run.

EFFORT REVIEW (the effort for each kind of lane is the current verdict, not a fixed choice):
- When: at every packet ruling and in a table at every checkpoint, by the director, from the ledger and the review counts.
- Ladder: low -> medium -> high -> xhigh, one step at a time.
- Raise one step for that lane kind when its packet carries a blocker of the lane's own making or a bar failed twice.
- Lower one step for the next lane of that kind after two lanes of that kind in a row returned with no blocker of their own and redo 0.
- The lowered lane's first packet is the proof; a blocker of its own making sends that kind back up and keeps it there for the round.
- A lane with a Joel item never runs lowered the first time.
- The verdict is keep, raise or lower, one line in the ledger (block 11).

RULES: one lane per phase, a fresh lane at each phase boundary (a lane re-reads its whole history every step); a lane over about 0.7 M tokens is split; verifiers only in a verified round the orchestrator rules (block 08); the lane's model and effort are the orchestrator's call per lane, written on its brief, by default Opus 5.5 xhigh for a planner or a lane stuck twice, Opus 5.5 high for a phase that changes the product's code or a shared script another phase reads or anything that failed once, Sonnet 5.5 medium otherwise, the stronger when two apply; nothing at xhigh that a written brief can make medium.
```
