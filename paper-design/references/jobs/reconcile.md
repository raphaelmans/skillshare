# Reconcile

Find where a spec and Paper disagree, decide per Drift Item which side should change, and apply only an approved Reconcile Plan. Code is never changed here.

## Triggers

- "Paper and the spec have drifted, fix it"
- "Update Paper to match the new user stories"
- "The designer changed the checkout screen, get the spec in line"
- Following a Compare report: "reconcile those"
- "Sync this implemented surface back to Paper" for an inferred design recorded in the inventory

## Needs

A Paper link and an open, Ready Spec for spec reconciliation. For code-to-Paper sync of a deferred inference, use the surface's inventory entry, its implemented code and the supplied reference. This path also works after delivery or for a spec-free port.

## Sync an inventory entry from code

Open the target with [open-paper-file](../steps/open-paper-file.md). Read the inventory entry, inspect the current code at the named entry point, and check the originating reference and accepted behavior. Show the inferred surface and inventory update in the Reconcile Plan. A conflict with an approved design or business decision needs resolution before drawing. After Reconcile Approval, [draw](../steps/draw.md) the inferred surface, compare the resulting nodes with the implemented surface, then resolve the same inventory entry and link the nodes. Preserve pending evidence if comparison is incomplete. A closed Spec can supply history and stays closed. If its Design Section is the inventory, limit the approved bookkeeping edit to that row.

## Reconcile a Spec

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md). For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) across the requested product boundary, including relevant surfaces absent from this Spec.
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [assess-design-scope](../steps/assess-design-scope.md) from the Spec and any redesign coverage. Reconcile uses its own approval.
5. [read-paper-surfaces](../steps/read-paper-surfaces.md) for those surfaces only. Reuse Compare evidence from this conversation while the spec, Paper nodes, and repository are unchanged.
6. [check-agreement](../steps/check-agreement.md) between Spec and Paper for each user story or scenario. For a redesign, also account for mapped target surfaces and record outstanding code ports under their delivery owners.
7. Classify and plan (below), then wait for **Reconcile Approval** (Gates in [SKILL.md](../../SKILL.md)).
8. Apply the approved plan (below).

## Classify each Drift Item

Infer direction per item; one run can hold both directions.

- **Spec to Paper**: a story, rule, or decision in the spec is missing, stale, or contradicted in Paper.
- **Paper-to-Spec candidate**: Paper shows intentional composition or behavior the spec lacks. A proposal until approved.
- **Unresolved**: both sides are explicit and conflict, provenance is unclear, or the fix would change business behavior without evidence. Ask the user.
- **Aligned**: equivalent. Leave it.

For ordinary spec reconciliation, use code and history as provenance. In a redesign, confirmed existing business requirements inform the Spec and any missing Paper states. The chosen target determines the new visual treatment. Use the coverage record to carry these decisions through both directions.

## The Reconcile Plan

Show one plan listing each Drift Item with evidence, direction, exact Paper nodes or spec text affected, dependency order, and status. When several surfaces depend on the same change, list it once with one owner and name its consumers. Include the Page Ownership Plan and the proposed name of each missing design. If the plan would change a signed-off design, name the affected surfaces and ask the user to reopen its closed Design Ticket before editing them. Resolve open decisions before applying the plan. For a multi-batch redesign, hold the affected items and their dependents while independent batches proceed under the approval for their edits.

Name each edit boundary separately so the approval covers them precisely:

- **Paper edits**
- **Spec text edits**
- **Inventory or tracker edits**: affected coverage entries, Design Section, UI ticket design instructions and acceptance criteria, Design Ticket

## Apply

- **Spec to Paper**: [draw](../steps/draw.md) the approved items on their owner pages, components before screens, reusing current nodes in place.
- **Paper to Spec**: edit exactly the approved spec text on the tracker, keeping its structure. Rerun [assess-design-scope](../steps/assess-design-scope.md) for affected rows when user stories changed.
- [link-design](../steps/link-design.md) only for the tracker edits the plan listed.

Then rerun the affected agreement rows, checking new or edited nodes and replacing proposed surfaces with their actual links. Report missing implementation tickets separately from completed Paper edits.

## Ends with

A report of aligned, applied, deferred, and unresolved items. Follow-ups: new delivery work → Relay `/to-tickets <spec>`, then Plan links the new tickets; code that now lags → ask paper-design to build it.
