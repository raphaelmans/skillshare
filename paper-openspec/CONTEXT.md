# Paper OpenSpec Delivery Workflow

This context names the artifacts, design surfaces, delivery passes, and evidence used to carry an OpenSpec Change from Paper composition through verified implementation.

## Language

**OpenSpec Change**:
A named proposal for changing system behavior, represented by one planning-complete artifact set.
_Avoid_: Feature brief, ticket

**Artifact Set**:
The proposal, delta specifications, design, and tasks belonging to an OpenSpec Change.
_Avoid_: Spec page, Paper notes

**Paper Target**:
The Paper file selected explicitly for the current request or resolved from one unambiguous Paper Manifest fallback.
_Avoid_: Active file, current canvas, recent file

**Paper Manifest**:
The single committed root `PAPER.md` record of durable Paper targeting, current-state page ownership, canonical surface mappings, repository UI-system context, required viewports, and freshness evidence.
_Avoid_: Workspace manifest, specification, parity report, audit cache

**Manifest Root**:
The repository directory that contains `openspec/` and owns its single Paper Manifest, even when nested inside a larger Git monorepo.
_Avoid_: Git root, workspace manifest directory

**Paper Initialization**:
An explicit project-level, Paper-read-only structural inventory pass that creates or refreshes the Paper Manifest without requiring an active OpenSpec Change or becoming a prerequisite for other workflow slices.
_Avoid_: Automatic bootstrap, mandatory preflight, full audit

**Manifest Refresh**:
An explicit Paper Initialization rerun that rebuilds the structural inventory, preserves confirmed valid entries, and removes an entry only after confirming its canonical surface is absent.
_Avoid_: Automatic rebuild, parity rerun, blind replacement

**Manifest Migration**:
An explicitly approved conversion of an existing Paper Manifest whose schema is unsupported or whose structure is malformed.
_Avoid_: Silent rewrite, destructive refresh

**Manifest Entry**:
A durable mapping from a canonical Paper surface to its owner page and relevant repository evidence.
_Avoid_: Requirement, specification, audit finding

**Structural Inventory**:
The observed current-state pages, canonical Component Families, Screen Artboards, and repository mappings recorded by Paper Initialization without inferring missing or intended coverage.
_Avoid_: Coverage matrix, design plan, parity audit

**Stale Manifest Entry**:
A Manifest Entry whose recorded target, page ownership, surface locator, or repository evidence can no longer be trusted without focused verification.
_Avoid_: Design Drift, parity gap, missing requirement

**Staleness Evidence**:
A concrete affected-path change, OpenSpec surface impact, locator failure, name or ownership mismatch, or reported manual Paper edit that makes a Manifest Entry stale; elapsed time alone is insufficient.
_Avoid_: Expiration date, routine re-audit

**Paper Locator Hint**:
A cached Paper page or node identifier paired with a human name to accelerate lookup without becoming authoritative.
_Avoid_: Canonical ID, source of truth, unnamed locator

**Visual Requirement**:
A requirement whose observable outcome changes visible content, state, interaction, navigation, hierarchy, or responsive composition.
_Avoid_: Screen note, mockup comment

**Non-visual Requirement**:
A requirement whose outcome is not represented directly on a user interface surface.
_Avoid_: Hidden screen state

**Component Family**:
A changed product component and the states or variations that share its identity and anatomy.
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
A non-production Paper page explicitly classified as Exploration or Archive and excluded from normal feature coverage while remaining ineligible to own canonical production components.
_Avoid_: Unnamed draft, convention bypass

**Design Scope**:
The smallest experience boundary that fully contains the impact of an OpenSpec Change.
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
A dependency-aware group of shared components, states, screens, or patterns that should be designed and validated together.
_Avoid_: Arbitrary chunk, implementation sprint

**Scope Approval**:
Explicit authorization to proceed from a reported Design Scope and sequence into Paper design while its source inputs remain unchanged.
_Avoid_: Paper Approval, implied continuation

**Paper Approval**:
Explicit authorization to use one Paper Target as the intended composition for delivering an OpenSpec Change.
_Avoid_: Scope Approval, implied consent, active-canvas approval

**Implementation Run**:
An explicitly authorized delivery pass for the outstanding tasks of one active OpenSpec Change against its approved Paper Target and repository conventions.
_Avoid_: Design resume, parity fix

**Implementation Task**:
An item in an Artifact Set's task list whose verified completion advances delivery of the OpenSpec Change.
_Avoid_: Paper note, inferred work

**Verification Gate**:
The required body of behavioral, repository, rendered, and parity evidence that establishes an Implementation Task as complete.
_Avoid_: Code written, visual similarity

**Resume**:
The act of finding the first incomplete or stale non-code design boundary for one OpenSpec Change within its Paper Target and continuing from there.
_Avoid_: Rerun all, restart

**Parity**:
An evidence-based assessment of whether the required sources express the same behavior and component relationships.
_Avoid_: Pixel equality, screenshot match

**Paper Lint**:
An independently invocable, Paper-target-level, read-only assessment of whether current-state pages and canonical frames follow structural conventions for naming, placement, colocation, exceptional-page classification, and canonical reuse; it requires no OpenSpec Change and never repairs findings.
_Avoid_: Parity, reconciliation, initialization, automatic cleanup

**Lint Finding**:
An evidence-backed structural convention violation identified by Paper Lint, with its Paper location, violated convention, and recommended canonical owner or corrective action.
_Avoid_: Design Drift, parity gap, automatic fix

**ASCII Component Preview**:
A chat-only structural sketch of one Component Family and its required states or variations before Paper composition.
_Avoid_: Screen wireframe, user-flow diagram, Paper mockup

**Design Alignment**:
Agreement between an Artifact Set and its Paper Target across every applicable visual requirement.
_Avoid_: Full Parity, design complete

**Full Parity**:
Agreement across every required Artifact Set, Paper Target, and implementation source with no Gap or Pending Evidence.
_Avoid_: Available-source parity, visual match

**Pending Evidence**:
The state in which a required source has no sufficient evidence to evaluate; it is not equivalent to a source being inapplicable.
_Avoid_: Not applicable, assumed alignment

**Reconciliation**:
The resolution of a parity gap in the source that owns the disputed concern.
_Avoid_: Canvas annotation, informal note

**Gap**:
A missing or contradictory required behavior, state, action, visibility rule, navigation path, component relationship, or material visual decision.
_Avoid_: Minor drift, preference

**Design Drift**:
A semantic difference between an Artifact Set and its Paper Target that may require reconciliation even when both remain internally coherent.
_Avoid_: Pixel difference, implementation bug

**Drift Item**:
One independently reconcilable instance of Design Drift with evidence, an owning concern, and a resolution status.
_Avoid_: Whole-page mismatch, audit note

**Sync Direction**:
The inferred movement of intent for one Drift Item from its owning source toward the source that lacks or contradicts it.
_Avoid_: Command option, run-wide mode

**Sync Audit**:
A targeted read-only comparison of affected design surfaces in an Artifact Set and Paper Target.
_Avoid_: Parity fix, implementation run

**Sync Plan**:
The reviewable set of proposed reconciliations for Drift Items, including their evidence, inferred direction, targets, and authorization boundaries.
_Avoid_: Automatic merge, task list

**Sync Approval**:
Explicit authorization to apply the named Paper and Artifact Set mutations in one Sync Plan; it authorizes production delivery only when that same request explicitly includes implementation.
_Avoid_: Audit approval, implied code authorization
