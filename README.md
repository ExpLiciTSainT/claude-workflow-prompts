# Claude workflow prompts

Reusable prompt blocks for running work with Claude Code and other agents (Opus, Sonnet, Haiku, Fable; AGY and Grok as reviewers): the orchestrator prompts, the plan-and-review loop, lane briefs, the human review points, the forgetting guard, ultracode cost control, the decision form, where each workflow fits, and a token ledger.

The page with copy buttons: https://explicitsaint.github.io/claude-workflow-prompts/

Seventeen sections: models and effort levels, the Fable orchestrator, the lean Opus orchestrator, the plan with the three-model review, the lane brief, the review and fix loop, the human review points, the forgetting and order guard, ultracode cost control, the decision form, where each workflow fits, the token ledger, orchestrator context discipline, the director window (Fable), the driver window (Sonnet), the operator for one phase, the project files and packet forms.

The prompts live in `prompts/*.md` (one block each, with "Use for" and "Why"); `python build.py` rebuilds `index.html` from them. Edit the Markdown, run the build, commit.

## Two windows: the Fable director window you drive, the Sonnet driver window (runs overnight, nothing to clear)

The director (Fable 5.1, xhigh) is the window the human talks to: it plans from the full inventory, writes briefs and rulings, root-causes problems, answers the human; it never runs a lane or holds a sub-agent's output (block 13). The driver (Sonnet 5.5, high) is the second window: it spawns one fresh operator agent per phase from the director's brief and relays the operator's return and the packet path verbatim, deciding nothing (block 14). Operators (block 15) run the lane, the three reviews and the chores and are thrown away. The project folder (block 16) is the memory, one writer per file. The windows talk by SendMessage, one message per hand-off, each starting with a fixed first line (director to driver: `director`, `run`, `workflow`, `stop`; driver to director: `ready`, `packet`, `blocked`, `stopped`, `workflow done`, `human`), listed in blocks 13 and 14. Start order (block 14's notes): open the driver window first and paste block 14 alone, it prints its session name; then open the Fable window in the same repository folder and permission mode and paste the "Two windows" preset with that name filled in. Plan and the adversarial review's rulings: `docs/director-operator-plan.md`.

`tools/director.py` (a fresh headless Fable call per decision, for a fully unattended run) is kept but is in no preset: the human's ruling is that no script calls Fable. Measured 2026-11-07: a headless call with the account's MCP connectors loaded wrote 337,435 tokens of tool schemas into the cache for a one-word answer; with `--strict-mcp-config` and an empty config it cost 3,177 tokens.
