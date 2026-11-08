# Where each workflow fits (a prompt block, and the reasons)

Use for: telling the orchestrator how to pick the workflow and the review depth for a kind of work.
Why: the cost that matters is rework, not tokens; the review depth should match how much rework a miss would cause.

```text
Pick the workflow by the kind of work, and say which you picked and why:

1. A complicated, multi-step piece (a character, a pipeline, a system, a map): the full plan with the plan review (Opus and Grok, AGY on its pictures) and the execution review (ultracode for those two reviews), then the lean workflow for the phases. A wrong plan costs every phase; a wrong phase costs one.

2. Animation and motion: the lean workflow, with pictures AND strips of consecutive frames at speed from every view at every phase, AGY and Opus reading them, and me seeing stills for every look decision early and the first video as soon as no later shared fix would change it, never after eight phases without a picture. Motion faults are seen, not computed.

3. Coding (a feature, a fix): the lean workflow; tests first for the mechanism; Opus for a code path that changes behaviour (a server rule, a scheduler, a renderer), Sonnet for the rest; one Opus adversarial read on behaviour changes. The holistic look still happens on the result.

4. A read, a check, a gate (anything later work trusts): built test-first on recorded known-goods and known-bads, then reviewed as a gate (ultracode allowed). Everything after it trusts it.

5. A decision that is mine (a look, a number, a purchase): the decision form, with the facts from the real output and one image with both options. My time is the scarce thing.

6. Research (a tool, an SDK, a vendor claim): AGY and Grok first (free), one Opus summary with sources, then a spike on our own asset before anything is built on it.

7. Docs, exports, data, pictures: one Sonnet lane with a written brief; AGY and Opus look at the result once. No plan round.

8. Tool-driven work (Blender, an exporter, a renderer): the tool's own operator first, in its own window, each step captured; a custom script for something the tool does is a defect.

9. Anything that has failed twice: stop. Two tries close a method; a third try of the same thing is the single largest waste seen.
```

## Why each, in one line

- Multi-step: the plan is the cheapest place to find a gap; every phase after it inherits the gap.
- Motion: a number cannot see a skip or a dead arm; a strip at speed from the side can, and so can I.
- Coding: a test is cheaper than a review for the mechanism, and useless for what the user experiences.
- A gate: a wrong gate makes every later judgement wrong; it is the one thing worth the expensive review.
- Decisions: one image, both options, the cost of yes and no, nothing else.
- Research: reading is cheap on the free models; judgement is what Opus is for.
- Mechanical: a clear brief and a clear end; no planning overhead.
- Tool-driven: the tool's own way is faster, reviewable in the window, and already debugged by its vendor.
- Failed twice: the pattern behind most wasted tokens.

RETIRED in this block (mb_movement_v2 R-34): "the first video after the first gait phase".
