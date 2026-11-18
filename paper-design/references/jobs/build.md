# Build

Confirm Paper Approval and that Paper and the tickets agree, then Relay to `/implement` or `/implement-spec`. paper-design writes no code.

## Triggers

- "Build it", "implement ENG-142", "put the design into the codebase"
- "Start on the UI tickets"

## Needs

A Ready Spec with tickets, a Paper link, and Paper Approval.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md), loading every ticket and its blocking edges. Continue only when the Design Ticket is closed; in any other state, take the next action from the lifecycle table in [SKILL.md](../../SKILL.md) and stop.
3. [read-paper-surfaces](../steps/read-paper-surfaces.md) for the artboards each UI ticket links.
4. [check-agreement](../steps/check-agreement.md) with one row per UI ticket, between the ticket and its linked artboards. The UI system is not loaded here; code conventions and component-system choices are `/implement`'s concern.

## Preflight report

- Tickets ready to build, and blocked chains: a ticket blocks only when it or a ticket it depends on intersects a Gap, a missing artboard, or an open decision.
- Small wording or visual questions, asked in one batch, each with a recommended answer.
- Gaps that need spec or Paper edits go to Reconcile, not into the Relay.

## Ends with

A Relay once the user answers the batch:

- One ticket: `/implement <ticket>`.
- The whole spec: `/implement-spec <spec>`.

The Relay carries the Paper file link, each ticket's artboard and Component Frame links, and the answered questions verbatim, so the implementer works from them without reopening this conversation.
