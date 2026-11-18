# Design

Draw or update a spec's canonical components and screens in Paper after Scope Approval, then link them from the tracker.

## Triggers

- "Design ENG-142 in Paper", "draw the screens for this spec"
- "Move our existing product to this new Paper design" when its screens or component states need completing
- "Go ahead" or "approved" while a Size-up report awaits Scope Approval

## Needs

A Paper link and Scope Approval. Use a Ready Spec for spec-driven work. A brownfield redesign can draw from the named product boundary, evidenced requirements and target direction before an open migration Spec exists.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md) for spec-bound work. For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) from the target and existing product. Use any prior closed specs as evidence. When no open migration Spec exists, limit this Job's writes to Paper.
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [assess-design-scope](../steps/assess-design-scope.md). Reuse an unchanged report already shown in this conversation. List screens, states and shared components chosen for Paper-first work as concrete Paper edits. Identify code-first surfaces in the delivery handoff.
5. **Scope Approval** (Gates in [SKILL.md](../../SKILL.md)). Stop here until granted.
6. [draw](../steps/draw.md) each approved batch, components before the screens that consume them. Check continuity at the required scope. For a redesign, confirm the resulting nodes against both the retained requirements and target composition, and replace proposed nodes in the coverage record with their links.
7. [link-design](../steps/link-design.md) for the authorized tracker edits when there is an open Spec.

## Ends with

A report with the Paper Target, spec or redesign boundary, completed batches, linked Component Frames and Screen Artboards, coverage and open work. Follow the Design Ticket lifecycle when a Spec exists. For spec-free delivery, use [Write-up's sizing and Relay rules](write-up.md#judge-the-size) with the confirmed scope and completed designs.
