# Component Families

Create or complete canonical Paper component frames for the selected OpenSpec change after Scope Approval.

## Determine the component inventory

Use the approved Impact Matrix or Experience Coverage Matrix and ordered User Flows or Design Batches. Include a product component when the change introduces it or changes its behavior, states, content contract, or composition. Reuse unchanged primitives and established shared components without giving each one a new frame.

Derive states and variations from explicit artifact scenarios, affected current specs, and established repository behavior. Do not invent loading, empty, error, disabled, hover, focus, size, or theme variants unless the artifacts require them or the changed component's existing contract already includes them.

Distinguish a component's absence from a visual state. For example, a card hidden because a count is zero is a screen visibility rule, not a blank card variant.

## Build one frame per family

1. Reuse or create an artboard named `Component / <Canonical Name>`.
2. Put every required state and variation inside that single frame.
3. Use concise state labels such as `Default`, `Filtered`, or `Disabled`; do not place requirements, prose annotations, acceptance criteria, or implementation notes in the frame.
4. Build the canonical state first, then duplicate or clone it for variations and apply only the differences.
5. Use repository/Paper tokens, available fonts, real domain copy, and existing component conventions.
6. Keep component artboards fit to their content and visually separate variations without turning the frame into a specification sheet.

Treat a state label as navigation within the design, not as a place for documentation.

## Review

After each component family, screenshot the frame and verify:

- Every artifact-required state is present exactly once.
- States share the same component anatomy where expected.
- Content, actions, visibility, and hierarchy satisfy their scenarios.
- Spacing, typography, contrast, alignment, and tokens match the established visual language.
- No specification text or review commentary appears on the canvas.

Fix targeted issues before starting the next family. Preserve acceptable existing variants. Complete shared and dependency-ready component families before creating Screen Artboards that consume them.

## Completion contract

Consider the slice complete when every changed product-component family has one canonical frame with all required states and no speculative variants. Return the component families created, reused, completed, or intentionally excluded as unchanged primitives.
