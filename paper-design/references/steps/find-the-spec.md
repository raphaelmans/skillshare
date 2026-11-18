# find-the-spec

Read the tracker config, resolve one Spec and its Tickets, and report what state they are in.

- **Reads:** `docs/agents/issue-tracker.md`, the Spec issue, its Tickets and blocking edges, the user's message, recent conversation
- **May change:** nothing

## Read the tracker config

Check that `docs/agents/issue-tracker.md` exists. When a Job needs a tracker Spec and configuration is missing, stop and tell the user to run `/setup-matt-pocock-skills`. Use the configured operations. Except for the focused target lookup in [open-paper-file](open-paper-file.md), load the Spec and tickets after opening Paper.

## Resolve one Spec

1. Resolve an explicit issue reference by type. A UI Ticket selects that slice and its dependencies. Follow its parent relation (or explicit Parent field) to load the Spec, Design Ticket and coverage record. Check Spec readiness on the parent. Preserve the original ticket as the requested work.
2. One unambiguous Spec named in recent conversation.
3. Otherwise ask, naming the plausible candidates.

Resolve Specs from the tracker. Paper page names describe current product modules and features, so they never identify a Spec.

For a redesign, distinguish the requested migration from earlier discrepancy fixes. Use the open migration Spec for its own scope. When the user explicitly names multiple modules or Specs, preserve the overall boundary and resolve ownership per Spec, including shared work. Prior closed Specs, their tickets and audit decisions are baseline evidence. New delivery work belongs to an open or new Spec.

## Load and report

- Read the Spec body and comments completely, then its sub-issue Tickets with their blocking edges.
- Check [Ready Spec](../../GLOSSARY.md) status when the Job requires it. For a read-only comparison, report missing or vague requirements as evidence gaps. For work on an open Spec, identify any needed text edit for approval through the Job's Gate.
- A closed Spec is evidence for audit and baseline recovery. Route new delivery scope to an open or new Spec. A requested code-to-Paper sync follows the separate inventory path in [Reconcile](../jobs/reconcile.md).
- Report the Design Ticket state by the lifecycle table in [SKILL.md](../../SKILL.md): no tickets, tickets without a Design Ticket or artboard links, open, or closed. Note whether the Spec has a Design Section.

Reuse the loaded Spec and Tickets within the conversation; re-read before any tracker write or when the user says it changed.

Done when: one Spec, its Tickets, its readiness, and its Design Ticket state are in working context, or the Job has stopped with one ask.
