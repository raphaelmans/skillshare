# Component Families

Create or complete canonical Paper component frames for the selected OpenSpec change after Scope Approval.

## Determine the component inventory

Use the approved Impact Matrix or Experience Coverage Matrix and ordered User Flows or Design Batches. Include a product component when the change introduces it or changes its behavior, states, content contract, or composition. Reuse unchanged primitives and established shared components without giving each one a new frame.

Load `ui-system.md` and use the affected workspace's audit before choosing component anatomy. When shadcn is Configured, map each changed Component Family to an existing repository wrapper, domain component, installed shadcn component, or composition of installed primitives. Consult the relevant shadcn documentation and local source before drawing the family so Paper reflects the actual anatomy, supported states, semantic tokens, icon system, and accessibility behavior. Do not add or update repository components from this slice.

Do not create a Paper frame merely to catalog an unchanged shadcn primitive. Create one only when the active change introduces or changes the product-level component contract. Never force a primitive whose behavior or anatomy conflicts with OpenSpec; record the mismatch as a design dependency or implementation consideration instead.

Derive states and variations from explicit artifact scenarios, affected current specs, and established repository behavior. Do not invent loading, empty, error, disabled, hover, focus, size, or theme variants unless the artifacts require them or the changed component's existing contract already includes them.

Distinguish a component's absence from a visual state. For example, a card hidden because a count is zero is a screen visibility rule, not a blank card variant.

## Build one frame per family

1. Resolve the Component Family's owner from the approved Page Ownership Plan.
2. Reuse or create `<Module> / Components` for a module-owned family. Use `Shared / Components` only for a genuinely cross-module family. Never create or use a change-slug page as its canonical owner.
3. On that page, reuse or create an artboard named `Component / <Canonical Name>`.
4. If the only satisfactory source is on a legacy change page, copy it once into the owner page and treat the new node as canonical. Preserve the legacy page unchanged.
5. Put every required state and variation inside that single frame.
6. Use concise state labels such as `Default`, `Filtered`, or `Disabled`; do not place requirements, prose annotations, acceptance criteria, or implementation notes in the frame.
7. Build the canonical state first, then duplicate or clone it for variations and apply only the differences.
8. Use repository/Paper tokens, available fonts, real domain copy, and existing component conventions.
9. When shadcn is Configured, preserve the selected local component's composition rules, built-in variants, semantic colors, icon library, and accessibility-relevant structure.
10. Keep component artboards fit to their content and visually separate variations without turning the frame into a specification sheet.

Treat a state label as navigation within the design, not as a place for documentation.

## Review

After each component family, screenshot the frame and verify:

- Every artifact-required state is present exactly once.
- States share the same component anatomy where expected.
- Content, actions, visibility, and hierarchy satisfy their scenarios.
- Spacing, typography, contrast, alignment, and tokens match the established visual language.
- Configured component-system mappings use existing wrappers or installed primitives where they satisfy the required contract.
- No specification text or review commentary appears on the canvas.

Fix targeted issues before starting the next family. Preserve acceptable existing variants. Complete shared and dependency-ready component families before creating Screen Artboards that consume them.

## Completion contract

Consider the slice complete when every changed product-component family has exactly one canonical frame on its approved module or shared component page, with all required states and no speculative variants. Return the component families and owner pages created, reused, completed, migrated, or intentionally excluded as unchanged primitives.
