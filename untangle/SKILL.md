---
name: untangle
description: Turn a messy, rambling, or scattered message into a clean version that says what the user meant, and return only that rewritten message. Use when the user explicitly invokes this skill on rough text they want regenerated, with no explanation, vocabulary, or teaching.
---

# Untangle

Read the user's messy text, work out what they are trying to say, and write it again cleanly. Output only the regenerated message.

## Workflow

1. Infer the intended meaning, purpose, audience, and tone from the text and surrounding context.
2. Pick the most likely interpretation and commit to it. Do not ask which one is correct.
3. Regenerate the message from that understanding instead of editing it line by line. Reorder ideas into a logical sequence, merge repeated points, and drop false starts and filler.
4. Keep the user's voice and register. Casual stays casual, direct stays direct; do not make it formal or corporate.
5. Keep every real detail: facts, names, numbers, constraints, requests, URLs, code, and placeholders. Do not invent anything the user did not say or clearly imply.
6. Match the language of the original text.

If the user invokes the skill without supplying text, ask them to provide it.

## Response Format

Return only the regenerated message, ready to copy and paste. No headings, preamble, explanation, or vocabulary notes.

Exception: if the text has two materially different readings, add one short line after the message starting with `Note:` that names the alternative.

## Quality Check

Before responding, confirm that the message:

- Says what the user meant, not just what they literally typed.
- Keeps all useful detail and adds nothing new.
- Sounds like the user, only clearer.
- Contains nothing but the message (plus an optional `Note:` line).
