---
name: paper-openspec
description: Audit an explicitly linked Paper file for page-hierarchy and canonical-surface structural conventions without requiring an OpenSpec change; classify the artifact-driven UI/UX scope of a planning-complete change; design, sync, and implement approved Paper work; resume partial design; and audit semantic parity with code. Require a Paper file link from the request or unambiguous recent chat context. Use when the user invokes $paper-openspec, asks to lint or audit Paper structure, scope or create Paper UI from a 4/4 OpenSpec change, continue or sync design work, implement an approved Paper design, or compare Paper and code with business requirements.
---

# Paper OpenSpec

Route Paper structure linting and OpenSpec-driven scope, design, implementation, sync, and parity work through modular slices. Treat a bare invocation as a context-aware design resume operation, preserve satisfactory work, and keep specifications off the Paper canvas.

## Start

1. Read [references/workflow.md](references/workflow.md) completely.
2. Resolve one explicit Paper file link from the latest request or unambiguous recent chat context. If none exists, ask for the link and stop.
3. Determine whether the user named a slice, a change, both, or neither.
4. For `lint`, skip change resolution and artifact-completeness checks. For every change-bound slice, resolve and validate one planning-complete OpenSpec Change before modifying Paper or production code.
5. Open the linked Paper file and retain its canonical file ID for every subsequent Paper call that accepts `fileId`.
6. Inspect only the evidence required by the selected slice. For `lint`, inspect the complete live page hierarchy and the canonical frames needed to assess structure. For change-bound slices, inspect the change artifacts, affected current specs, repository UI conventions, implementation state, and authorized Paper surfaces.
7. Select the smallest applicable slice set and read every selected reference completely before acting.
8. When a selected change-bound slice analyzes or changes a visual surface, read [references/ui-system.md](references/ui-system.md) completely and run its shared workspace-local audit before choosing, drawing, comparing, or implementing component primitives. Do not run this audit for structural `lint` alone.
9. Before any design-producing request, run `scope`, report the artifact-driven analysis, and obtain valid Scope Approval before modifying Paper. Treat an explicit `scope` invocation as analysis-only.
10. Build or refresh the appropriate coverage or impact matrix in working context only. Never draw or persist that matrix on the Paper canvas or create a new artifact for it.
11. Preserve existing Paper and implementation work that already satisfies the artifacts. Apply targeted changes instead of recreating it.
12. Modify production code only through `implement`, authorized either by an explicit `implement` invocation or by an approved `sync` plan that explicitly includes code implementation. Never infer implementation authorization from a bare invocation, `design`, `parity`, `all`, or a read-only sync audit.

## Route Slices

| Slice | Load when the task involves | Reference |
| --- | --- | --- |
| `lint` | Auditing the linked Paper file's page hierarchy, surface placement, colocation, exceptional pages, or canonical reuse without changing it | [references/lint.md](references/lint.md) |
| `scope` | Classifying a change as a screen/component change, user flow, user journey, or product overhaul before Paper design | [references/scope.md](references/scope.md) |
| `components` | Component families, variants, states, or the component inventory is incomplete | [references/components.md](references/components.md) |
| `screens` | Routes, views, scenarios, responsive targets, or screen composition | [references/screens.md](references/screens.md) |
| `sync` | Reading drift between OpenSpec and Paper, inferring its direction, proposing reconciliation, and applying an approved plan | [references/sync.md](references/sync.md) |
| `parity` | Reviewing artifacts, Paper, and existing code for semantic or compositional agreement | [references/parity.md](references/parity.md) |
| `implement` | Delivering an approved Paper design and every incomplete OpenSpec task in production code | [references/implementation.md](references/implementation.md) |

Treat `design` as `scope` + `components` + `screens`. Treat `all` as `scope` + `components` + `screens` + `parity`.

Treat `lint` as a standalone Paper-target operation. Do not infer or require an OpenSpec Change, verify a 4/4 artifact set, run `scope`, request approval, or mutate Paper, OpenSpec, production code, tasks, or the Paper Manifest. Keep `lint` outside `design`, `all`, and bare resume. Inspect live Paper structure even when a valid manifest exists; use manifest and repository evidence only to disambiguate names or ownership.

