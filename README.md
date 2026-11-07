# Claude workflow prompts

Reusable prompt blocks for running work with Claude Code and other agents (Opus, Sonnet, Haiku, Fable; AGY and Grok as reviewers): the orchestrator prompts, the plan-and-review loop, lane briefs, the human review points, the forgetting guard, ultracode cost control, the decision form, where each workflow fits, and a token ledger.

The page with copy buttons: https://explicitsaint.github.io/claude-workflow-prompts/

Twelve sections: models and effort levels, the Fable orchestrator, the lean Opus orchestrator, the plan with the three-model review, the lane brief, the review and fix loop, the human review points, the forgetting and order guard, ultracode cost control, the decision form, where each workflow fits, the token ledger.

The prompts live in `prompts/*.md` (one block each, with "Use for" and "Why"); `python build.py` rebuilds `index.html` from them. Edit the Markdown, run the build, commit.
