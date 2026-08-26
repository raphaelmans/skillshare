# Shared Workflow

Use this workflow for every slice.

## Resolve the Paper target

Require one explicit Paper file URL or equivalent linked-file reference. Resolve it in this order:

1. Use the Paper file link in the latest user request.
2. Reuse exactly one unambiguous Paper file link from recent chat context.
3. Ask the user for the Paper file link and stop when no link exists.

Ask which link to use when multiple plausible Paper file links remain. Never use the currently open file, recently accessed files, `list_files`, or Paper selection as a target-selection fallback. A bare file ID does not satisfy this contract; ask for the Paper file link.

Do not begin artifact inspection or call Paper tools while the target is unresolved. If the supplied link is invalid, inaccessible, or does not identify a Paper file, ask for a corrected Paper file link and stop without modifying Paper or artifacts.

After resolving the target:

1. Load the `paper-mcp-instructions` guide as the first Paper tool call.
2. Call `open_file` with the supplied URL.
3. Retain the canonical file ID returned by Paper.
4. Pass that canonical file ID explicitly to every later Paper read and write that accepts `fileId`, including page creation, screenshots, exports, and `finish_working_on_nodes`.
5. Announce the resolved Paper file name or link before mutation. Do not expose raw node IDs.

## Resolve the change

Resolve one change in this order:

1. Use an explicit change argument.
2. Use an unambiguous change named in the recent conversation.
3. Use the sole active planning-complete change in the repository.
4. Ask the user when multiple plausible changes remain or no change can be established.

Do not infer a change identifier from a Paper page name. Current-state pages are named for product modules and features and may be affected by many OpenSpec changes.

Interpret a recognized first argument (`scope`, `components`, `screens`, `sync`, `parity`, `implement`, `design`, or `all`) as a slice. Interpret any other first argument as a change identifier. Allow the slice and change in either supported form, such as `$paper-openspec scope barangay-routes` or `$paper-openspec barangay-routes sync`.

Select `implement` only when the current invocation names it explicitly or an approved Sync Plan explicitly includes code implementation and delegates to it. Treat either authorization as Paper Approval of the linked composition and permission to modify production code for the resolved change after preflight. Never infer it from recent chat, a bare invocation, `design`, `all`, or Sync Audit Approval.

## Verify the artifact set

Locate the repository root and `openspec/` directory. Prefer the installed OpenSpec CLI when available:

```bash
openspec status --change "<change>" --json
openspec validate "<change>"
```

Require `isPlanningComplete: true`, or the compatible `isComplete: true`, for the default `spec-driven` schema. If the CLI is unavailable, verify the active change folder contains:

- `proposal.md`
- one or more `specs/**/spec.md` delta specs
- `design.md`
- `tasks.md`

Do not install OpenSpec or create missing artifacts. Stop and identify what is missing when the change is not 4/4.

Read `openspec/config.yaml` when present, then read the proposal, every delta spec, design, and tasks completely. Read affected current specs under `openspec/specs/` because delta specs describe changes rather than the entire current behavior.

Treat an explicitly selected archived change as audit-only. Allow read-only `scope`, `sync`, or `parity`; reject Sync Plan mutations, design-producing slices, and `implement`; do not edit archived artifacts; and recommend a new OpenSpec change for newly discovered work.

## Establish split authority

Apply this ownership model when sources disagree:

- OpenSpec artifacts own user-visible behavior, business rules, scenarios, and scope.
- Existing repository components, styles, and design tokens own the established visual language.
- Paper owns the intended component and screen composition being reviewed.

Inspect relevant routes, components, tokens, stylesheets, tests, and existing UI patterns before creating Paper nodes. Do not treat implementation bugs as requirements. If code conflicts with an explicit requirement, preserve the requirement and record implementation work in `tasks.md` after approval.

If no repository visual system exists, reuse a coherent existing Paper token system. If neither source exists, provide Paper's required design brief in chat before creating nodes. Never overwrite conflicting shared Paper tokens without explicit approval.

## Audit the UI component system

For every selected slice that involves a visual component, screen, state, or interaction, read and follow `ui-system.md`. Run its audit once per affected owning workspace and reuse the result until material repository context changes.

Apply the audit to `scope`, `components`, `screens`, visual rows in `sync` and `parity`, and visual tasks in `implement`. The audit is repository evidence, not a new source of business intent. A Configured shadcn workspace establishes a preferred component vocabulary; a Compatible but unconfigured workspace establishes only an optional opportunity and authorizes no setup or dependency changes.

## Build the coverage matrix

For `scope`, build the route-appropriate Impact Matrix or Experience Coverage Matrix from the scope reference. For parity without a prior scope pass, maintain a working matrix with one row per requirement scenario and these fields:

- Requirement and scenario
- Visual or non-visual classification
- Affected component family and states
- Affected screen and viewport
- Paper evidence
- Code or test evidence, when implementation exists
- Status: missing, partial, aligned, close, gap, pending, or not applicable

Keep every matrix in working context and show the scope matrix in chat before design. Never add one to Paper, persist one in an OpenSpec artifact, or create a new parity or analysis artifact.

Classify as visual when the requirement changes visible content, state, interaction, navigation, visibility, hierarchy, or responsive composition. Classify infrastructure, caching, persistence, metadata, background processing, and similar behavior as non-visual unless it produces a user-visible state.

## Gate Paper design with scope

Treat `components`, `screens`, `design`, `all`, and bare design resume as design-producing routes. Before any Paper mutation on those routes:

