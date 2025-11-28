# Prompt-Engineering-Task03
"SkillCraft Technology Task-03-Prompting for Task Automation
# Task 03 — Prompting for Task Automation

Contents:
- prompt.txt      ← final clear prompt to give to an LLM
- examples.json   ← three input->output examples
- transform.py    ← simple heuristic script that converts notes/bullets -> JSON

How to run the script:
1. Put your notes into a file, e.g. notes.txt
2. Run:
   python3 transform.py notes.txt
   OR:
   cat notes.txt | python3 transform.py

What to submit:
- prompt.txt (the prompt you designed)
- examples.json (three working examples)
- transform.py (showing a reproducible semi-automation approach)
- README.md (this file)

Reflection / Iteration notes:
- The prompt enforces deterministic JSON output (title, bullets, summary, structured) — this helps automated parsing.
- Iterations: refined bullet parsing rules, added fallback for paragraphs -> bullets, and explicit structured key extraction.
- Future improvements: replace transform.py with an LLM call (OpenAI/other) using prompt.txt to get higher-quality summaries and better inferred keys.
