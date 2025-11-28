# Task 03 — Prompting for Task Automation

Contents:
- prompt.txt      ← final prompt design
- examples.json   ← three input→output examples
- Transform.py    ← simple heuristic script that converts notes/bullets -> JSON
- README.md       ← this file (with reflection)

How to run the script:
1. Put your notes into a file, e.g. notes.txt
2. Run:
   python3 Transform.py notes.txt
   OR:
   cat notes.txt | python3 Transform.py

What to submit:
- prompt.txt
- examples.json
- Transform.py
- README.md

Reflection on prompt iteration and debugging:
- Initial prompt produced inconsistent outputs (sometimes plain text, sometimes extra commentary). I added strict JSON output requirements and explicit field names (title, bullets, summary, structured) to force consistent structure.
- I added parsing rules for bullets and a fallback for paragraph inputs (split into sentences) to handle mixed input types.
- While testing the transform script, I found key-value patterns (e.g., "Key: Value") were easiest to extract reliably, so the script now normalizes such pairs to snake_case keys.
- Future improvements: call an LLM using prompt.txt for more natural summaries and smarter key inference; add unit tests for the parser.