Treat an explicit `implement` invocation as Paper Approval of the linked composition and authorization to modify production code for the resolved active change. A `sync` run may delegate to `implement` only after its displayed plan explicitly asks for and receives code authorization. Run the implementation alignment preflight before writing code in either case. Keep `implement` outside `all`, and never select it during bare resume.

When invoked as `$paper-openspec <change>`, resume that change. When invoked as `$paper-openspec` without arguments, infer the change and resume from the first incomplete or stale slice. Do not merely show a menu when one change is unambiguous.

Require a Paper file link in either form. The link may appear anywhere in the user's message:

```text
$paper-openspec lint <paper-file-url>
$paper-openspec <paper-file-url> barangay-routes
$paper-openspec scope barangay-routes <paper-file-url>
$paper-openspec screens barangay-routes <paper-file-url>
$paper-openspec sync barangay-routes <paper-file-url>
$paper-openspec implement barangay-routes <paper-file-url>
```

A bare invocation may reuse exactly one unambiguous Paper file link from recent chat history. It may never infer the target from whichever Paper file is currently open.

Run `scope` automatically before `components`, `screens`, `design`, `all`, or bare design resume when no valid recent Scope Approval exists. Stop after reporting the route, matrix, gaps, and sequence; continue the requested design work only after approval. Reuse one approval across ordered batches until a source input changes outside that approved sequence: the artifacts, Paper target or pre-existing relevant design, requested boundary, or material repository context. Paper changes produced by the approved sequence do not invalidate it.

After `scope`, identify potentially affected existing design surfaces from OpenSpec and repository evidence and offer a targeted Sync Audit. Do not spend Paper calls auditing those surfaces unless the user approves the audit or explicitly invokes `sync`. Treat `sync` as standalone: it runs its own scope preflight, infers direction per drift item rather than from a command argument, and stops on unresolved ownership.

When a higher scope introduces lower-level dependencies, design downward: create shared and required component frames with their states first, compose the screens that consume them, then validate flow, journey, or product continuity. When `all` is requested, inspect before writing and skip work already in parity.

## Preserve These Invariants

- Treat Paper as the latest approved design state. Put module-owned canonical Component Frames on `<Module> / Components`, genuinely cross-module families on `Shared / Components`, and Screen Artboards on `<Module> / <Feature>`.
- Keep `lint` file-wide and strictly read-only. Report evidence-backed structural findings without converting them into parity gaps, inferred requirements, manifest edits, or automatic cleanup.
- Require an explicit Paper file link. Never choose a target through the active file, recent-file order, or `list_files`.
- Open the linked file before inspecting it and pass its canonical file ID to every subsequent Paper read or write that accepts `fileId`.
- Never create specification frames, acceptance-criteria tables, coverage matrices, annotations, or comments in Paper. Do not use Paper comment threads as a specification channel.
- Let OpenSpec determine intended Design Scope. Use Paper and code as evidence of current state, reuse opportunities, and downstream effects; never let accidental implementation complexity reduce an explicit requirement.
- Start at screen/component scope and escalate only as required through user flow, user journey, and product overhaul. Use the highest necessary route while retaining every lower level as a design dependency.
- Require Scope Approval before Paper design and keep it distinct from Paper Approval for production implementation. Never persist either approval as a Paper annotation or invented artifact marker.
- Keep Sync Audit Approval read-only. Require a displayed Sync Plan and explicit Sync Approval before changing Paper or OpenSpec; require the same approval request to name code implementation before delegating to `implement`.
- Infer sync direction independently for each drift item from artifact ownership and Paper evidence. Never require `to-paper` or `from-paper`, assume one direction for the whole run, or silently convert Paper-only behavior into a business requirement.
- Never create or append to a page named after an OpenSpec change merely to preserve history. OpenSpec and repository history own change history; legacy change pages are noncanonical evidence and remain untouched unless an approved migration copies needed nodes into their current-state owner pages.
- Give each changed product-component family one component frame containing its artifact-required states and variations.
- Compose screens from canonical component nodes by cloning or duplicating them. Do not redraw changed components independently inside screens.
- Create screen artboards per materially distinct scenario and required viewport. Do not generate speculative breakpoints or states.
- Let OpenSpec own business behavior, existing code and design tokens own the established visual language, and Paper own the intended composition under review.
- Before analyzing, designing, reconciling, reviewing, or implementing visual surfaces, audit each affected workspace for shadcn configuration or compatibility. When configured, prefer its installed components, repository wrappers, and composition patterns; compatibility alone never authorizes initialization or registry changes.
- Keep visual and non-visual requirements in the same coverage pass, but represent only visual requirements in Paper.
- Require approval before changing proposal, spec, or design intent. Record approved implementation gaps in existing OpenSpec tasks; never create a separate parity artifact.
- Add or reopen implementation tasks only after approval. Change a task checkbox to complete only after its implementation passes the required verification.
- Keep `parity` read-only across OpenSpec, Paper, tasks, and production code. Route OpenSpec/Paper reconciliation through `sync` and code delivery through `implement`; never mutate a source inside `parity`.
- Treat archived OpenSpec changes as read-only audit history.
- Load the Paper MCP guide before other Paper operations, review screenshots after meaningful changes, and always finish working on edited nodes.

