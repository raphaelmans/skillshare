---
name: paper-design
description: Paper design work routed from what the message asks. Use for $paper-design, or when the user wants to sketch, draft, wireframe, or compare variants in a Paper file; check its page structure; set up its Paper manifest; size up, design, reconcile, or compare a spec against Paper; build from an approved Paper design; or turn Paper screens or components into a spec or tickets. Specs and tickets come from the issue tracker configured by /setup-matt-pocock-skills.
---

# Paper Design

Read the message, pick one **Job**, run it, and end with a report or a **Relay**. Consult [GLOSSARY.md](GLOSSARY.md) only when a term is unclear; the reasons behind each rule live in [docs/adr/](docs/adr/).

## Start

1. Pick the Job with the Router.
2. Read its file under `references/jobs/` completely and follow it. Each Job file names the Steps it loads, starting with [open-paper-file](references/steps/open-paper-file.md).

Spec-bound Jobs (Size-up, Design, Reconcile, Compare, Build, and Write-up when it needs a spec) stop in [find-the-spec](references/steps/find-the-spec.md) when the tracker is not configured. Sketch, Check-structure, and Set-up work without it.

## Router

Route by what the message asks for.

| The message asks to… | Example | Job |
| --- | --- | --- |
| Draw something with no spec: draft, wireframe, preview copy, compare variants, walk a journey | "sketch the stage control in two layouts" | [Sketch](references/jobs/sketch.md) |
| Check how the Paper file is arranged, or list its pages and surfaces | "is this file laid out right?" | [Check-structure](references/jobs/check-structure.md) |
| Create or refresh the Paper Manifest from a link in this message | "set up Paper for this repo: <link>" | [Set-up](references/jobs/set-up.md) |
| Judge how big a spec's design work is, without drawing | "how much design does #142 need?" | [Size-up](references/jobs/size-up.md) |
| Draw or update canonical components and screens for a spec | "design #142 in Paper" | [Design](references/jobs/design.md) |
| Make a spec and Paper agree, fixing whichever side is behind | "Paper and #142 drifted, fix it" | [Reconcile](references/jobs/reconcile.md) |
| Check spec, Paper, and code against each other, changing nothing | "does the code match the design?" | [Compare](references/jobs/compare.md) |
| Build an approved Paper design into the codebase | "build it", "put this design in the code" | [Build](references/jobs/build.md) |
| Turn chosen Paper screens or components (or a Sketch) into code, a spec, or tickets | "make tickets for these screens" | [Write-up](references/jobs/write-up.md) |

Old names still route: explore → Sketch; lint and inventory-tree → Check-structure; init → Set-up; scope → Size-up; components and screens → Design; sync → Reconcile; parity → Compare; implement → Build.

Routing rules:

- **Resume.** A bare `$paper-design` or "continue": when one spec resolves, read its state from the Design Ticket lifecycle table below and take the next action, continuing Design at its first incomplete Design Batch when drawing is unfinished. When none resolves, ask which spec.
- **Answers that need no Paper call.** A question about page-arrangement conventions (answer from Page arrangement below), a status or "where are we" answer, and the reply that structure fixes are manual.
- **Ask once.** When two Jobs that change different things both fit, ask one short question naming both. When the candidates are all read-only, pick the narrower one.
- **Routing grants nothing.** Picking a Job never passes a Gate.
- **Follow-on words.** "Commit", "push", "open a PR", or "run the migration" go into the Relay for the skill that owns them; paper-design records them there and moves on.
- **Structure fixes are manual.** Moving, renaming, or deleting pages to clear Structure Findings sits outside every Job; say so and point at the findings. A finding on an open spec's surfaces can go through Reconcile.

## Gates

A Gate is an explicit user approval. An approval covers exactly the writes its displayed report or plan listed, each boundary named separately; anything not listed needs its own ask. Steps that only read need no Gate.

- **Scope Approval**: Design may make the writes the shown Size-up report listed.
- **Reconcile Approval**: Reconcile may make the edits its displayed Reconcile Plan named.
- **Paper Approval**: the Design Ticket is closed.

Design Ticket lifecycle:

| State | Means | Next action |
| --- | --- | --- |
| Spec has no tickets | Nothing to block yet | Relay `/to-tickets <spec>` |
| Tickets exist, no Design Ticket or artboard links | The design is not linked from the tracker | [link-design](references/steps/link-design.md), under the approval that listed it; otherwise ask |
| Design Ticket open | Awaiting the user's sign-off | The user reviews the screens and closes it; Build stops until then |
| Design Ticket closed | Paper Approval | Build may proceed. A report or plan that would change approved surfaces says which, and asks the user to reopen the ticket first |

Gate rules:

- A bare "yes", "approve", or "go ahead" applies to the one Gate pending in the conversation. A message routed to Design counts as Scope Approval only when it says to go ahead with the shown report.
- An offer of another Job is never a pending Gate; a bare yes to it starts nothing. The user asks for the Job.
- Ask each Gate once per spec.
- Ask again when the spec, Paper Target, or requested boundary changes.
- Edits made by the approved work, and reconnects, do not re-ask.
- After approved corrections, rerun the assessment silently and ask again only when the Design Scope, owner pages, or sequence change.

## Relay

When a Job ends in `/to-spec`, `/to-tickets`, `/implement`, or `/implement-spec`, leave the evidence that skill needs in the conversation (Paper file link, frame and artboard links, Design Scope, open questions, answered decisions) and name the exact command for the user to type. Those skills are user-invoked; the user runs them.

For work that has a spec, only Build Relays to `/implement` or `/implement-spec`; every other Job ends with "ask paper-design to build it". Write-up's spec-free `/implement` is the one exception.

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

Specs, acceptance criteria, coverage tables, plans, reports, annotations, and approval markers stay in the conversation or the tracker, never on the canvas or in Paper comment threads.
