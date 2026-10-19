# UI Component-System Audit

Use one shared, read-only audit of the affected UI workspace whenever a slice analyzes, designs, reconciles, reviews, or implements a visual surface. The audit establishes the repository's component vocabulary; it never changes OpenSpec intent.

## Resolve the owning workspace

Audit each affected application or package independently. In a monorepo, configuration in one application does not establish support in another.

1. Resolve the owning workspace, framework, package manager, Tailwind setup, UI aliases, component directories, design-system imports, and repository-specific wrappers.
2. Search for `components.json` from the owning workspace and inspect existing shadcn component files and imports.
3. Classify the workspace as **Configured**, **Compatible but unconfigured**, or **Not applicable**.
4. Reuse the audit across selected slices while its workspace, configuration, dependencies, and relevant component inventory remain unchanged.

## Use configured shadcn evidence

For a **Configured** workspace, load and follow the `shadcn` skill. From the owning workspace, run `shadcn@latest info --json` through the project's package runner and retain this working context:

- Framework, package manager, React Server Component mode, and preset
- Aliases and resolved component, utility, hook, library, and CSS paths
- Tailwind version and CSS entry point
- Base, style, icon library, installed components, and configured registries
- Existing repository wrappers and domain components built on those primitives

Before a component is proposed for Paper, compared during an audit, or newly used in code, consult its shadcn documentation and existing local implementation. Prefer, in order:

1. Existing repository domain components or wrappers that already own the required product behavior
2. Installed shadcn components and their built-in anatomy, states, and variants
3. Composition of installed primitives
4. An approved registry addition or a justified custom component

Never assume the default `@/components/ui` alias. Follow the configured base, style, icon library, semantic colors, tokens, composition rules, accessibility behavior, and resolved paths. Component availability may suggest reuse, but it must not remove or weaken an explicit OpenSpec requirement.

## Handle other classifications

For a **Compatible but unconfigured** workspace, report shadcn as an optional implementation opportunity. Do not assume it in Paper, run `init`, create `components.json`, add dependencies, or replace the established component system without explicit approval.

For a **Not applicable** workspace, use the established repository component system and visual language. Do not introduce shadcn merely to match a Paper composition.

## Respect mutation boundaries

The audit itself is read-only. Keep its results in working context; do not add them to Paper or invent OpenSpec requirements, decisions, or tasks solely to record the audit.

For `inventory-tree` and the inventory phase of `init`, audit only workspaces mapped to observed canonical surfaces. Record current configuration and component roots without proposing adoption, additions, or implementation work. Return that context to the inventory caller; `init` owns any manifest serialization.

`scope`, `components`, `screens`, `sync`, and `parity` may inspect shadcn configuration, local source, CLI info, and documentation, but may not add, update, or overwrite repository components. Only an authorized `implement` run may change production code.

During `implement`, search installed components and configured registries before proposing custom UI. Resolve a registry explicitly and obtain approval before adding a missing registry item or dependency. Preview changes to existing components with dry-run and diff, never overwrite local changes without explicit approval, review every added file, and run the affected verification gates.
