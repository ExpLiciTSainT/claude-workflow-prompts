# Director and operator: the setup that keeps Fable 5.1's judgement and drops its context cost (plan v1, for adversarial review)

## Joel's goal, in his words (the bar this plan is judged against)
- "Fable 5.1 orchestrators, is the director, and the decision maker as the results are massively better than an individual opus orchestrator."
- "The main CLI holds the total vision, strategy, story, keeping the sub agents align on their work to deliver the intended results."
- "What I don't want is for all that context to end up in the main fable 5.1 CLI window as that is a HUGE hit in cost with almost zero benefits."
- "If the workflow reviewed their work ... opus, agy, and grok review and thought it was ready for me to review, then it should be trusted, the orchestrator / director creates the review content (pictures or video) for me."
- "The main CLI should be as clean as possible, and should never do work itself. It should only think about what work is needed in what order, who should do that work, and how ... to ensure once the full goal is done, the human is happy, or at each check point."
- "If there is a problem, the main cli should determine why that problem exists (order of work, the agent, the workflow, a missing review process, failing to have a human review earlier, failed planning, dependency tracking, or any other issue) ... document the lessons learned" and generalise them (the face-joints example: plan from the full inventory of the end result, not from the words of the request).
- "I can't manually clear this, as I let you run overnight ... give me the best setup to reduce the wasted tokens ... but yield the results that I get from Fable 5.1."
- Standing orders still bind: his order as given, nothing unrequested without his yes (FOLLOW_UPS while away), no dates or estimates, numbered direct answers, never ask him to choose a method, every approval captured, cleanup mandatory, full paths.

