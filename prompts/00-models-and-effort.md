# Models and effort levels

Use for: picking the model and effort before any prompt below.
Why: the orchestrator's reading volume and the per-finding verifiers were the cost drivers, not the lanes' effort.

```text
MODEL AND EFFORT (set with /model and /effort, or per agent in a brief)

Fable 5.1, xhigh      Orchestrator for a plan that commits weeks, a gate everything depends on, or a ruling after two failures. Nothing else.
Opus 5.5, high        Day-to-day orchestrator; hard lanes (code paths, tool settings, anything that failed once).
Opus 5.5, xhigh       Writing a plan; a lane stuck twice; a corpus or read that judges later work.
Sonnet 5.5, medium    Mechanical lanes: exports, scripts from a spec, docs, pictures, data tables, cleanup with a log.
Haiku 5.5, low        Small bounded tasks: a file move, a log line, a list from a folder.
AGY (Gemini), Grok    Reviewers first and often: they run on your own subscriptions and cost no Claude tokens.

Rules: one lane per phase, a fresh lane at each phase boundary (a lane re-reads its whole history every step); a lane that
exceeds about 0.7 M tokens is split; verifiers only on blockers; nothing at xhigh that a written brief can make medium.
```
