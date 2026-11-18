# Set-up

Create or refresh the Paper Manifest at `docs/agents/paper.md` from a Paper link given in the same message. Its only write is that file.

## Triggers

- "Set up paper-design for this repo with <link>"
- "Refresh the Paper manifest", "re-index the Paper file"
- "Point the manifest at this file instead: <link>"

## Needs

- A Paper link in the current message.
- Exactly one Manifest Root: the one directory holding `docs/agents/`. Stop and ask when the repository does not resolve exactly one.
- No spec and no tracker config; report whether `docs/agents/issue-tracker.md` exists.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. Check the existing manifest, then pick the branch:
   - **None, or same target at schema 1**: the Set-up request authorizes create or refresh.
   - **Different target**: an explicit request to point at the new file is the retarget approval; show the retarget plan and apply it.
   - **Legacy root `PAPER.md`, unsupported schema, or malformed**: a Manifest Migration. Keep the file unchanged, show the move or conversion, and wait for one approval.
3. [map-the-page-tree](../steps/map-the-page-tree.md) once; reuse that result for writing.
4. [read-the-ui-system](../steps/read-the-ui-system.md) for workspaces mapped to observed surfaces.
5. Write the manifest (below) after every inventory and preservation decision is resolved. Paper stays untouched.

## Manifest schema 1

```markdown
# Paper Manifest

Schema: 1

## Paper Target

- URL: <Paper file URL>
- File: <human Paper file name>
- File ID hint: <canonical file ID, if available>
- Inspected: <ISO-8601 timestamp>

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

Format rules:

- Write `None observed` under an empty inventory heading.
- Escape table delimiters in values.
- Sketch and Archive pages appear in Pages only.
- Drop a legacy `## Planning Convention` section on refresh.

On refresh:

- Keep entries confirmed against live Paper and the repository.
- Update only entries whose evidence changed.
- Add new valid canonical entries.
- Remove an entry only when the complete scan proves its surface absent. A lookup failure, rename, or stale locator is not proof; match by human names first.
- Leave surfaces with Structure Findings out of the inventory.
- Keep unrelated user-written content when schema ownership stays clear; otherwise stop for Manifest Migration approval.

## Ends with

A report:

- Manifest Root and Paper Target
- Counts of canonical pages, Component Families, Screen Artboards, and mapped workspaces
- Entries retained, added, updated, and removed
- Whether tracker config exists
- Structure Findings excluded, and Pending Evidence
- Retarget, migration, locator, or freshness issues

Set-up issues no verdict and ends there.