1. Load the scope reference and classify the change from the artifacts, using Paper and repository evidence for current context.
2. Report the selected Design Scope, escalation evidence, matrix, material gaps, optional enhancements, and ordered User Flows or Design Batches.
3. Stop on a material gap and reconcile its owning artifact after approval. Validate, rerun scope, and require fresh approval after any artifact correction.
4. When no material gap remains, stop and request Scope Approval. Do not interpret the design-producing invocation itself as approval.
5. Reuse one unambiguous recent-chat approval across the requested ordered work while its source inputs remain unchanged outside the approved sequence: the artifact set, Paper target or pre-existing relevant design, requested boundary, and material repository context. Do not invalidate it for Paper changes produced by that approved work.

Treat explicit `scope` as analysis-only and stop after its report even if approval already exists. Never persist approval in Paper or invent an OpenSpec approval marker. Scope Approval authorizes Paper design only; it does not grant Paper Approval for `implement`.

At the end of scope, derive potentially affected existing Component Families, Screen Artboards, states, flows, and required viewports from artifacts and repository evidence. Offer a targeted Sync Audit without performing detailed Paper reads. An explicit `sync` invocation itself grants read-only Sync Audit Approval; otherwise wait for approval before spending Paper calls on the audit. Read and follow the sync reference for the audit and any reconciliation.

Also resolve a Page Ownership Plan in working context:

- Place each module-owned canonical Component Family on `<Module> / Components`.
- Place a Component Family on `Shared / Components` only when ownership and reuse genuinely cross module boundaries.
- Place each Screen Artboard on `<Module> / <Feature>`.
- Treat `Exploration / <Name>` and `Archive / <Name>` as exceptional noncanonical pages that cannot own current production components or screen coverage.

Use human product names from artifacts and established repository language. Do not derive page titles from the OpenSpec change identifier. Include every target page in the scope report and approval boundary.

## Connect to Paper

1. Ensure Paper Desktop is running. If the MCP connection fails, ask the user to open Paper Desktop.
2. Follow the already resolved Paper-target sequence: load the guide, call `open_file` with the supplied link, and retain the canonical file ID.
3. Inspect tokens and the module component and feature pages named by the Page Ownership Plan using that file ID.
4. During scope analysis, limit Paper reads to target validation and immediately relevant current-state page context. Do not audit other potentially affected surfaces or legacy pages without Sync Audit Approval, and never create pages, nodes, annotations, or comments.
5. After valid Scope Approval for a design-producing route, reuse or create each approved current-state page: `<Module> / Components`, `Shared / Components`, or `<Module> / <Feature>` as applicable. Never create an OpenSpec change-slug page.
6. When creating a page, pass the canonical file ID to `create_page`, then call `open_file` with the same file ID and returned page ID before editing. Repeat only for missing approved owner pages.
7. Treat legacy change pages as noncanonical migration evidence. Preserve them unchanged. If an approved current design exists only there, copy only the needed node once into its current-state owner page, reconcile it there, and use the current-state node as canonical thereafter.
8. Call `get_font_family_info` before the first typographic write in the session.
9. Pass the canonical file ID to every operation that accepts `fileId`, write incrementally, screenshot after meaningful changes, apply targeted corrections, and call `finish_working_on_nodes` with that file ID when done.

Do not create a new Paper file automatically. Do not switch to another file because it is open or recent. Do not use comment threads to store requirements, review notes, or discrepancies.

## Resume

Treat bare invocation as `resume`, not as a destructive rerun:

1. Run scope analysis and stop for Scope Approval when no valid recent approval exists or its inputs changed.
2. Follow the approved User Flow or Design Batch order and compare required component families and states with canonical frames on their module or shared component pages.
3. Complete the first missing or partial dependency-ready component family.
4. Compare required scenario/viewport combinations with existing screen artboards on their module feature pages.
5. Complete the first missing or partial screen using canonical component nodes, then validate continuity at the approved scope.
6. When component and screen coverage is complete, run parity read-only when requested or included by the selected slice.
7. When Design Alignment is complete but required code evidence is missing, report Full Parity pending and provide the exact explicit `implement` invocation needed to authorize code changes.
8. Report Full Parity complete only when every required source has evidence and no Gap or Pending Evidence remains.

Explicit slices constrain the requested outcome, but always satisfy `scope` and required component dependencies for `screens`. `all` evaluates the same approved scope, design, and parity state and fills gaps; it never includes `implement` or deletes and recreates satisfactory artboards.

## Handoff from parity

Keep `parity` read-only. When it finds OpenSpec/Paper drift, report the exact `sync` action and wait for the user to invoke `sync` or explicitly say to proceed with sync. Never enter reconciliation automatically.

When the handoff is explicit, reuse parity evidence if the Artifact Set, Paper Target and relevant nodes, requested boundary, and material repository context have not changed. Re-audit only stale or missing rows. The handoff authorizes the read-only Sync Audit, not the resulting Sync Plan or any mutation.

## Reconcile artifacts

Use this section only from an approved `sync` or design-producing workflow, never from `parity`. When a gap originates in the artifacts, show a concise mapping of proposed edits and obtain approval before writing:

- Intent or scope change: update `proposal.md`.
- Requirement or scenario change: update the appropriate delta spec.
- Visual or technical decision: update `design.md`.
- Missing implementation work: add or reopen a task in `tasks.md` after approval.

Changing an existing task checkbox from incomplete to complete is implementation status, not a scope change; allow it only after the task's focused checks, affected-package checks, rendered review when visual, and affected parity rows pass. Preserve the OpenSpec format and rerun validation after approved edits or task-status updates. Invalidate Scope Approval when an approved artifact edit changes its inputs. Do not create `parity.md`, scope-analysis artifacts, design-note artifacts, or Paper annotations.
