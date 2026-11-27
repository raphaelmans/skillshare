# Paper Design

This context names the Jobs, specs, Paper surfaces, approvals, and evidence paper-design uses to carry product UI between a Paper file, a spec on the configured issue tracker, and the code. Specs and tickets live wherever `/setup-matt-pocock-skills` configured the tracker; no term below names a particular tracker.

## Language

### Jobs and routing

**Job**:
One complete thing paper-design does for the user, chosen from what their message asks for rather than from a typed name.
_Avoid_: Slice, command, mode, route, workflow pass

**Step**:
A unit of work several Jobs share and that the user never asks for on its own, such as drawing components or reading the tracker.
_Avoid_: Primitive, slice, sub-workflow

**Router**:
The part of paper-design that reads the user's message and picks exactly one Job.
_Avoid_: Dispatcher, menu, slice selection

**Relay**:
The close of a Job that ends in another skill the user must run themselves: paper-design leaves the Paper evidence that skill needs in the conversation and names the command to type, without invoking it.
_Avoid_: Handoff, delegation, auto-invoke

**Resume**:
Taking the next action for one Spec from its current state when the user's message names no Job.
_Avoid_: Rerun all, restart, menu

**Inventory**:
The Job that reads the code for a named product area and writes its Requirements Inventory.
_Avoid_: Audit, baseline scan, Structural Inventory

**Sketch**:
The Job that draws a Sketch from a Sketch Brief, with no Spec.
_Avoid_: Explore, draft slice

**Check-structure**:
The read-only Job that audits the Paper file's page arrangement.
_Avoid_: Lint, audit, cleanup

**Set-up**:
The Job that creates or refreshes the Paper Manifest.
_Avoid_: Init, initialization pass

**Size-up**:
The read-only Job that sizes the design work for a Spec, a chosen Sketch or a named redesign and reports gaps.
_Avoid_: Scope, scoping slice

**Design**:
The Job that draws or updates canonical components and screens from a Spec, a chosen Sketch or an evidenced redesign boundary. It writes only to Paper.
_Avoid_: Design slice, components + screens

**Reconcile**:
The Job that reconciles a Spec and Paper, or syncs an implemented inference from its inventory entry to Paper.
_Avoid_: Sync, to-paper, from-paper

**Compare**:
The read-only Job that compares accepted requirements, Paper and code within the requested boundary. A redesign can use an evidenced product baseline.
_Avoid_: Parity, review, audit

**Build**:
The Job that checks Paper against the Tickets and Relays to the implementing skill.
_Avoid_: Implement, implementation slice

**Plan**:
The Job that carries designed surfaces into a Spec and Tickets: it Relays to `/to-spec` and `/to-tickets`, then writes the Design Section, the UI Ticket links and the Design Ticket.
_Avoid_: Write-up, reverse-spec, extract, Paper-to-spec, Reconcile Plan

### Specs and tickets

**Spec**:
One issue on the configured tracker describing a planned product change, with at least a Problem Statement, Solution, and User Stories.
_Avoid_: Change, Change Source, plan document, proposal

