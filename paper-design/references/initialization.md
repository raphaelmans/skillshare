# Paper Initialization

Create or refresh the one Paper Manifest owned by the Manifest Root. Initialization is independent of Changes and read-only toward Paper, planning artifacts, tasks, and production code. Its only permitted mutation is root `PAPER.md`.

## Resolve the Manifest Root and target

1. Require an explicit Paper file link in the current request. Do not reuse a recent-chat link, the existing manifest target, the active Paper file, recent files, or `list_files`.
2. Resolve one Manifest Root. Use the directory that already holds `PAPER.md` when there is exactly one. Otherwise use the Git root, unless the user names a nested project or a nested project keeps its own planning artifacts and instructions that establish it as independent within a monorepo. That directory owns exactly one `PAPER.md`. Stop when repository context does not identify one root unambiguously.
3. Load the Paper MCP guide, open the explicit link, retain the canonical file ID, and pass it to every Paper read that accepts `fileId`.
4. If `PAPER.md` names a different target, show a bounded retarget plan and obtain explicit approval before replacing the target or inventory.
5. If `PAPER.md` claims an unsupported schema or is malformed, preserve it unchanged, show the migration needed to reach schema v1, and obtain explicit approval before rewriting it. Do not silently salvage ambiguous entries.

A missing manifest or a valid schema-v1 manifest with the same target needs no additional mutation approval: the explicit `init` invocation authorizes creation or refresh of `PAPER.md`.

## Build the structural inventory

Read [inventory-tree.md](inventory-tree.md) completely and use its shared page arrangement, observed-inventory procedure, repository-context rules, and exclusion handling. That reference is the source of truth for what qualifies for inventory and which evidence to collect.

Use the target already opened above and perform one inventory pass. Feed that result into schema v1 below; do not invoke the standalone slice separately or rescan for manifest serialization. Keep exclusions and Pending Evidence for the initialization completion report.

## Observe the Planning Convention

Follow **Establish the Planning Convention** in [workflow.md](workflow.md) to record how this repository plans changes, from repository instructions and established examples only. Record what is observed; do not choose, propose, or create a convention, and do not read individual Changes beyond what identifies the convention. When nothing establishes one, write `Not established`.

## Create or refresh schema v1

Write a human-readable Markdown manifest with these sections and no invented requirements:

```markdown
# Paper Manifest

Schema: 1

## Paper Target

- URL: <explicit Paper file URL>
- File: <human Paper file name>
- File ID hint: <canonical file ID, if available>
- Inspected: <ISO-8601 timestamp>

## Planning Convention

- Change Sources: <where changes are planned: repository paths, a tracker, or both>
- Change identifier: <how one change is named: path, folder, issue key, title>
- Source Roles: <which artifacts carry intent, requirements, decisions, and tasks>
- Closed changes: <how a change is marked closed or archived>
- Validation: <command, or none>
- Current Behavior Docs: <path, or none>

## Pages

| Type | Page | Page ID hint |
| --- | --- | --- |

## Component Families

| Owner page | Component family | States or variations | Node ID hint | Workspace | Repository paths | Verified commit |
| --- | --- | --- | --- | --- | --- | --- |

## Screen Artboards

| Owner page | Artboard | Scenario | Viewport | Node ID hint | Workspace | Repository paths | Verified commit |
| --- | --- | --- | --- | --- | --- | --- | --- |

## UI System Context

| Workspace | Classification | Configuration and component roots | Verified commit |
| --- | --- | --- | --- |
```

The **Planning Convention** section is optional within schema v1: a valid v1 manifest without it needs no migration, and a refresh adds it when a convention is observed. Use `None observed` below an inventory heading when that section is empty; an empty canonical inventory is valid. Escape Markdown table delimiters in values. Locator IDs are non-authoritative hints and must never appear without the corresponding human page or surface name.

On refresh:

- Preserve every existing entry confirmed against the live target and current repository evidence.
- Update an entry only when live structural or repository evidence changed.
- Add newly observed valid canonical entries.
- Remove an entry only after proving its canonical surface absent from the complete live scan. A lookup failure, renamed page, or stale locator alone is not proof of absence; resolve by human page and surface names first.
- Update the Planning Convention section when repository evidence shows the convention changed, such as a planning tool being retired in favor of another location or format.
- Preserve unrelated user-authored content only when it does not make schema ownership ambiguous. Stop for migration approval if a safe schema-v1 refresh cannot retain it.

Write `PAPER.md` only after the full inventory and preservation decisions are resolved. Never mutate Paper during initialization.

## Report completion

Report:

- Manifest Root and explicit Paper Target
- Canonical page, Component Family, Screen Artboard, and mapped workspace counts
- Retained, added, updated, and removed manifest entries
- The observed Planning Convention, or that none was established
- Lint exclusions and Pending Evidence
- Retarget, migration, locator, or repository-freshness issues

Do not issue Design Alignment or Full Parity verdicts and do not continue into scope, design, sync, parity, or implementation automatically.
