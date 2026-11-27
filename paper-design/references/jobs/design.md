# Design

Draw or update canonical components and screens on their owner pages after Scope Approval. Its only writes are in Paper.

## Triggers

- "Design ENG-142 in Paper", "draw the screens for this spec"
- "Make this sketch official", "promote option B from Sketch / Round 2"
- "Move our existing product to this new Paper design" when its screens or component states need completing
- "Go ahead" or "approved" while a Size-up report awaits Scope Approval

## Needs

A Paper link, Scope Approval, and one source of requirements:

- **A Ready Spec.**
- **A chosen Sketch.** The user names the Sketch Page and the variant to promote. When several variants remain and none is named, ask which one. The Sketch Brief, the chosen nodes and the area's Requirements Inventory supply the requirements.
- **A redesign boundary.** A brownfield redesign can draw from the named product boundary, evidenced requirements and target direction before an open migration Spec exists.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. Read the source:
   - **Spec:** [find-the-spec](../steps/find-the-spec.md).
   - **Sketch:** [read-paper-surfaces](../steps/read-paper-surfaces.md) on the chosen variant, and the area's Requirements Inventory when one exists.
   - **Redesign:** [map-redesign-coverage](../steps/map-redesign-coverage.md) from the target and existing product, using prior closed specs as evidence.
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [assess-design-scope](../steps/assess-design-scope.md). Reuse an unchanged report already shown in this conversation. List screens, states and shared components chosen for Paper-first work as concrete Paper edits. For a Sketch, list each chosen node with its owner page and canonical name, plus every state the inventory or component contract requires that the Sketch leaves out. Identify code-first surfaces for the delivery handoff.
5. **Scope Approval** (Gates in [SKILL.md](../../SKILL.md)). For a Sketch promotion, request approval for the chosen nodes you actually read and their concrete destination pages and names. If the variant's contents or ownership are still unknown, report what needs resolving before asking for approval. In either case, explain that promotion produces the canonical Paper design and that the user can request Plan afterward for a spec and tickets. Stop before drawing until the displayed edits are approved.
6. [draw](../steps/draw.md) each approved batch, components before the screens that consume them. Check continuity at the required scope. For a redesign, confirm the resulting nodes against both the retained requirements and target composition, and replace proposed nodes in the coverage record with their links.

## Ends with

A report with the Paper Target, the Spec, Sketch or redesign boundary, completed batches, linked Component Frames and Screen Artboards, coverage and open work. When the area has a Requirements Inventory, list its in-scope Visible Keep IDs beside the verified canonical references that cover them. List each uncovered ID with the missing state, and carry the Nonvisual IDs forward as delivery criteria.

Offer Plan to carry these surfaces and criteria into the Spec and Tickets and create the Design Ticket the user closes to approve them.
