# Review and fix loop (AGY, Opus, Grok on every hand-back; fix once; close on the second failure)

Use for: every hand-back, before the orchestrator builds on it or shows it to me.
Why: an independent eye on the real output caught what the lane's own reads passed (a skip, a frozen arm, a replayed render); a bounded loop stops it costing more than the work; and a test only proves the mechanism it tests, never what I see.

```text
Review this hand-back before anything is built on it or shown to me. Three reviewers on EVERY hand-back, each on the real output, not the lane's description of it:

1. AGY (Gemini), the motion and picture eye: the held frames from every view, and for anything that moves, STRIPS of consecutive frames at speed (10 a second through a whole cycle, every view) cut from the video, plus the video file itself where the tool accepts video; the one question "what is wrong, ranked by body part and view; does it read as a real person; where does it not?". Its read is recorded beside the item.
2. Opus 5.5 at high, adversarial: the same pictures and strips, the numbers table, the hand-back's claims against its files; it tries to refute what the lane claims. On a gate (a read, a check, a server rule, a plan change) it runs at xhigh.
3. Grok, the code and numbers eye: the files changed, the reads, the tests, the settings against the vendor's own documentation; findings with file and line (pictures too where its CLI takes images).
4. No per-finding verifiers unless a blocker's evidence is disputed; then ONE Sonnet verifier for that finding only.
5. The orchestrator rules in writing from the reviewers' compact tables (accepted, disputed with the file and line, deferred with why); it does not re-read the lane's full output. The accepted findings go to the SAME lane (resumed) for one fix pass; AGY re-reads the fixed pictures and strips.
6. A second failure of the same outcome closes the method: the orchestrator decides the next method or states the fault as known on the next pointer to me; never a third try of the same thing.
7. A test proves a mechanism; it never replaces the holistic look. Every hand-back gets the picture and strip review even when its tests pass, and I see the whole thing moving at the review points, because what I experience is the only bar that counts.
8. Nothing reaches my review folder until AGY and Opus have read it; the pointer lists what is known wrong so I judge the rest.
```
