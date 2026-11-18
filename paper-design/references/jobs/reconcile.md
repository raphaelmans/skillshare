# Reconcile

Find where a spec and Paper disagree, decide per Drift Item which side should change, and apply only an approved Reconcile Plan. Code is never changed here.

## Triggers

- "Paper and the spec have drifted, fix it"
- "Update Paper to match the new user stories"
- "The designer changed the checkout screen, get the spec in line"
- Following a Compare report: "reconcile those"

## Needs

An open, Ready Spec and a Paper link.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [find-the-spec](../steps/find-the-spec.md)
3. [read-the-ui-system](../steps/read-the-ui-system.md) for each affected workspace.
4. [assess-design-scope](../steps/assess-design-scope.md) to list affected surfaces before any detailed Paper read; no Scope Approval stop.
5. [read-paper-surfaces](../steps/read-paper-surfaces.md) for those surfaces only. Reuse Compare evidence from this conversation while the spec, Paper nodes, and repository are unchanged.
6. [check-agreement](../steps/check-agreement.md) with one row per user story or scenario, between spec and Paper.
7. Classify and plan (below), then wait for **Reconcile Approval** (Gates in [SKILL.md](../../SKILL.md)).
8. Apply the approved plan (below).

## Classify each Drift Item

Infer direction per item; one run can hold both directions.

- **Spec to Paper**: a story, rule, or decision in the spec is missing, stale, or contradicted in Paper.
- **Paper-to-Spec candidate**: Paper shows intentional composition or behavior the spec lacks. A proposal until approved.
- **Unresolved**: both sides are explicit and conflict, provenance is unclear, or the fix would change business behavior without evidence. Ask the user.
- **Aligned**: equivalent. Leave it.

Code and history are provenance only.

## The Reconcile Plan

One displayed plan listing each Drift Item with its evidence, direction, exact Paper nodes or spec text affected, dependency order, and status. Include the Page Ownership Plan for Paper edits. When the Design Ticket is closed, say which approved surfaces change and ask the user to reopen it first. Stop on any unresolved item.

Name each edit boundary separately so the approval covers them precisely:

- **Paper edits**
- **Spec text edits**
- **Tracker edits**: Design Section, ticket links, Design Ticket

## Apply

- **Spec to Paper**: [draw](../steps/draw.md) the approved items on their owner pages, components before screens, reusing current nodes in place.
- **Paper to Spec**: edit exactly the approved spec text on the tracker, keeping its structure. Rerun [assess-design-scope](../steps/assess-design-scope.md) for affected rows when user stories changed.
- [link-design](../steps/link-design.md) only for the tracker edits the plan listed.

Then rerun the affected agreement rows, re-reading only the nodes this run edited.

## Ends with

A report of aligned, applied, deferred, and unresolved items. Follow-ups: new delivery work → Relay `/to-tickets <spec>`; code that now lags → ask paper-design to build it.
