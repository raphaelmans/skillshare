---
name: paper-design
description: Use for $paper-design, sketches, wireframes and variants in Paper, page structure and manifest setup, spec-driven UI design and reconciliation, and porting an existing product to a new Paper design or rebrand. Covers scoping partial designs, completing missing screens and component states, syncing inferred designs from code, comparing Paper and code, preparing specs and tickets, and building from approved designs. Uses the project's configured issue tracker.
---

# Paper Design

Read the message, pick one **Job**, run it, and end with a report or a **Relay**. Consult [GLOSSARY.md](GLOSSARY.md) only when a term is unclear; the reasons behind each rule live in [docs/adr/](docs/adr/).

## Start

1. Pick the Job with the Router.
2. Read its file under `references/jobs/` completely and start with [open-paper-file](references/steps/open-paper-file.md).
3. For feature ports and partial designs, [confirm design intent](references/steps/confirm-design-intent.md) after focused discovery and before scoping the work. Follow the Job with that boundary, the source designs and the chosen order.

Jobs that need a tracker Spec use [find-the-spec](references/steps/find-the-spec.md). Sketch, Check-structure, Set-up, and a redesign's Paper-only work can start without one.

## Router

Route by what the message asks for.

| The message asks to… | Example | Job |
| --- | --- | --- |
| Draw something with no spec: draft, wireframe, preview copy, compare variants, walk a journey | "sketch the stage control in two layouts" | [Sketch](references/jobs/sketch.md) |
| Check how the Paper file is arranged, or list its pages and surfaces | "is this file laid out right?" | [Check-structure](references/jobs/check-structure.md) |
| Create or refresh the Paper Manifest from a link in this message | "set up Paper for this repo: <link>" | [Set-up](references/jobs/set-up.md) |
| Size the design work for a spec or a named redesign | "how much design does #142 need?" | [Size-up](references/jobs/size-up.md) |
| Draw or complete canonical components and screens for a spec or existing-product redesign | "design #142 in Paper", "move our existing app to this new design" | [Design](references/jobs/design.md) |
| Make a spec and Paper agree, fixing whichever side is behind | "Paper and #142 drifted, fix it" | [Reconcile](references/jobs/reconcile.md) |
| Check spec, Paper, and code against each other, changing nothing | "does the code match the design?" | [Compare](references/jobs/compare.md) |
| Implement an approved design for a Spec or its UI Ticket | "build ENG-142", "implement its approval screen" | [Build](references/jobs/build.md) |
| Turn chosen Paper screens or components (or a Sketch) into code, a spec, or tickets | "make tickets for these screens" | [Write-up](references/jobs/write-up.md) |

Old names still route: explore → Sketch; lint and inventory-tree → Check-structure; init → Set-up; scope → Size-up; components and screens → Design; sync → Reconcile; parity → Compare; implement → Build.

Routing rules:

