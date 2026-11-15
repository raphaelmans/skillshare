# Shared Workflow

Use this workflow for every slice.

For `explore`, use the target-resolution, argument, and Paper-connection sections below, then follow [explore.md](explore.md). It bypasses change resolution, artifact validation, coverage matrices, and scope.

For `inventory-tree`, use only the target-resolution section below, then follow [inventory-tree.md](inventory-tree.md). Its standalone route bypasses change resolution, artifact validation, coverage matrices, scope, and resume. A request to explain arrangement conventions alone needs no live target.

## Resolve the Paper target

Resolve one Paper file URL or equivalent linked-file reference in this order:

1. Use the Paper file link in the latest user request.
2. For `init`, ask for the Paper file link and stop; initialization never reuses recent context or the manifest target.
3. Reuse exactly one unambiguous Paper file link from recent chat context.
4. For non-initialization work, use the single target from a valid root `PAPER.md` when repository context resolves one Manifest Root unambiguously.
5. Ask the user for the Paper file link and stop when no link exists.

Ask which link to use when multiple plausible Paper file links remain. Never use the currently open file, recently accessed files, `list_files`, or Paper selection as a target-selection fallback. A bare file ID does not satisfy this contract; ask for the Paper file link.

A Paper file that was renamed but keeps the manifest's file ID is the same target: continue, mention the new name once, and update the recorded name during the next authorized manifest maintenance. An explicit request to point the manifest at a different Paper file is itself the retarget approval; show the retarget plan and apply it without a second stop.

Do not begin artifact inspection or call Paper tools while the target is unresolved. If the supplied link is invalid, inaccessible, or does not identify a Paper file, ask for a corrected Paper file link and stop without modifying Paper or artifacts.

After resolving the target, check the Paper connection before reading artifacts or reporting anything:

1. Load the `paper-mcp-instructions` guide as the first Paper tool call. If the Paper tools are missing or the call fails, stop here. Say that Paper is not connected and how to fix it: open Paper Desktop with the file available, then reconnect the `paper` MCP server (`/mcp` in Claude Code), because the server connects only at startup or on reconnect. Do not run scope, ask for any approval, or produce a long report against a target that could not be opened; a report made before the reconnect has to be repeated after it.
2. Call `open_file` with the supplied URL.
3. Retain the canonical file ID returned by Paper.
4. Pass that canonical file ID explicitly to every later Paper read and write that accepts `fileId`, including page creation, screenshots, exports, and `finish_working_on_nodes`.
5. Announce the resolved Paper file name or link before mutation. Do not expose raw node IDs.

## Resolve the change

Skip change resolution for explicit `init` and `lint` invocations. Paper Initialization is project-level and Paper Lint is Paper-target-level: do not infer a change from recent context, inspect active-change status, or require a planning-complete artifact set. Continue with the selected reference after opening the linked Paper file.

For every change-bound slice, resolve one change in this order:

1. Use an explicit change argument.
2. Use an unambiguous change named in the recent conversation.
3. Use the sole active planning-complete change in the repository.
4. Ask the user when multiple plausible changes remain or no change can be established.

Do not infer a change identifier from a Paper page name. Current-state pages are named for product modules and features and may be affected by many OpenSpec changes.

Interpret a recognized first argument (`inventory-tree`, `init`, `lint`, `explore`, `status`, `help`, `scope`, `components`, `screens`, `sync`, `parity`, `implement`, `design`, or `all`) as a slice. Interpret another first argument as a change identifier only when it matches a change directory under `openspec/changes/`. Read everything else as a plain-language request and route it by intent:

| The request says | Route |
| --- | --- |
| draft, wireframe, sketch, preview, mock up, A/B, compare variants, "no artifacts" | `explore` |
| hi-fi, design it, design the screens, for a resolved change | `design` |
| hi-fi or design with no change, meant to be built | Create the change, then `scope` (see **When no change exists**) |
| apply, build, sync to the codebase, put it into the codebase | `implement` |
| accept, approve, approved, proceed, go ahead, with nothing else | Approval of the gate currently pending in this conversation |
| audit, review, check against the spec | `parity`, or `lint` when the question is about structure |
| status, recap, where are we, what happened | `status` |
| help, how do I use this | `help` |

A bare approval word is never a change identifier or a new slice. Apply it to the pending Scope Approval, Sync Approval, or displayed artifact correction, and continue. When nothing is pending, say so and report the current state instead of guessing.

