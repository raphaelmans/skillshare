# Paper Structure Lint

Audit one explicitly linked Paper Target for structural convention compliance. Keep the entire run read-only and independent of any OpenSpec Change.

## Boundary

- Require and open the explicit Paper file link through the shared workflow, retain its canonical file ID, and use that ID for every Paper read that accepts `fileId`.
- Do not resolve a change, verify a 4/4 artifact set, run scope, request approval, or mutate Paper, OpenSpec, production code, tasks, or `PAPER.md`.
- Do not run the repository UI component-system audit merely to lint structure. Read a valid Paper Manifest, current specs, or repository language only when needed to disambiguate a human page name or canonical owner; treat them as evidence rather than authority over live Paper structure.
- Inspect the live Paper file even when the manifest has cached page or node locators. Never issue Design Alignment or Full Parity from lint.

## Audit the page hierarchy

1. Scan the complete live page tree once and classify every page.
2. Treat `<Module> / Components`, `Shared / Components`, and `<Module> / <Feature>` as canonical current-state page forms.
3. Treat `Exploration / <Name>` and `Archive / <Name>` as explicit exceptional-page forms. They remain outside normal production coverage and cannot own canonical production surfaces.
4. Flag unnamed, ambiguous, change-slug, component-per-page, and other pages that claim current production ownership outside the canonical forms.
5. Identify duplicate or conflicting module, feature, shared, or exceptional page ownership.

## Audit canonical surfaces

Inspect current-state pages deeply enough to establish these conventions:

- Each module-owned Component Family has one canonical Component Frame on `<Module> / Components`.
- Each genuinely cross-module Component Family has one canonical Component Frame on `Shared / Components`.
- Required states and variations remain colocated within their owning Component Frame rather than split across pages or competing canonical frames.
- Each Screen Artboard belongs to its owning `<Module> / <Feature>` page and identifies one material scenario and required viewport without claiming specification authority.
- Screens reuse their canonical Component Family nodes rather than maintaining independent competing redraws. When reuse cannot be established from available structural evidence, report Pending Evidence instead of a violation.
- Exploration and Archive pages do not own canonical production Component Frames or Screen Artboards.
- Paper contains no specification frames, acceptance-criteria tables, coverage matrices, change-history pages, or annotations presented as canonical production design.

Do not lint visual taste, pixel-level styling, token choices, implementation quality, requirement coverage, or semantic agreement between sources. Those concerns belong to visual review, `parity`, or `sync`.

## Report findings

Report the audited Paper Target, file-wide page count, inspected canonical-surface counts, and findings grouped by convention. For every Lint Finding include:

- Paper page and human-readable frame or artboard name
- Violated structural convention
- Direct structural evidence
- Recommended canonical owner or corrective action

List ambiguous ownership or reuse under Pending Evidence with the focused evidence needed to resolve it. Report `No structural lint findings` only after the complete page hierarchy and all candidate canonical owners have been assessed.

Stop after the report. Do not repair findings, create a mutation plan, or enter another slice automatically. If the user later requests correction, do not treat the lint report as mutation authorization: route work owned by an active change through the smallest authorized change-bound slice, or report that a separate maintenance path is required.
