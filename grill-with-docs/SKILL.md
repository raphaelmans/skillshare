---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
disable-model-invocation: true
---

# Grill with Docs

Run two coordinated responsibilities:

- **Grilling:** relentlessly interrogate the plan or design, challenge assumptions, and test concrete edge cases until boundaries and trade-offs are clear.
- **Domain modeling:** sharpen project language as terms crystallize, update the applicable glossary inline, and record an ADR only when the decision is hard to reverse, surprising without context, and the result of a real trade-off.

Load the `grilling` and `domain-modeling` companion skills through the current environment's supported skill mechanism when they are available. If either companion or a dedicated skill-invocation tool is unavailable, perform that responsibility directly; the workflow must not depend on one agent runtime's orchestration API.

References:

- [grilling](https://skills.sh/mattpocock/skills/grilling)
- [domain-modeling](https://skills.sh/mattpocock/skills/domain-modeling)
