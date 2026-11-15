---
name: product-guide
description: Create, read, or update the project's Product Behavior Guide in src/docs. Use when the user says "product guide", "/product-guide", asks to document a feature's behavior, or asks to check behavior against the guide. Never update the guide unless the user asks.
---

# Product Behavior Guide

The Product Behavior Guide is this repo's knowledge base for **how the product behaves**.
It lives in the same repo as the product, under `src/docs/`, and explains every feature through four lenses:

| Lens | Key | Language | Holds |
|---|---|---|---|
| A | `user` | Plain, no tech words | Purpose, who can use it, entry points, user journey, what the user sees |
| B | `behavior` | Product language | Business rules (BR-IDs), state transitions, permissions, errors, edge cases, side effects |
| C | `tech` | Light technical | Routes, layers (router → use case → service → repository), data, integrations, jobs, limitations |
| D | `qa` | Testable | Acceptance criteria (Given/When/Then), scenarios, test data, open questions, bugs |

Plus Part 1 `overview` (what it is, roles, glossary, product map) and
Part 3 `reference` (permissions matrix, notification catalog, environments) and a `changelog`.

---

## 1. File layout (source of truth)

Content is typed TypeScript data. Components only render it; they never hold content.

```
src/docs/
  AGENT.md                      # copy of sections 3–6 of this skill, for any agent
  index.ts                      # registry: export const guide = { overview, features, reference, changelog }
  content/
    overview.ts                 # Part 1
    reference.ts                # Part 3
    changelog.ts                # newest first
    features/
      _template.ts              # lenses A–D with TODO strings
      <feature-slug>.ts         # one file per feature
  lib/
    types.ts                    # Guide, Overview, Feature, BusinessRule, Transition, Scenario, ChangelogEntry
    components/
      docs-layout.tsx           # sidebar index + content area
      feature-page.tsx          # lenses A–D
      lifecycle-diagram.tsx     # renders behavior.transitions as a state diagram (SVG)
      permissions-matrix.tsx
      empty-state.tsx
      agent-guide.tsx           # renders section 6 for humans
```

The route is a thin file outside `src/docs`, e.g. `app/docs/[[...slug]]/page.tsx` (Next.js App Router),
that imports `guide` from `@/docs` and the layout from `@/docs/lib/components`. No content in the route.

### Types (minimum shape)

```ts
export type Status = "planned" | "in-progress" | "shipped" | "retired";

export type BusinessRule = { id: `BR-${string}-${number}`; text: string; retired?: string /* YYYY-MM-DD */ };
export type Transition = { from: string; trigger: string; to: string; by: string /* role or "System" */ };
export type Scenario = { title: string; rules: BusinessRule["id"][]; expected: string };

export type Feature = {
  slug: string; name: string; status: Status; updated: string;
  code: string[];                               // paths the agent reads to verify this feature
  user:     { purpose: string; roles: string[]; entryPoints: string[]; journey: string[]; screens: string[] };
  behavior: { rules: BusinessRule[]; transitions: Transition[]; permissions: string[];
              errors: { input: string; message: string; next: string }[]; edgeCases: string[]; sideEffects: string[] };
  tech:     { routes: string[]; layers: string[]; data: string[]; integrations: string[]; jobs: string[]; limitations: string[] };
  qa:       { criteria: { given: string; when: string; then: string }[]; scenarios: Scenario[];
              testData: string[]; openQuestions: string[]; bugs: string[] };
};
```

