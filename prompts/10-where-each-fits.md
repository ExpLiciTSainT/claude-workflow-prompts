# Where each workflow fits

Use for: choosing the workflow and the review depth per kind of work.
Why: the cost that matters is rework, not tokens; the review depth should match how much rework a miss would cause.

```text
KIND OF WORK            WORKFLOW                       WHY
Complicated, multi-step  A (ultracode) for the plan,    A wrong plan costs every phase; a wrong phase costs one. Review the plan deeply, the phases lightly.
pipeline (a character,   then B (lean) for the phases
a system, a map)
Animation and motion     B, with pictures at every      Motion faults are seen, not computed: AGY on strips and videos from every view beats any read; one video after the first gait, not after eight.
                         phase and me after the first
Coding (a feature,       B or C; tests first; Opus for  A test is cheaper than a review; a code path that changes behaviour (a server rule, a scheduler) gets the Opus adversarial read once.
a fix)                   code paths, Sonnet for the rest
A read, a check, a gate  A for its first version:       Everything after it trusts it; it is built test-first on recorded known-goods and known-bads, and reviewed as a gate.
(something that judges   corpus first, then review
later work)
Decision making (a       The decision form (09) with     My time is the scarce thing; one image with both options and the cost of yes and no, nothing else.
look, a number, a buy)   facts from the real output
Research (a tool, an     AGY and Grok first (free),      Research is reading; the free models read as well as Opus; Opus only to rule.
SDK, a vendor claim)     one Opus summary with sources
Docs, exports, data,     C: one Sonnet lane, AGY reads  Mechanical work with a clear end; no plan round.
pictures                 the result
Tool-driven work         The tool's own operator first,  A custom script for something the tool does is a defect; a visible window step is faster and reviewable.
(Blender, an exporter)   in its own window, captured
Anything that failed     Stop. Two tries close a method. A third try of the same thing is the single largest waste this session saw.
twice
```
