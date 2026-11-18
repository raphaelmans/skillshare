# Check-structure

Audit the whole Paper file's page arrangement against the page conventions and report Structure Findings. Read-only.

## Triggers

- "Is the Paper file organised properly?", "check the page structure"
- "Which components are on the wrong page?"
- "Show me the page tree and what's on it" (inventory report)

## Needs

A Paper link. No spec, tracker config, or Gate.

## Steps

1. [open-paper-file](../steps/open-paper-file.md)
2. [map-the-page-tree](../steps/map-the-page-tree.md) across the complete file. Inspect live Paper even when the Paper Manifest holds locator hints.
3. [read-the-ui-system](../steps/read-the-ui-system.md) only when the user asked for an inventory that maps surfaces to repository workspaces.

## Ends with

A read-only report:

- Paper Target, file-wide page count, inspected canonical-surface counts, and the classified tree.
- For an inventory request: the Step's Component Families and Screen Artboards by owner page.
- The Step's Structure Findings grouped by convention, or "No Structure Findings".
- The Step's Pending Evidence.

The report changes nothing and authorizes nothing.
