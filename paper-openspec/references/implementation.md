# Approved Implementation

Implement an active OpenSpec change only through this code-only workflow. Enter it when the user explicitly invokes `implement`, or when an approved Sync Plan explicitly includes code implementation and delegates here after its artifact updates validate. Treat either authorization as Paper Approval of the linked composition and permission to modify production code for every incomplete task in the resolved change, subject to normal approval requirements for dependencies, destructive actions, deployment, migrations, or other external side effects.

## Build the task delivery map

Read every task in `tasks.md` and build a working delivery map for each incomplete task containing:

- Owning requirement and scenario
- Visual or non-visual classification
- Paper component or screen evidence when visual
- Production boundaries and applicable repository skills
- Task dependencies and independent tasks
- Focused, affected-package, rendered, and parity evidence required for completion

Keep the map in working context. Do not persist it as a new artifact or place it in Paper. Include every incomplete task, including backend, infrastructure, and other non-visual work. Order work by declared and discovered dependencies while preserving the artifact's intended sequence.

## Audit the UI component system

Before choosing primitives for any visual task, load and follow `ui-system.md`. Reuse the workspace-local audit gathered by an earlier slice only when its configuration, dependencies, and relevant component inventory remain unchanged; otherwise refresh it.

Record the classification and configured component mapping in the working delivery map. For a Configured target, load and follow `shadcn`, prefer existing repository wrappers and installed components, and apply the shared reference's registry, dry-run, diff, overwrite, review, and approval rules. Compose primitives to match Paper semantics; never force shadcn when it weakens required behavior or accessibility. For Compatible but unconfigured or Not applicable targets, follow the shared reference without introducing shadcn implicitly.

## Preflight alignment

Before changing code:

1. Announce the resolved Paper file link, active change, and `implement` slice, including whether authorization came directly or from an approved Sync Plan.
2. Confirm the change is planning-complete, active rather than archived, and valid.
3. Inspect the repository worktree, applicable instructions, architecture, dependencies, production code, tests, commands, existing user changes, and the UI component-system audit.
4. Inspect the linked Paper page and compare OpenSpec and Paper for each mapped task. Require complete component and screen evidence only for visual requirements owned by that task or its dependencies; treat Paper as Not applicable for genuinely non-visual requirements.
5. Mark a task blocked when its owning requirement or dependency chain intersects a Gap, missing required artboard, or unresolved business or design decision. Propagate the blocker only through actual dependents.
6. Report blocked dependency chains, route their OpenSpec/Paper reconciliation through `sync`, and continue every dependency-ready independent task. Parity may diagnose the gap but never reconcile it.

Do not silently choose OpenSpec over Paper or Paper over OpenSpec. Do not treat implementation authorization as approval to change proposal, specification, design intent, or task scope. A delegating Sync Plan may already authorize its exact artifact and task edits; anything outside that plan still requires approval. If a completed task lacks implementation evidence, treat it as a gap and route the exact reopen candidate through `sync` before doing that work.

## Route implementation guidance

For visual tasks, load and follow `paper-desktop:design-to-code` to inspect exact Paper structure, styles, content, and computed layout. Use the canonical component frames and screen artboards from the linked file rather than an active-file selection or screenshot estimate.

Load applicable repository skills for the affected boundaries, such as `$client <slice>` for client architecture and tests. Load `shadcn` when the affected workspace is Configured; do not load it merely because an unrelated workspace uses shadcn. When no matching skill is available, derive the implementation from repository evidence and current primary documentation. Repository conventions and tokens own implementation language; Paper owns approved composition; OpenSpec owns behavior and scope.

Do not add dependencies, abstractions, fixtures, or configuration solely to mimic Paper. Obtain normal approval before adding a dependency or taking an external or destructive action. Preserve unrelated user changes and implement tests at the same behavioral boundary as the production change.

## Execute and verify tasks

For each dependency-ready task:

1. Implement the smallest complete behavior described by the task and its owning requirements.
2. Run focused tests or checks for that behavior.
3. Run relevant type, lint, test, and build checks for affected packages or applications when those commands exist.
4. For visual work, run the UI when feasible and review every required scenario and viewport against Paper. Compare semantics, hierarchy, component reuse, content, tokens, spacing, and interaction outcomes without requiring pixel identity.
5. Re-evaluate the affected parity rows. Mark the task complete only when every required layer passes.

Leave a blocked or failing task unchecked and retain its evidence. Continue with tasks that are independent of the blocker; do not execute dependent tasks or mark intent as completion. If verification reveals work absent from `tasks.md`, propose the exact add-or-reopen edit and wait for approval before expanding task scope.

After task-status edits, preserve OpenSpec checkbox formatting and validate the change. Do not archive the change, commit, deploy, or run destructive migrations unless the user explicitly requests the separate action.

## Finish with full parity

After all currently implementable tasks have been processed, load the parity reference and run one full OpenSpec-to-Paper-to-code batch, including non-visual requirements. Route any code gap back through this implementation workflow only when an approved incomplete task covers it; otherwise route the required add-or-reopen edit through `sync` first.

Consider implementation complete only when every task is verified and the final audit reports Full Parity complete, with no Gap or Pending Evidence across required sources. Otherwise report completed tasks, unchecked or approval-pending tasks, blocking dependency chains, failed checks, pending evidence, and the smallest next explicit action.
