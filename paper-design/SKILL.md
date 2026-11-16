---
name: paper-design
description: Inventory a Paper page tree and its canonical surfaces; initialize or refresh a repository's Paper Manifest; audit Paper structure; explore drafts, wireframes, content previews, and A/B variants in Paper without a planned change; scope, design, sync, implement, resume, and review Paper UI driven by a change's planning artifacts in whatever format the repository uses. Use when the user invokes $paper-design (formerly $paper-openspec), including inventory-tree, init, lint, and explore, asks to draft or preview UI in a Paper file, or asks about its Paper page arrangement conventions.
---

# Paper Design

Route Paper Manifest initialization, Paper structure linting, change-free exploration, and change-driven scope, design, implementation, sync, and parity work through modular slices. Treat a bare invocation as a context-aware design resume operation, preserve satisfactory work, and keep specifications off the Paper canvas.

This skill is agnostic to planning format. A Change's intent lives in its Change Source: whatever artifacts the repository or user uses to plan work. Identify that content by role (intent, requirements, decisions, tasks), never by file name or tool, and follow the repository's Planning Convention for where it lives, how it is written, and how it is validated.

## Start

For an explicit `inventory-tree` invocation, read [references/inventory-tree.md](references/inventory-tree.md) completely and follow its standalone route. It owns the shared page arrangement and inventory rules. Skip the change-bound startup below: this slice needs no repository, Change, scope approval, or manifest write. For a conventions-only question, explain its page arrangement without opening a live Paper file.

For `explore`, or a request to draft, wireframe, preview, or compare variants in Paper without planning artifacts, read [references/explore.md](references/explore.md) completely and follow it. It needs a Paper target but no Change, readiness check, or Scope Approval.

1. Read [references/workflow.md](references/workflow.md) completely. Route the invocation by what the user asked for, using its argument rules; plain-language arguments are requests, not change identifiers.
2. Resolve the Paper file link through the shared workflow. `init` always requires the link in the current request; never reuse a recent link or manifest target for initialization.
3. Determine whether the user named a slice, a change, both, or neither.
4. For `init` and `lint`, skip change resolution and readiness checks. For every change-bound slice, establish the Planning Convention, resolve one Change, and confirm its Change Source is Planning-Ready before modifying Paper or production code.
5. Check the Paper connection before any other work, then open the linked Paper file and retain its canonical file ID for every subsequent Paper call that accepts `fileId`.
6. Inspect only the evidence required by the selected slice. For `init`, inspect the structural inventory and repository mappings defined by its reference. For `lint`, inspect the complete live page hierarchy and the canonical frames needed to assess structure. For change-bound slices, inspect the Change Source, affected Current Behavior Docs, repository UI conventions, implementation state, and authorized Paper surfaces.
7. Select the smallest applicable slice set and read every selected reference completely before acting.
8. When `init` maps observed surfaces to repository workspaces, or a selected change-bound slice analyzes or changes a visual surface, read [references/ui-system.md](references/ui-system.md) completely and run its shared workspace-local audit. Do not run this audit for structural `lint` alone.
9. Before any design-producing request, run `scope`, report the source-driven analysis, and obtain valid Scope Approval before modifying Paper. Treat an explicit `scope` invocation as analysis-only.
10. Build or refresh the appropriate coverage or impact matrix in working context only. Never draw or persist that matrix on the Paper canvas or create a new artifact for it.
11. Preserve existing Paper and implementation work that already satisfies the Change Source. Apply targeted changes instead of recreating it.
12. Modify production code only through `implement`, authorized either by an explicit `implement` invocation or by an approved `sync` plan that explicitly includes code implementation. Never infer implementation authorization from a bare invocation, `design`, `parity`, `all`, or a read-only sync audit.

## Route Slices

