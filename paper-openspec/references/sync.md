# Design Synchronization

Read Design Drift between a planning-complete OpenSpec change and its Paper target, infer direction per Drift Item, and apply only an approved Sync Plan. Do not require the user to select a direction.

## Authorize the audit

Treat an explicit `sync` invocation or an explicit request to proceed with sync from a parity report as authorization for a targeted read-only Sync Audit. When scope merely predicts affected existing designs, report those surfaces and wait for Sync Audit Approval before making detailed Paper calls. The audit never authorizes mutations.

When parity has already gathered the required evidence, reuse it if the Artifact Set, Paper Target and relevant nodes, requested boundary, and material repository context have not changed. Re-audit only stale or missing rows. Parity never starts sync automatically; require the explicit handoff first.

Run scope as a preflight and derive the candidate affected surfaces from OpenSpec and repository evidence before inspecting Paper:

- Component Families and required states or variations
- Screen Artboards and scenarios
- User Flows or User Journeys whose continuity may change
- Required viewports and shared design foundations

Inspect only the relevant current and historical Paper nodes. Use tree summaries first, then batch exact structure and computed-style reads when necessary. Keep historical OpenSpec changes read-only.

## Infer direction per Drift Item

Do not choose one direction for the whole run. Classify every independently reconcilable Drift Item:

- **OpenSpec to Paper**: an explicit artifact requirement, scenario, rule, or design decision is missing, stale, or contradictory in Paper.
- **Paper to OpenSpec candidate**: Paper contains a material intentional composition or behavior that the active artifacts do not express. Treat it as a proposal, not a requirement, until approved.
- **Unresolved**: both sources are explicit but conflict, provenance is unclear, or a decision would change business behavior without sufficient artifact evidence. Ask the user; do not guess.
- **Aligned**: the sources are semantically equivalent. Skip mutation.

Use code and repository history only as supporting provenance and current-state evidence. They do not override explicit OpenSpec behavior or turn accidental implementation into intent. A run may contain both inferred directions.

Map Paper-to-OpenSpec candidates to the owning artifact:

- Product intent or scope: `proposal.md`
- Requirement, rule, or scenario: the applicable delta spec
- Visual or technical decision: `design.md`
- Missing delivery work: `tasks.md`

Never pull Paper-only business behavior into OpenSpec silently.

## Present the Sync Plan

Report each Drift Item with:

- Artifact, Paper, and relevant repository evidence
- Owning concern and inferred direction
- Exact Paper nodes or OpenSpec files affected
- Proposed mutation and dependency order
- Whether tasks change
- Whether production code would change
- Status: aligned, proposed, unresolved, or blocked

Stop on unresolved ownership. Before any mutation, present one bounded Sync Plan and ask for explicit Sync Approval. Name each authorization boundary in the request: Paper changes, OpenSpec artifact or task changes, and code implementation. One response may grant them together only when the request stated them separately and precisely.

Sync Audit Approval alone never grants Sync Approval, Scope Approval, Paper Approval, or code authorization. A Sync Approval that includes Paper mutations may also grant Scope Approval for exactly the displayed component and screen batches. It grants Paper Approval and code authorization only when the approval request explicitly includes implementation.

## Apply the approved plan

For **OpenSpec-to-Paper** items:

1. Preserve historical change pages unchanged.
2. Reuse existing current-change nodes when they remain valid.
3. When an affected canonical design exists only on a previous change page, clone the affected Component Families and Screen Artboards onto the active change page.
4. Load `components` before `screens`, update only approved drift, and review the affected scenarios and viewports.

For **Paper-to-OpenSpec** items:

1. Apply only the approved proposal, delta-spec, design, and task edits.
2. Preserve OpenSpec structure and validate the change.
3. Rerun scope for affected rows when intent or requirements changed.
4. If the approved Sync Plan explicitly included code implementation, delegate to the code-only `implement` workflow. Do not duplicate implementation logic inside sync.
5. If code was not approved, stop after artifact validation and report the exact remaining `implement` action.

After all approved mutations, rerun the affected audit rows. When code was implemented, finish with the implementation workflow's full parity batch. Report aligned rows, applied changes, deferred candidates, unresolved decisions, and remaining unchecked tasks. Never persist the Sync Plan or audit matrix in Paper or create a separate OpenSpec analysis artifact.
