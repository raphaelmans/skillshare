# Write-up

Read chosen Paper components or screens and Relay them toward delivery: straight to `/implement`, or through `/to-spec` and `/to-tickets`.

## Triggers

- "Turn this screen into a spec", "write up the settings page"
- "Make tickets for these components"
- "Let's build this sketch"

## Needs

A Paper link and the chosen surfaces, Sketch Page, or redesign boundary. Tracker config only for branches that reach `/to-spec` or `/to-tickets`.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md) when the user names one or the surfaces appear in a spec's Design Section. Use Reconcile for changes to an existing Spec. Closed specs can supply history. Keep an open Spec's identity when it already covers the work.
3. [Confirm design intent](../steps/confirm-design-intent.md). For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) across the agreed boundary.
4. [read-paper-surfaces](../steps/read-paper-surfaces.md) for the scoped components, screens or Sketch Page. [read-the-ui-system](../steps/read-the-ui-system.md) for the owning workspace.
5. Judge the size of the confirmed scope before choosing a Relay.

## Judge the size

Judge whether one fresh session can build the requested scope end to end. For a redesign, include the shared foundations, missing designs and retained behavior discovered in the coverage record. A single component or screen with known behavior usually fits. Several screens, a new flow, new data, or work that wants parallel tickets usually needs a Spec.

Use existing product evidence for permissions, error behavior, data and persistence. List any remaining unknowns as open questions.

## From a Sketch

A Sketch is not canonical. Recommend Design first so the needed nodes are copied to their owner pages before code is built. If the user goes straight to code, warn that the canonical Paper pages will lack these surfaces.

## Ends with

A Relay. Leave in the conversation: the Paper file link, each surface with its link, what it shows, its states, the real copy, the components used, the UI-system classification, and the open questions. Then name exactly one command:

- The user wants a spec or tickets and no open migration Spec exists: `/to-spec`. A multi-session delivery with no Spec starts here too.
- The user wants code, one session is enough, no Spec exists, and Paper-first decisions are settled: `/implement`. Pass the reference links, baseline criteria and any code-first inferences. Instruct the implementer to [check the delivery revision](../steps/check-agreement.md#retained-behavior-at-delivery) and record the findings in the inventory or handover.
- A spec exists and delivery work has no ticket: `/to-tickets <spec>`. Identify existing ticket owners so the breakdown covers only the unowned work.
- An open Spec and its tickets already cover the requested outcome: report those references. For a build request, continue to Build for preflight and its implementation Relay.

For a feature port, give `/to-spec` publishable text for Further Notes with the target, scope, baseline, verification instructions and coverage record or durable link. For `/to-tickets`, supply **ticket-ready text for each slice**, including its baseline revision or audit IDs, role and entry point, required action and outcome, exact Paper references, verification instructions and actual blockers. This also applies when the parent Spec already exists. Where design sign-off is pending, include that dependency in the published UI ticket. After publication, resume from the real records and run [link-design](../steps/link-design.md) under the approval covering those edits. Check the written criteria and links before declaring UI tickets ready. A triage label alone establishes no Paper sign-off.

When a needed Paper-first design is missing, take the Design path before a code Relay.

Tickets always come from a spec; a request for tickets with no spec goes through `/to-spec` first.
