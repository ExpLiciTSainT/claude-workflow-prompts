"""director.py (OPTIONAL, in no preset; the human ruled that no script calls Fable): one fresh Fable 5.1 director call, assembled from the project's files. Plain Python, no dependencies.

The director never lives in a window. Every decision is a new headless `claude -p` run whose context is only: the
director block, the human's rules, the request, the vision, the plan, the resume, the operator's state, the rulings
index, the lessons, the ledger tail and the one packet to judge. The files are the memory; nothing carries over.
The director has no tools (Read only on a CHECKPOINT, for the item's views): it writes its files as delimited blocks
in its output and this script writes them, so a call is one turn and never wanders into hand-backs.

Usage (the operator runs it as a background job and waits; by hand for a question):
  python tools/director.py --project Z:/Share/review/progress/<goal> --kind RULE --packet PACKETS/p03_handback.md
  kinds: PLAN | RULE | PROBLEM | CHECKPOINT | REDIRECT | QUESTION | APPROVAL
Options: --write-root <dir> (repeatable: other trees the director may write, e.g. the prompts repo, the docs),
         --model, --effort (default per kind), --timeout, --dry-run (print the assembled prompt, no call).
Output: the whole answer is saved to <project>/DIRECTOR/<seq>_<kind>.md; its file blocks are written; its summary is
printed; a ledger row with the call's tokens and cost is appended to <project>/LEDGER.md.

File blocks the director emits (paths relative to the project folder, or absolute under a write root):
  <<<FILE path>>> ... <<<END>>>      replaces the file
  <<<APPEND path>>> ... <<<END>>>    appends to the file
Rulings: lines `R-<n> | <ruling> | because <reason>` in RULINGS/<phase>.md; a change to a settled id must say
`supersedes R-<n>`; a reuse without it is refused (the block is kept in the DIRECTOR file, STATE.md gets a PROBLEM line).
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BLOCK = os.path.join(ROOT, "prompts", "13-director-window-fable.md")  # the same constitution, read as a block
DIRECTOR_DIR = os.path.join(os.path.expanduser("~"), ".claude-director")   # outside every project tree (F19)
DIRECTOR_CLAUDE_MD = ("# Director call directory\n\nThis folder exists so the director runs with no project memory and no "
                      "project CLAUDE.md: tools/director.py starts each headless call here; the prompt carries everything.\n")

FILES = [  # (path under the project folder, all or tail, required)
    ("RULES.md", "all", False),
    ("REQUEST.md", "all", True),
    ("VISION.md", "all", False),
    ("PLAN.md", "all", False),
    ("RESUME.md", "all", False),
    ("STATE.md", "all", False),
    ("LESSONS.md", "tail", False),
    ("LEDGER.md", "tail", False),
    ("FOLLOW_UPS.md", "all", False),
    ("ANSWERS.md", "all", False),
    ("RULINGS/INDEX.md", "all", False),
]
TAIL_LINES = 60
EFFORT = {"PLAN": "xhigh", "RULE": "high", "PROBLEM": "xhigh", "CHECKPOINT": "xhigh", "REDIRECT": "xhigh",
          "QUESTION": "xhigh", "APPROVAL": "xhigh"}
NEEDS_PACKET = {"RULE", "PROBLEM", "CHECKPOINT", "APPROVAL"}
KIND_TASK = {
    "PLAN": "Write the strategic plan yourself (PLAN.md: the end result the human judges, the FULL INVENTORY of everything the finished result contains mapped to phases, the dependency order, milestones and checkpoints, pre-rulings such as 'on an all-pass proceed to <phase>', each next phase marked 'hangs on the verdict' or 'free of rework and inside the order'), VISION.md, RESUME.md, and BRIEFS/plan_fill.md for an Opus xhigh planner lane that fills each phase's exact steps, inputs and reads; the plan then goes through the three-model review, which you rule on in RULE calls.",
    "RULE": "Rule on the packet only: RULINGS/<phase>.md with one line per finding `R-<n> | accepted with <change> / disputed at <file:line> / deferred because <why> | because <reason>`; then BRIEFS/<next>.md (a fix is by the same lane once, re-read by the picture reviewer; a second failure becomes a PROBLEM); update RESUME.md and VISION.md.",
    "PROBLEM": "Root-cause the problem packet: classify the cause (order of work, wrong agent or model, workflow gap, missing review, human review too late, planning gap in the inventory, dependency not tracked, tool or environment, other); write one lesson line to LESSONS.md (cause, what was missed, the check added, where it now lives) and, when it belongs in a prompt block or a process doc, the line for that file under a write root; a method that failed twice is retired and the corrective brief uses the tool's own way; update PLAN.md (inventory), RESUME.md, VISION.md.",
    "CHECKPOINT": "Check the checkpoint request is complete and that every review item exists at its path; look at each item's views once (Read the image paths named in the packet), from every view; do not re-review what the three reviewers passed; write FOR_JOEL/POINTERS.md (one line per item: ATTENTION NEEDED, the full path, the one thing to do) and the decisions in the decision form (what, why now, cost of yes, cost of no, the picture); write the milestone paragraph into LEDGER.md (spent for the result, wasted, lost to redo, forgot-counter, what changes); mark which next phases are free of rework and inside the human's order; update RESUME.md and VISION.md.",
    "REDIRECT": "Read the newest lines of REQUEST.md: decide what they change in the plan, the order or a ruling (a changed ruling says `supersedes R-<n>`); write the change into PLAN.md, RESUME.md, VISION.md and the next brief; anything the human did not ask for goes to FOLLOW_UPS.md as one line (part, what, why, found by).",
    "QUESTION": "Answer the human's question in the newest lines of REQUEST.md: numbered one-sentence answers, direct, no history unless asked; 'why is it taking so long' gets a diagnosis (the wrong decisions made and the human's own requests that made it worse, what each cost, what changes), never a defence; no dates, durations or estimates. Write the answer as the summary only (the window relays it unchanged); update VISION.md if the question changes what the human is happy with.",
    "APPROVAL": "The human approved the item in the packet: write the method as ordered steps for any humanoid at its own size with the read that proves it, under a rule id, into the step's doc (a write root); the catches on the way as MR rows; the registry line for the part; LESSONS.md line; RESUME.md and VISION.md updated, in this one call.",
}


def read(path, how):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except FileNotFoundError:
        return None
    if how == "tail":
        lines = text.splitlines()
        if len(lines) > TAIL_LINES:
            text = "(first %d lines omitted)\n" % (len(lines) - TAIL_LINES) + "\n".join(lines[-TAIL_LINES:])
    return text


def block_text():
    text = open(BLOCK, encoding="utf-8").read()
    m = re.search(r"```text\n(.*?)```", text, re.S)
    return m.group(1).strip() if m else text


def assemble(args):
    parts = [f"DIRECTOR CALL: {args.kind}. Project folder: {args.project}.",
             "Task for this call: " + KIND_TASK[args.kind],
             "You have no tools in this call" + (" except Read, for the image paths the packet names." if args.kind == "CHECKPOINT" else ".")
             + " Write every file as a block: <<<FILE relative/path>>> content <<<END>>> to replace, <<<APPEND relative/path>>> content <<<END>>> to add lines; "
             "paths are relative to the project folder" + (", or absolute under: " + ", ".join(args.write_root) if args.write_root else "") + ".",
             "", "=== THE DIRECTOR BLOCK (binding) ===", block_text()]
    for rel, how, required in FILES:
        text = read(os.path.join(args.project, rel), how)
        if text is None:
            if required:
                sys.exit(f"missing required file: {os.path.join(args.project, rel)}")
            continue
        parts += ["", f"=== {rel} ===", text.strip()]
    if args.packet:
        packet = read(os.path.join(args.project, args.packet), "all")
        if packet is None:
            sys.exit(f"missing packet: {os.path.join(args.project, args.packet)}")
        parts += ["", f"=== PACKET {args.packet} (the only thing to judge in this call) ===", packet.strip()]
    elif args.kind in NEEDS_PACKET:
        sys.exit(f"--packet is required for {args.kind}")
    parts += ["", "After the file blocks, end with a summary of at most 20 lines (for QUESTION the answer itself): what you ruled or wrote with paths, the next brief's phase, decisions that are the human's, what remains. Nothing after it."]
    return "\n".join(parts)


def next_seq(folder):
    os.makedirs(folder, exist_ok=True)
    nums = [int(m.group(1)) for n in os.listdir(folder) for m in [re.match(r"^(\d{3})_", n)] if m]
    return (max(nums) + 1) if nums else 1


def safe_target(path, project, roots):
    full = os.path.abspath(path if os.path.isabs(path) else os.path.join(project, path))
    for root in [project] + roots:
        if os.path.commonpath([full, root]) == root:
            return full
    return None


def load_index(project):
    idx = os.path.join(project, "RULINGS", "INDEX.md")
    ids = {}
    text = read(idx, "all") or ""
    for line in text.splitlines():
        m = re.match(r"^(R-\d+)\s*\|", line.strip())
        if m:
            ids[m.group(1)] = line.strip()
    return idx, ids


def write_blocks(output, args, problems):
    """Write the director's file blocks; return the list of paths written."""
    written = []
    idx_path, settled = load_index(args.project)
    new_index_rows = []
    for mode, rel, body in re.findall(r"<<<(FILE|APPEND) ([^>\n]+)>>>\n?(.*?)<<<END>>>", output, re.S):
        rel = rel.strip()
        target = safe_target(rel, args.project, args.write_root)
        if target is None:
            problems.append(f"refused write outside the allowed roots: {rel}")
            continue
        body = body.rstrip("\n") + "\n"
        if os.path.normpath(rel).replace("\\", "/").startswith("RULINGS/") and not rel.endswith("INDEX.md"):
            bad = []
            for line in body.splitlines():
                m = re.match(r"^(R-\d+)\s*\|", line.strip())
                if m and m.group(1) in settled and "supersedes" not in line:
                    bad.append(m.group(1))
                elif m:
                    settled[m.group(1)] = line.strip()
                    new_index_rows.append(f"{line.strip()[:200]}  ({rel})")
            if bad:
                problems.append(f"ruling ids reused without 'supersedes' in {rel}: {', '.join(bad)}; block kept in the DIRECTOR file, not written")
                continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "a" if mode == "APPEND" else "w", encoding="utf-8", newline="\n") as f:
            f.write(body)
        written.append(target)
    if new_index_rows:
        os.makedirs(os.path.dirname(idx_path), exist_ok=True)
        with open(idx_path, "a", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(new_index_rows) + "\n")
        written.append(idx_path)
    return written


