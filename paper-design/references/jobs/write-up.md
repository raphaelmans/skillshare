# Write-up

Read chosen Paper components or screens and Relay them toward delivery: straight to `/implement`, or through `/to-spec` and `/to-tickets`.

## Triggers

- "Turn this screen into a spec", "write up the settings page"
- "Make tickets for these components"
- "Let's build this sketch"

## Needs

A Paper link and the chosen surfaces (named, or the Sketch Page). Tracker config only for branches that reach `/to-spec` or `/to-tickets`.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [read-paper-surfaces](../steps/read-paper-surfaces.md) for the chosen components, screens, or Sketch Page.
3. [read-the-ui-system](../steps/read-the-ui-system.md) for the owning workspace.
4. [find-the-spec](../steps/find-the-spec.md) when the user names one or the surfaces already appear in a spec's Design Section. Surfaces that already belong to a spec go to Reconcile instead; say so and stop.
5. Judge the size (below).

## Judge the size

Ask one question: can one fresh session build this, end to end, without losing the thread? A single component or screen with known behavior usually can. Several screens, a new flow, new data, or work that wants parallel tickets usually cannot.

List what Paper cannot show as open questions, never as invented rules: who can see it, what happens on error, where data comes from, what is persisted.

## From a Sketch

A Sketch is not canonical. Recommend Design first so the needed nodes are copied to their owner pages before code is built. If the user goes straight to code, warn that the canonical Paper pages will lack these surfaces.

## Ends with

A Relay. Leave in the conversation: the Paper file link, each surface with its link, what it shows, its states, the real copy, the components used, the UI-system classification, and the open questions. Then name exactly one command:

- One session is enough: `/implement`.
- Bigger, no spec: `/to-spec`, then `/to-tickets` on the new spec.
- A spec exists without tickets: `/to-tickets <spec>`.

Tickets always come from a spec; a request for tickets with no spec goes through `/to-spec` first.
