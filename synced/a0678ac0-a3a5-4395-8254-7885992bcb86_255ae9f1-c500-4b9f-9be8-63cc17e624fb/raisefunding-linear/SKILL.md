---
name: "raisefunding-linear"
description: "Use for any RaiseFunding client work tracking in Linear (workspace raisefundingai-ext, team RAI): adding or closing tasks, logging hours, daily updates for Lynn, blocked items and client replies."
---

# RaiseFunding work tracking in Linear

Raphael does contract work for RaiseFunding (approver: **Lynn**). All tasks, hours and daily recaps live in Linear: workspace **raisefundingai-ext**, team **RAI** ("Raisefundingai-ext"). Use the Linear connector tools. Times and dates are **Philippine time (PHT)**.

**Start every session by reading the team document README.md** (get_document, or list_documents with query "README.md"). It is the source of truth for conventions and routines. If README.md and this skill disagree, follow README.md, and tell Raphael so the skill can be updated.

The team document **MIGRATION_GUIDE.md** maps old board tickets to Linear: **RF-n = RAI-(n+4)** for RF-001 to RF-040. Work added after the migration (RAI-45 onward) has no RF number. When a note mentions an RF number, translate it to the RAI issue; read MIGRATION_GUIDE.md only when you need that lookup or the migration history.

## Conventions (summary of README.md)

**Statuses:** Backlog (not scheduled), Todo (scheduled this month, not started), In Progress, Done, Canceled. There is no Blocked status; use the Blocked label.

**Labels** (always set all that apply):
- **Area** group, one per issue: CRM, Big Wave, Operations, Band websites, RaiseFunding AI, Websites, RaiseFunding website, LaunchAxis, Meta ads, Social accounts, Social media, INXS, Band marketing, Rebel Souls. Create a new Area child label only if none fits. INXS is spelled INXS.
- **Billing** group: Billable, No charge, Billing TBC. "Non-billable" means No charge.
- **Month** group: e.g. Oct 2026. Every scheduled task gets the current month; backlog tasks get none. If the month's label doesn't exist yet (e.g. Nov 2026), create it under the Month group.
- **Blocked**: added on top of the status while waiting on Lynn or access. **Obsolete**: with Canceled when work no longer applies.

**Priority:** Urgent 1, High 2, Medium 3, Low 4; unconfirmed = 0.
**Assignee:** me (Raphael). **Due date:** the target date, if one is known.

## Issue description format

```
**Area:** <area> · **Billing:** <Billable | No charge | To confirm>
**Assigned:** <Mon D, YYYY> · **Closed:** <date or —>

### Blocker / decision needed      (only if blocked)
### Next action / latest update
### Finished work / confirmation    (when there is completed work)

**Source:** <where the request came from>
```

Linear sets its own completed date; the Closed line is the real finish date. Add a time in PHT when it matters.

## Writing for Lynn

Raphael often pastes technical notes (commits, lint, build checks, file names such as `/llms.txt`, "pushed to origin/main"). Rewrite them in plain stakeholder language before saving: say what changed for the website or its visitors, what was checked, and what is still pending. Keep commit hashes only as a short reference, e.g. "(reference 2b48440)". Leave out tooling details and anything about unrelated local changes. "Pushed" or "committed" does not mean live: say it's saved to the main version and note that live deployment is not yet verified, unless Raphael confirms it's live. If he supplies stakeholder-ready wording, use it as given.

## Common tasks

**Add a completed task** ("add this as completed, today, non-billable, <area>"): create the issue with state Done, the Area, Billing and current-Month labels, Closed = today, and the plain-language summary under Finished work. If any check is still outstanding (e.g. live verification), put it under Next action.

**Move to or from the backlog:** to the backlog → status Backlog and remove the Month label; into a month → Todo or In Progress and add that month's label.

**Log hours.** Linear has no time tracking, so always do both:
1. On the issue, add to its **Time log** comment, or create one if missing: `- **Oct 16, 2026 · 1.5 h · Billable** — what was done _(Source: …)_`. Hours not given → "not recorded"; never invent durations.
2. In the team document **"<Month YYYY> hours"** (e.g. "October 2026 hours"), add a row to Entries and recompute the **Totals** (Logged, Billable, Billing TBC, Entries missing hours) and the **By day** table from all rows. Read the document first (get_document) and patch it; don't retype it from memory. Create the next month's hours document with the same layout when the first entry of a new month arrives.

**Daily update for Lynn:** read today's Done and In Progress issues, Blocked items and today's hours, then add a section at the top of **"Daily updates — <Month YYYY>"** with **Email:** status · **Hours:** logged / billable, then Completed, In progress, Blockers / decisions, Next workday. Also draft the email text in the reply for Raphael to send. Mark Email: Sent only when he confirms.

**Client reply on a blocked task:** add an issue comment `**Client reply from Lynn — <date, time PHT>:** …`. If it unblocks the work, remove the Blocked label, move the issue to In Progress, note the previous blocker in the comment, and clear the Blocker section.

**Cancel or obsolete:** state Canceled (plus the Obsolete label when it no longer applies), Closed = today, and a comment with the reason. To reopen: Todo and clear Closed.

**Month rollover:** create the new Month label and the new month's hours and daily-updates documents. Unfinished tasks stay open; ask before relabelling them to the new month, then swap their Month label. Finished tasks keep their old Month label.

## Before finishing

Confirm what was created or changed (issue IDs and links), say if any hours were left unrecorded, and flag anything that needs Raphael's confirmation (billing TBC, live deployment, missing dates).