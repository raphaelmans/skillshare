# Semantic Parity

Audit OpenSpec, Paper, and existing implementation code as one read-only batch while respecting their separate authority. Never modify Paper, OpenSpec artifacts or tasks, production code, or task status inside this slice.

## Gather evidence

Read the completed coverage matrix from the shared workflow. Inspect Paper with tree summaries first, then batch `get_jsx` and `get_computed_styles` for the component and screen nodes that need exact comparison. Read tokens directly rather than estimating colors or sizes from screenshots.

Inspect relevant production components, routes, state handling, tests, styles, and design tokens. When a runnable UI is already available or can be started without changing production code, inspect rendered structure and screenshots through available browser tooling. Do not add code, dependencies, fixtures, or configuration solely to make the audit possible.

If required implementation code does not exist, compare artifacts with Paper, mark code evidence as Pending Evidence, and report that Full Parity waits for implementation.

## Compare semantics

Evaluate each requirement scenario across these axes:

- Required states and variations
- Visible content and realistic data shape
- Actions, navigation, and interaction outcomes
- Conditional visibility and empty/error behavior
- Component-family reuse and screen composition
- Responsive hierarchy at required viewports
- Established tokens, typography, spacing, and layout intent
- Non-visual artifact-to-code behavior

Do not require pixel identity.

Classify each row:

- **Aligned**: Behavior, state coverage, composition, and established visual language agree.
- **Close**: Required behavior and state coverage agree; differences are limited to equivalent repository tokens or responsive reflow that preserves hierarchy.
- **Gap**: A required behavior, state, action, visibility rule, navigation path, component relationship, or material visual decision is missing or contradictory.
- **Pending Evidence**: A required source lacks sufficient implementation, rendered, test, artifact, or Paper evidence to evaluate.
- **Not applicable**: The source cannot represent the requirement, such as a non-visual cache rule in Paper.

Never label missing behavior as Close or Not applicable merely because screenshots look similar or implementation has not started.

## Route by owner

Identify the owner and report the handoff without applying a fix:

- Paper omission, artifact ambiguity, or OpenSpec/Paper conflict: route to `sync` for a read audit and approved Sync Plan.
- Code mismatch covered by an incomplete task: route to an authorized `implement` run.
- Code mismatch absent from the task set: report the exact add-or-reopen candidate and route it through `sync`; do not edit `tasks.md` here.
- Non-visual code mismatch: route its task candidate through `sync`; do not represent it in Paper.
- Archived change mismatch: report it and recommend a new OpenSpec change.

Do not enter `sync` automatically. Provide the exact sync invocation or ask for explicit intent to proceed with sync. Once granted, sync may reuse this audit's evidence while its artifact, Paper, boundary, and repository inputs remain unchanged and re-audit only stale rows.

When parity is the final verification stage of an authorized `implement` run, return covered code gaps to the implementation workflow. Route absent tasks through an approved sync plan first. Parity remains read-only in either context.

Never create a separate parity report file, Paper note frame, Paper comment, or task-status change.

## Report

Lead with two verdicts:

- **Design Alignment**: complete only when OpenSpec and Paper have sufficient evidence and every applicable visual row is Aligned or Close.
- **Full Parity**: complete only when every required source has sufficient evidence and every applicable row is Aligned or Close, with no Gap or Pending Evidence.

`Not applicable` does not block either verdict when that source genuinely cannot represent the requirement. Missing required code is Pending Evidence, so Design Alignment may be complete while Full Parity remains pending.

Then list blocking gaps, Pending Evidence, and non-blocking drift with artifact, Paper, and code evidence. Report the exact `sync` or `implement` handoff for each actionable row and make no changes inside this slice.