- **Existing product, new Paper design.** Use [map-redesign-coverage](references/steps/map-redesign-coverage.md) for the agreed scope. Draw Paper-first work in Design or Reconcile. Carry code-first inferences into Build or a spec-free implementation Relay. Use Write-up for a planning-only request and Compare for an audit-only request. A request to sync an implemented inventory entry back to Paper selects Reconcile.
- **A selected prototype or hi-fi.** The requested outcome determines the Job. A bounded port with a Spec uses Build. A selected surface with no delivery Spec uses Write-up to size the port. A request to complete missing Paper compositions uses Design. Sketch is for exploration. Use the surface references from [open-paper-file](references/steps/open-paper-file.md#reference-a-specific-surface) throughout.
- **Resume.** A bare `$paper-design` or "continue" resumes the first incomplete Design Batch or the next Design Ticket lifecycle action for the resolved Spec. An established redesign can also resume from its named product boundary and Paper Target before a Spec exists. Ask for the missing reference only when the context is ambiguous.
- **Status.** An existing report can answer “where did we leave off?” Quote its scope, revision and pending checks. For a current readiness or parity verdict, use Build or Compare and refresh stale evidence. Page conventions and manual structure fixes can be explained without opening Paper.
- **Ask once.** When two Jobs that change different things both fit, ask one short question naming both. When the candidates are all read-only, pick the narrower one.
- **Routing grants nothing.** Picking a Job never passes a Gate.
- **Follow-on words.** "Commit", "push", "open a PR", or "run the migration" go into the Relay for the skill that owns them; paper-design records them there and moves on.
- **Structure fixes are manual.** Moving, renaming, or deleting pages to clear Structure Findings sits outside every Job; say so and point at the findings. A finding on an open spec's surfaces can go through Reconcile.

## Gates

A Gate is an explicit user approval. An approval covers exactly the writes its displayed report or plan listed, each boundary named separately; anything not listed needs its own ask. Steps that only read need no Gate.

- **Scope Approval**: Design may make the writes listed in the scope report shown by Size-up or Design.
- **Reconcile Approval**: Reconcile may make the edits its displayed Reconcile Plan named.
- **Paper Approval**: the user has closed or resolved the Design Ticket under the configured tracker's convention for the referenced design.

Design Ticket lifecycle:

| State | Means | Next action |
| --- | --- | --- |
| Spec has no tickets | Nothing to block yet | Relay `/to-tickets <spec>` |
| UI tickets exist and their Design Ticket, links to required reference designs, or redesign coverage is incomplete | The tracker handoff is incomplete | Recover missing scope, then [link-design](references/steps/link-design.md) under the approval that covers the edits. Relay uncovered delivery work to `/to-tickets` |
| Design Ticket open | Awaiting the user's sign-off | The user reviews the screens and closes it. Its UI tickets wait. Report independently ready work from the actual dependency graph |
| Design Ticket closed | Paper Approval | Build checks delivery coverage. A report or plan that would change approved surfaces says which, and asks the user to reopen the ticket first |

Gate rules:

- A bare "yes", "approve", or "go ahead" applies to the one Gate pending in the conversation. A message routed to Design counts as Scope Approval only when it says to go ahead with the shown report.
- An offer of another Job is never a pending Gate; a bare yes to it starts nothing. The user asks for the Job.
- Ask each Gate once per spec, or per named boundary and Paper Target for a spec-free redesign.
- Ask again when the spec, Paper Target, or requested boundary changes.
- Edits made by the approved work, and reconnects, do not re-ask.
- After approved corrections, rerun the assessment silently and ask again only when the Design Scope, owner pages, or sequence change.

## Relay

When a Job ends in `/to-spec`, `/to-tickets`, `/implement`, or `/implement-spec`, leave the target and surface references, Design Scope, answered decisions, open questions and the user's verification instructions. Include the redesign inventory or its durable location when applicable. Name the exact command for the user to type. Those skills are user-invoked.

Planning Relays go to `/to-spec` or `/to-tickets`. For work that has a spec, Build owns the implementation Relay to `/implement` or `/implement-spec`. Write-up can Relay a spec-free single-session scope to `/implement` once its Paper-first decisions are settled. Every port Relay carries the working baseline and retained acceptance criteria. Give the delivery owner the [integrated behavior check](references/steps/check-agreement.md#retained-behavior-at-delivery) and the inventory location for results or deferred Paper sync.

## Invariants

### Page arrangement

Pages describe current design by enduring product ownership, in human module and feature names, never by the spec that last touched them.

| Page | Owns |
| --- | --- |
| `<Module> / Components` | Every canonical Component Family that module owns, one `Component / <Name>` frame per family with all its states inside |
| `Shared / Components` | Families whose ownership and reuse genuinely cross modules; never a miscellaneous bin |
| `<Module> / <Feature>` | Screen Artboards named `Screen / <Surface> / <Scenario> / <Viewport>` |
| `Sketch / <Name>` (legacy `Exploration / <Name>`) | One Sketch; Exceptional, owns nothing canonical |
| `Archive / <Name>` | Retained noncanonical designs; Exceptional |

Spec-named pages, unnamed drafts, and ambiguous collections own nothing.

### Paper holds composition only

Keep specs, acceptance criteria, plans, reports and approvals in the conversation or tracker. Keep surface coverage and deferred Paper sync in the project's design inventory. Keep these records off the canvas and out of Paper comment threads.