**Ready Spec**:
An open Spec whose Problem Statement, Solution, and User Stories (the sections of `/to-spec`'s template) are present and specific enough to size up.
_Avoid_: Planning-Ready, 4/4 complete

**Design Section**:
The `## Design` section of a Spec, holding Paper links and the Design Scope. For a redesign it also holds or links the coverage record. Plan writes it.
_Avoid_: Design notes, spec page, Paper annotations

**Ticket**:
A sub-issue of a Spec that delivers one vertical slice of it, with blocking edges to the tickets it depends on.
_Avoid_: Task, checklist item, Implementation Task

**Design Ticket**:
The human-in-the-loop \"Design in Paper\" Ticket that blocks every UI Ticket of a Spec; Plan creates it once the Spec has tickets, and only the user closes it.
_Avoid_: Design task, approval marker

**Visual Requirement**:
A user story or rule in a Spec whose observable outcome changes visible content, state, interaction, navigation, hierarchy, or responsive composition.
_Avoid_: Screen note, mockup comment

**Non-visual Requirement**:
A user story or rule in a Spec whose outcome is not shown directly on a user interface surface.
_Avoid_: Hidden screen state

### Gates

**Gate**:
An explicit user approval a Job must have before it changes anything outside the conversation.
_Avoid_: Step, routing decision, implied consent

**Scope Approval**:
The Gate that lets Design make the Paper writes a shown assessment report listed.
_Avoid_: Paper Approval, implied continuation

**Reconcile Audit**:
The read-only comparison of the surfaces a Spec affects, run inside Reconcile.
_Avoid_: Sync Audit, Gate, parity fix

**Reconcile Approval**:
The Gate that lets Reconcile make the edits its Reconcile Plan named.
_Avoid_: Sync Approval, audit approval, code authorization

**Paper Approval**:
The Gate given by closing a Spec's Design Ticket: approval of one Paper Target as the intended composition.
_Avoid_: Scope Approval, build intent, active-canvas approval

### Paper surfaces

**Paper Target**:
The Paper file identified by the current request, its referenced tracker or inventory record, related conversation, or one unambiguous Paper Manifest fallback.
_Avoid_: Active file, current canvas, recent file

**Component Family**:
A product component and the states or variations that share its identity and anatomy.
_Avoid_: Widget set, UI type

**Component Frame**:
A single Paper frame containing the canonical states and variations of one Component Family.
_Avoid_: Component spec, sticker sheet

**Screen Artboard**:
A Paper artboard representing one material scenario at one required viewport.
_Avoid_: Screen spec, route documentation

**Module Component Page**:
The current-state Paper page containing every canonical Component Family owned by one product module.
_Avoid_: Change page, component-per-page

**Feature Page**:
The current-state Paper page containing the Screen Artboards for one feature within a product module.
_Avoid_: Change page, change-slug page

**Shared Component Page**:
The current-state Paper page containing canonical Component Families that are genuinely owned across multiple modules.
_Avoid_: Miscellaneous components, duplicate module components

**Exceptional Page**:
A non-production Paper page classified as a Sketch Page or Archive, excluded from feature coverage and never the owner of canonical components.
_Avoid_: Unnamed draft, convention bypass

**Sketch**:
Spec-free Paper work drawn from a Sketch Brief: drafts, wireframes, content previews, variant comparisons, hi-fi concepts, or journey walkthroughs. Never canonical until Promotion.
_Avoid_: Exploration, design slice, canonical design, spike

**Sketch Page**:
The Exceptional Page that holds one Sketch, named `Sketch / <Name>`; a legacy `Exploration / <Name>` page is read as one. Sketch never draws anywhere else.
_Avoid_: Exploration page, scratch page

**Sketch Brief**:
The user's stated direction and supplied sources that stand in for a Spec during a Sketch: what to draw, at which fidelity, what varies, and what stays fixed.
_Avoid_: Exploration Brief, specification, scope report

**Promotion**:
Design copying a chosen Sketch's nodes into their canonical owner pages under Scope Approval, before Plan carries them to delivery.
_Avoid_: Implicit implementation, renaming the Sketch Page

### Paper Manifest

**Paper Manifest**:
The committed `docs/agents/paper.md` record of the Paper Target, current-state page ownership, canonical surface mappings, repository UI-system context, required viewports, and freshness evidence.
_Avoid_: PAPER.md, workspace manifest, specification, audit cache

**Manifest Root**:
The one repository directory that holds `docs/agents/` and owns the Paper Manifest.
_Avoid_: Workspace manifest directory

**Manifest Refresh**:
A Set-up rerun that rebuilds the Structural Inventory, keeps confirmed valid entries, and removes an entry only after confirming its canonical surface is absent.
_Avoid_: Automatic rebuild, blind replacement

**Manifest Migration**:
An approved conversion of an existing Paper Manifest whose schema is unsupported, whose structure is malformed, or that still lives at the legacy root `PAPER.md`.
_Avoid_: Silent rewrite, destructive refresh

**Manifest Entry**:
A durable mapping from a canonical Paper surface to its owner page and relevant repository evidence.
_Avoid_: Requirement, specification, audit finding

**Structural Inventory**:
The observed current-state pages, canonical Component Families, Screen Artboards, and repository mappings recorded by Set-up without inferring missing or intended coverage.
_Avoid_: Coverage matrix, design plan

**Stale Manifest Entry**:
A Manifest Entry whose recorded target, page ownership, surface locator, or repository evidence can no longer be trusted without focused verification.
_Avoid_: Design Drift, missing requirement

**Staleness Evidence**:
A concrete affected-path change, Spec surface impact, locator failure, name or ownership mismatch, or reported manual Paper edit that makes a Manifest Entry stale; elapsed time alone is insufficient.
_Avoid_: Expiration date, routine re-audit

**Paper Locator Hint**:
A cached Paper page or node identifier paired with a human name to speed up lookup without becoming authoritative.
_Avoid_: Canonical ID, source of truth, unnamed locator

### Requirements Inventory

**Requirements Inventory**:
The repository record at `docs/agents/design-inventory/<area>.md` of every business requirement one product area implements, each with a stable ID, code evidence at an inspected revision, and a Keep, Change or Retire status the user decides. It also holds the area's target-surface coverage and Paper sync pending entries.
_Avoid_: Structural Inventory, Spec, audit

### Scope

**Design Scope**:
The smallest experience boundary that contains the requested change and its effects. Its levels are Surface Change, User Flow, User Journey and Product Overhaul.
_Avoid_: Requested slice, implementation size

**Surface Change**:
A localized change to a screen, Component Family, interaction, state, variation, or responsive behavior that does not introduce a User Flow.
_Avoid_: Small journey, isolated mockup

**User Flow**:
An ordered set of user actions and decisions within a User Journey that begins with a trigger and ends in a defined outcome.
_Avoid_: Screen list, journey

**User Journey**:
The end-to-end experience through which a user pursues a distinct goal, potentially through multiple User Flows.
_Avoid_: Flow, feature

**Product Overhaul**:
A coordinated experience change spanning multiple User Journeys, major product areas, or shared navigation and experience foundations.
_Avoid_: Large screen update, long task list

**Design Batch**:
A dependency-aware group of shared components, states, screens, or patterns designed and validated together.
_Avoid_: Arbitrary chunk, implementation sprint

**Page Ownership Plan**:
The planned owner page for each Component Family and Screen Artboard a Spec touches.
_Avoid_: Page list, spec-named pages

### Findings

**Structure Finding**:
An evidence-backed page-arrangement violation reported by Check-structure, with its Paper location, the convention it breaks, and the recommended owner or fix.
_Avoid_: Lint Finding, Design Drift, automatic fix

**Design Alignment**:
Agreement between the accepted requirements and the Paper Target across every applicable Visual Requirement. A redesign can use its evidenced baseline before a migration Spec exists.
_Avoid_: Full Agreement, design complete

**Full Agreement**:
Agreement across the accepted requirements, Paper Target and code in the named scope, with evidence for every required behavior and composition. Equivalent token use or responsive reflow that preserves hierarchy can qualify as Close.
_Avoid_: Full Parity, visual match

**Pending Evidence**:
The state in which a required source has no sufficient evidence to evaluate; it is not the same as the source being inapplicable.
_Avoid_: Not applicable, assumed alignment

**Gap**:
A missing or contradictory required behavior, state, action, visibility rule, navigation path, component relationship, or material visual decision.
_Avoid_: Minor drift, preference

**Design Drift**:
A meaningful difference between intended, drawn, or implemented design. When an inferred surface is implemented ahead of Paper, the design inventory records the affected surface and the direction of the later sync.
_Avoid_: Pixel difference, implementation bug

**Drift Item**:
One independently fixable piece of Design Drift, with evidence, the source that owns it, its direction, and a status.
_Avoid_: Whole-page mismatch, audit note

**Drift Direction**:
The source and destination for one Drift Item. Directions include Spec to Paper, a Paper-to-Spec candidate, and code to Paper for an implemented inference recorded in the inventory. Conflicting evidence can leave direction unresolved.
_Avoid_: Sync Direction, command option, run-wide mode

**Reconcile Plan**:
The displayed set of proposed fixes for Drift Items, with evidence, direction, targets, and each edit boundary named separately.
_Avoid_: Sync Plan, automatic merge, task list
