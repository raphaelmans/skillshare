# assess-design-scope

Classify the smallest Design Scope that contains the requested change and its effects, list what needs a decision, and plan owner pages and batches. Analysis only.

- **Reads:** the Spec or scoped redesign coverage, the [read-the-ui-system](read-the-ui-system.md) result, repository routes, components, navigation, and tests, and the relevant Paper pages
- **May change:** nothing; its report is what Scope Approval approves

## Classify upward

Start at the lowest Design Scope level ([GLOSSARY.md](../../GLOSSARY.md)) and escalate when the user-visible impact requires it. For a redesign, use the named boundary and both inventories from [map-redesign-coverage](map-redesign-coverage.md). A discrepancy ticket describes only its own slice.

## Analyze

- Separate confirmed requirements, assumptions, gaps, and optional enhancements. In the scope report, identify what the user supplied, what will be drawn in context, and what will be inferred in code under [confirm-design-intent](confirm-design-intent.md). Put missing Paper-first designs in the drawing sequence. Ask a question with a recommended answer when a product decision is needed.
- Show a table: an Impact table for a Surface Change, a Coverage table above that. Use only applicable columns: user story, visual or non-visual, flow or journey, existing vs new, screens and Component Families, states, branches and recovery, dependencies, reuse from the UI system, status.
- Block design only on unresolved behavior, navigation, permissions, data, required states, flow, or composition. Optional enhancements stay out unless the Spec is changed to include them.
- When a gap lives in the Spec's text, show the exact edit so one approval covers the edit and the corrected scope.

## Plan

- **Page Ownership Plan:** the owner page for each family and artboard, by the Page arrangement table in [SKILL.md](../../SKILL.md), in human product names. Sketch and Archive pages are sources to copy from, never owners.
- **Sequence:** shared foundations, primary journeys and happy paths, branch paths, exceptions, edge cases; components before the screens that consume them.
- **Tracker edits:** for an open Spec, list the Design Section, coverage, UI ticket instructions and Design Ticket edits [link-design](link-design.md) will make, so Scope Approval covers them.
- **Approved surfaces:** if the work would change a signed-off design, identify the affected surfaces and ask the user to reopen its closed Design Ticket before editing them.
- **Possible drift:** from Spec and repository evidence alone, list existing families, artboards, flows, and viewports that may now be stale, and say that asking for Reconcile will audit them.

## Report

Lead with what needs a decision. Size the report to the scope: a Surface Change with no gap is a short report (target, Spec, families and states, pages, sequence). Include each workspace's UI-system classification.

Done when: the scope level, decisions, Page Ownership Plan, sequence, and tracker edits are reported, or every blocking gap is named as a question.
