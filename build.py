"""Build index.html (the composer page) from prompts/*.md. Plain Python, no dependencies.

Each prompts/NN-name.md holds: a title line "# ...", a "Use for:" line, a "Why:" line, one fenced ```text block (the
prompt to copy), and optional Markdown after it (rendered as plain paragraphs and tables). Run: python build.py

The page: a builder at the top (presets and a checkbox per block) composing ONE full prompt with a Copy button, then
every block with its own Copy button. Presets name block ids; edit PRESETS when blocks are added.
"""
import glob
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "index.html")

PRESETS = {
    "Ultracode (a plan or a gate: Fable orchestrator, three-model reviews with verifiers on blockers)":
        ["00-models-and-effort", "01-orchestrator-fable", "03-plan-with-three-model-review", "04-lane-brief",
         "05-review-and-fix-loop", "06-human-review-points", "07-forgetting-and-order-guard",
         "08-ultracode-cost-control", "09-decision-to-human", "11-token-ledger"],
    "Manual lean (Opus 5.5 orchestrator, Sonnet and Opus lanes, AGY, Opus and Grok reviews, no verifiers)":
        ["00-models-and-effort", "02-orchestrator-opus-lean", "03-plan-with-three-model-review", "04-lane-brief",
         "05-review-and-fix-loop", "06-human-review-points", "07-forgetting-and-order-guard", "09-decision-to-human",
         "10-where-each-fits", "11-token-ledger"],
    "Minimal (one phase: Opus orchestrator, one Sonnet lane, AGY and Opus look once)":
        ["00-models-and-effort", "04-lane-brief", "06-human-review-points", "07-forgetting-and-order-guard",
         "09-decision-to-human"],
    "Two windows (paste into the Fable 5.1 xhigh director window you drive; the Sonnet 5.5 high driver window gets block 14 alone; a fresh lane per phase, the driver runs every review round; no script, nothing to clear)":
        ["00-models-and-effort", "13-director-window-fable", "14-driver-window-sonnet", "15-operator-phase-agent",
         "16-project-files-and-packets", "04-lane-brief", "05-review-and-fix-loop", "06-human-review-points",
         "07-forgetting-and-order-guard", "09-decision-to-human", "11-token-ledger"],
    "Motion kickoff (paste into the director window after the Two windows preset, for a new character's movement or fighting motions)":
        ["17-motion-pipeline-kickoff"],
}


def parse(path):
    text = open(path, encoding="utf-8").read()
    title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    use = re.search(r"^Use for: (.+)$", text, re.M)
    why = re.search(r"^Why: (.+)$", text, re.M)
    block = re.search(r"```text\n(.*?)```", text, re.S)
    after = text[block.end():] if block else ""
    return {
        "id": os.path.basename(path)[:-3],
        "title": title,
        "use": use.group(1).strip() if use else "",
        "why": why.group(1).strip() if why else "",
        "prompt": block.group(1).rstrip("\n") if block else "",
        "after": after.strip(),
    }


def md_after(s):
    out = []
    lines = s.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## "):
            out.append(f"<h3>{html.escape(ln[3:])}</h3>")
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            cells = [[html.escape(c.strip()) for c in r.strip().strip("|").split("|")] for r in rows if not re.match(r"^\|[\s\-|:]+\|$", r)]
            if cells:
                head = "".join(f"<th>{c}</th>" for c in cells[0])
                body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in cells[1:])
                out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
            continue
        elif ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{html.escape(lines[i][2:])}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif ln.strip():
            out.append(f"<p>{html.escape(ln)}</p>")
        i += 1
    return "\n".join(out)


