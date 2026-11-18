# check-agreement

Compare the sources the Job names, one row per unit the Job names, and label where they agree. Strictly read-only; it fixes nothing.

- **Reads:** whichever of these the Job names: the Spec, Tickets and blocking edges, [read-paper-surfaces](read-paper-surfaces.md) evidence, the [read-the-ui-system](read-the-ui-system.md) result, code, tests, and a rendered UI that runs without changing code
- **May change:** nothing

## Rows

One row per unit the Job names: a user story, scenario, or UI Ticket. Classify each as visual or non-visual; non-visual rows compare Spec to code only.

## Axes

- Required states and variations
- Visible content and realistic data shape
- Actions, navigation, interaction outcomes
- Conditional visibility, empty and error behavior
- Component-family reuse and screen composition
- Responsive hierarchy at required viewports
- Tokens, typography, spacing, layout intent
- Component-system reuse where it materially affects consistency
- Non-visual behavior (code only)

An axis whose source was not loaded is Not applicable. Judge meaning, not pixels. For code evidence, inspect components, routes, state handling, tests, and styles; add no code, dependencies, fixtures, or config to make the check possible.

## Labels

- **Aligned:** behavior, states, composition, and visual language agree.
- **Close:** behavior and states agree; differences are equivalent tokens or reflow that keeps hierarchy.
- **Gap** and **Pending Evidence:** as [GLOSSARY.md](../../GLOSSARY.md) defines them. Missing code is Pending Evidence, never Close.
- **Not applicable:** the source cannot represent the row, such as a cache rule in Paper.

Custom markup that could reuse a Configured component is non-blocking drift unless it breaks a required behavior, state, accessibility contract, token, or material composition. Unconfigured shadcn compatibility is never evidence.

Reuse rows labelled earlier in the conversation while their inputs are unchanged.

## Owners

Name the owner of each Gap: Spec/Paper disagreement goes to Reconcile, code gaps to Build ("ask paper-design to build it"), missing Tickets to `/to-tickets`, work on a closed Spec to a new Spec. Block a Ticket only through real blocking edges.

Done when: every row has a label with evidence from each named source, and every Gap has an owner.
