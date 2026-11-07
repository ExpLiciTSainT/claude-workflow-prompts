# Ultracode: cheap when it can be, expensive when it must be

Use for: deciding whether to say "ultracode" at all, and how to shape the workflow when you do.
Why: this session's reviews cost 2 to 4 million tokens a round; two thirds of that was per-finding verifiers that mostly confirmed the reviewers. The same reviewers without verifiers cost under 1 million and found the same defects.

```text
WHEN TO MAKE IT EXPENSIVE (say "ultracode", allow verifiers, Opus at xhigh), measured, not felt:
- A plan with 4 or more phases, or one whose output other work will reuse (a pipeline, a method for the next character, a system), or where a wrong plan would redo 2 or more phases. Review it twice: the plan, then its execution method.
- A gate: anything later phases trust without re-checking (a read script, a server check, a corpus, a schema, an exporter). Build it test-first on recorded known-goods and known-bads, then review it as a gate.
- A stuck problem after two closed methods, where a wrong next method would cost more than the review.

WHEN TO KEEP IT CHEAP (or not say "ultracode" at all):
- A phase hand-back: the three reviewers (AGY on pictures and strips, Opus at high, Grok on code and numbers), no verifiers, one round.
- Mechanical work (exports, docs, pictures, data): one Sonnet lane; AGY and Opus look at the result once.
- A mechanism with a test: run the test for the mechanism; the holistic picture review still happens, and I still see the whole thing at the review points. A test that tests the wrong thing is caught only by that look.

HOW TO SHAPE A WORKFLOW SCRIPT (the Workflow tool):
- Set the model and effort PER AGENT in the script: agent(prompt, {model: "opus", effort: "high"}) for a reviewer; {model: "sonnet", effort: "medium"} for a verifier or a mechanical stage; {effort: "xhigh"} only for the planner or the judge of a gate. Omit effort to inherit the session's.
- Reviewers in parallel on ONE packet (the same files, the same question, the same output schema); at most 10 to 15 findings each, blockers and majors only.
- Verify blockers only, one verifier each, medium effort; pass a flag (args.verify: false) to skip verification and rule on raw findings.
- One round, then the orchestrator rules; a second round only on the corrected version.
- Log what was dropped (minors unverified, findings over the cap) so a short list is never read as "nothing else".
- Cap the agent count in the script and print it; a round over 20 agents needs a reason in the brief.
```
