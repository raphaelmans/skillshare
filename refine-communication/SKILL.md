---
name: refine-communication
description: Refine messages, prompts, explanations, thoughts, and rough ideas into clear, precise, concise, natural writing without changing their intent, nuance, constraints, context, or voice. Use when the user explicitly invokes this skill to rewrite text, explain the likely meaning, and teach useful vocabulary and reusable phrasing.
---

# Refine Communication

Improve how the user's text is expressed without changing what they mean.

## Workflow

1. Infer the intended meaning, purpose, audience, tone, nuance, and constraints from the text and surrounding context.
2. Choose the most likely interpretation. Mention an alternative only when it materially affects the message; do not stop to ask which interpretation is correct.
3. Rewrite the text for clarity, precision, concision, naturalness, and logical structure.
4. Preserve the user's voice and all useful detail. Do not make direct, casual, technical, persuasive, or reflective writing needlessly formal, corporate, academic, or verbose.
5. Remove filler and repetition, strengthen vague wording, and reorganize ideas when that improves comprehension without oversimplifying them.
6. Preserve factual claims, terminology, proper nouns, constraints, placeholders, data, URLs, code, and meaningful formatting unless the user asks to change them. Do not invent supporting information.
7. Teach only vocabulary and phrasing that will genuinely help the user communicate similar ideas more effectively in the future.

If the user invokes the skill without supplying text, ask them to provide the text to refine.

## Response Format

Use these four sections in this order unless the user explicitly requests a different format:

## What I understood

Briefly explain the intended message. Note a material ambiguity or plausible alternative interpretation only when relevant.

## Refined version

Provide the improved text. Keep useful detail even when the clearest version remains somewhat long.

## Useful vocabulary

List concise, practical suggestions in this form:

- **Term** — Short meaning. Example: “A sentence showing how to use it in a future prompt.”

Avoid obscure or forced vocabulary. If no stronger vocabulary is genuinely needed, say so briefly while retaining the section.

## Reusable phrasing

Provide a few sentence patterns tailored to the user's communication goal, such as:

- “The distinction I’m trying to make is…”
- “What I’m trying to convey is…”
- “Preserve X while reducing Y.”
- “Infer the intent rather than rewriting literally.”
- “Make this concise without sacrificing precision.”

## Quality Check

Before responding, confirm that the rewrite:

- Preserves intent, nuance, constraints, context, and voice.
- Is clearer and more precise without becoming unnecessarily formal.
- Removes repetition without deleting useful information.
- Uses specific, natural wording.
- Keeps all four sections concise and useful.
