#!/usr/bin/env python3
"""
Transform.py
Usage:
  python3 Transform.py notes.txt
  cat notes.txt | python3 Transform.py

Reads notes (bulleted or paragraph) and outputs JSON:
{
  "title": "...",
  "bullets": [...],
  "summary": "...",
  "structured": {...}
}
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
        with open(sys.argv[1], "r", encoding="utf8") as f:
            return f.read().strip()
    print("Usage: python3 Transform.py notes.txt")
    sys.exit(1)

def split_bullets(text):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    bullets = []

    for ln in lines:
        if re.match(r'^[-•\*\u2022]\s+', ln):
            bullets.append(re.sub(r'^[-•\*\u2022]\s+', '', ln))
        else:
            bullets.append(ln)

    if len(bullets) == 1:
        paragraph = bullets[0]
        if len(paragraph.split()) > 10:
            sents = re.split(r'(?<=[.!?])\s+', paragraph)
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
    if not bullets:
        return ""
    parts = []
    for b in bullets[:4]:
        s = b.rstrip('.').strip()
        if not s:
            continue
        parts.append(s + '.')
    summary = ' '.join(parts)
    return summary

def make_structured(bullets):
    structured = {}
    for i, b in enumerate(bullets):
        m = re.match(r'^\s*([^:–\-]+?)\s*[:\-–]\s*(.+)$', b)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            key_norm = re.sub(r'\s+', '_', key.lower())
            structured[key_norm] = val
        else:
            structured[f"point_{i+1}"] = b
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
