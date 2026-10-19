# Paper Inventory Tree

Describe the current-state Paper organization and inventory the canonical surfaces actually present. This reference owns the page arrangement and structural inventory rules shared by `inventory-tree`, `init`, and `lint`.

## Standalone invocation

Use `$paper-openspec inventory-tree <paper-file-url>` for a read-only inventory reported in chat. Resolve and open the Paper target using only **Resolve the Paper target** in [workflow.md](workflow.md): load the Paper MCP guide first, open the resolved link, and pass the returned canonical file ID to every subsequent read that accepts `fileId`.

No repository, root `openspec/`, active change, planning artifacts, scope approval, or manifest is required. Repository context enriches established mappings when available; it is not a prerequisite. Do not write `PAPER.md`, alter Paper or code, repair findings, or continue into another slice.

When `init` uses this reference, its own target-resolution and manifest-writing rules still apply. Build the inventory below once and return it to initialization; do not repeat the scan or run a second standalone report. `lint` uses the arrangement rules below with its own audit and reporting procedure.

## Page arrangement

Organize Paper by enduring product ownership, using human module and feature names. Pages represent current design, not the OpenSpec change that last touched it.

| Page name | Contents and ownership |
| --- | --- |
| `<Module> / Components` | All canonical Component Families owned by that module, one frame per family. |
| `Shared / Components` | Canonical families whose ownership and reuse genuinely cross module boundaries. This is not a miscellaneous collection or a second home for module components. |
| `<Module> / <Feature>` | Screen Artboards for that feature, each representing one material scenario at one viewport. |
| `Exploration / <Name>` | Noncanonical experiments; excluded from the current production inventory. |
| `Archive / <Name>` | Noncanonical retained designs; excluded from the current production inventory. |

The slash is part of the page naming convention; a grouped report does not require creating nested Paper pages. Classify the reserved component and exceptional forms before the general module/feature form. A matching name alone does not prove valid ownership.

- Name a canonical component frame `Component / <Canonical Name>`. Keep its states and variations inside that one frame, with concise labels. Do not split a family into one page per component or one competing canonical frame per state.
- Name a screen artboard `Screen / <Surface> / <Scenario> / <Viewport>`. Keep materially distinct scenario/viewport combinations on their feature page. Record observed labels and dimensions; do not invent breakpoint coverage.
- Screens consume cloned or duplicated canonical component nodes. A screen instance is not another canonical Component Family. Visual resemblance alone does not prove reuse or independent redrawing.
- Keep specification prose, acceptance criteria, coverage matrices, implementation notes, and change-history records off canonical design surfaces. State and scenario labels identify designs; they do not turn frames into specifications.
- Do not use change slugs, unnamed drafts, or ambiguous collections as canonical owners. Preserve exceptional and legacy pages during inspection; this convention does not authorize moving, renaming, or deleting anything.

For example, a product might have `Billing / Components`, `Billing / Invoices`, and `Shared / Components`. These illustrate ownership, not pages to create or expected inventory entries.

## Build the observed inventory

Scan the complete live page tree once, including every page of a paginated result. Classify each page as module components, shared components, feature, exploration, archive, or noncanonical/unresolved. Retain the observed page names and tree; do not replace them with an idealized hierarchy.

Deep inspection is limited to candidate canonical component and feature pages. Read their frames, labels, hierarchy, and dimensions to establish ownership and surface identity. Use screenshots or computed styles only when that structural evidence leaves a specific ambiguity. For exceptional or other noncanonical pages, use page and shallow surface evidence to explain exclusion without reconstructing their contents or history.

Include only surfaces with an established canonical identity and owner:

| Entry | Record |
| --- | --- |
| Component Family | Owner page, human frame name, and observed state or variation labels. One entry per family, not per state or screen instance. |
| Screen Artboard | Owner page, human artboard name, surface, scenario, and viewport. One entry per observed canonical surface/scenario/viewport combination. |
| Optional evidence on either entry | Page or node locator hints paired with their human names; established repository workspace and concrete paths; verification commit when supported by Git evidence. |

Preserve actual human names in the report, including naming deviations; never silently normalize a misplaced or invalid surface into the inventory. Do not guess which duplicate is canonical. If one owner is established, inventory that owner and exclude the competing copy; otherwise withhold the disputed entries and report the evidence needed to resolve them.

Record current observations only. Do not generate missing-state rows, expected pages, hypothetical screens, intended coverage from active changes, or historical reconstructions. An empty canonical inventory is valid. A failed or incomplete scan is partial evidence, not proof that a surface is absent.

## Repository context, when established

Map surfaces only when available repository evidence establishes the owning application or package and paths. Leave unknown mappings unestablished; do not search unrelated workspaces or require repository access to complete the Paper portion.

For mapped workspaces only, run the read-only audit in [ui-system.md](ui-system.md) once per workspace. Record its classification—**Configured**, **Compatible but unconfigured**, or **Not applicable**—and the concrete configuration, component roots, and relevant wrappers supporting that classification. Unavailable evidence is pending, not proof of incompatibility.

A verification commit identifies the repository revision inspected; it does not certify Paper/code parity. Qualify relevant uncommitted changes instead of implying the commit contains them. Do not initialize shadcn, add dependencies or registry items, or change code during inventory.

## Exclusions and evidence

Exclude Exploration and Archive contents, misplaced surfaces, competing duplicates, ambiguous owners, change-history surfaces, and specification-like surfaces from the canonical inventory.

Report every exclusion as a **Lint Finding** with the Paper page and human surface name when available, the observed structural evidence, and the recommended canonical owner or corrective action. A valid exceptional page is an informational exclusion: keeping it outside production inventory is sufficient, and it need not be moved. A page-level exclusion can cover its contents without deep inspection or an invented per-node list.

For unresolved identity, ownership, or reuse, also state **Pending Evidence** and the focused evidence needed. Do not declare an unproven violation. Never repair exclusions during this pass or reinterpret them as missing requirements or parity gaps.

## Standalone result

Return the Paper target and inspection completeness, followed by:

1. The observed page tree with each page's classification; include exceptional and noncanonical pages visibly marked as excluded.
2. Canonical Component Family and Screen Artboard entries with the fields above, grouped by owner page.
3. Established repository mappings and UI-system context, if any.
4. Counts of scanned pages, inventoried families, artboards, and mapped workspaces, followed by Lint Findings and Pending Evidence.

Use `None observed` for an empty inventory section. Keep locator hints secondary to human names. End with this current-state report; do not issue Design Alignment or Full Parity verdicts or persist a specification or manifest.
