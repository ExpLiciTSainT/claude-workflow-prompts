# The forgetting and wrong-order guard (add to the plan and to every brief)

Use for: anything with more than one step; anything whose output another tool, renderer, exporter or person consumes later.
Why: this session built a face driver before checking that the renderer could draw the body's shapes (it could not: a file-format mismatch), and built a baseline on reads that had not passed their review. Both were "the next step's needs not checked now".

```text
Before the first step, and again at every hand-back, do the consumer check and the order check in writing:

CONSUMER CHECK: for every output this work makes, name who or what consumes it next (a renderer, an exporter, a game, a reviewer, me) and what that consumer requires: file format and encoding, accessor or storage form, size limits, licence, API version, the machine it runs on, the light it is seen under. Verify each requirement NOW with one real sample through the real consumer (one frame drawn, one file loaded, one call made), not from documentation alone. Write the result as a line per consumer.

ORDER CHECK: list every later step that depends on this one and what it needs from it. If a later step would have to be redone when this step's output changes, that step waits. Never run a later step's numbers on an earlier step's output that has not passed its review. A fix a recording needs (framing, camera, room, build), a test recording included, lands before that recording; it is never folded into a later phase.

END-RESULT CHECK: write the end result I judge in one sentence, then walk backwards from it to this step; any piece the end result needs that no step makes is added to the plan now, not when it is found missing.

KNOWN-REMAINING LIST: every hand-back ends with the list of what is still wrong or not built, one line each; the next brief starts from that list; the pointer to me carries it. A thing that is not on the list and was not shown is a forgotten thing: it is logged in the ledger's forgot-counter with its cause and the check that would have caught it, and that check is added to this guard.
```