| Slice | Load when the task involves | Reference |
| --- | --- | --- |
| `inventory-tree` | Describing page arrangement or reporting the observed live page tree and canonical surfaces without writing a manifest | [references/inventory-tree.md](references/inventory-tree.md) |
| `init` | Creating or refreshing root `PAPER.md` from an explicit Paper target without resolving a change | [references/initialization.md](references/initialization.md) |
| `lint` | Auditing the linked Paper file's page hierarchy, surface placement, colocation, exceptional pages, or canonical reuse without changing it | [references/lint.md](references/lint.md) |
| `explore` | Drafts, wireframes, content or copy previews, A/B variants, hi-fi concepts, or journey walkthroughs drawn from a brief with no planned Change | [references/explore.md](references/explore.md) |
| `status` | Reporting where a change stands: pending gate, design coverage, tasks, commit state, and the next command, without mutating anything | [references/workflow.md](references/workflow.md) |
| `help` | Listing the slices, their gates, and example invocations without calling Paper | [references/workflow.md](references/workflow.md) |
| `scope` | Classifying a change as a screen/component change, user flow, user journey, or product overhaul before Paper design | [references/scope.md](references/scope.md) |
| `components` | Component families, variants, states, or the component inventory is incomplete | [references/components.md](references/components.md) |
| `screens` | Routes, views, scenarios, responsive targets, or screen composition | [references/screens.md](references/screens.md) |
| `sync` | Reading drift between the Change Source and Paper, inferring its direction, proposing reconciliation, and applying an approved plan | [references/sync.md](references/sync.md) |
| `parity` | Reviewing the Change Source, Paper, and existing code for semantic or compositional agreement | [references/parity.md](references/parity.md) |
| `implement` | Delivering an approved Paper design and every incomplete task of the Change in production code | [references/implementation.md](references/implementation.md) |

Treat `design` as `scope` + `components` + `screens`. Treat `all` as `scope` + `components` + `screens` + `parity`.

Treat `inventory-tree` as a standalone, read-only Paper-target operation with a chat report. Keep it outside `design`, `all`, and bare resume. `init` reuses its inventory procedure to write the manifest; `lint` reuses its arrangement rules to assess compliance.

Treat `explore` as a standalone Paper-target operation that draws from an Exploration Brief. It requires no Change or Scope Approval, draws on its own `Exploration / <Name>` page by default, stays inside the established design system, and never authorizes production code. Keep it outside `design`, `all`, and bare resume. When the user asks to build an exploration, promote it through its reference.

Treat `init` as a standalone project-level operation. Require one resolvable Manifest Root and an explicit Paper link, but do not infer or require a Change, check planning readiness, or run `scope`. Read Paper, planning artifacts, and repository code; mutate only root `PAPER.md`. Keep `init` outside `design`, `all`, and bare resume.

Treat `lint` as a standalone Paper-target operation. Do not infer or require a Change, check planning readiness, run `scope`, request approval, or mutate Paper, planning artifacts, production code, tasks, or the Paper Manifest. Keep `lint` outside `init`, `design`, `all`, and bare resume. Inspect live Paper structure even when a valid manifest exists; use manifest and repository evidence only to disambiguate names or ownership.

Treat an explicit `implement` invocation, or an invocation that asks in plain words to apply, build, or put the design into the codebase, as Paper Approval of the linked composition and authorization to modify production code for the resolved active change. A `sync` run may delegate to `implement` only after its displayed plan explicitly asks for and receives code authorization. Run the implementation alignment preflight before writing code in either case. Keep `implement` outside `all`, and never select it during bare resume.

When invoked as `$paper-design <change>`, resume that change. When invoked as `$paper-design` without arguments, infer the change and resume from the first incomplete or stale slice. Do not merely show a menu when one change is unambiguous.

A change argument is whatever identifies a Change under the repository's Planning Convention: a document path, a folder name, an issue key, a tracker link, or a title.

Require a Paper file link in either form. The link may appear anywhere in the user's message:

```text
$paper-design inventory-tree <paper-file-url>
$paper-design init <paper-file-url>
$paper-design lint <paper-file-url>
$paper-design explore <paper-file-url> draft the stage control
$paper-design <paper-file-url> barangay-routes
$paper-design scope barangay-routes <paper-file-url>
$paper-design screens docs/plans/barangay-routes.md <paper-file-url>
$paper-design sync ENG-142 <paper-file-url>
$paper-design implement barangay-routes <paper-file-url>
```

A bare invocation may reuse exactly one unambiguous Paper file link from recent chat history. It may never infer the target from whichever Paper file is currently open.

Run `scope` automatically before `components`, `screens`, `design`, `all`, or bare design resume when no valid recent Scope Approval exists. Stop after reporting the route, matrix, gaps, and sequence; continue the requested design work only after approval. Ask for each approval once: a `design`, `components`, or `screens` invocation made after a scope report shown in this conversation is Scope Approval for that report, and approval of displayed gap corrections also approves the scope as corrected. Reuse one approval across ordered batches until a source input changes outside that approved sequence: the Change Source, Paper target or pre-existing relevant design, requested boundary, or material repository context. Paper changes produced by the approved sequence do not invalidate it.

