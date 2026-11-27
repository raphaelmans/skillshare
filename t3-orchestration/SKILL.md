---
name: t3-orchestration
description: Use when asked to hand off, hand over, or delegate work in T3 Code, or when selecting a subagent's model and reasoning effort.
---

# T3 orchestration

## Explicit handoffs

Launch subagents when the user hands off execution of named work. “Hand this off,” “hand this over,” and “offload the investigation” all qualify. Follow the stated action or recipient when the user asks for handover notes, discusses policy, or names a person to take over.

Delegate from the first hands-on step, including exploration, routine edits, and tests as needed. Give each child a cohesive assignment and ask for findings, diffs, or check results to review. Limit the main thread to planning, review, and synthesis. For “hand over the investigation and give me a fix plan,” the child investigates and the main thread writes the plan.

## Child model and reasoning effort

- **Model.** Honor the user's explicit choice for the child, including Astra, Fable, an exact version, or “match the main thread.” Otherwise choose the latest **Sol** for OpenAI or the latest **Opus** for Claude. Use the requested child provider or, by default, the main thread's model family.
- **Reasoning effort.** Use **medium** unless the user specifies another effort for that child.

For example, from a Fable thread, “use Fable for the reviewer and high effort for the tester” gives Fable at medium for the reviewer and the latest Opus at high for the tester.

Resolve “latest” using the native launcher's model list or the thread's `orchestrator_capabilities` result. Reuse that catalog across children. Follow T3's routing rules for the selected settings. Inherit when both model and effort match. Otherwise pass the settings through the launcher's current tool contract. Report an unavailable model or effort before launching that child.
