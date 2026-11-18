# read-the-ui-system

Learn the repository's established visual language and component vocabulary for each affected workspace. Read-only evidence; it never adds business intent.

- **Reads:** package manifests, `components.json`, Tailwind and CSS config, component source and wrappers, `shadcn info --json`, shadcn docs, repository tokens and styles, Paper tokens
- **May change:** nothing

## Split authority

When sources disagree: the Spec owns behavior, rules, scenarios, and scope; the repository's components, styles, and tokens own the visual language; Paper owns the composition under review. Implementation bugs are evidence of current state, never requirements.

## Audit each owning workspace

Audit each affected application or package on its own; in a monorepo, one workspace's config says nothing about another.

1. Resolve the workspace, framework, package manager, Tailwind setup, aliases, component directories, design-system imports, and repository wrappers.
2. Search for `components.json` from the workspace and inspect existing shadcn files and imports.
3. Classify it:
   - **Configured:**
     - Run: load the `shadcn` skill and run `shadcn@latest info --json` through the project's runner.
     - Keep: framework, RSC mode, preset, resolved aliases and paths, Tailwind version and CSS entry, base, style, icon library, installed components, registries, and the wrappers built on them. Use the resolved aliases; `@/components/ui` is never assumed.
     - Prefer, in order: existing domain components and wrappers, installed components, compositions of installed primitives, then an approved registry addition or justified custom component.
   - **Compatible but unconfigured:** report shadcn as an optional opportunity only; Paper and plans keep the established system.
   - **Not applicable:** use the established component system and visual language.
4. Resolve the product font families and tokens from the repository and the Paper file. When the repository has no visual system, use a coherent existing Paper token system.

Reuse the result across Steps while the workspace config, dependencies, and component inventory are unchanged. Component availability suggests reuse and never weakens an explicit requirement. This audit authorizes no `shadcn init`, registry additions, dependency changes, or code edits.

For Set-up and inventories, audit only workspaces mapped to observed canonical surfaces and record configuration and component roots without proposing adoption. Unavailable evidence is Pending Evidence, not proof of incompatibility.

Done when: every affected workspace has a classification, its preferred component vocabulary, and resolved fonts and tokens.