def summary_of(output):
    text = re.sub(r"<<<(FILE|APPEND) [^>\n]+>>>.*?<<<END>>>", "", output, flags=re.S).strip()
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return "\n".join(lines[-20:]) if lines else "(the director returned no summary)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--kind", required=True, choices=sorted(KIND_TASK))
    ap.add_argument("--packet", help="path under the project folder")
    ap.add_argument("--write-root", action="append", default=[], help="another tree the director may write into")
    ap.add_argument("--model", default="claude-fable-5-1")
    ap.add_argument("--effort", help="default: xhigh, RULE at high")
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    args.project = os.path.abspath(args.project)
    args.write_root = [os.path.abspath(r) for r in args.write_root]
    effort = args.effort or EFFORT[args.kind]
    prompt = assemble(args)
    if args.dry_run:
        print(prompt)
        return
    os.makedirs(DIRECTOR_DIR, exist_ok=True)
    md = os.path.join(DIRECTOR_DIR, "CLAUDE.md")
    if not os.path.exists(md):
        open(md, "w", encoding="utf-8", newline="\n").write(DIRECTOR_CLAUDE_MD)
    # No MCP servers: with the account's connectors loaded, one trivial headless call wrote 337,435 tokens of tool
    # schemas into the cache (measured 2026-11-07); with --strict-mcp-config and an empty config they never load.
    empty_mcp = os.path.join(DIRECTOR_DIR, "empty_mcp.json")
    if not os.path.exists(empty_mcp):
        open(empty_mcp, "w", encoding="utf-8", newline="\n").write('{"mcpServers":{}}\n')
    cmd = ["claude", "-p", "--model", args.model, "--effort", effort, "--output-format", "json", "--add-dir", args.project,
           "--strict-mcp-config", "--mcp-config", empty_mcp]
    if args.kind == "CHECKPOINT":
        cmd += ["--tools", "Read", "--allowedTools", "Read"]
    else:
        cmd += ["--tools", ""]
    try:
        run = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
                             cwd=DIRECTOR_DIR, timeout=args.timeout, shell=(os.name == "nt"))
    except subprocess.TimeoutExpired:
        sys.exit(f"director call timed out after {args.timeout} s")
    out, usage, cost = run.stdout, {}, None
    try:
        data = json.loads(run.stdout)
        out = data.get("result") or run.stdout
        usage = data.get("usage") or {}
        cost = data.get("total_cost_usd")
    except ValueError:
        pass
    seq = next_seq(os.path.join(args.project, "DIRECTOR"))
    out_path = os.path.join(args.project, "DIRECTOR", f"{seq:03d}_{args.kind}.md")
    problems = []
    if run.returncode != 0:
        problems.append(f"claude exited {run.returncode}: {run.stderr.strip()[:1500]}")
    written = write_blocks(out, args, problems) if run.returncode == 0 else []
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out.strip() + "\n")
        if problems:
            f.write("\n## director.py problems\n" + "\n".join(f"- {p}" for p in problems) + "\n")
    if problems:
        with open(os.path.join(args.project, "STATE.md"), "a", encoding="utf-8", newline="\n") as f:
            f.write("".join(f"PROBLEM (director.py, DIRECTOR/{os.path.basename(out_path)}): {p}\n" for p in problems))
    t = {k: usage.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")}
    row = (f"| director {args.kind} {seq:03d} | in {t['input_tokens']} + cache-new {t['cache_creation_input_tokens']} + cache-read "
           f"{t['cache_read_input_tokens']} / out {t['output_tokens']} | {args.model} {effort} | "
           f"{'%.3f USD' % cost if cost is not None else ''} | DIRECTOR/{os.path.basename(out_path)} | files {len(written)} |")
    with open(os.path.join(args.project, "LEDGER.md"), "a", encoding="utf-8", newline="\n") as f:
        f.write(row + "\n")
    print(summary_of(out))
    print(f"\n[director] saved {out_path}; wrote {len(written)} file(s); problems {len(problems)}; {row}", file=sys.stderr)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
