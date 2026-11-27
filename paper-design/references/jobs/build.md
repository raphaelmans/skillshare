# Build

Confirm Paper Approval and that Paper and the tickets agree, then Relay to `/implement` or `/implement-spec`. paper-design writes no code.

## Triggers

- "Build it", "implement ENG-142", "put the design into the codebase"
- "Start on the UI tickets"

## Needs

A Ready Spec and a Paper link. An implementation Relay also needs linked delivery tickets and Paper Approval.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md), loading every ticket, its blocking edges and the Design Ticket state.
3. [Confirm design intent](../steps/confirm-design-intent.md) for the port. For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) against the published tickets. Check for unowned surfaces and missing design evidence. A single-ticket request checks its slice and affected hosts within the confirmed scope.
4. Check [the Design Ticket lifecycle](../../SKILL.md). A UI ticket can start when its Design Ticket is closed or resolved and its own blockers are satisfied. For a whole Spec, check the coverage and dependency graph, then identify which tickets can start now. Do the coverage assessment before asking for sign-off. Send missing Paper-first designs to Design or Reconcile, and missing design links or a missing Design Ticket to Plan. For an agreed code-first inference, use the supplied reference, outcome and inventory row. Reopen approval only for changes to an approved design.
5. [read-paper-surfaces](../steps/read-paper-surfaces.md) and [check-agreement](../steps/check-agreement.md) for ticket-to-design coverage. Compare the requested ticket's statements against what its references show. Its future implementation is evaluated at delivery. Identify who owns each port and which independent chains can start.

## Preflight report

- Check that each port ticket includes its retained acceptance criteria and working baseline alongside its Paper links. Identify any missing criteria for the authorized tracker update before declaring the ticket ready. Report dependencies and unresolved requirements or Paper-first designs. An intentionally deferred artboard for an inferred surface is compatible with implementation readiness.
- Small wording or visual questions, asked in one batch, each with a recommended answer.
- Gaps that need spec or Paper edits go to Reconcile, not into the Relay.
- Missing delivery tickets go to `/to-tickets <spec>` with the unowned rows. Report the full redesign ready only when the entire requested boundary meets the coverage criteria. Label a partial frontier with the specific tickets ready to start.

## Ends with

A Relay once the user answers the batch:

- One ticket: `/implement <ticket>`.
- The whole spec: `/implement-spec <spec>` once every in-scope port has an owner, reference, retained criteria and a dependency path. Normal sequencing between covered tickets belongs in the graph. Report an incomplete spec separately from ready individual tickets.

Carry the direct Paper links, baseline criteria and answered decisions into the Relay. Instruct the delivery owner to [trace retained behavior on the integrated revision](../steps/check-agreement.md#retained-behavior-at-delivery) before declaring completion, including shared hosts changed by other tickets. Supply the inventory location for the results.