After `scope`, identify potentially affected existing design surfaces from Change Source and repository evidence and offer a targeted Sync Audit. Do not spend Paper calls auditing those surfaces unless the user approves the audit or explicitly invokes `sync`. Treat `sync` as standalone: it runs its own scope preflight, infers direction per drift item rather than from a command argument, and stops on unresolved ownership.

When a higher scope introduces lower-level dependencies, design downward: create shared and required component frames with their states first, compose the screens that consume them, then validate flow, journey, or product continuity. When `all` is requested, inspect before writing and skip work already in parity.

## Preserve These Invariants

- Stay agnostic to planning format. Read the Change Source by role, follow the repository's Planning Convention for location, format, identification, and validation, and never require, install, or introduce a particular spec tool, file layout, or artifact set.
- Treat Paper as the latest approved design state. Put module-owned canonical Component Frames on `<Module> / Components`, genuinely cross-module families on `Shared / Components`, and Screen Artboards on `<Module> / <Feature>`.
- Keep `init` independent of Changes and read-only toward Paper, planning artifacts, tasks, and production code. Its only mutation is the Manifest Root's `PAPER.md`; require approval before retargeting or migrating an existing manifest.
- Keep `lint` file-wide and strictly read-only. Report evidence-backed structural findings without converting them into parity gaps, inferred requirements, manifest edits, or automatic cleanup.
- Keep `explore` change-free and noncanonical by default. Give each exploration its own `Exploration / <Name>` page, vary only what the user asked to vary, use real content with no placeholders, and remove nothing the brief did not say to remove.
- Require a resolved Paper target: a link in the request, one unambiguous recent link, or the manifest target. Never choose a target through the active file, recent-file order, or `list_files`.
- Open the linked file before inspecting it and pass its canonical file ID to every subsequent Paper read or write that accepts `fileId`.
- Never create specification frames, acceptance-criteria tables, coverage matrices, annotations, or comments in Paper. Do not use Paper comment threads as a specification channel.
- Let the Change Source determine intended Design Scope. Use Paper and code as evidence of current state, reuse opportunities, and downstream effects; never let accidental implementation complexity reduce an explicit requirement.
- Start at screen/component scope and escalate only as required through user flow, user journey, and product overhaul. Use the highest necessary route while retaining every lower level as a design dependency.
- Require Scope Approval before Paper design and keep it distinct from Paper Approval for production implementation. Never persist either approval as a Paper annotation or invented artifact marker.
- Keep Sync Audit Approval read-only. Require a displayed Sync Plan and explicit Sync Approval before changing Paper or the Change Source; require the same approval request to name code implementation before delegating to `implement`.
- Infer sync direction independently for each drift item from source ownership and Paper evidence. Never require `to-paper` or `from-paper`, assume one direction for the whole run, or silently convert Paper-only behavior into a business requirement.
- Never create or append to a page named after a Change merely to preserve history. Planning artifacts and repository history own change history; legacy change pages are noncanonical evidence and remain untouched unless an approved migration copies needed nodes into their current-state owner pages.
- Give each changed product-component family one component frame containing its required states and variations.
- Compose screens from canonical component nodes by cloning or duplicating them. Do not redraw changed components independently inside screens.
- Create screen artboards per materially distinct scenario and required viewport. Do not generate speculative breakpoints or states.
- Let the Change Source own business behavior, existing code and design tokens own the established visual language, and Paper own the intended composition under review.
- Before inventorying repository mappings or analyzing, designing, reconciling, reviewing, or implementing visual surfaces, audit each affected workspace for shadcn configuration or compatibility. When configured, prefer its installed components, repository wrappers, and composition patterns; compatibility alone never authorizes shadcn initialization or registry changes.
- Keep visual and non-visual requirements in the same coverage pass, but represent only visual requirements in Paper.
- Require approval before changing intent, requirements, or decisions in the Change Source. Record approved implementation gaps in its existing tasks; never create a separate parity artifact.
- Add or reopen implementation tasks only after approval. Mark a task complete only after its implementation passes the required verification.
- Keep `parity` read-only across the Change Source, Paper, tasks, and production code. Route source/Paper reconciliation through `sync` and code delivery through `implement`; never mutate a source inside `parity`.
- Treat a Change that its Planning Convention marks closed, archived, or done as read-only audit history.
- Resolve the product font and tokens before the first write and use them from the first node; never draw in a default font and correct it afterwards.
- Load the Paper MCP guide before other Paper operations, review screenshots after meaningful changes, and always finish working on edited nodes.