def main():
    files = sorted(glob.glob(os.path.join(HERE, "prompts", "*.md")))
    secs = [parse(f) for f in files]
    ids = [s["id"] for s in secs]
    for name, members in PRESETS.items():
        for m in members:
            assert m in ids, f"preset {name!r} names a missing block {m}"
    data = json.dumps({s["id"]: {"title": s["title"], "prompt": s["prompt"]} for s in secs}, ensure_ascii=False)
    presets = json.dumps(PRESETS, ensure_ascii=False)
    checks = "\n".join(
        f'<label class="pick"><input type="checkbox" class="inc" data-id="{s["id"]}"> {html.escape(s["title"])}</label>'
        for s in secs)
    preset_buttons = "\n".join(f'<button class="preset" data-name="{html.escape(n)}">{html.escape(n.split(" (")[0])}</button>' for n in PRESETS)
    body = []
    for s in secs:
        body.append(f'''<section id="{s["id"]}">
<h2><label class="pick"><input type="checkbox" class="inc" data-id="{s["id"]}"> {html.escape(s["title"])}</label></h2>
<p class="meta"><b>Use for:</b> {html.escape(s["use"])}</p>
<p class="meta"><b>Why:</b> {html.escape(s["why"])}</p>
<div class="block"><button class="copy" data-target="p-{s["id"]}">Copy</button><pre id="p-{s["id"]}">{html.escape(s["prompt"])}</pre></div>
{md_after(s["after"])}
</section>''')
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Workflow Prompts</title>
<style>
:root{{--bg:#fff;--fg:#1a1a1a;--muted:#555;--line:#ddd;--pre:#f6f6f6;--accent:#0b57d0;--panel:#f0f4ff}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111;--fg:#eee;--muted:#aaa;--line:#333;--pre:#1b1b1b;--accent:#8ab4f8;--panel:#182033}}}}
:root[data-theme="dark"]{{--bg:#111;--fg:#eee;--muted:#aaa;--line:#333;--pre:#1b1b1b;--accent:#8ab4f8;--panel:#182033}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,Segoe UI,Roboto,sans-serif}}
main{{max-width:960px;margin:0 auto;padding:16px}}
h1{{font-size:1.6rem;margin:.5rem 0}} h2{{font-size:1.25rem;margin:2rem 0 .5rem;border-top:1px solid var(--line);padding-top:1rem}}
h3{{font-size:1.05rem;margin:1rem 0 .3rem}}
.meta{{color:var(--muted);margin:.2rem 0}}
.builder{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px;margin:12px 0}}
.builder .presets button{{margin:4px 6px 4px 0;background:var(--accent);color:#fff;border:0;border-radius:4px;padding:6px 10px;cursor:pointer}}
.builder .picks{{columns:2;margin:8px 0}} @media (max-width:640px){{.builder .picks{{columns:1}}}}
.pick{{display:block;break-inside:avoid;font-weight:normal;font-size:.95rem;cursor:pointer}}
.block{{position:relative;margin:.6rem 0}}
pre{{background:var(--pre);border:1px solid var(--line);border-radius:6px;padding:12px;overflow:auto;white-space:pre-wrap;word-break:break-word;font:13px/1.45 ui-monospace,Consolas,monospace}}
#composed{{min-height:120px;max-height:60vh}}
.copy{{position:absolute;top:8px;right:8px;background:var(--accent);color:#fff;border:0;border-radius:4px;padding:4px 10px;font-size:13px;cursor:pointer}}
.copy.done{{background:#2e7d32}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:.5rem 0}} th,td{{border:1px solid var(--line);padding:6px;text-align:left;vertical-align:top}}
a{{color:var(--accent)}} .count{{color:var(--muted);font-size:.9rem}}
</style></head><body><main>
<h1>Workflow prompts</h1>
<p class="meta">Blocks to add to any Claude Code prompt. Pick a preset or tick blocks; the box below holds the full combined prompt; press Copy and paste it into the CLI, then add your own task under it.</p>
<div class="builder">
<div class="presets">{preset_buttons}<button class="preset" data-name="">Clear</button></div>
<div class="picks">{checks}</div>
<p class="count" id="count">Nothing selected.</p>
<div class="block"><button class="copy" data-target="composed">Copy</button><pre id="composed"></pre></div>
</div>
{"".join(body)}
<p class="meta">Source: the Markdown files under <code>prompts/</code> in this repository; this page is built from them by <code>build.py</code>.</p>
</main>
<script>
const DATA={data};const PRESETS={presets};const ORDER=Object.keys(DATA);
function selected(){{const s=new Set();document.querySelectorAll('.inc:checked').forEach(c=>s.add(c.dataset.id));return ORDER.filter(i=>s.has(i));}}
function sync(id,on){{document.querySelectorAll('.inc[data-id="'+id+'"]').forEach(c=>c.checked=on);}}
function compose(){{const ids=selected();const parts=ids.map(i=>'=== '+DATA[i].title+' ===\\n'+DATA[i].prompt);document.getElementById('composed').textContent=parts.join('\\n\\n');document.getElementById('count').textContent=ids.length?ids.length+' block(s) selected; add your own task under the prompt when you paste it.':'Nothing selected.';}}
document.querySelectorAll('.inc').forEach(c=>c.addEventListener('change',()=>{{sync(c.dataset.id,c.checked);compose();}}));
document.querySelectorAll('.preset').forEach(b=>b.addEventListener('click',()=>{{const m=PRESETS[b.dataset.name]||[];ORDER.forEach(i=>sync(i,m.includes(i)));compose();}}));
document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',async()=>{{const t=document.getElementById(b.dataset.target).innerText;try{{await navigator.clipboard.writeText(t);b.textContent='Copied';b.classList.add('done');setTimeout(()=>{{b.textContent='Copy';b.classList.remove('done')}},1500)}}catch(e){{const r=document.createRange();r.selectNodeContents(document.getElementById(b.dataset.target));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected: Ctrl+C'}}}}));
compose();
</script></body></html>'''
    open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    print("wrote", OUT, len(secs), "sections,", len(PRESETS), "presets")


if __name__ == "__main__":
    main()
