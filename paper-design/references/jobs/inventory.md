# Inventory

Read the code for a named product area and record every business requirement it implements today, so a redesign is sketched, designed and delivered against them. Its only write is that area's Requirements Inventory file.

## Triggers

- "Inventory the business requirements for Studio campaigns"
- "What does billing do today, before we overhaul it?"
- "Refresh the campaigns inventory"

## Needs

A named product area in a repository. No Paper link, Spec, tracker config or Gate: the request authorizes the one file. This Job starts without [open-paper-file](../steps/open-paper-file.md).

When the area's edge is unclear, ask one question naming the candidate routes or modules, with a recommended boundary.

## Steps

1. **Fix the boundary.** Name the routes, screens and shared hosts the area owns, and record the revision inspected. When the area's file already exists, this is a refresh: keep every ID, re-inspect rows whose code changed since the recorded revision, add rows for new behavior, and mark a row whose code is gone as `Absent at <revision>` for the user to decide.
2. **Walk every entry point in the boundary.** Cover navigation and direct links, each role, each screen's actions, validation, empty, loading and error states, recovery and return paths, and side effects such as persistence, notifications and downstream changes. Follow a shared component into every host inside the boundary. Tests, earlier Specs and recorded decisions are supporting evidence.
3. **Write one row per requirement** in the format below. For a large area, work one module or journey at a time and list what remains under Unscanned.
4. **Write the file**, then report.

## The file

`docs/agents/design-inventory/<area>.md` under the Manifest Root, with the area, its boundary, the revision and date inspected, then:

| ID | Requirement | Kind | Evidence | Status |
| --- | --- | --- | --- | --- |
| R-12 | A reviewer entering from the queue can retry a failed import and returns to the same filtered queue | Visible | Queue route, retry handler and its test at the recorded revision | Keep |

- **ID** is stable for the life of the file. Later Jobs cite it in sketches, scope reports, Specs and Tickets.
- **Requirement** is an observable journey: entry point, eligible role, action and outcome. A rule with no visible consequence is one sentence stating the rule.
- **Kind** is Visible or Nonvisual.
- **Evidence** names the code entry point and what proves the behavior.
- **Status** starts as Keep. Only the user's decision makes it Change or Retire, recorded with that decision. A control missing from a later design retires nothing.

Defects and incidental styling carry no product authority. List a suspected defect under Open questions with its evidence. Close the file with Unscanned parts of the boundary and Open questions.

The same file is the area's design inventory. Later Jobs add the target Paper surface for each row and any Paper sync pending entries to it.

## Ends with

A report: the boundary and revision, row counts by Kind, the open questions and the unscanned parts. Close with two offers, neither started here:

- **Sketch**, which draws against these rows.
- **Size-up**, which sizes the design work for the area.

Done when: every entry point in the boundary has its rows or is listed as Unscanned, and every row has evidence at the recorded revision.
