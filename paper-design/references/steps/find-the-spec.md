# find-the-spec

Read the tracker config, resolve one Spec and its Tickets, and report what state they are in.

- **Reads:** `docs/agents/issue-tracker.md`, the Spec issue, its Tickets and blocking edges, the user's message, recent conversation
- **May change:** nothing

## Read the tracker config

Check that `docs/agents/issue-tracker.md` exists; this one check may run before [open-paper-file](open-paper-file.md). When it is missing, stop and tell the user to run `/setup-matt-pocock-skills`. Everything else in this Step runs after open-paper-file and follows the operations in `docs/agents/issue-tracker.md`.

## Resolve one Spec

1. An explicit issue reference in the message.
2. One unambiguous Spec named in recent conversation.
3. Otherwise ask, naming the plausible candidates.

Resolve Specs from the tracker. Paper page names describe current product modules and features, so they never identify a Spec.

## Load and report

- Read the Spec body and comments completely, then its sub-issue Tickets with their blocking edges.
- Check it is a Ready Spec ([GLOSSARY.md](../../GLOSSARY.md)). When a section is missing or vague, name exactly what is missing and offer the edit for approval through the Job's Gate.
- A closed Spec is audit history: allow read-only Jobs (Size-up, Compare), refuse Paper, Spec, and ticket writes, and recommend a new Spec for new work.
- Report the Design Ticket state by the lifecycle table in [SKILL.md](../../SKILL.md): no tickets, tickets without a Design Ticket or artboard links, open, or closed. Note whether the Spec has a Design Section.

Reuse the loaded Spec and Tickets within the conversation; re-read before any tracker write or when the user says it changed.

Done when: one Spec, its Tickets, its readiness, and its Design Ticket state are in working context, or the Job has stopped with one ask.
