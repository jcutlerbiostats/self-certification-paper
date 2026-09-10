#!/usr/bin/env python3
"""Copy the paper draft and cliff-notes outline from the Obsidian vault into content/.
Strips vault frontmatter, strips '(N paragraphs)' heading notes, adds the draft banner,
and rewrites the outline's wikilinks to point at the site's own pages."""
import re, os, datetime
VAULT = "/Users/jamescutler/Documents/PKM/Atlas/Dots/Social Sciences & Humanities"
DRAFT = "The Self-Certification Problem — Why attributions of intellectual honesty require arbiter-free, adversarial infrastructure with an objectively readable, external honesty ledger.md"
OUTLINE = "The Self-Certification Problem — Cliff notes outline.md"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
today = datetime.date.today().isoformat()

d = open(os.path.join(VAULT, DRAFT), encoding="utf-8").read()
d = re.sub(r'^---\ntags:.*?\n---\n', '', d, flags=re.S)
d = re.sub(r'^(# \d\..*?) \(.*?paragraphs\)\s*$', r'\1', d, flags=re.M)
banner = f'''---
title: "The Self-Certification Problem"
---
> [!info] Early working draft — updated {today}
> **Full title:** *The Self-Certification Problem: Why attributions of intellectual honesty require arbiter-free, adversarial infrastructure with an objectively readable, external honesty ledger.*
> This is an unfinished draft shared with friends for comment. Sections under a warning callout are reference prose still being rewritten in the author's own voice. Not for citation. A condensed version is at [[outline|Cliff notes outline]].

'''
open(os.path.join(HERE, "content/index.md"), "w", encoding="utf-8").write(banner + d)

o = open(os.path.join(VAULT, OUTLINE), encoding="utf-8").read()
o = re.sub(r'^---\ntags:.*?\n---\n', '', o, flags=re.S)
o = o.replace("[[" + DRAFT[:-3] + "]]", "[[index|the full draft]]")
o = re.sub(r' Section map: \[\[The Self-Certification Problem — Outline\]\]\.', '', o)
o = o.replace("# The Self-Certification Problem — Cliff notes outline\n", "", 1)
open(os.path.join(HERE, "content/outline.md"), "w", encoding="utf-8").write('---\ntitle: "Cliff notes outline"\n---\n' + o)
print("copied draft and outline into content/ (banner dated", today + ")")