## Facts established (probes run in this session, 2026-11-07)
1. A sub-agent spawned with the Agent tool can itself spawn sub-agents and wait for them (probe: Haiku parent, Haiku child, returned the child's text).
2. A headless run (`claude -p`) started from a script can spawn a sub-agent, wait for it and print the result (12 s round trip; flags available: `--model`, `--effort`, `--append-system-prompt-file`, `--system-prompt-file`, `--allowedTools`, `--permission-mode`, `--add-dir`, `--settings`, `--output-format`).
3. A sub-agent's transcript never enters its parent's context; only its return does. The parent's cost is its own turns times its own context; each turn re-sends the whole context.
4. Sub-agents receive the project's CLAUDE.md; a headless run receives the CLAUDE.md of the directory it is started in, so a lean directory gives a lean fixed cost per call.
5. In this session the Fable orchestrator was 59 percent of the 93 percent weekly spend: hundreds of mechanical turns (waiting on renders, checking logs, digesting transcripts, writing briefs and rulings) on a context that grew for the whole session, plus plan versions, review tables and pictures read in-line.
6. Hooks (PreToolUse spot check, two-strike, SessionStart) are session-wide and apply inside sub-agents and headless runs.

## The shape (one window, one script, files as the memory)

### Roles
- **Director = Fable 5.1 at xhigh, never a persistent window.** Every director call is a fresh headless run made by `director.py`, with its context assembled from files: Joel's request verbatim (REQUEST.md, with his later words appended), PLAN.md, RESUME.md, the rulings index, LESSONS.md, LEDGER.md, and the one packet it is asked to judge. It thinks about order, dependencies, who does what and how, rules on hand-backs, root-causes problems, writes lessons, and assembles the checkpoint for Joel. It writes files (a ruling, a brief, a lessons line, resume lines) and prints a summary of at most 20 lines. It never runs a lane, a render, a log check, a merge or a cleanup. Call kinds: PLAN, RULE, PROBLEM, CHECKPOINT, and REDIRECT (Joel said something new).
- **Operator = Opus 5.5 at high, one fresh sub-agent per milestone**, spawned by the window. It runs the director's plan phase by phase: one fresh lane per phase (Sonnet medium for mechanical, Opus high for hard), the three reviews on every hand-back (AGY on strips at speed and video, an Opus adversarial agent, Grok on code and numbers; the Workflow tool with verifiers only when the measured trigger is met), all chores (renders, waits, logs, merges, cleanup), and the packets. At every decision it calls `director.py` and follows the ruling. It never decides direction. It returns at most 20 lines to the window when the milestone is at a checkpoint or blocked.
- **Window = Opus 5.5 at high, interactive, in the repo; a thin loop.** It starts the first director call (PLAN), spawns the operator agent for the milestone, and waits. It relays Joel's words: anything he types is appended verbatim to REQUEST.md and triggers a director REDIRECT call. Its context grows by the operator's 20-line returns and Joel's lines only, so it never needs clearing within a project phase. It does no work itself.
- **Lanes, reviewers**: unchanged from the existing blocks (04, 05, 08).

### Why this needs no /clear
- The director is new on every call: the "clear" is automatic, and the carry-over is the files it re-reads (request, plan, resume, rulings, lessons, ledger).
- The operator is new on every milestone (fresh sub-agent), and re-reads the brief and resume at every phase start, so compaction inside it loses nothing that matters.
- The window holds only returns and Joel's words; `/clear` on it is optional and manual.
- Nobody re-reads what a lane already read: the lane's 20-line return and the reviewers' one-line tables are the only traffic upward; the hand-back files are opened only to settle a dispute, by the operator, and only the lines named.

### Files on the share (the memory of the whole thing; one folder per project goal)
- `REQUEST.md`: Joel's goal and every later instruction, verbatim, dated by sequence (no dates shown to him), appended only.
- `PLAN.md`: the director's plan (the existing block 03 form: end result, inventory, inputs, phases with consumer checks, risks, out of scope, failed methods), with a dependency list (phase -> what it needs from which phase) and the milestone checkpoints.
- `RESUME.md`: START HERE, done, running, next, what remains, decisions waiting on Joel. The operator updates it at every hand-back; the director at every call.
- `RULINGS/<phase>.md`: one line per finding: accepted with the change, disputed with file and line, deferred with why. Binding on later calls unless a PROBLEM reopens one.
- `BRIEFS/<phase>.md`: the director's brief for the lane: goal, inputs, exact steps, reads, what the output's consumer needs, the review it must pass, hand-back folder, cleanup.
- `PACKETS/<phase>_handback.md` (written by the operator from the lane's return and the three review tables, at most 60 lines plus paths) and `PACKETS/<phase>_problem.md` (fixed form below).
- `LESSONS.md`: one line per lesson: cause category, what was missed, the check added, where it now lives (which block or plan section).
- `LEDGER.md`: block 11's rows; the operator fills tokens from task notifications; the director writes the milestone paragraph.
- `FOR_JOEL/`: the review items (pictures, video) with one pointer line each, copied to REVIEW_NOW by the operator; `ANSWERS.md` where the window writes Joel's answers to decisions.
- `FOLLOW_UPS.md`: unrequested work found on the way, one line each, nothing on it starts without his yes.

### The packet forms (the only traffic to the director)
Hand-back packet: phase; what was built (5 lines); the lane's bar results, one line per bar; the three reviewers' verdicts, one line per finding (id, severity, claim, evidence path, proposed fix); the review content made for Joel (paths, one per view); what the lane says is open; the ledger row.
Problem packet: phase; what failed (one line); evidence path; what was tried (at most two tries, by rule); what the lane and reviewers think the cause is; what it blocks.
Checkpoint request: milestone; every phase's ruling status; the review items ready for Joel (paths); decisions that are his (each with what, why now, cost of yes, cost of no, the picture); what remains.

### The director's standing procedure per call kind
- PLAN: block 03 steps 1 to 3, plus the inventory step: before phases, list everything the finished result contains (every region, part, joint, move, surface, state, consumer) and map each to a phase, so nothing is planned from the words of the request alone; write the dependency list; name the checkpoints (a still before anything is generated on a look decision, the first video after the first real phase, every milestone, never more than two phases without a picture).
- RULE: read the packet only; rule per finding; write the ruling and the next brief (fix by the same lane once; AGY re-reads; second failure becomes a PROBLEM); update RESUME.
- PROBLEM: classify the cause as one of: order of work, wrong agent or model, workflow gap, missing review, human review too late, planning gap (inventory), dependency not tracked, tool or environment, other; write the lesson line (cause, what was missed, the check added, where it lives); write the corrective brief; if the cause is a planning gap, write the inventory item into PLAN.md and the check into the plan block; if the method failed twice, retire it and brief the artist's way.
- CHECKPOINT: verify the packet is complete and every review item exists at its path from every view; do not re-review what the three passed; write the one-line pointer per item and the decisions in MR-143 form; write the milestone ledger paragraph; update RESUME; stop.
- REDIRECT: read Joel's new words; decide whether they change the plan, the order or a ruling; write the change into PLAN.md and RESUME.md and the next brief; everything he did not ask for goes to FOLLOW_UPS.

### director.py (in the prompts repo, generic)
- Inputs: the project folder on the share, the call kind, the packet path. It assembles the prompt: the director block (13), the standing orders section extracted from the project's CLAUDE.md, then the files in a fixed order (REQUEST, PLAN, RESUME, rulings index, LESSONS, LEDGER tail, the packet), each with its path.
- Runs: `claude -p --model claude-fable-5-1 --effort xhigh --append-system-prompt-file director_system.md --allowedTools Read Write Edit Glob Grep --add-dir <share folder> --output-format text` from a lean `director/` directory whose CLAUDE.md is the director block alone (no project memory, no repo CLAUDE.md), with a timeout, and saves the output to `DIRECTOR/<seq>_<kind>.md`.
- Returns the summary to the caller (the operator), which follows it.
- Cost shape: one fresh context per call of a few tens of thousands of tokens; three to five calls per phase (RULE after each hand-back, PROBLEM when needed, CHECKPOINT per milestone, PLAN once).

### Overnight behaviour
- The window starts the milestone and waits; the operator runs phases and lanes; when the milestone reaches a checkpoint the operator posts the review items to REVIEW_NOW with pointers, returns 20 lines to the window, and the window stops. Nothing new starts until Joel answers; what he types goes to REQUEST.md and a REDIRECT call.
- A blocked phase (method failed twice, missing input, a decision that is his) ends the operator's milestone early with a problem packet and a FOLLOW_UPS or decision line; the window stops.

### Where Joel sits
- He talks to the window as now; his words reach the director verbatim on the next call. He reviews only items that passed the three reviews, in REVIEW_NOW, one pointer line each. He answers decisions in the window.

### Proof case
- Run M1-PREP of the movement set this way; the ledger measures the director's share against this session's 59 percent, and the forgot-counter and order errors against 3 and 2.

## Open questions for the reviewer
1. Does any part of this put the director's judgement at risk compared with a persistent Fable window (continuity, consistency of rulings across calls)?
2. Is anything Joel asked for omitted, or decided for him?
3. Where could the operator's own context grow out of hand overnight, and is the fresh-agent-per-milestone enough?
4. What is the failure mode when the director's ruling and an earlier ruling conflict?
5. Is the one-window shape right, or does Joel lose something he wants to watch?


# Director and operator: rulings on the Opus adversarial review, round 1 (2026-11-07)

Probe added after the review: the Workflow tool is NOT available inside a sub-agent (probe: a Haiku agent found no Workflow tool). Consequence ruled below (W1).

| id | ruling | the change |
|---|---|---|
| F1 | accepted | The operator runs director.py as a background job and waits for its notification; one retry; on a second failure it writes a PROBLEM line to STATE.md, cleans up and stops. The operator never rules in the director's place. |
| F2 | accepted | One fresh operator per PHASE (not per milestone), started from BRIEFS/<phase>.md, RESUME.md and STATE.md; job ids written to STATE.md before every wait; waits are background jobs that notify, never polling turns. |
| F3 | accepted | The director emits its files as delimited blocks in its output; director.py writes them. Tools: none for PLAN, RULE, PROBLEM, REDIRECT, QUESTION, APPROVAL; Read only for CHECKPOINT (the item's views, named in the packet). One turn per call. |
| F4 | accepted (already in director.py) | `--output-format json`; tokens and cost per call appended to LEDGER.md by director.py; the proof case scores director tokens per phase. |
| F5 | accepted | The hand-back packet is the lane's return and the reviewers' tables copied verbatim, no operator prose; cap 120 lines; over the cap a Sonnet digest is added, the full tables stay at a path, and the cut is logged in the packet. |
| F6 | accepted | RULES.md in the project folder: the human's standing rules in one file (for Torvane, built from the CLAUDE.md standing-orders section and the joel-* memory files at project start, by the operator, once); director.py includes it in every call. |
| F7 | accepted | One writer per file: the director (through director.py) writes RESUME.md, PLAN.md, VISION.md, RULINGS, BRIEFS, LESSONS; the operator writes STATE.md and PACKETS. The window appends REQUEST.md and sets REDIRECT_PENDING; the operator checks it at every phase boundary; for an urgent change the window messages the running operator. |
| F8 | accepted | QUESTION call kind: the human's words verbatim in, numbered one-sentence answers out, relayed by the window unchanged; diagnosis not defence lives in the director block. |
| F9 | accepted | APPROVAL call kind on the human's yes: writes the step's method under a rule id, the MR rows and the registry line as file blocks the operator commits in the same turn. |
| F10 | accepted | director.py takes `--write-root` (repeatable) for the prompts repo and the project's docs; the director emits lesson lines there; the operator commits and records the commit in LESSONS.md. |
| F11 | accepted with a split | PLAN: the director writes the strategic plan itself (end result, full inventory, dependency order, milestones, checkpoints, pre-rulings) and the brief for an Opus xhigh planner lane that fills the phases' exact steps, inputs and reads; then RULE on each plan-review round, RULE on the execution review, then proceed. A three-model review runs on the item before every PROBLEM call (the operator's chore). |
| F12 | accepted | Every ruling is `R-<n> | <ruling> | because <reason>`; a change names `supersedes R-<n>`; director.py keeps RULINGS/INDEX.md and refuses a ruling that reuses a settled id without "supersedes" (the output is saved, STATE.md gets a PROBLEM line). |
| F13 | accepted | VISION.md: strategy, story, what the human is happy with, reliability seen per lane, reviewer and tool; rewritten by the director on every call, one page cap. |
| F14 | accepted | Permission mode and allow-lists per role set before an unattended run; a phase that needs a Blender-port script waits for the human (decision line); depth-3 nesting probed now (result in the setup). |
| F15 | accepted | On an operator failure notification the window spawns a cleanup agent from STATE.md's RUNNING list, then a fresh operator from RESUME and STATE; a second failure stops everything with a pointer. |
| F16 | accepted | CHECKPOINT reads the item's views once (Read allowed for the paths in the packet), from every view. |
| F17 | accepted | Effort: PLAN, PROBLEM, REDIRECT, QUESTION, APPROVAL at xhigh; RULE at high; an all-pass hand-back with a pre-ruling "on all-pass proceed to <phase>" in PLAN.md needs no RULE call. |
| F18 | accepted | The director marks each next phase "hangs on the verdict" or "free of rework and inside the order"; only the latter continue while the human is away. |
| F19 | accepted | director.py starts the call in `%USERPROFILE%/.claude-director/` (a two-line CLAUDE.md), outside any project tree; the user-level CLAUDE.md still loads and is measured. |
| W1 | new | The Workflow tool (ultracode) is unavailable inside sub-agents: the operator runs the three reviewers as agents (AGY, Opus adversarial, Grok), no verifiers; when the measured trigger for verifiers is met the operator returns "run plan review workflow <packet>" and the window runs it and hands the result path to the next operator. |
| OM1 | accepted | Approvals, questions, plan-review loops: covered by F8, F9, F11. |
| OM2 | put to the human | Who he talks to: the plan takes Fable out of his window; this is his decision, put in the decision form in the setup message (A: one Opus window relaying his words verbatim to Fable and Fable's answers back verbatim; B: a second, Fable window that only talks to him and writes REQUEST.md, messaging the operator window). |
| DJ2 | noted | The proof case is the next phase in his own order, not new work; it runs only on his yes to the setup. |
| DJ3 | accepted | The window never paraphrases his words or the director's; verbatim both ways. |


# Ruling by the human (2026-11-07): no script calls Fable; two windows

"I fear a script calling Fable 5.1. I want to control the work as I see problems ... I do not want opus driving work ... I do not want fable holding every piece of output from a sub agent ... I want a fable 5.1 window I drive from no matter what." Shape in force: the director window (Fable 5.1 xhigh, block 13) the human drives; the driver window (Sonnet 5.5 high, block 14) that spawns a fresh operator per phase (block 15) and relays 20-line packets; files with one writer each (block 16); SendMessage between the windows. director.py is kept for a fully unattended run only, outside every preset. The adversarial review's rulings F1 to F19 and W1 carry over where they apply (fresh operator per phase, verbatim packets, rulings with ids and supersedes, VISION.md, RULES in the director's own instructions, stop-and-report on failures, workflow only from a window).
