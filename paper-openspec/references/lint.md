# Paper Structure Lint

Audit one explicitly linked Paper Target for structural convention compliance. Keep the entire run read-only and independent of any OpenSpec Change.

## Boundary

- Require and open the explicit Paper file link through the shared workflow, retain its canonical file ID, and use that ID for every Paper read that accepts `fileId`.
- Do not resolve a change, verify a 4/4 artifact set, run scope, request approval, or mutate Paper, OpenSpec, production code, tasks, or `PAPER.md`.
- Do not run the repository UI component-system audit merely to lint structure. Read a valid Paper Manifest, current specs, or repository language only when needed to disambiguate a human page name or canonical owner; treat them as evidence rather than authority over live Paper structure.
- Inspect the live Paper file even when the manifest has cached page or node locators. Never issue Design Alignment or Full Parity from lint.

## Audit the page hierarchy

Read **Page arrangement** in [inventory-tree.md](inventory-tree.md) as the shared source of structural conventions. Scan the complete live page tree once and classify every page against those rules. Identify invalid naming and placement, competing owners, and exceptional pages claiming canonical production ownership. Correctly classified exceptional pages are not violations merely because they are excluded from production inventory.

## Audit canonical surfaces

Inspect current-state pages deeply enough to assess the shared rules for family ownership, state colocation, screen scenario/viewport identity, canonical component reuse, and separation of design from specifications or history. When ownership or reuse cannot be established from structural evidence, report Pending Evidence instead of asserting a violation.

Use this slice's boundary and reporting contract; do not run the standalone inventory report, repository UI-system audit, or manifest initialization merely to lint structure.

Do not lint visual taste, pixel-level styling, token choices, implementation quality, requirement coverage, or semantic agreement between sources. Those concerns belong to visual review, `parity`, or `sync`.

## Report findings

Report the audited Paper Target, file-wide page count, inspected canonical-surface counts, and findings grouped by convention. For every Lint Finding include:

- Paper page and human-readable frame or artboard name
- Violated structural convention
- Direct structural evidence
- Recommended canonical owner or corrective action

List ambiguous ownership or reuse under Pending Evidence with the focused evidence needed to resolve it. Report `No structural lint findings` only after the complete page hierarchy and all candidate canonical owners have been assessed.

Stop after the report. Do not repair findings, create a mutation plan, or enter another slice automatically. If the user later requests correction, do not treat the lint report as mutation authorization: route work owned by an active change through the smallest authorized change-bound slice, or report that a separate maintenance path is required.