Words such as "commit", "push", or "run the migration" in the same request are instructions for after the slice completes; carry them out then under the repository's own rules. When the request is ambiguous between two routes that mutate different things, ask one short question naming both. Allow change-bound slices and changes in either supported form, such as `$paper-openspec scope barangay-routes` or `$paper-openspec barangay-routes sync`. Invoke `inventory-tree`, `init`, and `lint` without a change argument.

Select `implement` only when the current invocation names it explicitly, asks in plain words to apply or build the design in the codebase, or an approved Sync Plan explicitly includes code implementation and delegates to it. Treat either authorization as Paper Approval of the linked composition and permission to modify production code for the resolved change after preflight. Never infer it from recent chat, a bare invocation, `design`, `all`, or Sync Audit Approval.

## Verify the artifact set

Skip this section for `init` and `lint`; neither requires or validates an OpenSpec Change.

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

Do not install OpenSpec. Stop and identify what is missing when a named change is not 4/4.

### When no change exists

A design request with no matching change is not a reason to stop and ask.

- When the request reads as a draft, wireframe, preview, or comparison, route to `explore`.
- When the request is for canonical or hi-fi design that is meant to be built, create the change through the repository's own OpenSpec proposal workflow from the conversation, any exploration, and repository evidence. Announce the change name, validate it, run `scope`, and stop once at Scope Approval. The user reviews the new change and its scope in that single stop.
- Ask only when it is unclear which of the two the user wants.

Read `openspec/config.yaml` when present, then read the proposal, every delta spec, design, and tasks completely. Read affected current specs under `openspec/specs/` because delta specs describe changes rather than the entire current behavior.

Treat an explicitly selected archived change as audit-only. Allow read-only `scope`, `sync`, or `parity`; reject Sync Plan mutations, design-producing slices, and `implement`; do not edit archived artifacts; and recommend a new OpenSpec change for newly discovered work.

## Establish split authority

Apply this ownership model when sources disagree:

- OpenSpec artifacts own user-visible behavior, business rules, scenarios, and scope.
- Existing repository components, styles, and design tokens own the established visual language.
- Paper owns the intended component and screen composition being reviewed.

Inspect relevant routes, components, tokens, stylesheets, tests, and existing UI patterns before creating Paper nodes. Do not treat implementation bugs as requirements. If code conflicts with an explicit requirement, preserve the requirement and record implementation work in `tasks.md` after approval.

For `lint`, the Paper structural conventions define expected organization and live Paper is the object under audit. Use a valid Paper Manifest, current specs, and repository language only as non-authoritative evidence when page or surface ownership is ambiguous; do not evaluate requirement coverage or semantic alignment.

For `init`, the same structural conventions determine what may enter the manifest. Inventory observed canonical state only. Do not infer missing requirements, repair Paper, reconstruct history, or issue a semantic alignment verdict.

If no repository visual system exists, reuse a coherent existing Paper token system. If neither source exists, provide Paper's required design brief in chat before creating nodes. Never overwrite conflicting shared Paper tokens without explicit approval.

## Audit the UI component system

For every selected slice that involves a visual component, screen, state, or interaction, read and follow `ui-system.md`. Run its audit once per affected owning workspace and reuse the result until material repository context changes.

Apply the audit to `init`, `scope`, `components`, `screens`, visual rows in `sync` and `parity`, and visual tasks in `implement`. During `init`, use it only for workspaces mapped to observed canonical surfaces and record repository UI-system context without proposing changes. Do not run it for structural `lint` alone. The audit is repository evidence, not a new source of business intent. A Configured shadcn workspace establishes a preferred component vocabulary; a Compatible but unconfigured workspace establishes only an optional opportunity and authorizes no setup or dependency changes.

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
3. Stop on a material gap and reconcile its owning artifact after approval. Validate and rerun scope after any artifact correction, following the ask-once rules below.
4. When no material gap remains, stop and request Scope Approval. A design-producing invocation is not approval of a scope report the user has not yet seen.

Ask for each approval once:

- A `design`, `components`, or `screens` invocation made after a scope report was shown in this conversation, with its inputs unchanged, is Scope Approval for that report.
- When the report displays the exact artifact corrections for its material gaps, one approval covers both the corrections and the scope as corrected. Apply them, validate, and rerun scope silently. Ask again only when the rerun changes the route, the target pages, or the design sequence.
- Never request the same approval twice because a session reconnected, Paper became reachable, or the skill was re-invoked.
5. Reuse one unambiguous recent-chat approval across the requested ordered work while its source inputs remain unchanged outside the approved sequence: the artifact set, Paper target or pre-existing relevant design, requested boundary, and material repository context. Do not invalidate it for Paper changes produced by that approved work.