## Review Discipline

For initialization work:

1. Report the Manifest Root, explicit Paper file link, and `init` slice; do not resolve a Change.
2. Scan the complete live page hierarchy once, inventory only observed canonical current-state pages and surfaces, and exclude exceptional or structurally invalid surfaces with Lint Findings rather than repairing them.
3. Preserve confirmed valid manifest entries, remove entries only after proving the corresponding canonical surface absent, and stop for approval before target replacement or schema migration.
4. Write or refresh only root `PAPER.md`, then report inventory counts, retained, added, and removed entries, the observed Planning Convention, lint exclusions, and freshness or migration issues. Do not issue Design Alignment or Full Parity verdicts.

For lint work:

1. Report the resolved Paper file link and `lint` slice; do not resolve a Change.
2. Audit the complete page hierarchy and inspect canonical frames only to the depth needed to evaluate placement, colocation, exceptional-page classification, and reuse.
3. Report each Lint Finding with its Paper location, violated convention, evidence, and recommended canonical owner or corrective action; separate unresolved structural evidence as Pending Evidence.
4. Make no changes and do not issue Design Alignment or Full Parity verdicts.

For exploration work:

1. Report the resolved Paper file link and the `explore` slice; do not resolve a Change.
2. State the Exploration Brief in a few lines (subject, surfaces, viewports, fidelity, what varies, target page), then draw in the same turn without waiting for approval.
3. Review each section by screenshot against the brief and the established design system.
4. Report the page link, what each artboard shows, open items that need real content or a decision, and the promotion step when relevant. Do not issue Design Alignment or Full Parity verdicts.

For scope work:

1. Report the resolved Paper file link, active change and where its Change Source lives, selected Design Scope, and evidence before any Paper mutation.
2. Include the affected workspace's component-system classification and relevant reuse opportunities in current-state evidence.
3. Show the appropriate chat-only coverage or impact matrix, material gaps, optional enhancements, and recommended user-flow or batch sequence. Size the report to the scope: a Screen/Component Change with no material gap needs a short report, not a journey audit.
4. Block design only on unresolved behavior, navigation, permissions, data, required states, flow, or composition decisions.
5. Stop after explicit `scope`; for automatic preflight, wait for Scope Approval and reuse it only while its inputs remain unchanged.

For design and resume work:

1. Report the resolved Paper file link, inferred change, and selected slice before modifying Paper.
2. State the evidence used for component families, states, scenarios, viewports, and configured component-system mappings.
3. Review spacing, typography, contrast, alignment, artboard fit, and component reuse after every meaningful section.
4. Reconcile only source-of-truth gaps; do not polish beyond the Change Source and established visual language without user direction.

For parity work:

1. Report findings by requirement or scenario with Change Source, Paper, and code evidence.
2. Separate blocking semantic gaps from non-blocking visual or component-system drift.
3. Report Design Alignment separately from Full Parity and keep Full Parity pending while any required source evidence is missing.
4. Route source/Paper drift to an explicitly requested `sync` handoff and code drift to `implement`; never apply a fix inside `parity`.

For sync work:

1. Report the source-derived affected design surfaces before detailed Paper inspection.
2. Audit only those surfaces, use the owning workspace's component system as visual-language evidence, classify every drift item as Source-to-Paper, Paper-to-Source candidate, unresolved, or aligned, and show the evidence.
3. Present one mutation plan that names Paper edits, Change Source edits, task changes, and whether code implementation is included; wait for explicit approval.
4. Apply approved Paper changes through `components` and `screens`, approved source changes in the artifacts that own them, and approved code work only by delegating to `implement`.

For implementation work:

1. Report the resolved Paper file link, active change, and incomplete-task inventory before modifying code.
2. Audit the affected UI workspace for shadcn configuration and compatibility before choosing component primitives.
3. Map alignment gaps to their owning requirements, tasks, and dependency chains; block only intersecting work and continue independent tasks.
4. Verify each task at focused, affected-package, and rendered-viewport boundaries as applicable before marking it complete.
5. Continue verifiable independent tasks around a blocker, then finish with a full parity batch and report all remaining gaps.
6. Leave other sessions' uncommitted work in place, commit only this run's files, and close by stating what is verified, whether the screens were seen rendered, what is committed and pushed, and where each migration has been applied.