Content rules:
- Rule IDs are stable: `BR-<PREFIX>-<n>` (e.g. `BR-BOOK-2`). Never renumber. Retire with `retired: "YYYY-MM-DD"`.
- Use only glossary terms from `overview.ts`. A new term goes into the glossary in the same update.
- Unknown or unconfirmed behavior goes in `qa.openQuestions`, never in `behavior.rules`.
- After any content change, the project must still type-check (`tsc --noEmit` or the project's script).

---

## 2. Rendering (check the project first)

1. Read `package.json`; look for `components.json` at the repo root.
2. **shadcn mode** if `components.json` exists, or React + `class-variance-authority` + `tailwind-merge`
   + a `components/ui` folder.
3. Otherwise → **pure HTML mode**.

### 2a. shadcn mode (preferred)

- Components in `src/docs/lib/components/*.tsx`, built from the project's shadcn `components/ui`.
- Layout: shadcn `Sidebar` with the index: Overview · Features (grouped by status) · Reference · Changelog · Agent guide.
- Use: `sidebar`, `scroll-area`, `tabs` or `card` (lenses A–D), `badge` (status, lens, Yes/No/Own),
  `table`, `accordion` (edge cases, open questions), `breadcrumb`, `separator`.
- Before writing components, list the ones missing from `components/ui/`.
  **Ask before installing**, showing the exact command, e.g.
  `npx shadcn@latest add sidebar scroll-area tabs badge table accordion breadcrumb separator`.
  No install without a yes. If declined, build with what exists.
- Diagrams: inline SVG components using theme variables (`hsl(var(--foreground))`, `--muted-foreground`, `--border`).
  `lifecycle-diagram.tsx` draws from `behavior.transitions`; dashed edges where `by === "System"`.

### 2b. Pure HTML mode (fallback)

- Content stays in `src/docs/content/*` (use `.js` with JSDoc types if the project has no TypeScript).
- View: `src/docs/index.html` + `src/docs/lib/render.js`, vanilla JS, no build step.
- Sticky sidebar index (collapsible on mobile); stable anchors: `#overview`, `#feature-<slug>`, `#reference`, `#changelog`, `#agent-guide`.
- Light/dark via `prefers-color-scheme`. Diagrams as inline SVG.

---

## 3. Empty slate (first run: `/product-guide init`)

When `src/docs/` does not exist:

1. Detect the mode (section 2) and say which one you'll use. In shadcn mode, ask about missing components now.
2. Create the layout with **placeholders only**. No invented features, rules or roles.
   - `overview.ts`: `"TODO: What it is, in one paragraph"`, empty roles, glossary and product map.
   - `features/_template.ts` only; `index.ts` exports `features: []`.
   - `reference.ts`: empty arrays. `changelog.ts`: one entry, `{ date, change: "Guide created (empty slate)" }`.
   - `AGENT.md`: sections 3–6 of this skill.
3. Build the view. With no features it shows:
   - "No features documented yet. Ask your agent: `/product-guide add <feature>`."
   - The Agent guide section (section 6).
4. Offer in one line to draft Part 1 from the codebase. Don't draft it unasked.

---

## 4. Read mode (knowledge base)

When the user points you at the guide ("check the guide", "is this per spec?", "what does BR-BOOK-2 say?"):

- Start at `src/docs/index.ts`; read `overview.ts` for terms and roles, then only the feature files you need.
- Treat `behavior` (rules, transitions, permissions) as the **spec**.
- To verify, read the paths in that feature's `code` array.
- If code and guide disagree, **report the mismatch** with rule IDs and file paths.
  Don't change either until the user says which one is right.
- Cite rule IDs in answers and commit messages ("enforces BR-BOOK-2").
- Read mode never writes.

---

## 5. Update mode (user-invoked only)

| User says | Agent does | Writes |
|---|---|---|
| `/product-guide init` | Empty slate (section 3) | Yes |
| `/product-guide add <feature>` | New `features/<slug>.ts` from the template, filled from code + user input; registered in `index.ts` | Yes |
| `/product-guide update <feature>` | Re-reads the feature's `code` paths and updates its file | Yes |
| `/product-guide sync` | Lists drift across all features; writes only after the user confirms the list | After yes |
| `/product-guide check <feature>` | Reports code vs. guide mismatches | No |
| `/product-guide render` | Rebuilds the view (components or `index.html`) | View only |

Never:
- Edit `src/docs/` as a side effect of other work (features, bug fixes, refactors).
  At most end that task with one line: "This changes BR-BOOK-2; run `/product-guide update book-a-slot` to record it."
- Write a rule you didn't read in code or hear from the user.
- Delete a feature file. Set `status: "retired"` unless the user asks to delete.

Every write:
1. Read the current feature file and its `code` paths.
2. Fill in this order: `behavior` → `tech` → `user` → `qa`.
3. Every non-retired BR-ID appears in at least one `qa.scenarios[].rules`.
4. Every state change is a `transitions` entry; jobs and timers use `by: "System"`.
5. Bump `updated`, prepend a `changelog.ts` entry (`date`, `feature`, `change`).
6. Type-check, then rebuild the view if in pure HTML mode.
7. Reply briefly: files changed; rules added / changed / retired; open questions.

---

## 6. Agent guide (rendered on the page by `agent-guide.tsx`, anchor `#agent-guide`)

- **What this is:** the source of truth for how each feature behaves. Agents read it as spec.
- **How to ask:** `/product-guide init`, `add <feature>`, `update <feature>`, `check <feature>`, `sync`, `render`.
- **Update policy:** changes only when someone asks. Agents report drift; they don't fix it silently.
- **Where things live:** `src/docs/index.ts` (registry), `src/docs/content/` (content), `src/docs/lib/components/` (view).
- **Conventions:** BR-IDs never renumber; glossary terms only; unknowns go to open questions; features are retired, not deleted.