Treat explicit `scope` as analysis-only and stop after its report even if approval already exists. Never persist approval in Paper or invent an OpenSpec approval marker. Scope Approval authorizes Paper design only; it does not grant Paper Approval for `implement`.

At the end of scope, derive potentially affected existing Component Families, Screen Artboards, states, flows, and required viewports from artifacts and repository evidence. Offer a targeted Sync Audit without performing detailed Paper reads. An explicit `sync` invocation itself grants read-only Sync Audit Approval; otherwise wait for approval before spending Paper calls on the audit. Read and follow the sync reference for the audit and any reconciliation.

Also resolve a Page Ownership Plan in working context:

- Place each module-owned canonical Component Family on `<Module> / Components`.
- Place a Component Family on `Shared / Components` only when ownership and reuse genuinely cross module boundaries.
- Place each Screen Artboard on `<Module> / <Feature>`.
- Treat `Exploration / <Name>` and `Archive / <Name>` as exceptional noncanonical pages that cannot own current production components or screen coverage. An exploration that the change promotes is a source to copy nodes from, not a target page.

Use human product names from artifacts and established repository language. Do not derive page titles from the OpenSpec change identifier. Include every target page in the scope report and approval boundary.

## Connect to Paper

1. Ensure Paper Desktop is running. If the MCP connection fails, ask the user to open Paper Desktop.
2. Follow the already resolved Paper-target sequence: load the guide, call `open_file` with the supplied link, and retain the canonical file ID.
3. For `init`, scan the complete page hierarchy once and inspect canonical current-state component and feature pages to the depth required by the initialization reference. For `lint`, inspect the complete page hierarchy and only the canonical frames needed by the lint reference. For change-bound slices, inspect tokens and the module component and feature pages named by the Page Ownership Plan using that file ID.
4. During scope analysis, limit Paper reads to target validation and immediately relevant current-state page context. Do not audit other potentially affected surfaces or legacy pages without Sync Audit Approval, and never create pages, nodes, annotations, or comments.
5. After valid Scope Approval for a design-producing route, reuse or create each approved current-state page: `<Module> / Components`, `Shared / Components`, or `<Module> / <Feature>` as applicable. Never create an OpenSpec change-slug page.
6. When creating a page, pass the canonical file ID to `create_page`, then call `open_file` with the same file ID and returned page ID before editing. Repeat only for missing approved owner pages.
7. Treat legacy change pages as noncanonical migration evidence. Preserve them unchanged. If an approved current design exists only there, copy only the needed node once into its current-state owner page, reconcile it there, and use the current-state node as canonical thereafter.
8. Before the first write, resolve the product font families and tokens from the repository and the Paper file, name them in the report, and call `get_font_family_info`. Use them from the first node.
9. When drawing is delegated to subagents or a workflow, give each one the canonical file ID, the target pages, the font families and tokens, the canonical component nodes to clone, and the content source. A delegate that lacks them draws in defaults that then need bulk correction.
10. Pass the canonical file ID to every operation that accepts `fileId`, write incrementally, screenshot after meaningful changes, apply targeted corrections, and call `finish_working_on_nodes` with that file ID when done.

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

Explicit change-bound slices constrain the requested outcome, but always satisfy `scope` and required component dependencies for `screens`. `init` and `lint` remain independent and never trigger scope or change resolution. `all` evaluates the same approved scope, design, and parity state and fills gaps; it never includes `init`, `lint`, `implement`, or deletion and recreation of satisfactory artboards.

## Status and help

`status` and `help` are read-only and never mutate Paper, OpenSpec, code, or the manifest.

For `status`, resolve the change and the Paper target without opening Paper unless a specific question needs it. Report in a few lines: the change and whether it is planning-complete and valid; the Paper target; which gate is pending, if any, and what approving it will do; design coverage as far as the manifest and this conversation establish it; tasks verified out of the total; whether work is committed, pushed, and migrated; and the single next command to run. Mark anything not checked as unknown instead of inferring it.

For `help`, print the slices with one line each, which ones need a change, which ones stop for approval, and three example invocations that fit the current repository. Call no Paper tools.

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
