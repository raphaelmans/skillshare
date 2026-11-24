# Use the configured issue tracker for specs and tickets

paper-design no longer observes a per-repository Planning Convention. A spec is one issue on the tracker that `/setup-matt-pocock-skills` records in `docs/agents/issue-tracker.md`, its delivery work is that issue's tickets with blocking edges, and it is ready when it has a Problem Statement, Solution, and User Stories. This puts paper-design on the same planning layer as `/to-spec`, `/to-tickets`, `/implement`, and `/implement-spec` instead of keeping a second, looser model. Jobs that need a spec stop and point to setup when the tracker config is missing; Sketch, Check-structure, and Set-up keep working without it. paper-design never writes a spec from scratch (Write-up Relays to `/to-spec`), but after approval it may edit an existing spec's text and its Design Section, because `/to-spec` only creates new issues. Supersedes ADR 0014.

## Consequences

- Source Roles, Planning-Ready, Current Behavior Docs, and task checklists are gone; "Change" reads as "Spec" in earlier ADRs.
- The Paper Manifest moves from root `PAPER.md` to `docs/agents/paper.md`, next to the tracker config; moving a legacy file is a Manifest Migration that needs one approval.
