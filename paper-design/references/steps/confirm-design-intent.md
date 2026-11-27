# Confirm design intent

Use this Step when a supplied design guides a feature port or shows only part of an interaction. Read the request, the selected design, any agreed spec, and the actual entry points where people use it.

## Establish the boundary

For every port of existing behavior, capture the last known working revision before implementation. When the area has a Requirements Inventory (`docs/agents/design-inventory/<area>.md`), it is the baseline: reuse its rows and IDs, and re-inspect only rows whose code changed since its recorded revision. If work has already started, recover the baseline from a known release, prior commit or versioned audit. Record its reference once in the inventory or handoff and reuse its requirement IDs. If the working baseline cannot be established, identify the affected behaviors as unverified. For a genuinely new flow, identify the new requirements and baseline the existing hosts and contracts it touches.

For each affected flow, record a short acceptance criterion stating the entry point, eligible role, action and observable outcome. Include material visibility restrictions, alternate paths, recovery and downstream effects. Trace these through the working product and accepted decisions, including screens or states absent from Paper. Keep explicit changes and retirements with their source decisions. For a shared control, trace how each host opens it, uses a supported action, and returns. Cite the host-specific findings when scoping the change and carry them into the handoff. Identify any paths that still need inspection.

If the visual boundary is unclear, ask one question **before** planning or changing the inferred surfaces. Name the actual surfaces and recommend a scope with a reason. For example, “Should I fit this into the existing [host], extend its visual design across [host and flow], or also update [related feature]?” Offer the plausible choices and wait for the answer. When the request, spec or an earlier answer already settles the scope, state it briefly and proceed. An intent answer sets the boundary for the Job's existing approvals.

For a surrounding flow, use the supplied design as the visual foundation and the real host for its content, actions and constraints. Account for materially different entry, active and return states. Extend visual treatment only within the confirmed boundary. For broader consistency, follow the changed action, state or design pattern through its producers and consumers, including separate implementations. Update evidenced mismatches and stop where the next feature's behavior and presentation remain consistent. Record which surfaces were supplied and which compositions the agent inferred.

## Choose the order for inferred surfaces

Follow the user's explicit order. Otherwise, use **Paper first** when materially different layouts or interactions are plausible and costly to reverse. Draw the alternatives in context for review. Use **code first** when the outcome follows predictably from the supplied design and established product patterns, and implementation is requested. Carry the inference and its source design links into the implementation Relay. Supplied designs retain their authority, and open business decisions still need resolution.

## Record code-first drift

Give the implementer the existing inventory location and affected rows. Start with planned code-first. When the [delivery check](check-agreement.md#retained-behavior-at-delivery) confirms the scoped behavior is reachable on the integrated revision, update the row to **Implemented — Paper sync pending**. Record the revision, entry point and exact difference from the source design or stale frame. A broken or unverified path keeps its corresponding finding.

The inventory entry suffices for deferred sync. Use the area's Requirements Inventory file when one exists, otherwise the existing coverage record if it serves as the inventory. If the Paper Manifest is the inventory, use a separate **Paper sync pending** section so its canonical tables continue to describe observed nodes. If there is no established inventory, use the Design Section or a small inventory table in the implementation handover.

On a later requested sync, update Paper from the implemented inferred surface, compare both sides, and clear or resolve the same entry once the recorded difference is reconciled. Implementation can finish while that row is open. Keep visual parity pending for the affected surface until comparison supports it.
