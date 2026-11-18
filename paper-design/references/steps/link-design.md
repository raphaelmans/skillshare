# link-design

Write the Spec's Design Section, the artboard links on its UI Tickets, and its Design Ticket, so a fresh session can find the design and its sign-off state from the tracker.

- **Reads:** the Spec, its Tickets, the frames and artboards [draw](draw.md) produced or confirmed
- **May change:** the Spec's `## Design` section; artboard links on UI Tickets; the Design Ticket and its blocking edges
- **Gate:** Scope Approval (Design) or Reconcile Approval (Reconcile)

Use the operations in `docs/agents/issue-tracker.md` for every write.

## Design Section

Write or refresh one `## Design` section on the Spec:

- The Paper file link and links to the owner pages or frames for this Spec
- The Design Scope level ([GLOSSARY.md](../../GLOSSARY.md))

Keep the rest of the Spec body as it was. The section holds links and the scope only.

## UI Ticket links

For each UI Ticket, add links to the specific artboards and component frames it builds, so `/implement` opens only what that Ticket needs. Leave non-UI Tickets unchanged. When no Tickets exist yet, skip this and the Design Ticket.

## Design Ticket

paper-design owns this ticket; upstream skills know nothing about it. When the Spec has UI Tickets and no Design Ticket, create a sub-issue of the Spec titled "Design in Paper", give it the human-in-the-loop role from `docs/agents/triage-labels.md` (never `ready-for-agent`), and add blocking edges to every UI Ticket. Its body holds the Paper file link, the Design Section's links, and one line saying a human closes it to approve the design. Leave non-UI Tickets unblocked.

Never close or reopen it yourself; that is the user's approval.

## Report

State what was written and the resulting Design Ticket state from the lifecycle table in [SKILL.md](../../SKILL.md).

Done when: the Design Section and every UI Ticket's links match the approved edits exactly.
