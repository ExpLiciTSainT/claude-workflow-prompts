# Ultracode: cheap when it can be, expensive when it must be

Use for: deciding whether to say "ultracode" at all, and how to shape the workflow when you do.
Why: this session's reviews cost 2 to 4 million tokens a round; two thirds of that was per-finding verifiers that mostly confirmed the reviewers. The same reviewers without verifiers cost under 1 million and found the same defects.

```text
WHEN TO MAKE IT EXPENSIVE (say "ultracode", allow verifiers, Opus at xhigh):
- A plan that commits weeks of work (review it twice: the plan, then its execution method).
- A gate that everything downstream depends on (a read script, a server check, a corpus, a schema).
- A stuck problem after two closed methods, where a wrong next method costs more than the review.

WHEN TO KEEP IT CHEAP (or not use it at all):
- A phase hand-back: AGY on the pictures and Grok on the code, no Opus, no verifiers.
- Mechanical work (exports, docs, pictures, data): one Sonnet lane, AGY reads the result.
- Anything with a clear test: run the test, not a review.

HOW TO SHAPE A WORKFLOW SCRIPT (the Workflow tool):
- Set the model and effort PER AGENT in the script: agent(prompt, {model: "opus", effort: "high"}) for a reviewer; {model: "sonnet", effort: "medium"} for a verifier or a mechanical stage; {effort: "xhigh"} only for the planner or a judge of a gate. Omit effort to inherit the session's.
- Reviewers in parallel on ONE packet (the same files, the same question, the same output schema); at most 10 to 15 findings each, blockers and majors only.
- Verify blockers only, one verifier each, medium effort; pass a flag (for example args.verify: false) to skip verification entirely and rule on raw findings.
- One round, then the orchestrator rules; a second round only on the corrected version, never on the same version.
- Log what was dropped (minors unverified, findings over the cap) so a short list is never read as "nothing else".
- Cap the agent count (reviewers + verifiers) in the script and print it; a round over 20 agents needs a reason in the brief.

HOW TO AVOID THE ORCHESTRATOR'S OWN COST:
- The orchestrator reads compact tables (one line per finding, one line per read), never full transcripts; lanes return at most N lines.
- Fable only for the plan rulings and the stuck-twice rulings; Opus at high for the rest.
```
