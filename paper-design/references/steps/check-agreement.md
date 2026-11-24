# check-agreement

Compare the sources the Job names, one row per unit the Job names, and label where they agree. Strictly read-only; it fixes nothing.

- **Reads:** whichever of these the Job names: the Spec, Tickets and blocking edges, [read-paper-surfaces](read-paper-surfaces.md) evidence, the [read-the-ui-system](read-the-ui-system.md) result, code, tests, and a rendered UI that runs without changing code
- **May change:** nothing

## Rows

Use each unit the Job names. For a redesign, check retained requirements and target surfaces independently using [map-redesign-coverage](map-redesign-coverage.md). Record the evidence for behavior and for composition separately. Nonvisual rows compare requirements to code.

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

Use only the axes the Job calls for. A required source that was unavailable or uninspected leaves Pending Evidence. Not applicable means the source cannot represent that axis. For code evidence, inspect components, routes, state handling, tests and styles. Where rendered evidence is needed, respect the user's verification instructions and name any pending checks.

## Retained behavior at delivery

Compare the last known working baseline with the revision being delivered. For parallel work, use the combined integration revision after the relevant merges. For each retained criterion, follow its real navigation or direct entry, role and state conditions, reachable action, and resulting transition or side effect. An existing component or handler can be orphaned by a change in its host. Record both revisions and the decisive evidence against the inventory row. Recheck affected rows if subsequent integration changes their paths.

| Finding | Disposition |
| --- | --- |
| A supported baseline path is now unreachable or its required outcome is broken without an accepted change | **Regression (Gap).** Identify where the path broke. The implementing owner restores it before claiming completion and rechecks the integrated path. |
| The product owner accepted a replacement or retirement | Cite the decision and, for a replacement, trace the new path to the agreed outcome. |
| A required new behavior is demonstrably absent | **Gap.** Track the outstanding implementation work. |
| The behavior works, but the implementation still uses a different layout from the approved Paper target | **Implementation gap.** Cite the target and the differing host or state. Correct the port before claiming visual agreement. |
| The required behavior works in code, and evidence shows that its Paper representation is missing or stale | **Paper drift.** Record **Implemented — Paper sync pending** for an agreed code-first inference or accepted Paper update. If the direction is unresolved, report the conflict for Reconcile. |
| The evidence cannot establish baseline behavior, current reachability, or the result | **Unverified (Pending Evidence).** Name the missing evidence. Keep any rendered or interaction checks reserved for the user pending. |

## Labels

- **Aligned:** behavior, states, composition, and visual language agree.
- **Close:** behavior and states agree; differences are equivalent tokens or reflow that keeps hierarchy.
- **Gap** and **Pending Evidence:** use the delivery findings above for code comparisons. A known discrepancy or an unverified required source keeps parity open for the affected scope.
- **Not applicable:** the source cannot represent the row, such as a cache rule in Paper.

Custom markup that could reuse a Configured component is non-blocking drift unless it breaks a required behavior, state, accessibility contract, token, or material composition. Unconfigured shadcn compatibility is never evidence.

Keep findings per behavior and composition. One surface can have both a broken action and an outstanding Paper drawing. Restore the action and recheck it before classifying the remaining difference as Paper-only. If a mockup suggests a new action without an accepted business rule, report the product decision for Reconcile. Reuse earlier evidence while its inputs are unchanged.

## Owners

Route spec/Paper disagreements to Reconcile, code gaps to Build, missing delivery tickets to `/to-tickets`, and new product work on a closed Spec to a new Spec. For intentionally deferred code-to-Paper sync, the existing inventory entry tracks the difference. Block a Ticket only through real blocking edges.

Done when: every row has a label with evidence from each named source, and every Gap has an owner.
