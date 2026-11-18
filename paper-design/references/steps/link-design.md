# link-design

Write the Spec's Design Section, the artboard links on its UI Tickets, and its Design Ticket, so a fresh session can find the design and its sign-off state from the tracker.

- **Reads:** the Spec, its Tickets, any redesign coverage record, and the frames and artboards confirmed in Paper
- **May change:** the Spec's Design Section, UI ticket design instructions and acceptance criteria for visual and retained behavior, the Design Ticket and its blocking edges
- **Gate:** Scope Approval (Design) or Reconcile Approval (Reconcile)

Use the operations in `docs/agents/issue-tracker.md` for every write.

## Design Section

Write or refresh one `## Design` section on the Spec:

- The Paper file link and links to the owner pages or frames for this Spec
- The Design Scope level ([GLOSSARY.md](../../GLOSSARY.md))

For a redesign, add its named boundary and the coverage record from [map-redesign-coverage](map-redesign-coverage.md), or link to the existing durable record. Carry forward its requirement IDs. If the audit only compares business rules, keep that evidence and add the missing design-to-code and ticket mappings here. For large specs, group the rows or links by module. Update entries in place as proposed work gets real node links and ticket IDs. Keep the rest of the Spec body as it was.

For a port, put the working baseline reference in the Design Section. Include this completion instruction for the person integrating the work: trace every retained acceptance criterion on the final combined revision, record evidence by inventory row, and restore confirmed regressions before reporting the port complete.

## UI Ticket links

Make each UI Ticket usable when opened directly in a fresh session. Name the parent Design Section and Design Ticket, have the implementer check its blockers, and instruct them to open the [specific surface references](open-paper-file.md#reference-a-specific-surface) before coding. Name the confirmed hosts, required effects, related features in scope and observable result. For a code-first surface, identify the inferred portion, link its supplied reference and tell the implementer where to record drift on completion. Include the shared component owner where applicable. Check the reverse mapping for target surfaces that need work and have no owning delivery ticket. Relay those to `/to-tickets <spec>`.

Put the slice's retained behaviors directly in its acceptance criteria with the baseline reference or audit IDs. Write them as observable role-specific journeys, including those missing from the hi-fi. For example, “A viewer following a record link can read the record. A contributor entering from the list can submit a correction and return to the same record.” Use the actual roles, actions and outcomes evidenced for that ticket. Put any user-specified verification limits and the person responsible for remaining checks in the ticket and parent handoff so a fresh implementer inherits them.

Leave non-UI Tickets unchanged. When no Tickets exist yet, persist the approved Design Section with the planned work, then Relay to `/to-tickets <spec>`. On return, read the published tickets and link their actual IDs and designs.

## Design Ticket

When the Spec has UI Tickets, reuse its "Design in Paper" sub-issue or create it with the human-in-the-loop role from `docs/agents/triage-labels.md`. Ensure every UI Ticket, including newly added ones, has this blocking edge. Its body holds the Paper file link, the Design Section's links, and one line saying a human closes it to approve the design. Leave non-UI Tickets unblocked.

Never close or reopen it yourself; that is the user's approval.

## Report

State what was written, uncovered work and the resulting Design Ticket state from the lifecycle table in [SKILL.md](../../SKILL.md). For a redesign, check the published Spec and ticket bodies from the perspective of a fresh implementer.

Done when: the Design Section and every UI Ticket's links match the approved edits exactly.
