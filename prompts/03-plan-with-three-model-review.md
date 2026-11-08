# Plan, then the three-model review, then the execution review

Use for: any work with 4 or more phases, anything other work will reuse (a pipeline, a character, a system), or anything where a wrong plan would redo 2 or more phases.
Why: the reviews found gaps the planner could not see (a jump that cleared nothing, bars from invented numbers, a look decision buried under four phases); each gap found here saves rework later.

```text
Make the plan before any step runs, and get it reviewed before any step runs; the one exception is a look decision the plan's inventory is built on (for a character's motion, the stance reference), run first as its own phase.

1. A fresh Opus 5.5 xhigh planner lane writes the plan from the records, in this form, working back from the end:
   A. The end result I judge, in one picture or video, and what "done" means per piece as measurable reads whose source is something I judged or a published reference; everything else measured and listed.
   B. The complete list of pieces, with what exists today and the read that proves each.
   C. The inputs and where they come from (ours only; licences named).
   D. The phases, one lane each, sized small/medium/hard (Haiku/Sonnet/Opus), each with inputs, exact steps, reads, hand-back folder, what it retires, what it cleans up, who sees what; an order table whose "starts after" column names an output, never a phase, and each phase's shares-with line (files, machine, GPU, the unfinished output it builds on); an empty shares-with line runs in parallel.
   E. Risks, each with its proof case and fallback.
   F. Out of scope, and what must stay untouched.
   G. Methods already failed twice (never repeated).
   H. Open questions for the reviewers.
   No dates, no durations, plain actions, rule IDs.
   Every numeric bar carries its derivation (a known-good measurement or the anatomy); every time I named in a reviewed video carries the move from that video's index; every bar is the magnitude it asserts on the frames it names, run on the data that will be judged; my order runs as I gave it unless a named dependency would redo something I approved; nothing I did not ask for (no variants, no extra files).

2. Review it with three independent models on ONE packet (my words unfiltered, the state, the record paths, a read-only checkout), spawned by the top-level window in one message (in two windows, the driver, block 14), never from inside a lane: AGY by the agy command and Grok by the grok command (each returns its command line and a raw output file with the CLI's version line, or it is refused), an Opus adversarial agent (high). Each returns findings in one schema: id, severity (blocker, major, minor), section, claim, evidence (file and line or a record), fix; plus "which phase waits on something it does not use", "what I asked for that the plan omits" and "what the plan decides for me that is mine". No verifiers: a reviewer's figure is a pointer the planner measures on the file before accepting or disputing it; a verified round (block 08) only when the orchestrator rules the plan is a gate. The planner answers every finding id (accepted with the change, disputed at file and line) and writes the next version; I (the orchestrator) rule only the disputes still standing.

3. The same three review HOW it is executed and reviewed (lane sizes, steps, reads, pictures, review cadence, the expected outcome per phase, and each fix's method before it is coded). Each round is a fresh planner lane started from the dispositions on disk. Rule, correct, then proceed.

4. Show me the plan's one-page summary and every look decision as a still before anything is generated on it.
```

RETIRED in this block (mb_movement_v2 R-45, R-53): "Verify blockers only, with one Sonnet verifier each" as the default (the planner measures; a verified round is block 08's, by the orchestrator's ruling).
