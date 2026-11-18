# Compare

Check a spec, Paper, and the existing code against each other and report where they disagree. Read-only.

## Triggers

- "Does Paper match the spec?", "is the build faithful to the design?"
- "What's left before ENG-142 is done?"
- "Review the checkout screens against the code"

## Needs

A Ready Spec and a Paper link.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md)
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [read-paper-surfaces](../steps/read-paper-surfaces.md)
5. [check-agreement](../steps/check-agreement.md) with one row per user story or scenario, across spec, Paper, and code. Inspect running UI only when it is already available or starts without changing code.

## Ends with

A report that leads with two verdicts:

- **Design Alignment**: spec and Paper have evidence and every visual row is Aligned or Close.
- **Full Agreement**: every required source has evidence and no Gap or Pending Evidence remains. Missing code is Pending Evidence, so Design Alignment can hold while Full Agreement waits.

Then Gaps by owner as check-agreement named them, Pending Evidence, and non-blocking drift, each with its evidence.

Done when both verdicts are stated. The report is the only output; nothing it lists is started.
