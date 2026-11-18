# assess-design-scope

Classify the smallest Design Scope that contains a Spec's impact, list what needs a decision, and plan owner pages and batches. Analysis only.

- **Reads:** the Spec, the [read-the-ui-system](read-the-ui-system.md) result, repository routes, components, navigation, and tests, relevant Paper pages only (target validation)
- **May change:** nothing; its report is what Scope Approval approves

## Classify upward

Start at the lowest Design Scope level ([GLOSSARY.md](../../GLOSSARY.md)) and escalate only when the Spec's user stories require it. Use the highest level required and keep every lower level as a nested dependency. Classify by user-visible impact, not data-model complexity.

## Analyze

- Separate confirmed requirements, assumptions, gaps, and optional enhancements. Write each gap as a question with a recommended answer.
- Show a table: an Impact table for a Surface Change, a Coverage table above that. Use only applicable columns: user story, visual or non-visual, flow or journey, existing vs new, screens and Component Families, states, branches and recovery, dependencies, reuse from the UI system, status.
- Block design only on unresolved behavior, navigation, permissions, data, required states, flow, or composition. Optional enhancements stay out unless the Spec is changed to include them.
- When a gap lives in the Spec's text, show the exact edit so one approval covers the edit and the corrected scope.

## Plan

- **Page Ownership Plan:** the owner page for each family and artboard, by the Page arrangement table in [SKILL.md](../../SKILL.md), in human product names. Sketch and Archive pages are sources to copy from, never owners.
- **Sequence:** shared foundations, primary journeys and happy paths, branch paths, exceptions, edge cases; components before the screens that consume them.
- **Tracker edits:** list the Design Section edits, UI-ticket links, and Design Ticket creation [link-design](link-design.md) will make, so Scope Approval covers them.
- **Approved surfaces:** when the Design Ticket is closed, say which approved surfaces this work would change and ask the user to reopen the ticket first.
- **Possible drift:** from Spec and repository evidence alone, list existing families, artboards, flows, and viewports that may now be stale, and say that asking for Reconcile will audit them.

## Report

Lead with what needs a decision. Size the report to the scope: a Surface Change with no gap is a short report (target, Spec, families and states, pages, sequence). Include each workspace's UI-system classification.

Done when: the scope level, decisions, Page Ownership Plan, sequence, and tracker edits are reported, or every blocking gap is named as a question.
