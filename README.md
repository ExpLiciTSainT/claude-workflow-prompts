# Claude workflow prompts

Reusable prompt blocks for running work with Claude Code and other agents (Opus, Sonnet, Haiku, Fable; AGY and Grok as reviewers): the orchestrator prompts, the plan-and-review loop, lane briefs, the human review points, the forgetting guard, ultracode cost control, the decision form, where each workflow fits, and a token ledger.

The page with copy buttons: https://explicitsaint.github.io/claude-workflow-prompts/

Seventeen sections: models and effort levels, the Fable orchestrator, the lean Opus orchestrator, the plan with the three-model review, the lane brief, the review and fix loop, the human review points, the forgetting and order guard, ultracode cost control, the decision form, where each workflow fits, the token ledger, orchestrator context discipline, the director (fresh per call), the operator window, the operator for one phase, the project files and packet forms.

The prompts live in `prompts/*.md` (one block each, with "Use for" and "Why"); `python build.py` rebuilds `index.html` from them. Edit the Markdown, run the build, commit.

## Director and operator (runs overnight with no clear)

The director (Fable 5.1) is never a window: `tools/director.py` makes one fresh headless call per decision (PLAN, RULE, PROBLEM, CHECKPOINT, REDIRECT, QUESTION, APPROVAL), assembled from the goal's folder on the share (blocks 13 to 16). One Opus 5.5 window spawns a fresh operator agent per phase; operators run lanes, reviews and chores and call the director. The files are the memory, so nothing has to be cleared. Plan and the adversarial review's rulings: `docs/director-operator-plan.md`.

Measured 2026-11-07: a headless call with the account's MCP connectors loaded wrote 337,435 tokens of tool schemas into the cache for a one-word answer; with `--strict-mcp-config` and an empty config (what director.py passes) the same call cost 3,177 tokens.
