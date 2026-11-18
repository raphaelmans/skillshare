# map-the-page-tree

Scan the whole live Paper page tree, classify every page against the page arrangement, and build the observed Structural Inventory. Strictly read-only.

- **Reads:** the full Paper page tree, canonical component and feature frames (shallow), repository paths and Git HEAD, `docs/agents/paper.md` or repository language only to disambiguate names
- **May change:** nothing

## Classify

Classify against the Page arrangement table in [SKILL.md](../../SKILL.md). Classify the reserved component and Exceptional forms before the general module/feature form; a matching name alone does not prove ownership. Screens consume cloned canonical component nodes, so a screen instance is never another family.

## Build the inventory

1. Scan every page once, following pagination. Classify each as module components, shared components, feature, Sketch, Archive, or unresolved, and keep the observed names and tree.
2. Read candidate canonical component and feature pages deeply enough to establish owner and identity: frames, labels, hierarchy, dimensions. Use screenshots or computed styles only for a specific ambiguity. Exceptional pages get page-level evidence only.
3. Record one entry per Component Family (owner page, frame name, state labels) and per Screen Artboard (owner page, name, surface, scenario, viewport). Add locator hints only paired with human names, and repository mappings only where evidence establishes the workspace and paths.
4. Record observations only: no missing-state rows, expected pages, hypothetical screens, or history. An empty inventory is valid. When duplicates compete and no owner is established, withhold both and report the evidence needed.

## Findings

Report each exclusion or violation as a **Structure Finding**: Paper page and human surface name, the convention it breaks, the structural evidence, and the recommended owner or fix. A valid Exceptional Page is an informational exclusion. Unproven ownership or reuse goes under **Pending Evidence** with the focused evidence needed.

This Step judges structure only: naming, placement, colocation, Exceptional classification, canonical reuse. Visual taste, tokens, implementation quality, and requirement coverage belong to other Jobs. A failed or partial scan is partial evidence, never proof of absence. Say "No Structure Findings" only after every page and every candidate canonical owner has been assessed.

Done when: every page is classified and every canonical surface is inventoried, excluded with a finding, or listed as Pending Evidence.
