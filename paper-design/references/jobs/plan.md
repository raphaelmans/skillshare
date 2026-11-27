# Plan

Carry designed Paper surfaces into a Spec and Tickets that link them, so Build and a fresh implementer find the design from the tracker. Plan's own writes are on the tracker. `/to-spec` and `/to-tickets` stay with the user.

## Triggers

- "Plan these screens", "turn this screen into a spec", "write up the settings page"
- "Make tickets for these components"
- "Link the design to ENG-142"
- "Continue" after `/to-spec` or `/to-tickets` has published
- "Let's build this sketch"

## Needs

A Paper link and the chosen surfaces, Sketch Page, Spec or redesign boundary. Tracker config for every branch that reaches the tracker.

Asking for Plan on a Spec authorizes [link-design](../steps/link-design.md)'s writes on that Spec: its Design Section, its UI Tickets' design instructions and criteria, and its Design Ticket. Changes to the Spec's requirements go through Reconcile.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md) when the user names one, the conversation just published one, or the surfaces appear in a Spec's Design Section. Closed specs can supply history. Keep an open Spec's identity when it already covers the work.
3. [Confirm design intent](../steps/confirm-design-intent.md). For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) across the agreed boundary.
4. [read-paper-surfaces](../steps/read-paper-surfaces.md) for the scoped components, screens or Sketch Page. [read-the-ui-system](../steps/read-the-ui-system.md) for the owning workspace.
5. Take the one next action for the state found.

## Next action

| State | Action |
| --- | --- |
| The surfaces live only on a Sketch Page | Recommend Design first ([From a Sketch](#from-a-sketch)) |
| No Spec, the user wants code, and [one session](#judge-the-size) can build it | Relay `/implement` |
| No Spec otherwise | Relay `/to-spec` |
| A Spec exists | Run [link-design](../steps/link-design.md) for whatever the Spec and its Tickets lack, then follow the Design Ticket lifecycle in [SKILL.md](../../SKILL.md) |

Each run takes one action and stops, so "continue" after the user's `/to-spec` or `/to-tickets` picks up the next row from the tracker's real records.

## Judge the size

Judge whether one fresh session can build the requested scope end to end. For a redesign, include the shared foundations, missing designs and retained behavior discovered in the coverage record. A single component or screen with known behavior usually fits. Several screens, a new flow, new data, or work that wants parallel tickets usually needs a Spec.

Use the area's Requirements Inventory and existing product evidence for permissions, error behavior, data and persistence. List any remaining unknowns as open questions.

## From a Sketch

A Sketch is not canonical. Recommend Design first so the chosen nodes are copied to their owner pages and the tracker links point at canonical surfaces. If the user goes straight on, warn that the canonical Paper pages will lack these surfaces.

## Ends with

A Relay or the link-design report. For a Relay, leave in the conversation: the Paper file link, each surface with its link, what it shows, its states, the real copy, the components used, the UI-system classification, the Requirements Inventory IDs it covers, and the open questions. Then name exactly one command:

- `/to-spec` when no Spec covers the work. A multi-session delivery with no Spec starts here too.
- `/implement` for the single-session branch, once Paper-first decisions are settled. Pass the reference links, baseline criteria and any code-first inferences. Instruct the implementer to [check the delivery revision](../steps/check-agreement.md#retained-behavior-at-delivery) and record the findings in the inventory or handover.
- `/to-tickets <spec>` when a Spec exists and delivery work has no ticket. Identify existing ticket owners so the breakdown covers only the unowned work.

Once the Spec and its UI Tickets have their design links, report the references and the Design Ticket state. If it is open, tell the user which screens to review and which ticket to close, then name **Build** as the Job to request for that Spec or UI Ticket after sign-off. If the ticket is already closed, offer Build for an implementation request.

For a feature port, give `/to-spec` publishable text for Further Notes with the target, scope, baseline, verification instructions and coverage record or durable link. For `/to-tickets`, supply **ticket-ready text for each slice**, including its baseline revision or inventory IDs, role and entry point, required action and outcome, exact Paper references, verification instructions and actual blockers. This also applies when the parent Spec already exists. Where design sign-off is pending, include that dependency in the published UI ticket. Check the written criteria and links before declaring UI tickets ready. A triage label alone establishes no Paper sign-off.

When a needed Paper-first design is missing, name Design as the next Job before any code Relay.

Tickets always come from a spec; a request for tickets with no spec goes through `/to-spec` first.
