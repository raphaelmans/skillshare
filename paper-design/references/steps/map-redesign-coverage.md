# Map redesign coverage

Use this read-only Step when an existing product is moving to a new Paper design. Use the boundary established in [confirm-design-intent](confirm-design-intent.md). For a larger redesign, work by module or journey and include the shared shell once.

## Establish both sides

1. Use the last known working baseline from [confirm-design-intent](confirm-design-intent.md), the target Paper file and the accepted decisions. Record what supports each retained requirement. Existing defects and incidental styling carry no product authority.
2. Independently walk the target's relevant owner pages and referenced shared components, including paginated results. Inventory Screen Artboards by scenario and required viewport, and Component Families by their material states. Inspect the shell and navigation embedded in screens even when they lack a standalone frame. A user-selected prototype or legacy page can supply the target direction for promotion to canonical pages. A partial scan leaves Pending Evidence.
3. Join both inventories. A retained or approved new behavior may span several screens. A redesigned screen or component may need a visual port even when every business rule already works. Include both in the coverage record. Reuse fresh evidence when resuming and refresh rows affected by changes to the target, code, decisions, or tickets.

## Record what each item needs

Keep the record in the report until a tracker write is authorized. For each item retain enough information to recover these fields:

| Requirement or target surface | Baseline behavior and source decision | Target Paper screen, frame, state or gap | Code entry point and evidence at the revision inspected | Work, owner ticket and dependencies |
| --- | --- | --- | --- | --- |
| Sidebar pending count (example) | The product shows the number of items awaiting a decision | New sidebar is drawn on the module screen. Its count state is missing. | The old navigation renders the right count in the previous layout. | Draw the target count state. Assign one shared sidebar port and link consuming screens to it. |

Use human names and direct Paper links for existing nodes. A missing node gets a proposed owner page and name until drawn. Group related items when their IDs, links and dispositions remain individually traceable. Preserve the existing audit as evidence. A business-rule match alone establishes only behavior.

- **Retained visible behavior missing from Paper.** By default, put the smallest screen, component or state that expresses the requirement on the drawing plan. Design or Reconcile draws it under the approval for those edits. A read-only audit reports it. When implementation is in scope and a code-first inference fits the agreed boundary, give the implementer the reference, required outcome and inventory row for later Paper sync.
- **New composition or rebrand missing from code.** Record implementation work for the actual application entry point, including shared layout, navigation, or tokens where they differ. Give each shared change one owner. Connect consuming tickets through real dependencies.
- **Nonvisual rule.** Carry it into the spec or acceptance criteria with its code evidence. A redirect or permission check needs a Paper state only when it has a visible consequence.
- **Changed behavior or conflicting evidence.** Carry forward explicit additions, retirements, and deferrals with their decisions. A missing control alone does not retire a capability. A Paper-only action that implies new permissions, costs, or persistence needs product evidence. Isolate unresolved decisions to the affected work and continue independent batches.

## Handover and completion

- **Design coverage.** Account for every target surface and map each visible requirement to a confirmed state or a named gap. Distinguish deferred code-first surfaces from missing Paper-first work. Design parity remains open wherever a required composition is missing.
- **Ready for parallel development.** Every needed port has a published owner ticket with direct reference links, an observable outcome and its blocking edges. For a code-first inference, link the supplied design and the inventory row in place of a future artboard. Other surfaces have evidence that code already matches or an agreed exclusion. Report ticket coverage separately from permission to start. UI work can start once Paper Approval and its actual dependencies are satisfied. An uncovered shared component prevents a whole-scope readiness claim.
- **Implemented and verified.** At delivery, [check agreement](check-agreement.md#retained-behavior-at-delivery) for each baseline criterion against the integrated revision. Keep its result alongside the original baseline and evaluate Paper composition separately. State which visual checks are still pending.

Size the report to the request. For a large project, reconcile the baseline requirement IDs and target surface list separately against the detailed rows. Summarize accounted-for and outstanding items by module and name unmatched IDs or surfaces, including shared work. A partial scan supports a partial verdict. A fresh session must be able to recover both inventories, decisions, ownership and remaining verification from the published handoff.
