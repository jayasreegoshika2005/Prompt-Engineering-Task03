#!/usr/bin/env python3
"""
transform.py
Usage:
  python transform.py input.txt
Or:
  echo -e "- a\n- b\n- c" | python transform.py
Produces JSON to stdout in the required format.
"""

import sys
import json
import re

def read_input():
    if not sys.stdin.isatty():
        text = sys.stdin.read().strip()
        if text:
            return text
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf8') as f:
            return f.read().strip()
    print("Provide input via file or stdin. Example: python transform.py notes.txt")
    sys.exit(1)

def split_bullets(text):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    bullets = []
    # detect bullets with leading -, •, *
    for ln in lines:
        if re.match(r'^[-•*]\s+', ln):
            bullets.append(re.sub(r'^[-•*]\s+', '', ln))
        else:
            bullets.append(ln)
    # if single paragraph, split into sentences and make bullets
    if len(bullets) == 1 and len(bullets[0].split()) > 10:
        sents = re.split(r'(?<=[.!?])\s+', bullets[0])
        bullets = [s.strip() for s in sents if s.strip()]
        if len(bullets) > 6:
            bullets = bullets[:6]
    return bullets

def make_title(bullets):
    if not bullets:
        return "Untitled"
    first = bullets[0]
    if len(first.split()) <= 6:
        return first
    return ' '.join(first.split()[:6])

def make_summary(bullets):
    # simple heuristic: join first 3 bullets into 3 sentences
    if not bullets:
        return ""
    sents = []
    for b in bullets[:4]:
        b = b.rstrip('.')
        sents.append(b + '.')
    summary = ' '.join(sents)
    # ensure 3-5 sentences
    return summary

def make_structured(bullets):
    structured = {}
    for i,b in enumerate(bullets):
        # detect key: value or key - value
        m = re.match(r'^(?P<k>[^:-]+)\s*[:\-]\s*(?P<v>.+)$', b)
        if m:
            key = m.group('k').strip()
            val = m.group('v').strip()
            structured[key] = val
        else:
            structured[f"point{i+1}"] = b
    return structured

def main():
    text = read_input()
    bullets = split_bullets(text)
    title = make_title(bullets)
    summary = make_summary(bullets)
    structured = make_structured(bullets)
    out = {
        "title": title,
        "bullets": bullets,
        "summary": summary,
        "structured": structured
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))

if _name_ == "_main_":
    main()
