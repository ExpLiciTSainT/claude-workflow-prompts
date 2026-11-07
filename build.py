"""Build index.html (the copy-button page) from prompts/*.md. Plain Python, no dependencies.

Each prompts/NN-name.md holds: a title line "# ...", a "Use for:" line, a "Why:" line, one fenced ```text block (the
prompt to copy), and optional Markdown after it (rendered as plain paragraphs and tables). Run: python build.py
"""
import glob
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "index.html")


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
    """Headings, paragraphs and pipe tables only (enough for the ledger)."""
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
        elif ln.strip():
            out.append(f"<p>{html.escape(ln)}</p>")
        i += 1
    return "\n".join(out)


def main():
    files = sorted(glob.glob(os.path.join(HERE, "prompts", "*.md")))
    secs = [parse(f) for f in files]
    nav = "\n".join(f'<li><a href="#{s["id"]}">{html.escape(s["title"])}</a></li>' for s in secs)
    body = []
    for s in secs:
        body.append(f'''<section id="{s["id"]}">
<h2>{html.escape(s["title"])}</h2>
<p class="meta"><b>Use for:</b> {html.escape(s["use"])}</p>
<p class="meta"><b>Why:</b> {html.escape(s["why"])}</p>
<div class="block"><button class="copy" data-target="p-{s["id"]}">Copy</button><pre id="p-{s["id"]}">{html.escape(s["prompt"])}</pre></div>
{md_after(s["after"])}
</section>''')
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Workflow Prompts</title>
<style>
:root{{--bg:#fff;--fg:#1a1a1a;--muted:#555;--line:#ddd;--pre:#f6f6f6;--accent:#0b57d0}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111;--fg:#eee;--muted:#aaa;--line:#333;--pre:#1b1b1b;--accent:#8ab4f8}}}}
:root[data-theme="dark"]{{--bg:#111;--fg:#eee;--muted:#aaa;--line:#333;--pre:#1b1b1b;--accent:#8ab4f8}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,Segoe UI,Roboto,sans-serif}}
main{{max-width:960px;margin:0 auto;padding:16px}}
h1{{font-size:1.6rem;margin:.5rem 0}} h2{{font-size:1.25rem;margin:2rem 0 .5rem;border-top:1px solid var(--line);padding-top:1rem}}
h3{{font-size:1.05rem;margin:1rem 0 .3rem}}
.meta{{color:var(--muted);margin:.2rem 0}}
nav ol{{padding-left:1.2rem;columns:2}} @media (max-width:640px){{nav ol{{columns:1}}}}
.block{{position:relative;margin:.6rem 0}}
pre{{background:var(--pre);border:1px solid var(--line);border-radius:6px;padding:12px;overflow:auto;white-space:pre-wrap;word-break:break-word;font:13px/1.45 ui-monospace,Consolas,monospace}}
.copy{{position:absolute;top:8px;right:8px;background:var(--accent);color:#fff;border:0;border-radius:4px;padding:4px 10px;font-size:13px;cursor:pointer}}
.copy.done{{background:#2e7d32}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:.5rem 0}} th,td{{border:1px solid var(--line);padding:6px;text-align:left;vertical-align:top}}
a{{color:var(--accent)}}
</style></head><body><main>
<h1>Workflow prompts</h1>
<p class="meta">Reusable blocks to add to any Claude Code prompt: the orchestrator prompts (Fable and Opus), the plan and review loop, lane briefs, the human review points, the forgetting guard, ultracode cost control, the decision form, where each fits, and the token ledger. Press Copy on a block and paste it into your prompt.</p>
<nav><ol>{nav}</ol></nav>
{"".join(body)}
<p class="meta">Source: the Markdown files under <code>prompts/</code> in this repository; this page is built from them by <code>build.py</code>.</p>
</main>
<script>
document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',async()=>{{const t=document.getElementById(b.dataset.target).innerText;try{{await navigator.clipboard.writeText(t);b.textContent='Copied';b.classList.add('done');setTimeout(()=>{{b.textContent='Copy';b.classList.remove('done')}},1500)}}catch(e){{const r=document.createRange();r.selectNodeContents(document.getElementById(b.dataset.target));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected: Ctrl+C'}}}}));
</script></body></html>'''
    open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    print("wrote", OUT, len(secs), "sections")


if __name__ == "__main__":
    main()