## Review Discipline

For lint work:

1. Report the resolved Paper file link and `lint` slice; do not resolve an OpenSpec Change.
2. Audit the complete page hierarchy and inspect canonical frames only to the depth needed to evaluate placement, colocation, exceptional-page classification, and reuse.
3. Report each Lint Finding with its Paper location, violated convention, evidence, and recommended canonical owner or corrective action; separate unresolved structural evidence as Pending Evidence.
4. Make no changes and do not issue Design Alignment or Full Parity verdicts.

For scope work:

1. Report the resolved Paper file link, active change, selected Design Scope, and evidence before any Paper mutation.
2. Include the affected workspace's component-system classification and relevant reuse opportunities in current-state evidence.
3. Show the appropriate chat-only coverage or impact matrix, material gaps, optional enhancements, and recommended user-flow or batch sequence.
4. Block design only on unresolved behavior, navigation, permissions, data, required states, flow, or composition decisions.
5. Stop after explicit `scope`; for automatic preflight, wait for Scope Approval and reuse it only while its inputs remain unchanged.

For design and resume work:

1. Report the resolved Paper file link, inferred change, and selected slice before modifying Paper.
2. State the evidence used for component families, states, scenarios, viewports, and configured component-system mappings.
3. Review spacing, typography, contrast, alignment, artboard fit, and component reuse after every meaningful section.
4. Reconcile only source-of-truth gaps; do not polish beyond the artifacts and established visual language without user direction.

For parity work:

1. Report findings by requirement or scenario with artifact, Paper, and code evidence.
2. Separate blocking semantic gaps from non-blocking visual or component-system drift.
3. Report Design Alignment separately from Full Parity and keep Full Parity pending while any required source evidence is missing.
4. Route Paper/OpenSpec drift to an explicitly requested `sync` handoff and code drift to `implement`; never apply a fix inside `parity`.

For sync work:

1. Report the artifact-derived affected design surfaces before detailed Paper inspection.
2. Audit only those surfaces, use the owning workspace's component system as visual-language evidence, classify every drift item as OpenSpec-to-Paper, Paper-to-OpenSpec candidate, unresolved, or aligned, and show the evidence.
3. Present one mutation plan that names Paper edits, artifact edits, task changes, and whether code implementation is included; wait for explicit approval.
4. Apply approved Paper changes through `components` and `screens`, approved artifact changes through the owning files, and approved code work only by delegating to `implement`.

For implementation work:

1. Report the resolved Paper file link, active change, and incomplete-task inventory before modifying code.
2. Audit the affected UI workspace for shadcn configuration and compatibility before choosing component primitives.
3. Map alignment gaps to their owning requirements, tasks, and dependency chains; block only intersecting work and continue independent tasks.
4. Verify each task at focused, affected-package, and rendered-viewport boundaries as applicable before checking it off.
5. Continue verifiable independent tasks around a blocker, then finish with a full parity batch and report all remaining gaps.
