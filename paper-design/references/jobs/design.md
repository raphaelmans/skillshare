# Design

Draw or update a spec's canonical components and screens in Paper after Scope Approval, then link them from the tracker.

## Triggers

- "Design ENG-142 in Paper", "draw the screens for this spec"
- "Go ahead" or "approved" while a Size-up report awaits Scope Approval

## Needs

A Ready Spec, a Paper link, and Scope Approval.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md)
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [assess-design-scope](../steps/assess-design-scope.md). Reuse an unchanged report already shown in this conversation.
5. **Scope Approval** (Gates in [SKILL.md](../../SKILL.md)). Stop here until granted.
6. [draw](../steps/draw.md) Design Batch by Design Batch in the approved order: every Component Frame a batch needs before the Screen Artboards that consume it, then check flow, journey, or product continuity as the Design Scope requires. Work already in agreement with the spec stays as it is.
7. [link-design](../steps/link-design.md) with the tracker edits the approved report showed.

## Ends with

A report: Paper Target, spec, batches completed, Component Frames and Screen Artboards created or updated with links, coverage against the spec's Visual Requirements, and anything left open. Then the next action for the Design Ticket state link-design reported, from the lifecycle table in [SKILL.md](../../SKILL.md).
