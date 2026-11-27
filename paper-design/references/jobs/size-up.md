# Size-up

Classify the Design Scope of a Spec, a chosen Sketch or a redesign and report gaps, coverage, and a design sequence. Read-only analysis; it stops after the report.

## Triggers

- "How big is this?", "size up ENG-142"
- "What would designing this involve?"
- "What's missing from the spec before we design?"

Design and Reconcile run the same assessment themselves; this Job is for asking for it alone.

## Needs

A Paper link and one of: a Ready Spec, a chosen Sketch, or a named redesign boundary with evidence of existing behavior. The area's Requirements Inventory is that evidence when one exists; closed specs can add to it.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md) for spec-bound work. For a Sketch, [read-paper-surfaces](../steps/read-paper-surfaces.md) on the chosen variant. For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) to identify the affected workspaces and surfaces.
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [assess-design-scope](../steps/assess-design-scope.md)

## Ends with

The Step's report. Close with two offers, neither started here:

- **Design**, which needs Scope Approval of this report (Gates in [SKILL.md](../../SKILL.md)).
- **Reconcile**, when the assessment lists existing surfaces that may have drifted. Name them.
