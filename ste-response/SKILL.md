---
name: ste-response
description: Write all assistant-authored English prose for the current request in a clear style aligned with ASD-STE100 Simplified Technical English. Use only when the user explicitly invokes `$ste-response`. Apply the style to progress updates, questions, explanations, and final answers without claiming formal ASD-STE100 compliance.
disable-model-invocation: true
---

# STE Response

Respond in clear technical English that is aligned with ASD-STE100 Issue 9. Do not claim that the response complies with, conforms to, or is certified under ASD-STE100.

## Scope

- Apply this skill only to the request in which the user invokes it.
- Apply the style to all assistant-authored English prose, including commentary and the final answer.
- Complete the requested task. Do not treat the invocation as a request to rewrite the user's text unless the user asks for a rewrite.
- Keep all necessary facts, qualifications, and technical detail. Do not remove useful content only to make the response brief.
- Do not add an STE label, a compliance statement, or an explanation of the style unless the user asks for it.
- Keep code, commands, identifiers, file paths, URLs, quotations, logs, and error messages unchanged.
- If the requested output is not English, apply this skill only to the surrounding English prose.

## Write the response

1. Determine the result that the user needs.
2. Draft the complete answer with the necessary detail.
3. Revise the assistant-authored English prose with the rules below.
4. Check that the revision preserves the original meaning and exact technical tokens.

## Use clear words

- Prefer common words with one clear meaning.
- Use technical terms when they are necessary for accuracy.
- Use one term consistently for each concept. Do not alternate between synonyms for variety.
- Define an unfamiliar technical term when the context does not make its meaning clear.
- Avoid idioms, slang, regional expressions, filler, and unnecessary jargon.
- Use American English spelling unless the user requests a different spelling convention.
- Use a noun as a noun and a verb as a verb when a simple construction is available.

Do not enforce the ASD-STE100 controlled dictionary. This skill is STE-aligned, not a formal vocabulary checker.

## Use direct grammar

- Prefer the active voice.
- Use the imperative form for instructions.
- Put a condition before the action when the reader must know the condition first.
- Write one instruction in each sentence. Combine actions only when they occur at the same time.
- Do not use contractions.
- Avoid complex verb chains and unnecessary `-ing` constructions.
- Use articles and demonstrative adjectives when they prevent ambiguity.
- Use a pronoun only when its referent is clear.

## Use short structures

- Aim for no more than 20 words in an instructional sentence.
- Aim for no more than 25 words in a descriptive sentence.
- Split a sentence when the split improves clarity. Do not split exact text or damage technical meaning.
- Give one main topic in each paragraph.
- Use no more than six sentences in a paragraph when practical.
- Use a vertical list for complex information, alternatives, or multiple steps.
- Give information gradually and put the result before supporting detail.
- Use connecting words when they make the relationship between sentences clear.
- Do not use semicolons.

## Resolve conflicts

Follow higher-priority instructions and the user's explicit requirements. Preserve required terminology, legal wording, safety wording, quotations, and output formats even when they do not follow this style.

When a style rule conflicts with accuracy, use the accurate wording. Then make the surrounding prose as clear as possible.

## Check the response

Before sending the response, confirm that:

- The response completes the user's task.
- The first sentence gives the result when a result is available.
- Each sentence has a clear purpose.
- Instructions use direct commands and clear conditions.
- Terms remain consistent.
- Pronouns have clear referents.
- All necessary detail remains present.
- Exact technical text remains unchanged.
- The response makes no formal compliance claim.

The source standard is [ASD-STE100 Simplified Technical English, Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), published on January 15, 2025.
