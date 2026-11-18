# Compare

Check a spec, Paper, and the existing code against each other and report where they disagree. Read-only.

## Triggers

- "Does Paper match the spec?", "is the build faithful to the design?"
- "What's left before ENG-142 is done?"
- "Review the checkout screens against the code"
- "Which screens or workflows did the port lose?"

## Needs

A Paper link and identifiable requirements for the comparison. An open or closed Spec can supply them. A redesign comparison can use the named product baseline and target file before a migration Spec exists. Mark any requirement whose evidence is insufficient as unverified.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md) for a spec comparison. For a redesign, [map-redesign-coverage](../steps/map-redesign-coverage.md) using the existing product and the target Paper design. Read available specs and decisions as sources.
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [read-paper-surfaces](../steps/read-paper-surfaces.md)
5. [check-agreement](../steps/check-agreement.md) across the named sources. For a redesign include both requirements and target surfaces. Inspect running UI only when authorized and available without changing code.

## Ends with

A report that leads with two verdicts:

- **Design Alignment**: the requirements and Paper have evidence and every visual row is Aligned or Close. Name the baseline used when a redesign has no migration Spec.
- **Full Agreement**: every required source has evidence and all required behavior and composition agree. Outstanding Paper drift, a regression, an implementation gap or an unverified required path keeps this verdict open. For a delivered port, apply the [baseline-to-integrated comparison](../steps/check-agreement.md#retained-behavior-at-delivery).

Then report gaps by owner, pending evidence and non-blocking drift. Distinguish planned, drawn, implemented and visually verified scope. If the user owns rendered verification, leave the applicable visual verdict pending. A comparison-only request ends with this report.

Done when both verdicts are stated. The report is the only output; nothing it lists is started.
